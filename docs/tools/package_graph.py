"""Scan the max-models repos for the package graph on /projects/package-graph/.

For each package, read which other packages of the ecosystem it imports (Python ``import``
statements in its source, tests, examples and notebooks), its languages and its lines of
code, and write them to ``src/data/package-graph.json``.

An import is

- ``required`` when the library imports the package and lists it in ``[project.dependencies]``,
- ``optional`` when the library imports it but only an extra of ``[project.optional-dependencies]``
  installs it,
- ``dev`` when only the tests, examples or docs import it.

Run it from ``docs/`` with the checkouts (``devel`` branches) side by side in one directory::

    python tools/package_graph.py --repos /Users/max/git_repos/max-models

Repos missing there are shallow-cloned from GitHub with ``--clone``.
"""

import argparse
import ast
import json
import re
import subprocess
import tomllib
from collections import Counter
from pathlib import Path

# The packages in the graph: repo name, a few words on what it does, and the page on this site.
PACKAGES = [
    ("cunumpy", "NumPy on the CPU, CuPy on the GPU", "/projects/cunumpy/"),
    ("maybempi", "MPI only when launched under MPI", "/projects/maybempi/"),
    ("scope-profiler", "Profiling of code regions", "/projects/scope-profiler/"),
    ("methodcard", "The math of each numerical method", None),
    ("mpiarray", "Distributed arrays with halo exchange", "/projects/mpiarray/"),
    ("mpiparticles", "Distributed particles and migration", "/projects/mpiparticles/"),
    ("mpifield", "Distributed fields and particle gather/scatter", None),
    ("simgeometry", "Shapes, grids and domains", "/projects/simgeometry/"),
    ("patchwork", "Block-structured adaptive meshes", "/projects/patchwork/"),
    ("tree-d-3d", "Barnes-Hut trees and fast multipoles", "/projects/tree-d-3d/"),
    ("plasmacoll", "Monte Carlo collisions with neutrals", "/projects/plasmacoll/"),
    ("opencr", "Collisional-radiative models", None),
    ("carafe", "Global and fluid plasma models", "/projects/carafe/"),
    ("beamtracer", "Self-consistent ion beam extraction", "/projects/beamtracer/"),
    ("freeofcharge", "Neutral beams in tokamaks", None),
    ("mhd-sandbox", "2D ideal MHD on a periodic grid", "/projects/mhd-sandbox/"),
    ("plasma-plots", "Plots of labeled xarray output", "/projects/plasma-plots/"),
    ("plasma-posters", "Scientific posters from Python", "/projects/plasma-posters/"),
    ("maxplotlib", "Plots with several backends", "/projects/maxplotlib/"),
    ("tikzfigure", "Readable TikZ figures from Python", "/projects/tikzfigure/"),
    (
        "slurm-script-generator",
        "Slurm job scripts",
        "/projects/slurm-script-generator/",
    ),
    (
        "strava-collections",
        "Collections of Strava activities",
        "/projects/strava-collections/",
    ),
]

LANGUAGES = {
    ".py": "Python",
    ".pyi": "Python",
    ".cu": "CUDA",
    ".cuh": "CUDA",
    ".c": "C",
    ".h": "C",
    ".f90": "Fortran",
    ".jl": "Julia",
    ".metal": "Metal",
    ".ts": "TypeScript",
    ".js": "JavaScript",
    ".mjs": "JavaScript",
    ".astro": "Astro",
    ".sh": "Shell",
    ".tex": "TeX",
    ".ipynb": "Jupyter",
}

OUTPUT = Path(__file__).resolve().parent.parent / "src" / "data" / "package-graph.json"


def git_files(repo):
    """Return the files tracked in a repo, relative to its root.

    Parameters
    ----------
    repo : Path
        The checkout.

    Returns
    -------
    list of Path
        The tracked files.
    """
    out = subprocess.run(
        ["git", "ls-files"], cwd=repo, capture_output=True, text=True, check=True
    )
    return [Path(line) for line in out.stdout.splitlines()]


def source(path):
    """Return the Python code of a file: the file itself, or the code cells of a notebook.

    Parameters
    ----------
    path : Path
        A ``.py`` file or a notebook.

    Returns
    -------
    str
        The code.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix != ".ipynb":
        return text
    cells = json.loads(text).get("cells", [])
    code = (
        "".join(c["source"]) if isinstance(c["source"], list) else c["source"]
        for c in cells
        if c["cell_type"] == "code"
    )
    # drop IPython magics and shell escapes, which are not Python
    return "\n".join(
        line
        for cell in code
        for line in cell.splitlines()
        if not line.lstrip().startswith(("%", "!"))
    )


def imported_modules(code):
    """Return the top-level modules imported by absolute imports in some Python code.

    Parameters
    ----------
    code : str
        The code.

    Returns
    -------
    set of str
        The module names, such as ``"cunumpy"``.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return set()
    modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            modules.add(node.module.split(".")[0])
    return modules


def count_lines(path):
    """Return the number of non-blank lines of code in a file.

    Parameters
    ----------
    path : Path
        A source file or a notebook (only its code cells count).

    Returns
    -------
    int
        The number of lines.
    """
    text = (
        source(path)
        if path.suffix == ".ipynb"
        else path.read_text(encoding="utf-8", errors="replace")
    )
    return sum(1 for line in text.splitlines() if line.strip())


def requirement_name(requirement):
    """Return the normalised distribution name of a requirement string.

    Parameters
    ----------
    requirement : str
        Such as ``"cunumpy>=0.7"`` or ``"tree-d-3d @ git+https://..."``.

    Returns
    -------
    str
        Such as ``"cunumpy"``.
    """
    return (
        re.split(r"[\s\[<>=!~;@]", requirement.strip(), maxsplit=1)[0]
        .lower()
        .replace("_", "-")
    )


def scan(repo, name):
    """Scan one repo.

    Parameters
    ----------
    repo : Path
        The checkout.
    name : str
        The repo name.

    Returns
    -------
    dict
        The distribution and import names, dependencies, imports, languages and lines.
    """
    project = tomllib.loads((repo / "pyproject.toml").read_text())["project"]
    packages = [
        p.name for p in (repo / "src").iterdir() if (p / "__init__.py").is_file()
    ]
    required = {requirement_name(r) for r in project.get("dependencies", [])}
    optional = {
        requirement_name(r)
        for extra in project.get("optional-dependencies", {}).values()
        for r in extra
    }
    library_imports, other_imports = set(), set()
    languages, library_lines = Counter(), 0
    for file in git_files(repo):
        path = repo / file
        language = LANGUAGES.get(file.suffix)
        if language is None or not path.is_file():
            continue
        in_library = file.parts[0] == "src"
        # the docs/ site scaffolding (Astro, TypeScript) is the shared theme's, not the package's
        if file.parts[0] == "docs" and language != "Jupyter":
            continue
        lines = count_lines(path)
        languages[language] += lines
        if in_library:
            library_lines += lines
        if language in ("Python", "Jupyter"):
            (library_imports if in_library else other_imports).update(
                imported_modules(source(path))
            )
    return {
        "repo": name,
        "distribution": project["name"].lower().replace("_", "-"),
        "imports_as": packages[0] if packages else name.replace("-", "_"),
        "required": required,
        "optional": optional,
        "library_imports": library_imports,
        "other_imports": other_imports,
        "languages": dict(languages.most_common()),
        "library_lines": library_lines,
        "lines": sum(languages.values()),
    }


def main():
    """Scan the repos and write the graph."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--repos", type=Path, required=True, help="directory with the checkouts"
    )
    parser.add_argument(
        "--clone",
        action="store_true",
        help="shallow-clone the devel branch of missing repos",
    )
    args = parser.parse_args()

    scans = []
    for name, _, _ in PACKAGES:
        repo = args.repos / name
        if not repo.is_dir() and args.clone:
            url = f"https://github.com/max-models/{name}"
            subprocess.run(
                [
                    "git",
                    "clone",
                    "--quiet",
                    "--depth",
                    "1",
                    "--branch",
                    "devel",
                    url,
                    str(repo),
                ],
                check=True,
            )
        scans.append(scan(repo, name))

    by_module = {s["imports_as"]: s for s in scans}
    nodes, edges = [], []
    for (name, short, page), s in zip(PACKAGES, scans, strict=True):
        nodes.append(
            {
                "id": name,
                "module": s["imports_as"],
                "pypi": s["distribution"],
                "description": short,
                "page": page,
                "github": f"https://github.com/max-models/{name}",
                "languages": s["languages"],
                "lines": s["lines"],
                "libraryLines": s["library_lines"],
            }
        )
        for module in sorted(
            (s["library_imports"] | s["other_imports"])
            & by_module.keys() - {s["imports_as"]}
        ):
            target = by_module[module]
            if module in s["library_imports"]:
                kind = (
                    "required"
                    if target["distribution"] in s["required"]
                    else "optional"
                )
            else:
                kind = "dev"
            edges.append({"source": name, "target": target["repo"], "kind": kind})

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"nodes": nodes, "edges": edges}, indent=1) + "\n")
    print(f"{len(nodes)} packages, {len(edges)} imports -> {OUTPUT}")


if __name__ == "__main__":
    main()
