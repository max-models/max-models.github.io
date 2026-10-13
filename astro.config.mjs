// @ts-check
// The shared max-models setup (@max-models/starlight-theme), adapted to a user site: served at the
// root of max-models.github.io instead of under /<repo>/, from master, without edit links.
import { defineDocs } from '@max-models/starlight-theme';

export default defineDocs({
	repo: 'max-models.github.io',
	branch: 'master',
	title: 'Max Lindqvist',
	description: 'Max Lindqvist: plasma physics, scientific computing and open-source tools.',
	nav: [
		{ label: 'Publications', link: '/publications/' },
		{ label: 'Projects', link: '/projects/' },
	],
	sidebar: [
		{ label: 'About', link: '/' },
		{ label: 'Publications', link: '/publications/' },
		{ label: 'Projects', items: [{ autogenerate: { directory: 'projects' } }] },
	],
	starlight: {
		favicon: '/favicon.svg',
		head: [{ tag: 'link', attrs: { rel: 'apple-touch-icon', href: '/apple-touch-icon-180x180.png' } }],
		social: [
			{ icon: 'github', label: 'GitHub', href: 'https://github.com/max-models' },
			{ icon: 'linkedin', label: 'LinkedIn', href: 'https://www.linkedin.com/in/maxlindqv' },
			{ icon: 'email', label: 'Email', href: 'mailto:max.lindqvist@ipp.mpg.de' },
		],
		editLink: {},
		// prev/next links across unrelated pages make little sense on a personal site
		pagination: false,
		customCss: ['./src/styles/custom.css'],
		components: {
			PageTitle: './src/components/PageTitle.astro',
		},
	},
	astro: {
		base: '/',
		// The URLs of the old academicpages (Jekyll) site
		redirects: {
			'/about': '/',
			'/about.html': '/',
			'/portfolio': '/projects/',
			'/portfolio/1-onix': '/projects/onix/',
			'/portfolio/2-struphy': '/projects/struphy/',
			'/portfolio/3-strava-collections': '/projects/strava-collections/',
			'/portfolio/4-tikzpics': '/projects/tikzfigure/',
			'/portfolio/5-tekniskfysik': '/projects/tekniskfysik/',
			'/portfolio/6-scope-profiler': '/projects/scope-profiler/',
			'/portfolio/7-cunumpy': '/projects/cunumpy/',
			'/portfolio/8-maxplotlib': '/projects/maxplotlib/',
			'/portfolio/9-slurm-script-generator': '/projects/slurm-script-generator/',
			'/year-archive': '/projects/strava-collections/',
			'/posts/2025/10/bavarian-alps-traverse': '/projects/strava-collections/',
			'/publication/2019-09-25-effects-of-the-extraction-voltage-on-the-beam-divergence': '/publications/2019-09-25-effects-of-the-extraction-voltage/',
			'/publication/2021-08-03-effects-of-magnetic-field-topology': '/publications/2021-08-03-effects-of-magnetic-field-topology/',
			'/publication/2021-09-20-beam-formation-studies-on-the-cern-is03b-h-source': '/publications/2021-09-20-beam-formation-studies/',
			'/publication/2021-ion-source-developments-at-ipp': '/publications/2022-04-01-ion-source-developments/',
			'/publication/2022-11-11-from-meniscus-formation-to-accelerated-h-beam': '/publications/2022-11-11-from-meniscus-formation-to-accelerated-h-beam/',
			'/publication/2022-12-12-sensitivity-of-negative-ion-beam-extraction': '/publications/2022-12-12-sensitivity-of-negative-ion-beam-extraction/',
			'/publication/2023-06-20-correlation-of-h-beam-properties-to-cs-coverage': '/publications/2023-06-20-correlation-of-h-beam-properties/',
			'/publication/2024-03-25-particle-injection-methods': '/publications/2024-03-25-particle-injection-methods/',
			'/publication/2024-beam-optics-of-rf-ion-sources-in-view-of-iters-nbi-systems': '/publications/2024-06-10-beam-optics/',
			'/publication/2024-07-15-contributions-of-the-extended-elise-and-batman-upgrade-test-facilities': '/publications/2024-07-15-contributions-of-the-extended-elise-and-batman-upgrade/',
			'/publication/2024-08-23-computationally-studying-h-extraction-and-beamlet-formation': '/publications/2024-08-23-computationally-studying-h-extraction/',
		},
	},
});
