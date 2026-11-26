# Bright Sparks Electrical & Data Services — website redesign concept

Static prototype of the redesigned **bseds.com.au**, built on the same design system as the BuildMarque redesign (editorial, image-led layouts, sticky split screens, expanding image panels, Google review rows, FAQ accordions) and re-skinned for Bright Sparks: charcoal + spark yellow, Archivo headings, Manrope body. Its own touches: yellow top bar, squared buttons, hero quote form, scrolling yellow ticker, blueprint-grid dark sections, yellow stat cards.

Open `index.html` in a browser to review. Images, the logo and Instagram photos load directly from the live site's media library.

## Pages
- `index.html` — homepage: hero with copy on the left and a quote form on the right, yellow services ticker, Google reviews (score panel + quote cards), six service panels that expand on hover, "What we do best" cards that stack as you scroll, recent work strip (Instagram photos, drag to scroll), why choose us, who we are, FAQs, quote form, service areas.
- `services.html` — services overview (homepage banner, service panels, stacking cards, reviews, quote section, area map).
- Six service pages: `residential-electrician`, `commercial-electrician`, `electrical-installations`, `maintenance-repairs`, `data-fibre`, `emergency-electrician`. Each uses the homepage banner with the quote card, then an overview, sub-service cards, a "what's included" list, detail sections, a price guide (where the live page gives one), why choose us, recent work, Google reviews, the quote section with map and the service-area map. Like the live site, service pages have no FAQ block; the 10 live FAQs (same wording) appear on Home, About and FAQ.
- `about.html`, `faq.html` (filter by topic), `contact.html` (quote form, service area map).

## Editing
All pages are generated. Edit copy in `tools/content.py` or layout in `tools/build.py`, then run `python3 tools/build.py`. Styles live in `assets/css/style.css` (the BuildMarque stylesheet with a Bright Sparks layer at the end); interactions in `assets/js/main.js`.

## Notes for the WordPress rebuild
- Copy comes from the live site, shortened and lightly tidied. Headings are new where the live page had none (e.g. "Fresh from the job site").
- The ~24 sub-service pages (switchboard upgrades, test & tag, phone wiring, etc.) and suburb lists are left for the WordPress build; on service pages they appear as cards.
- Suburb names were tidied (Currimundi, Ilkley, Moffat Beach, Noosa Heads, Glass House Mountains). Please confirm.
- Instagram link assumed to be `instagram.com/bright.sparks.electrical` (from the feed plugin's file names). Please confirm.
- Review dates are as shown on the live site in November 2026; in WordPress these should come from the reviews plugin.
- Most photos on the live site are stock or pre-darkened banners. Real job photos (like the Instagram ones) would lift the hero, service panels and gallery a lot.
- The quote form is visual only; in WordPress it would connect to the existing form plugin.

## Motion
`assets/js/main.js` ends with a motion layer: headline words rise into place, highlighter strokes draw in, cards and lists arrive in a stagger, images wipe open, service panels rise in sequence, the banner photo drifts (parallax), cards get a soft cursor spotlight, primary buttons get a light sweep, a yellow scroll-progress bar runs along the top, eyebrows draw a yellow line, feature cards flip up, job photos wipe open, lists slide and pop in, cards tilt in 3D, buttons are magnetic, section photos have parallax. All of it switches off for visitors who prefer reduced motion.

## Menu and layout
- The menu mirrors the live site: Home, About, Residential, Commercial, Installation, Maintenance, Data & Fibre, Emergency, Contact. Sub-menu items link to the matching service page's services section until those sub-pages are built in WordPress. FAQ and Services overview are linked from the footer.
- Content width is 1440px on laptops and desktops and 1880px on large screens (1800px+ viewports).
