(() => {
  const root = document.documentElement;
  root.classList.remove('no-js');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced) root.classList.add('reduced');
  const hasGsap = !!window.gsap;
  if (hasGsap && window.ScrollTrigger) gsap.registerPlugin(ScrollTrigger);

  /* ---------- smooth scroll ---------- */
  let lenis = null;
  if (!reduced && window.Lenis) {
    lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
    if (hasGsap) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(t => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    } else {
      const raf = t => { lenis.raf(t); requestAnimationFrame(raf); };
      requestAnimationFrame(raf);
    }
  }

  /* ---------- nav ---------- */
  const nav = document.querySelector('.nav');
  const megaBtn = document.querySelector('[data-mega]');
  const mega = document.querySelector('.mega');
  const veil = document.querySelector('.mega-veil');
  let lastY = 0;
  const onScroll = () => {
    const y = window.scrollY;
    nav.classList.toggle('is-solid', y > 20 || !document.querySelector('.hero, .phero'));
    const open = mega && mega.classList.contains('is-open');
    nav.classList.toggle('is-hidden', y > 400 && y > lastY && !open && !root.classList.contains('menu-open'));
    lastY = y;
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (megaBtn && mega) {
    let t;
    const open = () => { clearTimeout(t); mega.classList.add('is-open'); veil.classList.add('is-open'); megaBtn.setAttribute('aria-expanded', 'true'); nav.classList.add('is-solid'); };
    const close = () => { t = setTimeout(() => { mega.classList.remove('is-open'); veil.classList.remove('is-open'); megaBtn.setAttribute('aria-expanded', 'false'); onScroll(); }, 140); };
    megaBtn.addEventListener('mouseenter', open);
    megaBtn.addEventListener('click', () => mega.classList.contains('is-open') ? close() : open());
    megaBtn.addEventListener('mouseleave', close);
    mega.addEventListener('mouseenter', () => clearTimeout(t));
    mega.addEventListener('mouseleave', close);
    veil.addEventListener('click', close);
    addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }

  const burger = document.querySelector('.burger');
  if (burger) burger.addEventListener('click', () => {
    const on = root.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', on);
    nav.classList.add('is-solid');
    if (lenis) on ? lenis.stop() : lenis.start();
  });

  /* ---------- loader ---------- */
  const loader = document.querySelector('.loader');
  const seen = (() => { try { return sessionStorage.getItem('zp-loaded'); } catch (e) { return null; } })();
  const startPage = () => { document.dispatchEvent(new Event('zp:ready')); };
  if (loader && hasGsap && !reduced && !seen) {
    try { sessionStorage.setItem('zp-loaded', '1'); } catch (e) {}
    const tl = gsap.timeline({ onComplete: () => loader.remove() });
    tl.to('.loader__in img', { clipPath: 'inset(0 0% 0 0)', duration: 0.9, ease: 'power3.inOut' })
      .to('.loader__line', { scaleX: 1, duration: 0.7, ease: 'power3.inOut' }, '-=0.45')
      .to('.loader__line', { transformOrigin: 'right', scaleX: 0, duration: 0.5, ease: 'power3.in' }, '+=0.05')
      .to(loader, { yPercent: -100, duration: 0.85, ease: 'power4.inOut' }, '-=0.1')
      .add(startPage, '-=0.55');
  } else {
    if (loader) loader.remove();
    requestAnimationFrame(startPage);
  }

  /* ---------- hero carousel ---------- */
  const hero = document.querySelector('.hero');
  if (hero) {
    const words = [...hero.querySelectorAll('.hero__word')];
    const prods = [...hero.querySelectorAll('.hero__prod')];
    const tabs = [...hero.querySelectorAll('.hero__tab')];
    const caps = [...hero.querySelectorAll('.hero__cap')];
    words.forEach(w => { w.innerHTML = [...w.textContent].map(c => `<span>${c === ' ' ? '&nbsp;' : c}</span>`).join(''); });
    if (hasGsap && !reduced) {
      root.classList.add('js-hero');
      words.forEach(w => gsap.set(w.children, { yPercent: 110 }));
      words.forEach(w => w.style.visibility = 'visible');
    }
    let cur = -1, timer = null;
    const DUR = 6;
    const show = (i, first) => {
      if (i === cur) return;
      const prev = cur; cur = i;
      tabs.forEach((t, k) => t.classList.toggle('is-on', k === i));
      caps.forEach((c, k) => c.hidden = k !== i);
      if (!hasGsap || reduced) {
        words.forEach((w, k) => { w.style.visibility = k === i ? 'visible' : 'hidden'; w.querySelectorAll('span').forEach(s => s.style.transform = 'none'); });
        prods.forEach((p, k) => p.style.opacity = k === i ? 1 : 0);
        return;
      }
      if (prev > -1) {
        gsap.to(words[prev].children, { yPercent: -110, duration: 0.7, stagger: 0.03, ease: 'power3.in', overwrite: true });
        gsap.to(prods[prev], { opacity: 0, scale: 0.86, rotate: -10, x: -60, duration: 0.7, ease: 'power3.in', overwrite: true });
      }
      gsap.fromTo(words[i].children, { yPercent: 110 }, { yPercent: 0, duration: 1.1, stagger: 0.045, ease: 'power4.out', delay: first ? 0 : 0.45, overwrite: true });
      gsap.fromTo(prods[i], { opacity: 0, scale: 1.12, rotate: 10, x: 80 }, { opacity: 1, scale: 1, rotate: 0, x: 0, duration: 1.3, ease: 'power4.out', delay: first ? 0.15 : 0.6, overwrite: true });
      tabs.forEach(t => gsap.killTweensOf(t.querySelector('i')));
      tabs.forEach((t, k) => gsap.set(t.querySelector('i'), { scaleX: k < i ? 1 : 0 }));
      gsap.fromTo(tabs[i].querySelector('i'), { scaleX: 0 }, { scaleX: 1, duration: DUR, ease: 'none', onComplete: () => show((cur + 1) % words.length) });
    };
    tabs.forEach((t, k) => t.addEventListener('click', () => show(k)));
    document.addEventListener('zp:ready', () => {
      show(0, true);
      if (hasGsap && !reduced) {
        gsap.from('.hero h1 .mask > span', { yPercent: 105, duration: 1.1, stagger: 0.08, ease: 'power4.out', delay: 0.2 });
        gsap.from('.hero__side, .hero__top', { opacity: 0, y: 20, duration: 1, delay: 0.6, ease: 'power3.out' });
        gsap.to('.hero__stage', { yPercent: 18, ease: 'none', scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true } });
        gsap.to('.hero__words', { yPercent: 30, opacity: 0.2, ease: 'none', scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true } });
      }
    }, { once: true });
  }

  if (!hasGsap || reduced) {
    // still allow statement words to be readable
    document.querySelectorAll('.statement .w').forEach(w => w.style.color = 'inherit');
  }

  document.addEventListener('zp:ready', () => {
    if (!hasGsap || reduced) return;

    /* reveals */
    gsap.utils.toArray('.rv').forEach(el => {
      gsap.to(el, { opacity: 1, y: 0, duration: 1.1, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 88%' } });
    });
    gsap.utils.toArray('[data-split]').forEach(el => {
      gsap.from(el.querySelectorAll('.mask > span'), { yPercent: 105, duration: 1.1, stagger: 0.07, ease: 'power4.out', scrollTrigger: { trigger: el, start: 'top 85%' } });
    });
    gsap.utils.toArray('[data-stagger]').forEach(el => {
      gsap.from(el.children, { opacity: 0, y: 50, duration: 1, stagger: 0.07, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 85%' } });
    });
    const pheroH = document.querySelector('.phero h1, .contact h1');
    if (pheroH) gsap.from(pheroH.querySelectorAll('.mask > span'), { yPercent: 105, duration: 1.2, stagger: 0.08, ease: 'power4.out', delay: 0.1 });
    const pimg = document.querySelector('.phero__img img');
    if (pimg) gsap.from(pimg, { opacity: 0, scale: 1.1, x: 60, duration: 1.4, ease: 'power4.out', delay: 0.2 });

    /* statement word fill */
    const st = document.querySelector('.statement p');
    if (st) {
      gsap.to(st.querySelectorAll('.w'), { color: '#0d0f12', stagger: 0.1, ease: 'none', scrollTrigger: { trigger: st, start: 'top 80%', end: 'bottom 45%', scrub: true } });
    }

    /* counters */
    gsap.utils.toArray('[data-count]').forEach(el => {
      const end = +el.dataset.count; const from = +(el.dataset.from || 0); const o = { v: from };
      const sup = el.querySelector('sup'); const supHtml = sup ? sup.outerHTML : '';
      el.innerHTML = from + supHtml;
      gsap.to(o, { v: end, duration: 2, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 88%' }, onUpdate: () => el.innerHTML = Math.round(o.v) + supHtml });
    });

    /* product story pin */
    const story = document.querySelector('.story');
    if (story && matchMedia('(min-width:1081px)').matches) {
      const facts = [...story.querySelectorAll('.fact')];
      ScrollTrigger.create({
        trigger: story, start: 'top top', end: '+=260%', pin: '.story__pin', scrub: true,
        onUpdate: s => {
          const idx = Math.min(facts.length - 1, Math.floor(s.progress * facts.length));
          facts.forEach((f, k) => f.classList.toggle('is-on', k <= idx));
          gsap.set('.story__bar i', { scaleX: s.progress });
          gsap.set('.story__prod img', { rotate: s.progress * 120, scale: 0.9 + s.progress * 0.15 });
          gsap.set('.story__ring', { rotate: -s.progress * 60 });
        }
      });
    }

    /* subtle parallax inside image frames */
    gsap.utils.toArray('[data-par]').forEach(el => {
      gsap.fromTo(el, { yPercent: -6 }, { yPercent: 6, ease: 'none', scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } });
    });

    ScrollTrigger.refresh();
  }, { once: true });

  /* ---------- rail (drag + arrows) ---------- */
  document.querySelectorAll('[data-rail]').forEach(wrap => {
    const rail = wrap.querySelector('.rail');
    const step = () => rail.querySelector('.card').getBoundingClientRect().width + 6;
    wrap.querySelector('[data-prev]')?.addEventListener('click', () => rail.scrollBy({ left: -step(), behavior: 'smooth' }));
    wrap.querySelector('[data-next]')?.addEventListener('click', () => rail.scrollBy({ left: step(), behavior: 'smooth' }));
    let down = false, sx = 0, sl = 0, moved = false;
    rail.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; moved = false; sx = e.clientX; sl = rail.scrollLeft; });
    addEventListener('pointermove', e => { if (!down) return; const dx = e.clientX - sx; if (Math.abs(dx) > 4) { moved = true; rail.classList.add('is-drag'); } rail.scrollLeft = sl - dx; });
    addEventListener('pointerup', () => { if (!down) return; down = false; rail.classList.remove('is-drag'); });
    rail.addEventListener('click', e => { if (moved) { e.preventDefault(); moved = false; } }, true);
  });

  /* ---------- catalogues: show all ---------- */
  document.querySelectorAll('[data-more]').forEach(b => b.addEventListener('click', () => {
    const g = document.querySelector(b.dataset.more);
    const on = g.classList.toggle('is-all');
    b.querySelector('span').textContent = on ? 'Prikaži manj' : b.dataset.label;
    if (window.ScrollTrigger) ScrollTrigger.refresh();
  }));

  /* ---------- contact form ---------- */
  const form = document.querySelector('.form');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      let ok = true;
      form.querySelectorAll('[required]').forEach(inp => {
        const wrap = inp.closest('.field, .check');
        let valid = inp.type === 'checkbox' ? inp.checked : inp.value.trim().length > 1;
        if (inp.type === 'email') valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inp.value.trim());
        wrap.classList.toggle('err', !valid);
        if (!valid) ok = false;
      });
      if (ok) { form.classList.add('is-sent'); form.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
    });
    form.querySelectorAll('input, textarea').forEach(i => i.addEventListener('input', () => i.closest('.field, .check')?.classList.remove('err')));
  }
})();
