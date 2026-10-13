import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				/** Publication date, or the date of an outdoors post. */
				date: z.coerce.date().optional(),
				/** Publications: the heading they are grouped under on /publications/. */
				category: z.enum(['manuscripts', 'conferences', 'books']).optional(),
				venue: z.string().optional(),
				doi: z.string().optional(),
				/** Author list and reference, with **bold** and *italics*. */
				citation: z.string().optional(),
				/** Projects: the picture on the card on /projects/. */
				image: z.string().url().optional(),
				/** Outdoors posts. */
				tags: z.array(z.string()).optional(),
			}),
		}),
	}),
};
