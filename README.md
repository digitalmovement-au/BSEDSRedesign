# Bright Sparks Electrical & Data Services — website redesign concept

Static prototype of the redesigned **bseds.com.au**, built on the same design system as the BuildMarque redesign (editorial, image-led layouts, sticky split screens, expanding image panels, Google review rows, FAQ accordions) and re-skinned for Bright Sparks: charcoal + spark yellow, Archivo headings, Manrope body.

Open `index.html` in a browser to review. Images, the logo and Instagram photos load directly from the live site's media library.

## Pages
- `index.html` — homepage: full-screen hero with a 24/7 emergency call button and trust chips, Google reviews + proof figures, six service panels that expand on hover, "What we do best" sticky split screen, recent work strip (Instagram photos, drag to scroll), why choose us, who we are, FAQs, quote form, service areas.
- `services.html` — services overview.
- Six service pages: `residential-electrician`, `commercial-electrician`, `electrical-installations`, `maintenance-repairs`, `data-fibre`, `emergency-electrician`. Each has an overview, sub-service cards, a "what's included" list, detail sections, a price guide (where the live page gives one), why choose us, FAQs and a call to action.
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
