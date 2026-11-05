# Handoff: cozy-weighted-guide (Heavy Hugs)

- **Goal:** Earn affiliate commission from a weighted-plush gift guide with no stock (Noah, 2026-11-02). Live at https://ndabney562.github.io/cozy-weighted-guide/ (single `index.html`, GitHub Pages, main branch). Main program: Hugimals on Awin (15%).
- **Done:**
  - Guide live (v4, after AUDIT-2026-11-02.md, kept local only): 6 picks, 4 brands, sold at Hugimals, Crate & Barrel, Target, Lehman's.
  - Awin publisher account approved 2026-11-02 (publisher ID 3142901). Hugimals application sent 2026-11-02.
  - 2026-11-05: 5 Pinterest pin images in `pins/` (1000x1500, made from `pins/template.html` with headless Chrome over the Unsplash photos in `img/`). Pinterest account: daemonsawning3b (the Dink & Paw account), posted through Metricool brand "datenightwithval" (blogId 7854768). Dink & Paw pins already fill 12:15, 15:45 and 20:30 ET through Nov 12 on board 235453955457897841; Heavy Hugs pins use a separate board and 18:00 ET.
- **In progress:** 5 pins SCHEDULED 2026-11-05 in Metricool on board "Weighted Plush Gifts" (id 235453955457900076): Nov 6, 8, 10, 12, 14 at 18:00 ET, each linking to a guide section. Pinterest About text updated 2026-11-05 (Dink & Paw + Heavy Hugs + commission disclosure), confirmed on the public profile. Profile website fixed 2026-11-05 to dinkpawco.etsy.com (was the broken `http://dinkpawco.etsy`).
- **Next step (exact):** [Claude Code] Check pin 1 posted after 2026-11-06 18:00 ET. [Claude Code] Once Awin approves Hugimals: replace `href="https://hugimalsworld.com"` on the 9 links with `data-affiliate="hugimals-awin"` with the Awin deep link; swap in brand-kit product photos.
- **Blockers:** Hugimals approval (no email as of 2026-11-05). Crate & Barrel, Target and Lehman's programs not joined.
- **Last test result:** 2026-11-05: pin PNGs render at 1000x1500, checked by eye. Site has no test suite (PROJECT.md).
- **Last commit hash:** see `git log -1` (this commit adds pins/).
- **Model + timestamp:** Claude Code (Opus 5.5), 2026-11-05
