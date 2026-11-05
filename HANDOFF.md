# Handoff: cozy-weighted-guide (Heavy Hugs)

- **Goal:** Earn affiliate commission from a weighted-plush gift guide with no stock (Noah, 2026-11-02). Live at https://ndabney562.github.io/cozy-weighted-guide/ (single `index.html`, GitHub Pages, main branch). Main program: Hugimals on Awin (15%).
- **Done:**
  - Guide live (v4, after AUDIT-2026-11-02.md, kept local only): 6 picks, 4 brands, sold at Hugimals, Crate & Barrel, Target, Lehman's.
  - Awin publisher account approved 2026-11-02 (publisher ID 3142901). Hugimals application sent 2026-11-02.
  - 2026-11-05: 5 Pinterest pin images in `pins/` (1000x1500, made from `pins/template.html` with headless Chrome over the Unsplash photos in `img/`). Pinterest account: daemonsawning3b (the Dink & Paw account), posted through Metricool brand "datenightwithval" (blogId 7854768). Dink & Paw pins already fill 12:15, 15:45 and 20:30 ET through Nov 12 on board 235453955457897841; Heavy Hugs pins use a separate board and 18:00 ET.
- **In progress:** Metricool moved 2026-11-05: old account (user 6150934, brand 7854768) unreachable, Noah says replaced. New account user 6188672, brand 7897774 ("oddlyhistorical67"), same Pinterest daemonsawning3b, free plan 20 posts/month. 4 Hugimals-free pins saved there as DRAFTS (Noah 2026-11-05: limited post slots go only to paths that can earn now; Dink & Paw is the focus until Hugimals approves), board 235453955457900076, dated Nov 6, 8, 10, 12 18:00 ET (images pins/01-guide-v2.png, 02-budget-v2.png, 03-kids.png, 04-warm.png). Hug Baby pin (05) held until approval. Guide: 3 Hugimals picks hidden (PR #9, commit 936c8c1: revert it to restore). Dink & Paw 24 pins: list in ~/Downloads/dinkpaw-kit/pinterest-schedule-2026-11.json, rescheduling handed to a separate session.
- **Next step (exact):** [Claude Code] Once Awin approves Hugimals: revert 936c8c1, swap the 9 `data-affiliate="hugimals-awin"` hrefs to the Awin deep link, move the 4 draft pins to new dates and schedule them with pin 05 (Hug Baby).
- **Rule (Noah, 2026-11-05):** post nothing about Hugimals until the Hugimals affiliate approval comes through.
- **Blockers:** Hugimals approval (no email as of 2026-11-05). Crate & Barrel, Target and Lehman's programs not joined.
- **Last test result:** 2026-11-05: pin PNGs render at 1000x1500, checked by eye. Site has no test suite (PROJECT.md).
- **Last commit hash:** see `git log -1` (this commit adds pins/).
- **Model + timestamp:** Claude Code (Opus 5.5), 2026-11-05
