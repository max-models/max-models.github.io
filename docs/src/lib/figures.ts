// Figures embedded from the documentation sites of the projects: hotlinked, not copied, and
// looked up once per build.

export interface Figure {
	/** The documentation page the figure is on. */
	page: string;
	/** The image; or, without it, */
	src?: string;
	/** the first image on `page` whose alt text starts with this. */
	match?: string;
	/** The figure as Plotly JSON, for an interactive version. */
	plotly?: string;
	caption: string;
}

export interface ResolvedFigure {
	page: string;
	src: string;
	plotly?: string;
	caption: string;
}

const pages = new Map<string, Promise<string>>();
const images = new Map<string, Promise<boolean>>();

/** The HTML of a page, fetched once per build; empty when the request fails. */
function getPage(url: string): Promise<string> {
	if (!pages.has(url)) pages.set(url, fetch(url).then((r) => (r.ok ? r.text() : ''), () => ''));
	return pages.get(url)!;
}

/** Whether an image is there, asked once per build. */
function exists(url: string): Promise<boolean> {
	if (!images.has(url)) images.set(url, fetch(url, { method: 'HEAD' }).then((r) => r.ok, () => false));
	return images.get(url)!;
}

const decode = (s: string) =>
	s
		.replace(/&#x27;|&#39;/g, "'")
		.replace(/&quot;/g, '"')
		.replace(/&lt;/g, '<')
		.replace(/&gt;/g, '>')
		.replace(/&amp;/g, '&');

/** The URL of the first <img> on `page` whose alt text starts with `match`. */
async function findImage(page: string, match: string): Promise<string | undefined> {
	const html = await getPage(page);
	for (const [img] of html.matchAll(/<img\b[^>]*>/g)) {
		const alt = /\balt="([^"]*)"/.exec(img)?.[1];
		const src = /\bsrc="([^"]*)"/.exec(img)?.[1];
		if (alt !== undefined && src && decode(alt).startsWith(match)) return new URL(decode(src), page).href;
	}
}

/**
 * The figures that are still on the docs sites. Notebook outputs and Astro-processed images are
 * rebuilt with each deployment of the docs, so a missing one is left out, with a warning.
 */
export async function resolveFigures(figures: Figure[]): Promise<ResolvedFigure[]> {
	const resolved = await Promise.all(
		figures.map(async ({ page, src, match, plotly, caption }) => {
			const url = src ?? (match === undefined ? undefined : await findImage(page, match));
			if (url && (await exists(url))) return { page, src: url, plotly, caption };
			console.warn(`[gallery] left out a figure that is not found: ${src ?? `"${match}" on ${page}`}`);
		})
	);
	return resolved.filter((figure) => figure !== undefined);
}
