import { getCollection, type CollectionEntry } from 'astro:content';

export type Entry = CollectionEntry<'docs'>;

/** The pages in a directory of src/content/docs, without its index page. */
export async function getSection(section: string): Promise<Entry[]> {
	return getCollection('docs', (entry) => entry.id.startsWith(`${section}/`));
}

/** Newest first. */
export function byDate(a: Entry, b: Entry): number {
	return (b.data.date?.getTime() ?? 0) - (a.data.date?.getTime() ?? 0);
}

export const href = (entry: Entry) => `/${entry.id}/`;

/** The **bold** and *italics* of a citation, as HTML. */
export function citationHtml(citation: string): string {
	return citation
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
		.replace(/\*(.+?)\*/g, '<em>$1</em>');
}

export const formatDate = (date: Date) =>
	date.toLocaleDateString('en-GB', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });
