"""Builds every page of the Bright Sparks redesign prototype.

Run:  python3 tools/build.py
Copy lives in tools/content.py; layout lives here; styles in assets/css/style.css.
"""
import html
import re
from pathlib import Path

from content import (W, IG, PHONE, TEL, EMAIL, FACEBOOK, INSTAGRAM, LOGO, FAQ, FAQ_ALL,
                     REVIEWS, SUBURBS, INSTAGRAM_POSTS, WHY, SERVICES)

ROOT = Path(__file__).resolve().parent.parent
V = "29"  # asset version (cache busting)
e = html.escape

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHEV = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>'
PLUS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>'
PHONE_I = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/></svg>'
BOLT = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.2 2 4.5 13.4h6.1L9.8 22l8.7-11.4h-6.1L13.2 2z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0114 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6 8.5-6"/></svg>'
FB = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.4H8v3h2.6V21h2.9z"/></svg>'
IGI = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor" stroke="none"/></svg>'
G = '<svg class="g" viewBox="0 0 48 48" aria-hidden="true"><path fill="#EA4335" d="M24 9.5c3.5 0 6.6 1.2 9.1 3.6l6.8-6.8C35.8 2.4 30.3 0 24 0 14.6 0 6.6 5.4 2.6 13.2l7.9 6.2C12.4 13.6 17.7 9.5 24 9.5z"/><path fill="#4285F4" d="M46.1 24.5c0-1.6-.1-3.1-.4-4.5H24v9h12.4c-.5 2.9-2.2 5.3-4.6 6.9l7.4 5.8c4.3-4 6.9-9.9 6.9-17.2z"/><path fill="#FBBC05" d="M10.5 28.6c-.5-1.4-.8-3-.8-4.6s.3-3.2.8-4.6l-7.9-6.2C.9 16.6 0 20.2 0 24s.9 7.4 2.6 10.8l7.9-6.2z"/><path fill="#34A853" d="M24 48c6.5 0 11.9-2.1 15.9-5.8l-7.4-5.8c-2.1 1.4-4.8 2.3-8.5 2.3-6.3 0-11.6-4.1-13.5-9.8l-7.9 6.2C6.6 42.6 14.6 48 24 48z"/></svg>'
ICONS = {  # simple line icons for "why choose us"
    0: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3v18M16.5 7.5c0-1.7-2-3-4.5-3s-4.5 1.3-4.5 3 1.6 2.6 4.5 3.2 4.5 1.6 4.5 3.3-2 3-4.5 3-4.5-1.3-4.5-3"/></svg>',
    1: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    2: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6l7-3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
}

TRUST = ["Fully licensed &amp; insured", "24/7 emergency call-outs", "ACMA-approved NBN contractor"]


# ------------------------------------------------------------------ shared parts
def head(title, desc=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)} | Bright Sparks Electrical &amp; Data</title>
  <meta name="description" content="{e(desc)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100,500;100,600;100,700;100,800&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css?v={V}">
</head>
<body>
'''


def nav(active=""):
    a = lambda k: ' class="active"' if active == k else ""
    svc = "\n".join(f'          <a href="{s["slug"]}.html">{e(s["nav"])}</a>' for s in SERVICES)
    return f'''<nav aria-label="Main">
      <a href="index.html"{a("home")}>Home</a>
      <a href="about.html"{a("about")}>About</a>
      <div class="dd">
        <a href="services.html"{a("services")}>Services {CHEV}</a>
        <div class="dd-menu">
{svc}
        </div>
      </div>
      <a href="emergency-electrician.html"{a("emergency")}>Emergency</a>
      <a href="faq.html"{a("faq")}>FAQ</a>
      <a href="contact.html"{a("contact")}>Contact</a>
    </nav>'''


def header(active="", solid=False):
    return f'''
<header class="site-header{' solid' if solid else ''}">
  <div class="topbar"><div class="wrap">
    <span>{BOLT}Licensed Sunshine Coast electricians · 20+ years · Servicing Noosa to Caloundra</span>
    <span class="tb-r"><a href="tel:{TEL}">24/7 Emergency <b>{PHONE}</b></a><a href="mailto:{EMAIL}">{EMAIL}</a></span>
  </div></div>
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Bright Sparks home">
      <img src="{LOGO}" alt="Bright Sparks Electrical &amp; Data Services">
    </a>
    {nav(active)}
    <div class="header-cta">
      <a class="phone" href="tel:{TEL}"><small><i class="live"></i>24/7 Emergency</small>{PHONE}</a>
      <a class="btn btn-primary" href="contact.html">Get A Quote</a>
      <a class="hdr-call" href="tel:{TEL}" aria-label="Call {PHONE}">{PHONE_I}</a>
    </div>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
'''


def footer():
    svc = "".join(f'<li><a href="{s["slug"]}.html">{e(s["nav"])}</a></li>' for s in SERVICES)
    return f'''<footer>
  <div class="wrap">
    <div class="foot-cta">
      <div><span class="eyebrow light">Power out? Switchboard tripping? Sparking outlet?</span>
      <h2 class="h2">24/7 emergency electricians, <em>Sunshine Coast wide</em>.</h2></div>
      <div class="cta-actions">
        <a class="btn btn-primary" href="tel:{TEL}">{PHONE_I} Call {PHONE}</a>
        <a class="btn btn-ghost" href="contact.html">Get A Quote {ARROW}</a>
      </div>
    </div>
    <div class="cols">
      <div>
        <img class="flogo" src="{LOGO}" alt="Bright Sparks Electrical &amp; Data Services">
        <p style="max-width:42ch">For over 20 years, Bright Sparks have been the local electricians Sunshine Coast homes and businesses trust for all their electrical and data needs.</p>
        <div class="socials">
          <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{FB}</a>
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{IGI}</a>
        </div>
      </div>
      <div><h4>Quick Links</h4><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="services.html">Services</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact</a></li><li><a href="https://www.bseds.com.au/user-sitemap/" target="_blank" rel="noopener">User Sitemap</a></li></ul></div>
      <div><h4>Services</h4><ul>{svc}</ul></div>
      <div><h4>Get In Touch</h4><ul class="contact-list">
        <li><a href="https://maps.app.goo.gl/RELnWzGeZfQqzEseA" target="_blank" rel="noopener"><i>{PIN}</i><span>Sunshine Coast, QLD<br>Noosa to Caloundra</span></a></li>
        <li><a href="tel:{TEL}"><i>{PHONE_I}</i><span>{PHONE}</span></a></li>
        <li><a href="mailto:{EMAIL}"><i>{MAIL}</i><span>{EMAIL}</span></a></li></ul></div>
    </div>
    <div class="base"><span>Copyright © 2026 Bright Sparks Electrical &amp; Data Services. All rights reserved.</span><span>Designed By <a href="https://www.digitalmovement.com.au/" target="_blank" rel="noopener">Digital Movement</a></span></div>
  </div>
</footer>
'''


def tail():
    return f'''<a class="float-call" href="tel:{TEL}" aria-label="Call Bright Sparks on {PHONE}">{PHONE_I}Call Us Now</a>
<script src="assets/js/main.js?v={V}"></script>
</body>
</html>
'''


def ticker():
    items = ["Residential", "Commercial", "Electrical Installations", "Maintenance &amp; Repairs", "Data &amp; Fibre", "24/7 Emergency", "Licensed &amp; Insured", "ACMA-Approved NBN Contractor", "Noosa to Caloundra"]
    row = "".join(f"<span>{t}</span><i>{BOLT}</i>" for t in items)
    return f'''
<div class="ticker" aria-hidden="true"><div class="ticker-track">{row}{row}</div></div>
'''


def chips(cls="ph-chips"):
    return f'<ul class="{cls}">' + "".join(f"<li>{CHECK}{t}</li>" for t in TRUST) + "</ul>"


def page_hero(img, eyebrow, h1, lead="", crumbs=(), buttons=True, short=False):
    cr = " / ".join([f'<a href="{h}">{e(t)}</a>' if h else e(t) for t, h in crumbs])
    btns = f'''
      <div class="hero-actions" style="margin-top:30px">
        <a class="btn btn-primary" href="contact.html">Get A Free Quote {ARROW}</a>
        <a class="btn btn-ghost btn-call" href="tel:{TEL}">{PHONE_I} {PHONE}</a>
      </div>
      {chips()}''' if buttons else ""
    return f'''
<section class="page-hero{' short' if short else ''}">
  <img src="{img}" alt="">
  <div class="wrap">
    <div class="crumbs">{cr}</div>
    <span class="eyebrow light">{e(eyebrow)}</span>
    <h1 class="page-title">{h1}</h1>
    {f'<p class="page-lead">{e(lead)}</p>' if lead else ''}{btns}
  </div>
</section>
''' + ticker()


def faq_items(faqs, cats=None):
    out = []
    for i, (q, a) in enumerate(faqs):
        c = f' data-cat="{cats[i]}"' if cats else ""
        out.append(f'''        <div class="faq-item"{c}>
          <button aria-expanded="false"><span><span class="n">{i+1:02d}</span>{e(q)}</span><span class="pm">{PLUS}</span></button>
          <div class="ans"><div>{''.join(f'<p>{e(x)}</p>' for x in a)}</div></div>
        </div>''')
    return "\n".join(out)


def faq_section(faqs, h2="Questions, <em>answered</em>.", lead="", img=W + "2026/08/Right-image-3.jpg", more=True):
    return f'''
<section class="faq" id="faq">
  <div class="wrap faq-grid">
    <div class="faq-side">
      <span class="eyebrow reveal">FAQs</span>
      <h2 class="h2 reveal">{h2}</h2>
      {f'<p class="lead reveal">{e(lead)}</p>' if lead else ''}
      <div class="faq-card reveal">
        <img loading="lazy" src="{img}" alt="">
        <div><h3>Still have a question?</h3><a class="tel" href="tel:{TEL}">{PHONE}</a></div>
      </div>
      {f'<a class="text-link reveal" href="faq.html">View All FAQs {ARROW}</a>' if more else ''}
    </div>
    <div class="faq-list">
{faq_items(faqs)}
    </div>
  </div>
</section>
'''


def cta_band(h2="Need an electrician? <em>Let’s talk.</em>", p="Tell us what you need. We’ll come back with a detailed, transparent quote with no hidden charges.", img=W + "2026/08/homepage-banner-img-2a.webp"):
    return f'''
<section class="cta center">
  <img loading="lazy" src="{img}" alt="">
  <div class="wrap">
    <span class="eyebrow light">Get a quote</span>
    <h2 class="h2">{h2}</h2>
    <p class="lead">{e(p)}</p>
    <div class="cta-actions">
      <a class="btn btn-primary" href="contact.html">Get A Free Quote {ARROW}</a>
      <a class="btn btn-ghost btn-call" href="tel:{TEL}">{PHONE_I} {PHONE}</a>
    </div>
  </div>
</section>
'''


def quote_form(cls="quote", btn="btn-primary"):
    opts = "".join(f"<option>{e(s['nav'])}</option>" for s in SERVICES) + "<option>Something else</option>"
    return f'''<form class="{cls}">
        <label>Name<input type="text" placeholder="Your full name" required></label>
        <label>Phone<input type="tel" placeholder="0400 000 000" required></label>
        <label>Email<input type="email" placeholder="you@example.com" required></label>
        <label>Suburb of works<input type="text" placeholder="Maroochydore"></label>
        <div class="field full"><span class="flabel">Service</span>
          <select>{opts}</select>
        </div>
        <label class="full">Tell us what you need<textarea placeholder="A few details about the job…"></textarea></label>
        <button class="btn {btn}" type="submit">Request A Quote {ARROW}</button>
      </form>'''


def why_section(head_h2="Why choose <em>Bright Sparks</em>?"):
    cards = "".join(f'<div class="feature why reveal"><span class="ico">{ICONS[i]}</span><h3>{e(t)}</h3><p>{e(x)}</p></div>' for i, (t, x) in enumerate(WHY))
    return f'''
<section class="features">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow reveal">The Bright Sparks difference</span>
      <h2 class="h2 reveal">{head_h2}</h2></div>
      <p class="lead reveal">Local electricians Sunshine Coast home and business owners have trusted for over 20 years.</p>
    </div>
    <div class="feature-grid">{cards}</div>
  </div>
</section>
'''


def areas_section():
    sub = "".join(f"<li>{e(s)}</li>" for s in SUBURBS)
    return f'''
<section class="areas">
  <div class="wrap areas-grid">
    <div>
      <span class="eyebrow reveal">Service areas</span>
      <h2 class="h2 reveal">From Noosa to <em>Caloundra</em>, and the hinterland.</h2>
      <p class="lead reveal">Local electricians based on the Sunshine Coast, so help is never far away.</p>
      <div class="cta-actions reveal" style="justify-content:flex-start">
        <a class="btn btn-dark" href="contact.html">Book An Electrician {ARROW}</a>
      </div>
    </div>
    <ul class="suburbs reveal">{sub}</ul>
  </div>
</section>
'''


def reviews_section(title="Trusted by Sunshine Coast homes and businesses, in their <em>own words</em>."):
    cols = ["#17191c", "#8a6d1c", "#2f4a3a", "#5a3b2e", "#3a3d42"]
    keys = ["nothing but good things to say", "always quick to respond", "can highly recommend them", "professionalism is above and beyond",
            "there to help in a heartbeat", "up and running in minimal time", "the best on the sunny coast", "work is always excellent",
            "did an excellent job", "Clean, neat and tidy"]
    cards = []
    for i, (n, when, txt) in enumerate(REVIEWS):
        body = e(txt)
        k = e(keys[i])
        if k in body:
            body = body.replace(k, f"<mark>{k}</mark>", 1)
        cls = "r2-card gstyle" + (" more" if i >= 6 else "")
        cards.append(f'''      <article class="{cls} reveal">
        <div class="gstars"><span>★★★★★</span>{G}</div>
        <p>{body}</p>
        <header><span class="av" style="background:{cols[i % len(cols)]}">{n[0]}</span><span class="who"><b>{e(n)}</b><small>{e(when)}</small></span></header>
      </article>''')
    return f'''
<section class="reviews2" id="reviews">
  <div class="wrap r2-head">
    <span class="eyebrow reveal">Google reviews</span>
    <h2 class="h2 reveal">{title}</h2>
    <div class="r2-rating reveal">{G}<span><span class="r"><b>5.0</b><i>★★★★★</i></span><small>Rated excellent on Google</small></span></div>
  </div>
  <div class="wrap r2-grid">
    <div class="r2-list">
{chr(10).join(cards)}
      <button class="btn btn-dark r2-more" type="button" data-rv2-more>Show More Reviews {ARROW}</button>
    </div>
  </div>
  </div>
</section>
'''


def other_services(cur):
    others = "".join(f'<a class="chip-link" href="{s["slug"]}.html">{e(s["nav"])} {ARROW}</a>' for s in SERVICES if s["slug"] != cur)
    return f'''
<section class="other-inds">
  <div class="wrap">
    <span class="eyebrow">Other services</span>
    <div class="chip-links">{others}</div>
  </div>
</section>
'''


SMALL = {"a", "an", "and", "the", "for", "of", "to", "in", "on", "or", "with", "from", "by", "at", "as", "vs"}


def tc(text):
    """Title Case for headings (matches the BuildMarque build), leaving tags and small words alone."""
    parts = re.split(r"(<[^>]+>)", text)
    first = True
    for i, p in enumerate(parts):
        if p.startswith("<"):
            continue
        def cap(m):
            nonlocal first
            w = m.group(0)
            if not first and w.lower() in SMALL:
                first = False
                return w.lower()
            first = False
            return w[0].upper() + w[1:]
        parts[i] = re.sub(r"(?<![&\w])[A-Za-z][\w’'\-]*", cap, p)
    return "".join(parts)


def headings(body):
    return re.sub(r"(<h[123][^>]*>)(.*?)(</h[123]>)", lambda m: m.group(1) + tc(m.group(2)) + m.group(3), body, flags=re.S)


def write(name, body):
    (ROOT / name).write_text(headings(body))
    print("wrote", name)


# ------------------------------------------------------------------ homepage
def index_page():
    panels = "".join(f'''
    <a class="panel" href="{s["slug"]}.html">
      <img loading="lazy" src="{s["panel"]}" alt="">
      <div class="inner"><span class="num">{i+1:02d}</span><h3>{e(s["nav"])}</h3>
        <p>{e(s["card_text"])}</p>
        <span class="go">Explore →</span></div>
    </a>''' for i, s in enumerate(SERVICES))

    steps = [
        ("Residential", "New builds &amp; renovations", "Full house wiring, switchboards, lighting and power design, NBN and data, and smoke alarm compliance, delivered with homeowners, builders and developers.", W + "2026/08/Left-image-9.jpg", "residential-electrician.html"),
        ("Commercial", "Commercial fit-outs", "Offices, shops, cafés, restaurants and schools. Safe, compliant electrical solutions that slot into your overall fit-out plan.", W + "2026/08/Commercial-Electrical-Fit-Outs-image.jpg", "commercial-electrician.html"),
        ("Data &amp; Fibre", "Data, NBN &amp; fibre", "Structured cabling, network design and fibre upgrades from ACMA-approved, registered NBN contractors.", W + "2026/08/Data-Fibre-image-1.jpg", "data-fibre.html"),
        ("24/7", "Emergency call-outs", "Power outages, faulty switchboards and urgent repairs, handled promptly by a licensed team any hour of the day or night.", W + "2026/08/emergency-elex-img-1.png", "emergency-electrician.html"),
    ]
    ticks = {0: SERVICES[0]["list"][:4], 1: SERVICES[1]["list"][:3], 2: SERVICES[4]["list"][:4], 3: SERVICES[5]["list"][:4]}
    tones = ["t-light", "t-dark", "t-light", "t-yellow"]
    stack = "".join(f'''
      <article class="stack-card {tones[i]}" style="--i:{i}">
        <div class="sc-copy">
          <div class="sc-top"><span class="sc-n">{i+1:02d}</span><span class="sc-tag">{k}</span></div>
          <h3>{t}</h3>
          <p>{p}</p>
          <ul class="ticks">{"".join(f"<li>{CHECK}{e(x)}</li>" for x in ticks[i])}</ul>
          <a class="btn {"btn-primary" if i != 3 else "btn-dark"}" href="{h}">Learn More {ARROW}</a>
        </div>
        <div class="sc-img"><img loading="lazy" src="{img}" alt=""></div>
      </article>''' for i, (k, t, p, img, h) in enumerate(steps))
    ig = "".join(f'<figure><img loading="lazy" src="{IG}{f}" alt="Recent electrical work by Bright Sparks"></figure>' for f in INSTAGRAM_POSTS)

    body = (head("Sunshine Coast Electricians, Electrical & Data Services", "Licensed Sunshine Coast electricians for homes and businesses: residential, commercial, installations, maintenance, data and fibre, and 24/7 emergency call-outs.")
            + header("home") + f'''
<!-- Hero: copy left, quote form right -->
<section class="bs-hero">
  <img class="bs-hero-bg" src="{W}2026/08/homepage-banner-img-2a.webp" alt="">
  <div class="wrap bs-hero-grid">
    <div class="bs-hero-copy">
      <span class="eyebrow light">Sunshine Coast electrical &amp; data specialists</span>
      <h1 class="display">Safe, quality electrical work, <em>done right</em>.</h1>
      <p class="hero-lead">Electrical and data solutions for your home and business that meet the highest safety and quality standards, from trusted local electricians.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="tel:{TEL}">{PHONE_I} Call {PHONE}</a>
        <a class="btn btn-ghost" href="services.html">Our Services {ARROW}</a>
        <a class="g-rating" href="#reviews">{G}<span><b>5.0</b> <i>★★★★★</i><small>Rated excellent on Google</small></span></a>
      </div>
      {chips("hero-chips")}
    </div>
    <div class="qf-card" id="quote">
      <div class="qf-head">
        <span class="qf-ico">{BOLT}</span>
        <div><h2>Get a free quote</h2><p>Detailed, transparent quotes. No hidden charges.</p></div>
      </div>
      <form class="qf">
        <fieldset class="qf-svc"><legend>What do you need help with?</legend>
          {"".join(f'<label><input type="radio" name="svc"{" checked" if i == 0 else ""}><span>{e(x["nav"])}</span></label>' for i, x in enumerate(SERVICES))}
        </fieldset>
        <div class="qf-grid">
          <label class="qf-f"><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg></i><input type="text" placeholder="Full name" required></label>
          <label class="qf-f"><i>{PHONE_I}</i><input type="tel" placeholder="Phone" required></label>
          <label class="qf-f"><i>{MAIL}</i><input type="email" placeholder="Email" required></label>
          <label class="qf-f"><i>{PIN}</i><input type="text" placeholder="Suburb of works"></label>
          <label class="qf-f full"><textarea placeholder="Tell us a little about the job…" rows="3"></textarea></label>
        </div>
        <button class="btn btn-primary qf-btn" type="submit">Request My Free Quote {ARROW}</button>
      </form>
      <a class="qf-sos" href="tel:{TEL}"><span class="live"></span>Electrical emergency? Call 24/7 <b>{PHONE}</b></a>
    </div>
  </div>
</section>
''' + ticker() + f'''
''' + reviews_section() + f'''
<!-- Services: image panels -->
<section class="sectors v2" id="services">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">What we can do for you</span>
        <h2 class="h2 reveal">Reliable, affordable electrical services for <em>homes and businesses</em>.</h2>
      </div>
      <p class="lead reveal" style="color:rgba(255,255,255,.72)">One licensed local team for electrical and data work, so you never have to juggle trades.</p>
    </div>
  </div>
  <div class="panels">{panels}
  </div>
</section>

<!-- What we do best: cards that stack as you scroll -->
<section class="stack-sec" id="work">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow light reveal">What we do best</span>
      <h2 class="h2 reveal">Decades of delivering <em>peace of mind</em>.</h2></div>
      <p class="lead reveal">From new builds to 2am emergencies, one licensed local team handles it all.</p>
    </div>
    <div class="stack">{stack}
    </div>
  </div>
</section>

<!-- Recent work (Instagram) -->
<section class="showcase recent">
  <div class="wrap showcase-head">
    <div>
      <span class="eyebrow reveal">Recent work</span>
      <h2 class="h2 reveal">Fresh from the <em>job site</em>.</h2>
    </div>
    <div class="showcase-tools">
      <a class="btn btn-line" href="{INSTAGRAM}" target="_blank" rel="noopener">{IGI} Follow On Instagram</a>
      <div class="strip-nav"><button data-strip="prev" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M11 6l-6 6 6 6"/></svg></button><button data-strip="next" aria-label="Next">{ARROW}</button></div>
    </div>
  </div>
  <div class="strip">{ig}</div>
</section>
''' + why_section() + f'''
<!-- Who we are -->
<section class="about-intro home-about">
  <div class="wrap">
    <div class="about-grid">
      <div class="about-photo reveal"><img loading="lazy" src="{W}2026/08/Right-image-8-1.jpg" alt=""></div>
      <div>
        <span class="eyebrow reveal">Who we are</span>
        <p class="statement reveal" style="margin-top:20px">For more than 20 years, we’ve provided Sunshine Coast homes and businesses with electrical and data solutions that meet the <em>highest standards</em>.</p>
        <p class="lead reveal" style="margin-top:28px;max-width:62ch">From residential lighting and power upgrades to commercial fit-outs, data cabling, routine maintenance and emergency repairs, we’ve built a strong reputation for precision, reliability and workmanship.</p>
        <div class="cta-actions reveal" style="justify-content:flex-start;margin-top:34px"><a class="btn btn-dark" href="about.html">About Bright Sparks {ARROW}</a></div>
      </div>
    </div>
    <ul class="r2-proof row reveal">
      <li><b data-count="20" data-suffix="+">20+</b><span>Years on the Coast</span></li>
      <li><b>24/7</b><span>Emergency call-outs</span></li>
      <li><b>ACMA</b><span>Registered NBN contractor</span></li>
      <li><b>1 team</b><span>For power &amp; data</span></li>
    </ul>
  </div>
</section>
''' + faq_section(FAQ_ALL, lead="Everything Sunshine Coast homeowners and business owners usually ask before booking an electrician.") + f'''
<!-- CTA / quote -->
<section class="cta" id="contact">
  <img loading="lazy" src="{W}2026/08/Hero-Banner.jpg" alt="">
  <div class="wrap">
    <div>
      <span class="eyebrow light">Get in touch</span>
      <h2 class="h2">Detailed, transparent quotes. <em>No hidden charges.</em></h2>
      <p class="lead" style="color:rgba(255,255,255,.75)">Tell us what you need and we’ll come back to you promptly.</p>
      <div class="contact-lines">
        <a href="tel:{TEL}"><small>Call, 24/7</small>{PHONE}</a>
        <a href="mailto:{EMAIL}"><small>Email</small>{EMAIL}</a>
      </div>
    </div>
    {quote_form()}
  </div>
</section>
''' + areas_section() + footer() + tail())
    write("index.html", body)


# ------------------------------------------------------------------ service page
def service_page(d):
    paras = "".join(f'<p class="reveal">{e(p)}</p>' for p in d["intro"])
    lst = "".join(f'<li class="reveal"><span class="n">{i+1:02d}</span>{e(x)}</li>' for i, x in enumerate(d["list"]))
    subs = ""
    if d["subs"]:
        cards = "".join(f'''
      <div class="ind-card svc reveal">
        <div class="ph"><img loading="lazy" src="{img}" alt=""></div>
        <div class="body"><span class="num">{i+1:02d}</span><h3>{e(t)}</h3></div>
      </div>''' for i, (t, img) in enumerate(d["subs"]))
        subs = f'''
<section class="ind-overview">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow reveal">Services</span>
      <h2 class="h2 reveal">{e(d["subs_h2"])}</h2></div>
    </div>
    <div class="ind-cards n{len(d["subs"])}">{cards}
    </div>
  </div>
</section>
'''
    blocks = ""
    for i, (eb, h2, ps, bl, imgs) in enumerate(d["blocks"]):
        bp = "".join(f'<p class="reveal">{e(p)}</p>' for p in ps)
        bul = ('<ul class="ticks reveal">' + "".join(f"<li>{CHECK}{e(x)}</li>" for x in bl) + "</ul>") if bl else ""
        blocks += f'''
<section class="ind-intro{' alt' if i % 2 == 0 else ''}">
  <div class="wrap ind-intro-grid{' rev' if i % 2 == 0 else ''}">
    <div class="ind-copy">
      <span class="eyebrow reveal">{e(eb)}</span>
      <h2 class="h2 reveal">{e(h2)}</h2>
      {bp}{bul}
      <div class="hero-actions copy-ctas reveal"><a class="btn btn-primary" href="contact.html">Get A Quote {ARROW}</a><a class="btn btn-dark btn-call" href="tel:{TEL}">{PHONE_I} {PHONE}</a></div>
    </div>
    <div class="ind-imgs reveal">
      <img loading="lazy" src="{imgs[0]}" alt="">
      <img loading="lazy" src="{imgs[1]}" alt="">
    </div>
  </div>
</section>
'''
    prices = ""
    if d["prices"]:
        cards = "".join(f'<div class="feature price reveal"><b>{e(a)}</b><small>{e(b)}</small><p>{e(c)}</p></div>' for a, b, c in d["prices"])
        prices = f'''
<section class="features prices">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow reveal">Price guide</span>
      <h2 class="h2 reveal">Upfront about <em>cost</em>.</h2></div>
      <p class="lead reveal">Typical Sunshine Coast prices, as a guide only. Every job is quoted in detail before work starts, with no hidden charges.</p>
    </div>
    <div class="feature-grid n{len(d["prices"])}">{cards}</div>
  </div>
</section>
'''
    body = (head(d["title"], d["lead"]) + header("emergency" if d["key"] == "emergency" else "services")
            + page_hero(d["banner"], d["eyebrow"], d["h1"], d["lead"], crumbs=(("Home", "index.html"), ("Services", "services.html"), (d["nav"], "")))
            + f'''
<section class="ind-intro">
  <div class="wrap ind-intro-grid">
    <div class="ind-copy">
      <span class="eyebrow reveal">Overview</span>
      <h2 class="h2 reveal">{e(d["intro_h2"])}</h2>
      {paras}
    </div>
    <div class="ind-imgs reveal">
      <img loading="lazy" src="{d["intro_imgs"][0]}" alt="">
      <img loading="lazy" src="{d["intro_imgs"][1]}" alt="">
    </div>
  </div>
</section>
''' + subs + f'''
<section class="included">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow reveal">What’s included</span>
      <h2 class="h2 reveal">{e(d["list_h2"])}</h2></div>
      <p class="lead reveal" style="color:rgba(255,255,255,.72)">{e(d["list_lead"])}</p>
    </div>
    <div class="inc-grid">
      <figure class="inc-img reveal"><img loading="lazy" src="{d["card_img"]}" alt=""></figure>
      <ul class="included-list">{lst}</ul>
    </div>
  </div>
</section>
''' + blocks + prices + why_section("Why choose <em>Bright Sparks</em>?")
            + faq_section(d["faqs"], h2=f'{e(d["nav"])} <em>FAQs</em>.', lead="Quick answers to the questions we hear most.")
            + cta_band(h2=d["closing_h2"], p=d["closing"], img=d["banner"])
            + other_services(d["slug"]) + footer() + tail())
    write(f'{d["slug"]}.html', body)


# ------------------------------------------------------------------ services overview
def services_page():
    cards = "".join(f'''
      <a class="ind-card reveal" href="{d["slug"]}.html">
        <div class="ph"><img loading="lazy" src="{d["card_img"]}" alt=""></div>
        <div class="body"><span class="num">{i+1:02d}</span><h3>{e(d["nav"])}</h3><p>{e(d["card_text"])}</p><span class="go">Explore {ARROW}</span></div>
      </a>''' for i, d in enumerate(SERVICES))
    body = (head("Electrical & Data Services", "Residential, commercial, installation, maintenance and repairs, data and fibre, and 24/7 emergency electricians on the Sunshine Coast.") + header("services")
            + page_hero(W + "2026/08/homepage-banner-img-3a-1.webp", "Services", "Electrical services for homes <em>and businesses</em>", "Reliable and affordable electrician services Sunshine Coast homes and businesses know they can trust.", crumbs=(("Home", "index.html"), ("Services", "")))
            + f'''
<section class="ind-overview">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow reveal">Six specialisms, one team</span>
      <h2 class="h2 reveal">Find the right <em>service</em>.</h2></div>
      <p class="lead reveal">Because the same licensed team handles electrical and data work, you can use one contractor for the whole job.</p>
    </div>
    <div class="ind-cards">{cards}
    </div>
  </div>
</section>

<section class="ind-intro alt">
  <div class="wrap ind-intro-grid">
    <div class="ind-copy">
      <span class="eyebrow reveal">Residential</span>
      <h2 class="h2 reveal">New builds and renovations, <em>wired right</em>.</h2>
      <p class="reveal">We specialise in residential electrical work for new builds and renovations, partnering with homeowners, builders and developers to deliver reliable, high-quality electrical systems that meet today’s standards and tomorrow’s needs.</p>
      <ul class="ticks reveal">{"".join(f"<li>{CHECK}{x}</li>" for x in SERVICES[0]["list"])}</ul>
    </div>
    <div class="ind-imgs reveal">
      <img loading="lazy" src="{W}2026/08/Left-image-9.jpg" alt="">
      <img loading="lazy" src="{W}2026/08/Electrical-Fit-Outs-image.jpg" alt="">
    </div>
  </div>
</section>

<section class="ind-intro">
  <div class="wrap ind-intro-grid rev">
    <div class="ind-copy">
      <span class="eyebrow reveal">Commercial</span>
      <h2 class="h2 reveal">Need a commercial electrician on the <em>Sunshine Coast</em>?</h2>
      <p class="reveal">We provide commercial electrical fit-outs for offices, shops, cafés, restaurants, schools and other commercial establishments. Whether you’re setting up a new space or upgrading an existing one, we deliver safe and compliant solutions tailored to your needs.</p>
      <p class="reveal">Our team works closely with business owners, project managers and contractors to ensure seamless integration with your overall fit-out plan.</p>
    </div>
    <div class="ind-imgs reveal">
      <img loading="lazy" src="{W}2026/08/Commercial-Electrical-Fit-Outs-image.jpg" alt="">
      <img loading="lazy" src="{W}2025/10/Commercial-servicer.jpg" alt="">
    </div>
  </div>
</section>
''' + faq_section(FAQ["general"] + FAQ["commercial"], h2="Service <em>FAQs</em>.", lead="How we work across homes and businesses.")
            + cta_band() + footer() + tail())
    write("services.html", body)


# ------------------------------------------------------------------ about
def about_page():
    svc = ["Residential electrical, from lighting to full fit-outs", "Commercial installations, fit-outs and test and tag", "Electrical installations of all types, makes and models", "Maintenance, troubleshooting and repairs", "Data points, network and fibre-optic cabling", "24/7 emergency call-outs"]
    lst = "".join(f'<li class="reveal"><span class="n">{i+1:02d}</span>{e(x)}</li>' for i, x in enumerate(svc))
    body = (head("About Bright Sparks, Sunshine Coast Electricians", "Local electricians Sunshine Coast home and business owners have trusted for over 20 years.") + header("about")
            + page_hero(W + "2025/10/About-banner.jpg", "About us", "Local electricians the Sunshine Coast has trusted for <em>20+ years</em>", "Electrical and data installation, repair and maintenance for homes and businesses.", crumbs=(("Home", "index.html"), ("About", "")))
            + f'''
<section class="about-intro">
  <div class="wrap">
    <div class="about-grid">
      <div class="about-photo reveal"><img loading="lazy" src="{W}2025/11/abt-us-content-img-1.webp" alt="Bright Sparks electrician at work"></div>
      <div>
        <span class="eyebrow reveal">Who we are</span>
        <p class="statement reveal" style="margin-top:20px">We take pride in being the local electricians Sunshine Coast home and business owners trust for all their <em>electrical and data</em> needs.</p>
        <p class="lead reveal" style="margin-top:28px;max-width:62ch">Because of our service excellence, our team has gained the trust of countless home and business owners. Ensuring safety and quality for your peace of mind is what we do best. Let us show you what we can do for you.</p>
        <div class="stats reveal">
          <div class="stat"><b data-count="20" data-suffix="+">20+</b><span>Years’ experience</span></div>
          <div class="stat"><b>5.0</b><span>Google rating</span></div>
          <div class="stat"><b>24/7</b><span>Emergency call-outs</span></div>
          <div class="stat"><b>1</b><span>Team for power &amp; data</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="included">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow reveal">What we can do for you</span>
      <h2 class="h2 reveal">One licensed team, <em>every job</em>.</h2></div>
      <p class="lead reveal" style="color:rgba(255,255,255,.72)">Reliable and affordable electrician services Sunshine Coast homes and businesses know they can trust.</p>
    </div>
    <div class="inc-grid">
      <figure class="inc-img reveal"><img loading="lazy" src="{W}2025/10/Right-image-2.jpg" alt=""></figure>
      <ul class="included-list">{lst}</ul>
    </div>
  </div>
</section>

<section class="ind-intro alt">
  <div class="wrap ind-intro-grid">
    <div class="ind-copy">
      <span class="eyebrow reveal">Emergency</span>
      <h2 class="h2 reveal">Need a local emergency electrician? <em>We’re on our way.</em></h2>
      <p class="reveal">When electrical issues strike unexpectedly, you need a fast and reliable emergency electrician you can count on.</p>
      <p class="reveal">Our licensed team responds promptly to urgent call-outs across the Sunshine Coast, handling everything from power outages and faulty switchboards to urgent repairs in commercial and industrial settings.</p>
      <p class="reveal">We prioritise safety, minimise downtime and restore your systems with minimal disruption, 24 hours a day, 7 days a week.</p>
      <div class="cta-actions reveal" style="justify-content:flex-start;margin-top:30px"><a class="btn btn-dark" href="tel:{TEL}">{PHONE_I} Call {PHONE}</a></div>
    </div>
    <div class="ind-imgs reveal">
      <img loading="lazy" src="{W}2025/11/emergency-elex-img.png" alt="">
      <img loading="lazy" src="{W}2025/10/Right-image-3.jpg" alt="">
    </div>
  </div>
</section>
''' + why_section() + reviews_section("What our customers <em>say</em>.")
            + faq_section(FAQ["general"], h2="About <em>Bright Sparks</em>.", lead="Who we are and how we work.")
            + cta_band() + footer() + tail())
    write("about.html", body)


# ------------------------------------------------------------------ FAQ
def faq_page():
    groups = [("general", "General"), ("residential", "Residential"), ("commercial", "Commercial"), ("data", "Data &amp; fibre"), ("emergency", "Emergency")]
    tabs = '<button class="on" data-cat="all">All</button>' + "".join(f'<button data-cat="{k}">{t}</button>' for k, t in groups)
    faqs, cats = [], []
    for k, _ in groups:
        faqs += FAQ[k]
        cats += [k] * len(FAQ[k])
    body = (head("Frequently Asked Questions", "Answers to common questions about electrical and data services from Bright Sparks on the Sunshine Coast.") + header("faq")
            + page_hero(W + "2025/10/Installation-banner.jpg", "FAQ", "Frequently asked <em>questions</em>", "Everything you usually ask before booking an electrician.", crumbs=(("Home", "index.html"), ("FAQ", "")), buttons=False, short=True)
            + f'''
<section class="faq faq-page">
  <div class="wrap faq-grid">
    <div class="faq-side">
      <span class="eyebrow">Browse by topic</span>
      <div class="filters faq-tabs">{tabs}</div>
      <div class="faq-card">
        <img loading="lazy" src="{W}2026/08/Right-image-3.jpg" alt="">
        <div><h3>Still have a question?</h3><a class="tel" href="tel:{TEL}">{PHONE}</a></div>
      </div>
      <a class="text-link" href="contact.html">Send Us A Message {ARROW}</a>
    </div>
    <div class="faq-list">
{faq_items(faqs, cats)}
    </div>
  </div>
</section>
''' + cta_band() + footer() + tail())
    write("faq.html", body)


# ------------------------------------------------------------------ contact
def contact_page():
    body = (head("Contact Us | Get a Quote", f"Call {PHONE} or send a message for a detailed, upfront quote from Bright Sparks Electrical & Data Services.") + header("contact", solid=True)
            + f'''
<section class="contact-main first">
  <div class="wrap contact-grid">
    <div class="contact-info">
      <span class="eyebrow reveal">Contact us today</span>
      <h1 class="h2 reveal">Tell us what <em>you need</em>.</h1>
      <p class="lead reveal">Get in touch to discuss the electrical and data solutions you need for your home or business. We provide detailed, transparent quotes with no hidden charges or surprises.</p>
      <div class="info-cards">
        <a class="info-card reveal" href="tel:{TEL}"><i class="ii">{PHONE_I}</i><span class="it"><small>Call, 24/7</small><b>{PHONE}</b></span></a>
        <a class="info-card reveal" href="mailto:{EMAIL}"><i class="ii">{MAIL}</i><span class="it"><small>Email</small><b>{EMAIL}</b></span></a>
        <a class="info-card reveal" href="https://maps.app.goo.gl/RELnWzGeZfQqzEseA" target="_blank" rel="noopener"><i class="ii">{PIN}</i><span class="it"><small>Service area</small><b>Sunshine Coast, QLD<br>Noosa to Caloundra &amp; hinterland</b></span></a>
      </div>
    </div>
    <div class="contact-form reveal">
      <h3>Request a free quote</h3>
      {quote_form("quote light", "btn-dark")}
    </div>
  </div>
</section>

<section class="visit" id="visit">
  <iframe title="Sunshine Coast service area on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
    src="https://maps.google.com/maps?q=Sunshine%20Coast%20QLD&z=10&output=embed"></iframe>
  <div class="wrap">
    <div class="visit-card reveal">
      <span class="eyebrow">Where we work</span>
      <h3>Sunshine Coast wide</h3>
      <address>Noosa to Caloundra,<br>and the hinterland</address>
      <div class="lines"><a href="tel:{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      <a class="btn btn-dark" href="tel:{TEL}">{PHONE_I} Call Now</a>
    </div>
  </div>
</section>
''' + areas_section() + faq_section(FAQ["general"] + FAQ["emergency"], h2="Before you <em>call</em>.", lead="Quick answers to the questions we hear most.")
            + footer() + tail())
    write("contact.html", body)


if __name__ == "__main__":
    index_page()
    for d in SERVICES:
        service_page(d)
    services_page()
    about_page()
    faq_page()
    contact_page()
