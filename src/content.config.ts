// The theme's collections (@max-models/starlight-theme/content), with the extra frontmatter of the
// publications and projects pages.
import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				/** Publication date. */
				date: z.coerce.date().optional(),
				/** Publications: the heading they are grouped under on /publications/. */
				category: z.enum(['manuscripts', 'conferences', 'books']).optional(),
				venue: z.string().optional(),
				doi: z.string().optional(),
				/** Author list and reference, with **bold** and *italics*. */
				citation: z.string().optional(),
				/** Projects: the picture on the card on /projects/. */
				image: z.string().url().optional(),
			}),
		}),
	}),
};
