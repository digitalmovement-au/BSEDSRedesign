// BuildMarque redesign prototype — interactions
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  // Header: solid background once the hero is scrolled past a little
  const header = $('.site-header');
  const onScroll = () => header && header.classList.toggle('scrolled', window.scrollY > 60);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu
  const toggle = $('.menu-toggle');
  const nav = $('.site-header nav');
  if (toggle && nav) {
    const setMenu = open => {
      nav.classList.toggle('open', open);
      toggle.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open);
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      header.classList.toggle('menu-open', open);
      document.body.classList.toggle('menu-is-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    };
    toggle.addEventListener('click', () => setMenu(!nav.classList.contains('open')));
    $$('a', nav).forEach(a => a.addEventListener('click', () => setMenu(false)));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });
  }

  // Reveal on scroll
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  $$('.reveal').forEach(el => io.observe(el));

  // Count-up stats
  const counters = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target, end = +el.dataset.count, suffix = el.dataset.suffix || '';
      const t0 = performance.now(), dur = 1600;
      const tick = t => {
        const p = Math.min(1, (t - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - p, 3)));
        el.textContent = v + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      counters.unobserve(el);
    });
  }, { threshold: 0.6 });
  $$('[data-count]').forEach(el => counters.observe(el));

  // Drag-to-scroll showcase strip
  $$('.strip').forEach(strip => {
    let down = false, startX = 0, startLeft = 0;
    strip.addEventListener('pointerdown', e => {
      if (e.pointerType !== 'mouse') return;
      down = true; startX = e.clientX; startLeft = strip.scrollLeft; strip.classList.add('dragging');
    });
    window.addEventListener('pointerup', () => { down = false; strip.classList.remove('dragging'); });
    window.addEventListener('pointermove', e => { if (down) strip.scrollLeft = startLeft - (e.clientX - startX); });
    const wrap = strip.closest('section');
    const step = () => strip.clientWidth * 0.6;
    wrap && $('[data-strip="prev"]', wrap)?.addEventListener('click', () => strip.scrollBy({ left: -step(), behavior: 'smooth' }));
    wrap && $('[data-strip="next"]', wrap)?.addEventListener('click', () => strip.scrollBy({ left: step(), behavior: 'smooth' }));
  });

  // Logos: tabs between brands and clients, "show all" for long lists, staggered card entrance
  const lgTabs = $$('.lg-tabs button');
  const stagger = panel => $$('.lgc', panel).forEach((c, i) => { c.style.animation = 'none'; void c.offsetWidth; c.style.animation = ''; c.style.animationDelay = Math.min(i, 18) * 0.03 + 's'; });
  lgTabs.forEach(btn => btn.addEventListener('click', () => {
    lgTabs.forEach(b => b.classList.toggle('on', b === btn));
    $$('.lg-panel').forEach(p => { const on = p.dataset.panel === btn.dataset.lg; p.classList.toggle('off', !on); if (on) stagger(p); });
  }));
  $$('[data-lg-more]').forEach(b => b.addEventListener('click', () => b.closest('.lg-panel').classList.add('expanded')));

  // What we do best: earlier cards shrink and dim as the next one slides over them
  const stackCards = $$('.stack-card');
  if (stackCards.length && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const runStack = () => {
      const on = innerWidth > 900;
      stackCards.forEach((c, i) => {
        const nx = stackCards[i + 1];
        if (!on || !nx) { c.style.transform = ''; c.style.filter = ''; return; }
        const r = c.getBoundingClientRect(), n = nx.getBoundingClientRect();
        const o = Math.min(1, Math.max(0, 1 - (n.top - r.top) / r.height));
        c.style.transform = `scale(${1 - o * 0.06})`;
        c.style.filter = `brightness(${1 - o * 0.35})`;
      });
    };
    runStack();
    addEventListener('scroll', () => requestAnimationFrame(runStack), { passive: true });
    addEventListener('resize', runStack);
  }
  // What we do best: tabs
  $$('.wdb-tabs button').forEach(b => b.addEventListener('click', () => {
    const k = b.dataset.wdb;
    $$('.wdb-tabs button').forEach(x => { x.classList.toggle('on', x === b); x.setAttribute('aria-selected', x === b); });
    $$('.wdb-pane').forEach(p => p.classList.toggle('on', p.dataset.wdb === k));
  }));
  $$('[data-rv2-more]').forEach(b => b.addEventListener('click', () => b.closest('.reviews2').classList.add('all')));
  // Reviews (mobile): reveal the rest on demand
  $$('[data-rv-more]').forEach(b => b.addEventListener('click', () => b.closest('.greviews').classList.add('all-reviews')));

  // Project filters
  const filterBtns = $$('.filters button[data-filter]');
  const applyFilter = (f, animate = true) => {
    filterBtns.forEach(b => b.classList.toggle('on', b.dataset.filter === f));
    let n = 0;
    $$('.p-card').forEach(card => {
      const show = f === 'all' || card.dataset.sector === f;
      card.classList.toggle('hide', !show);
      if (show && animate) { card.classList.remove('pop'); void card.offsetWidth; card.style.animationDelay = (n % 6) * 0.06 + 's'; card.classList.add('pop'); }
      if (show) n++;
    });
    const cnt = $('[data-count-shown]'); if (cnt) cnt.textContent = n;
  };
  filterBtns.forEach(btn => btn.addEventListener('click', () => {
    applyFilter(btn.dataset.filter);
    if ($('[data-count-shown]')) history.replaceState(null, '', btn.dataset.filter === 'all' ? location.pathname : '#' + btn.dataset.filter);
  }));
  const h0 = location.hash.slice(1);
  if (h0 && filterBtns.some(b => b.dataset.filter === h0)) applyFilter(h0, false);
  else { const on = filterBtns.find(b => b.classList.contains('on')); if (on) applyFilter(on.dataset.filter, false); }

  // Gentle parallax on spotlight image
  const para = $$('[data-parallax]');
  if (para.length && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const run = () => {
      para.forEach(img => {
        const r = img.parentElement.getBoundingClientRect();
        if (r.bottom < 0 || r.top > innerHeight) return;
        const p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
        img.style.transform = `translateY(${p * -60 - 40}px)`;
      });
    };
    run();
    window.addEventListener('scroll', () => requestAnimationFrame(run), { passive: true });
  }

  // Film modal
  const filmModal = $('#film');
  if (filmModal) {
    const v = $('video', filmModal);
    const open = () => { filmModal.classList.add('open'); v.currentTime = 0; v.muted = false; v.play().catch(() => {}); };
    const close = () => { filmModal.classList.remove('open'); v.pause(); };
    $$('[data-film]').forEach(b => b.addEventListener('click', open));
    $('.close', filmModal).addEventListener('click', close);
    filmModal.addEventListener('click', e => { if (e.target === filmModal) close(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }

  // Gallery lightbox
  const lb = $('#lightbox');
  if (lb) {
    const items = $$('.gallery button');
    const img = $('img', lb), count = $('.count', lb);
    let i = 0;
    const show = n => {
      i = (n + items.length) % items.length;
      img.src = items[i].dataset.full;
      count.textContent = `${i + 1} / ${items.length}`;
    };
    items.forEach((b, n) => b.addEventListener('click', () => { show(n); lb.classList.add('open'); }));
    $('.prev', lb).addEventListener('click', () => show(i - 1));
    $('.next', lb).addEventListener('click', () => show(i + 1));
    $('.close', lb).addEventListener('click', () => lb.classList.remove('open'));
    lb.addEventListener('click', e => { if (e.target === lb) lb.classList.remove('open'); });
    document.addEventListener('keydown', e => {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') lb.classList.remove('open');
      if (e.key === 'ArrowLeft') show(i - 1);
      if (e.key === 'ArrowRight') show(i + 1);
    });
  }

  $$('form.qf').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const b = $('.qf-btn', f); b.textContent = 'Thanks! Prototype only'; b.disabled = true;
  }));
  // Prototype form: don't actually submit
  $$('form.quote').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const b = $('button', f);
    b.textContent = 'Thanks! Prototype Only';
  }));

  // ---------- v2 ----------
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Hero video shrinks into a framed card as you scroll
  const hero = $('.hero'), heroMedia = $('.hero-media'), heroContent = $('.hero-content');
  if (hero && heroMedia) {
    const run = () => {
      const p = Math.min(1, Math.max(0, window.scrollY / hero.offsetHeight));
      if (!reduce) {
        const inset = p * 7;
        heroMedia.style.clipPath = `inset(${inset}% ${inset}% ${inset}% ${inset}% round ${p * 22}px)`;
        if (heroContent) {
          heroContent.style.opacity = String(1 - p * 1.6);
          heroContent.style.transform = `translateY(${p * -60}px)`;
        }
      }
      const cue = $('.scroll-cue'); if (cue) cue.style.opacity = String(1 - p * 3);
    };
    run();
    window.addEventListener('scroll', () => requestAnimationFrame(run), { passive: true });
  }

  // Process: highlight the step whose image is in view; click a step to jump to its image
  const stepItems = $$('.steps li[data-step]');
  if (stepItems.length) {
    const figs = $$('.process .split-media figure');
    const sio = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const n = e.target.dataset.step;
        stepItems.forEach(li => li.classList.toggle('on', li.dataset.step === n));
        const ghost = $('.step-ghost'), label = String(+n + 1).padStart(2, '0');
        if (ghost && ghost.textContent !== label) {
          ghost.classList.add('swap');
          setTimeout(() => { ghost.textContent = label; ghost.classList.remove('swap'); }, 280);
        }
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    figs.forEach(f => sio.observe(f));
    // Images open up as they scroll in; brass rail tracks progress through the steps
    const fio = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); fio.unobserve(e.target); } }), { threshold: 0.2 });
    figs.forEach(f => fio.observe(f));
    const rail = $('.steps-rail i'), media = $('.process .split-media');
    if (rail && media) {
      const prog = () => {
        const r = media.getBoundingClientRect();
        const p = Math.min(1, Math.max(0, (innerHeight / 2 - r.top) / r.height));
        rail.style.height = (p * 100) + '%';
      };
      window.addEventListener('scroll', () => requestAnimationFrame(prog), { passive: true }); prog();
    }
    stepItems.forEach(li => li.addEventListener('click', () => {
      const f = figs.find(x => x.dataset.step === li.dataset.step);
      if (f) window.scrollTo({ top: f.getBoundingClientRect().top + scrollY - innerHeight * 0.04, behavior: 'smooth' });
    }));
  }

  // All projects timeline: wheel scrolls sideways, drag, progress bar, filters (+ #hash)
  const tl = $('.timeline');
  if (tl) {
    tl.addEventListener('wheel', e => {
      if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
        const atStart = tl.scrollLeft <= 0 && e.deltaY < 0;
        const atEnd = tl.scrollLeft + tl.clientWidth >= tl.scrollWidth - 1 && e.deltaY > 0;
        if (!atStart && !atEnd) { e.preventDefault(); tl.scrollLeft += e.deltaY; }
      }
    }, { passive: false });
    let down = false, sx = 0, sl = 0, moved = false;
    tl.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; moved = false; sx = e.clientX; sl = tl.scrollLeft; });
    window.addEventListener('pointermove', e => { if (!down) return; if (Math.abs(e.clientX - sx) > 4) { moved = true; tl.classList.add('dragging'); } tl.scrollLeft = sl - (e.clientX - sx); });
    window.addEventListener('pointerup', () => { down = false; tl.classList.remove('dragging'); });
    tl.addEventListener('click', e => { if (moved) { e.preventDefault(); moved = false; } }, true);
    const bar = $('.progress i');
    const upd = () => { if (bar) bar.style.width = (tl.scrollLeft / Math.max(1, tl.scrollWidth - tl.clientWidth) * 100) + '%'; };
    tl.addEventListener('scroll', upd, { passive: true }); upd();

    const btns = $$('.index-head .filters button');
    const count = $('[data-count-shown]');
    const apply = f => {
      btns.forEach(b => b.classList.toggle('on', b.dataset.filter === f));
      let n = 0;
      $$('.col', tl).forEach(c => { const show = f === 'all' || c.dataset.sector === f; c.classList.toggle('hide', !show); if (show) n++; });
      if (count) count.textContent = n;
      tl.scrollLeft = 0; upd();
    };
    btns.forEach(b => b.addEventListener('click', () => { apply(b.dataset.filter); history.replaceState(null, '', b.dataset.filter === 'all' ? location.pathname : '#' + b.dataset.filter); }));
    const hash = location.hash.slice(1);
    if (hash && btns.some(b => b.dataset.filter === hash)) apply(hash);
  }
})();

// FAQ accordion (one open at a time)
document.querySelectorAll('.faq-item button').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.parentElement, open = !item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => { i.classList.remove('open'); i.querySelector('button').setAttribute('aria-expanded', 'false'); });
    if (open) { item.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
  });
});

// Custom styled dropdowns for the quote form
(() => {
  const chev = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>';
  const tick = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>';
  const all = [];
  document.querySelectorAll('form.quote select').forEach(sel => {
    const wrap = document.createElement('div');
    wrap.className = 'cselect';
    sel.parentNode.insertBefore(wrap, sel);
    wrap.appendChild(sel);
    sel.tabIndex = -1;
    const btn = document.createElement('button');
    btn.type = 'button'; btn.className = 'cs-btn';
    btn.setAttribute('aria-haspopup', 'listbox'); btn.setAttribute('aria-expanded', 'false');
    const label = wrap.parentElement.querySelector('.flabel');
    if (label) btn.setAttribute('aria-label', label.textContent);
    const list = document.createElement('ul');
    list.className = 'cs-list'; list.setAttribute('role', 'listbox');
    [...sel.options].forEach((o, i) => {
      const li = document.createElement('li');
      li.setAttribute('role', 'option'); li.dataset.i = i;
      li.innerHTML = `<span>${o.text}</span>${tick}`;
      list.appendChild(li);
    });
    wrap.append(btn, list);
    let focus = sel.selectedIndex;
    const items = [...list.children];
    const render = () => {
      btn.innerHTML = `<span>${sel.options[sel.selectedIndex].text}</span>${chev}`;
      items.forEach((li, i) => { li.classList.toggle('sel', i === sel.selectedIndex); li.setAttribute('aria-selected', i === sel.selectedIndex); li.classList.toggle('focus', i === focus); });
    };
    const open = v => {
      all.forEach(a => a !== wrap && a.classList.remove('open'));
      wrap.classList.toggle('open', v); btn.setAttribute('aria-expanded', v);
      focus = sel.selectedIndex; render();
    };
    const choose = i => { sel.selectedIndex = i; sel.dispatchEvent(new Event('change', { bubbles: true })); open(false); btn.focus(); };
    btn.addEventListener('click', () => open(!wrap.classList.contains('open')));
    items.forEach((li, i) => li.addEventListener('click', () => choose(i)));
    btn.addEventListener('keydown', e => {
      const isOpen = wrap.classList.contains('open');
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        if (!isOpen) return open(true);
        focus = (focus + (e.key === 'ArrowDown' ? 1 : -1) + items.length) % items.length; render();
      } else if ((e.key === 'Enter' || e.key === ' ') && isOpen) { e.preventDefault(); choose(focus); }
      else if (e.key === 'Escape') open(false);
    });
    all.push(wrap);
    render();
  });
  document.addEventListener('click', e => all.forEach(w => { if (!w.contains(e.target)) w.classList.remove('open'); }));
})();

// Scroll-to-top button with scroll progress ring
(() => {
  const btn = document.createElement('button');
  btn.className = 'to-top'; btn.setAttribute('aria-label', 'Scroll to top');
  btn.innerHTML = '<svg class="ring" viewBox="0 0 56 56"><circle cx="28" cy="28" r="26"/><circle class="bar" cx="28" cy="28" r="26"/></svg><svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19V5M6 11l6-6 6 6"/></svg>';
  document.body.appendChild(btn);
  const bar = btn.querySelector('.bar'), C = 2 * Math.PI * 26;
  bar.style.strokeDasharray = C;
  const upd = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    const p = max > 0 ? scrollY / max : 0;
    bar.style.strokeDashoffset = C * (1 - p);
    btn.classList.toggle('show', scrollY > innerHeight * 0.6);
    const fc = document.querySelector('.float-call'); if (fc) fc.classList.toggle('show', btn.classList.contains('show'));
    btn.classList.toggle('lift', scrollY + innerHeight > document.documentElement.scrollHeight - 70);
  };
  upd();
  window.addEventListener('scroll', () => requestAnimationFrame(upd), { passive: true });
  window.addEventListener('resize', upd);
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
})();

// FAQ page: filter questions by topic
(() => {
  const tabs = document.querySelectorAll('.faq-tabs button');
  if (!tabs.length) return;
  tabs.forEach(t => t.addEventListener('click', () => {
    tabs.forEach(b => b.classList.toggle('on', b === t));
    const c = t.dataset.cat;
    document.querySelectorAll('.faq-page .faq-item').forEach(i => i.classList.toggle('hide', c !== 'all' && i.dataset.cat !== c));
  }));
})();

// ---------- Motion layer (Bright Sparks) ----------
(() => {
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('js-motion');

  // Scroll progress bar
  const bar = document.createElement('div');
  bar.className = 'scroll-bar';
  document.body.appendChild(bar);
  const setBar = () => { const h = document.documentElement.scrollHeight - innerHeight; bar.style.transform = `scaleX(${h > 0 ? scrollY / h : 0})`; };
  setBar(); addEventListener('scroll', () => requestAnimationFrame(setBar), { passive: true });

  if (reduce) return;

  // Headlines: words rise into place one after another
  const split = el => {
    let n = 0;
    const walk = node => {
      [...node.childNodes].forEach(c => {
        if (c.nodeType === 3) {
          const frag = document.createDocumentFragment();
          c.textContent.split(/(\s+)/).forEach(part => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            const w = document.createElement('span'); w.className = 'w';
            const i = document.createElement('span'); i.textContent = part; i.style.transitionDelay = (n++ * 0.06) + 's';
            w.appendChild(i); frag.appendChild(w);
          });
          c.replaceWith(frag);
        } else if (c.nodeType === 1) walk(c);
      });
    };
    walk(el); el.classList.add('split');
    el.style.setProperty('--hl-delay', (n * 0.06 + 0.15) + 's');
  };
  $$('.bs-hero h1, .page-hero h1, .section-head .h2, .r2-head .h2, .faq-side .h2, .stack-sec .h2, .showcase-head .h2, .areas .h2, .cta .h2, .ind-copy .h2, .contact-info .h2').forEach(split);
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.2 });
  $$('.split').forEach(el => io.observe(el));
  requestAnimationFrame(() => $$('.bs-hero .split, .page-hero .split').forEach(el => el.classList.add('in')));

  // Cards and list items arrive in a stagger
  $$('.r2-list, .feature-grid, .ind-cards, .included-list, .suburbs, .r2-proof, .hero-chips, .ph-chips, .faq-list, .strip').forEach(g => {
    [...g.children].forEach((c, i) => { c.style.transitionDelay = Math.min(i, 12) * 0.07 + 's'; c.classList.add('st'); });
    const o = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { g.classList.add('st-in'); o.disconnect(); } }), { threshold: 0.1 });
    o.observe(g);
  });

  // Service panels rise up one after another
  const panels = document.querySelector('.panels');
  if (panels) new IntersectionObserver((es, o) => es.forEach(e => { if (e.isIntersecting) { panels.classList.add('in'); o.disconnect(); } }), { threshold: 0.15 }).observe(panels);

  // Spotlight that follows the cursor on cards
  $$('.r2-card, .feature, .ind-card, .stack-card, .qf-card').forEach(c => c.addEventListener('pointermove', e => {
    const r = c.getBoundingClientRect();
    c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px');
  }));

  // Gentle 3D tilt on the banner quote card
  const qf = document.querySelector('.qf-card');
  if (qf && matchMedia('(hover: hover)').matches) {
    qf.addEventListener('pointermove', e => {
      const r = qf.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      qf.style.transform = `perspective(1200px) rotateY(${x * 4}deg) rotateX(${-y * 4}deg)`;
    });
    qf.addEventListener('pointerleave', () => { qf.style.transform = ''; });
  }

  // Banner photo drifts slower than the page
  const bg = document.querySelector('.bs-hero-bg');
  if (bg) addEventListener('scroll', () => requestAnimationFrame(() => { if (scrollY < innerHeight * 1.2) bg.style.translate = `0 ${scrollY * 0.25}px`; }), { passive: true });
})();
