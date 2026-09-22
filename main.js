/* Energieberatung Regio Stolberg – Skript. GSAP + ScrollTrigger + Lenis (CDN). Alle Tweens nur auf transform/opacity/clip-path. */
(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) document.documentElement.classList.add('no-motion');
  gsap.registerPlugin(ScrollTrigger);
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  const $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const fmt = (n, d = 0) => n.toLocaleString('de-DE', { minimumFractionDigits: d, maximumFractionDigits: d });
  const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;

  // ---------- Lenis (weiches Scrollen), gekoppelt an ScrollTrigger ----------
  let lenis;
  if (!reduce) {
    lenis = new Lenis({ lerp: 0.09, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
  }
  const scrollToEl = (el, off = -80) => lenis ? lenis.scrollTo(el, { offset: off, duration: 1.2 }) : el.scrollIntoView({ behavior: 'smooth' });

  // ---------- Kopfzeile: Aufklappliste, Menü, Verhalten beim Scrollen ----------
  const head = $('#head');
  const subBtn = $('.has-sub > button'), sub = $('#subnav');
  const setSub = open => { subBtn.setAttribute('aria-expanded', open ? 'true' : 'false'); sub.classList.toggle('open', open); };
  subBtn.addEventListener('click', () => setSub(subBtn.getAttribute('aria-expanded') !== 'true'));
  const hasSub = $('.has-sub');
  if (fine) { hasSub.addEventListener('mouseenter', () => setSub(true)); hasSub.addEventListener('mouseleave', () => setSub(false)); }
  hasSub.addEventListener('focusout', e => { if (!hasSub.contains(e.relatedTarget)) setSub(false); });

  const menu = $('#menu'), menuBtn = $('.menu-btn');
  $$('li', menu).forEach((li, i) => li.style.setProperty('--i', i));
  let lastFocus;
  const closeMenu = () => {
    if (!menu.classList.contains('open')) return;
    document.body.classList.remove('menu-open'); menu.classList.remove('open');
    menuBtn.setAttribute('aria-expanded', 'false'); $('.lbl', menuBtn).textContent = 'Menü';
    lenis && lenis.start(); lastFocus && lastFocus.focus();
  };
  const openMenu = () => {
    lastFocus = document.activeElement;
    document.body.classList.add('menu-open'); menu.classList.add('open');
    menuBtn.setAttribute('aria-expanded', 'true'); $('.lbl', menuBtn).textContent = 'Schließen';
    lenis && lenis.stop(); setTimeout(() => $('a', menu).focus(), 400);
  };
  menuBtn.addEventListener('click', () => menu.classList.contains('open') ? closeMenu() : openMenu());
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') { if (menu.classList.contains('open')) { closeMenu(); menuBtn.focus(); } setSub(false); }
    if (e.key === 'Tab' && menu.classList.contains('open')) {
      const f = $$('a, button', menu).filter(x => x.offsetParent); const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); menuBtn.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); menuBtn.focus(); }
      else if (!e.shiftKey && document.activeElement === menuBtn) { e.preventDefault(); first.focus(); }
    }
  });
  const hasHero = !!$('.scene') && !reduce;
  if (hasHero) document.body.classList.add('over-hero');
  let lastY = 0;
  ScrollTrigger.create({ onUpdate: () => {
    const y = scrollY;
    head.classList.toggle('solid', !hasHero || y > 40);
    head.classList.toggle('hide', y > lastY + 6 && y > 400 && !document.body.classList.contains('menu-open'));
    if (Math.abs(y - lastY) > 6) lastY = y;
  } });
  head.classList.toggle('solid', !hasHero || scrollY > 40);

  // ---------- Wort-für-Wort-Reveals ----------
  $$('.split').forEach(el => {
    const words = el.textContent.trim().split(/\s+/);
    el.setAttribute('aria-label', words.join(' '));
    el.innerHTML = words.map(w => `<span class="split-line" aria-hidden="true"><span class="w">${w}</span></span>`).join(' ');
  });

  // ---------- Vorhang + Brand-Intro (nur beim ersten Besuch) ----------
  let seen = false; try { seen = sessionStorage.getItem('eb-intro'); } catch (e) {}
  if (!seen && !reduce) {
    try { sessionStorage.setItem('eb-intro', '1'); } catch (e) {}
    document.body.classList.add('intro-on');
  }
  $$('a[href$=".html"], a[href*=".html#"], a[href*=".html?"]').forEach(a => a.addEventListener('click', e => {
    if (e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank' || reduce) return;
    const href = a.getAttribute('href'); if (/^https?:/.test(href)) return;
    const [path] = href.split(/[#?]/), here = location.pathname.split('/').pop() || 'index.html';
    if (path === here && href.includes('#')) { const el = $('#' + href.split('#')[1]); if (el) { e.preventDefault(); closeMenu(); scrollToEl(el); return; } }
    e.preventDefault(); closeMenu(); document.body.classList.add('leaving');
    setTimeout(() => location.href = href, 520);
  }));
  $$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
    const id = a.getAttribute('href'); if (id.length < 2) return;
    const el = $(id); if (!el) return; e.preventDefault(); closeMenu(); scrollToEl(el);
  }));
  addEventListener('pageshow', e => { if (e.persisted) document.body.classList.remove('leaving'); });

  // ---------- Fortschrittsbalken, Sticky-CTA, nach oben ----------
  const prog = $('#progress');
  ScrollTrigger.create({ onUpdate: s => prog.style.transform = `scaleX(${s.progress})` });
  const sticky = $('.sticky-cta');
  const first = $('.scene') || $('.ph');
  ScrollTrigger.create({ start: () => (first ? first.offsetTop + first.offsetHeight - innerHeight * .6 : 300), end: 'max', onToggle: t => sticky.classList.toggle('show', t.isActive) });
  $$('.totop').forEach(a => a.addEventListener('click', e => { e.preventDefault(); lenis ? lenis.scrollTo(0, { duration: 1.2 }) : scrollTo({ top: 0, behavior: 'smooth' }); }));

  // ---------- Magnetische Buttons mit Lichtreflex, 3D-Tilt ----------
  if (fine && !reduce) {
    $$('.btn').forEach(b => {
      b.addEventListener('mousemove', e => {
        const r = b.getBoundingClientRect(); const x = e.clientX - r.left, y = e.clientY - r.top;
        b.style.setProperty('--mx', x + 'px'); b.style.setProperty('--my', y + 'px');
        gsap.to(b, { x: (x - r.width / 2) * .2, y: (y - r.height / 2) * .3, duration: .45, ease: 'power3.out' });
      });
      b.addEventListener('mouseleave', () => gsap.to(b, { x: 0, y: 0, duration: .7, ease: 'elastic.out(1,.5)' }));
    });
    $$('.tilt').forEach(c => {
      c.addEventListener('mousemove', e => { const r = c.getBoundingClientRect(); const px = (e.clientX - r.left) / r.width - .5, py = (e.clientY - r.top) / r.height - .5; gsap.to(c, { rotateY: px * 6, rotateX: -py * 6, transformPerspective: 900, duration: .5, ease: 'power2.out' }); });
      c.addEventListener('mouseleave', () => gsap.to(c, { rotateY: 0, rotateX: 0, duration: .8, ease: 'power3.out' }));
    });
  }

  // ---------- Allgemeine Reveals (nicht in der Szene) ----------
  if (!reduce) {
    $$('.split').filter(el => !el.closest('.scene')).forEach(el => {
      gsap.to($$('.w', el), { y: 0, duration: 1, ease: 'expo.out', stagger: .045, scrollTrigger: { trigger: el, start: 'top 88%', once: true }, onComplete: () => el.classList.add('done') });
    });
    $$('.reveal').forEach(el => gsap.to(el, { opacity: 1, y: 0, duration: .9, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 90%', once: true } }));
  }

  // ---------- Szene: Foto-Scroll-Through ----------
  const scene = $('.scene');
  if (scene && !reduce) {
    // Fotos ab Bild 2 erst nach "load"
    const late = () => $$('[data-late]', scene).forEach(i => { if (i.dataset.src) { if (i.dataset.srcset) i.srcset = i.dataset.srcset; i.src = i.dataset.src; } });
    document.readyState === 'complete' ? late() : addEventListener('load', late);
    const caps = [1, 2, 3, 4, 5].map(n => $('.cap.c' + n, scene));
    const W = c => $$('.w', c);
    // erste Bildunterschrift beim Laden
    gsap.set(caps[0], { autoAlpha: 1 });
    gsap.fromTo(W(caps[0]), { y: '110%' }, { y: '0%', duration: 1.1, ease: 'expo.out', stagger: .05, delay: seen ? .3 : 1.3 });
    const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { trigger: scene, start: 'top top', end: 'bottom bottom', scrub: .8 } });
    const capIn = (i, at, dur = .045) => tl.set(caps[i], { autoAlpha: 1 }, at).fromTo(W(caps[i]), { y: '110%' }, { y: '0%', duration: dur, stagger: dur / W(caps[i]).length, ease: 'power2.out' }, at);
    const capOut = (i, at, dur = .035) => tl.to(W(caps[i]), { y: '-110%', duration: dur, stagger: dur / W(caps[i]).length, ease: 'power2.in' }, at).set(caps[i], { autoAlpha: 0 }, at + dur * 2);
    tl.fromTo('.f1 > img:first-child', { scale: 1.1 }, { scale: 1, duration: .16 }, 0);
    capOut(0, .09);
    // Blende 1: Wärmebild-Blende (Foto kippt von oben nach unten ins Falschfarbenbild), dann ins nächste Foto
    tl.to('.f1 .warm', { clipPath: 'inset(0 0 0% 0)', duration: .13 }, .12);
    tl.to('.f2', { opacity: 1, duration: .07 }, .27);
    capIn(1, .31); capOut(1, .44);
    // Blende 2: Fenster-Blende (Foto 3 wächst aus einem gerahmten Fenster)
    tl.set('.f3', { opacity: 1 }, .47).fromTo('.f3 .win', { scale: .22 }, { scale: 1, duration: .13, ease: 'power2.inOut' }, .47);
    capIn(2, .58); capOut(2, .70);
    // Blende 3: Schärfe-Blende (nur vorgerechnete Unschärfe-Bilder, nur Opacity)
    tl.to('.f3 .blur', { opacity: 1, duration: .05 }, .71);
    tl.set('.f4 .blur', { opacity: 1 }, .71).to('.f4', { opacity: 1, duration: .04 }, .76);
    tl.to('.f4 .blur', { opacity: 0, duration: .05 }, .80);
    capIn(3, .84); capOut(3, .93);
    // Blende 4: Scan-Blende (Messlinie fährt über das Bild, dahinter liegt Foto 5)
    tl.set('.f5', { opacity: 1, clipPath: 'inset(0 100% 0 0)' }, .92).to('.f5', { clipPath: 'inset(0 0% 0 0)', duration: .06 }, .92);
    tl.fromTo('.scanline', { x: 0, opacity: 1 }, { x: '104vw', duration: .06 }, .92).set('.scanline', { opacity: 0 }, .985);
    capIn(4, .955, .04);
    tl.fromTo('.temp-fill', { scaleY: 0 }, { scaleY: 1, duration: 1 }, 0);
  } else if (scene) {
    scene.remove(); $('.scene-static').hidden = false;
  }

  // ---------- Drei Kreise ----------
  const rings = $('.ring-wrap');
  if (rings && !reduce) {
    const tl = gsap.timeline({ scrollTrigger: { trigger: rings, start: 'top 85%', end: 'top 30%', scrub: .8 } });
    tl.fromTo('.ring.r1', { xPercent: -50, x: '-45vw', yPercent: -50 }, { x: 0, ease: 'power2.out' }, 0)
      .fromTo('.ring.r3', { xPercent: -50, x: '45vw', yPercent: -50 }, { x: 0, ease: 'power2.out' }, 0)
      .fromTo('.ring.r2', { xPercent: -50, yPercent: -50, scale: 0 }, { scale: 1, ease: 'back.out(1.4)' }, .15)
      .to('.ring span', { opacity: 1, stagger: .12, duration: .3 }, .6);
  }

  // ---------- Wärmebild-Lupe (Signature) ----------
  const lensSec = $('.lens-sec');
  if (lensSec && !reduce) {
    const photo = $('.lens-photo'), tags = $$('.tag', lensSec);
    const pts = [[18, 28], [63, 36], [34, 52], [50, 58], [40, 78], [72, 70]]; // Pfad der Linse in Prozent
    let manual = false, manualTimer;
    const setLens = (x, y, r) => { photo.style.setProperty('--x', x + '%'); photo.style.setProperty('--y', y + '%'); photo.style.setProperty('--r', r + 'px'); };
    const showTags = p => { // Hinweis erscheint, wenn die Linse den Punkt passiert hat
      const per = 1 / (pts.length - 1);
      tags.forEach((t, i) => { const at = (i + 1) * per; gsap.to(t, { opacity: p > at - .04 && p < at + per * 1.6 ? 1 : 0, y: p > at - .04 ? 0 : 8, duration: .3, overwrite: true }); });
    };
    ScrollTrigger.create({ trigger: lensSec, start: 'top top', end: 'bottom bottom', scrub: true, onUpdate: s => {
      if (manual) return;
      const p = s.progress, seg = (pts.length - 1), i = Math.min(seg - 1, Math.floor(p * seg)), k = p * seg - i;
      const ease = k * k * (3 - 2 * k);
      const x = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * ease, y = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * ease;
      const r = photo.offsetWidth * (p < .08 ? p / .08 * .17 : .17);
      setLens(x, y, r); showTags(p);
    } });
    if (fine) {
      photo.addEventListener('mousemove', e => {
        const b = photo.getBoundingClientRect(); manual = true; clearTimeout(manualTimer);
        setLens((e.clientX - b.left) / b.width * 100, (e.clientY - b.top) / b.height * 100, photo.offsetWidth * .17);
        manualTimer = setTimeout(() => manual = false, 1200);
      });
      photo.addEventListener('mouseleave', () => { manual = false; ScrollTrigger.update(); });
    }
  }

  // ---------- Effizienzklassen-Skala ----------
  const scale = $('.scale');
  if (scale && !reduce) {
    const bars = $$('.bar', scale), marker = $('.marker', scale);
    const rowY = i => bars[i].offsetTop + bars[i].offsetHeight / 2 - marker.offsetHeight / 2 + 4;
    gsap.set(marker, { y: () => rowY(7) });
    const tl = gsap.timeline({ scrollTrigger: { trigger: scale, start: 'top 80%', end: 'bottom 40%', scrub: .8, invalidateOnRefresh: true } });
    tl.to(bars, { scaleX: 1, stagger: .06, duration: .5, ease: 'power2.out' }, 0)
      .to(marker, { y: () => rowY(2), duration: .6, ease: 'power2.inOut' }, .45);
  }

  // ---------- Hausakte: Schubladen ----------
  const drawers = $('.drawers');
  if (drawers && !reduce) {
    gsap.to($$('.drawer', drawers), { x: 0, opacity: 1, stagger: .05, duration: .6, ease: 'power3.out', scrollTrigger: { trigger: drawers, start: 'top 85%', end: 'top 35%', scrub: .7 } });
  }

  // ---------- Zitat um die Ecke ----------
  const q = $('.q-block');
  if (q && !reduce) gsap.to(q, { rotateY: 0, x: 0, opacity: 1, ease: 'power2.out', scrollTrigger: { trigger: $('.quote3d'), start: 'top 80%', end: 'top 20%', scrub: .8 } });

  // ---------- Förder-Beleg druckt sich ----------
  const paper = $('.paper');
  if (paper && !reduce) {
    const tl = gsap.timeline({ scrollTrigger: { trigger: paper, start: 'top 85%', end: 'bottom 55%', scrub: .8 } });
    tl.to(paper, { clipPath: 'inset(0 0 -2% 0)', duration: 1, ease: 'none' }, 0)
      .to($$('.r-line', paper), { opacity: 1, y: 0, stagger: .1, duration: .25, ease: 'power2.out' }, .1);
  }

  // ---------- Stempel ----------
  const stamps = $$('.stamp');
  if (stamps.length && !reduce) gsap.to(stamps, { scale: 1, rotate: 0, opacity: 1, duration: .38, ease: 'power4.out', stagger: .14, scrollTrigger: { trigger: $('.stamps'), start: 'top 85%', once: true } });

  // ---------- Unterseiten: klebendes Inhaltsverzeichnis ----------
  const toc = $('.toc');
  if (toc) {
    const links = $$('a', toc);
    links.forEach(a => { const sec = $(a.getAttribute('href')); if (!sec) return;
      ScrollTrigger.create({ trigger: sec, start: 'top 45%', end: 'bottom 45%', onToggle: t => { if (t.isActive) { links.forEach(l => l.classList.remove('on')); a.classList.add('on'); } } });
    });
  }

  // ---------- Donut: Förderung der Beratung ----------
  const donut = $('.donut');
  if (donut) {
    const C = 2 * Math.PI * 70, segs = { eigen: $('.s-eigen'), zuschuss: $('.s-zuschuss'), weg: $('.s-weg') };
    const legend = $$('.d-legend button'), val = $('.d-val'), lbl = $('.d-lbl'), note = $('.d-note');
    let state = { fee: 1300, cap: 650, weg: 0, sel: 'eigen' };
    const texts = { eigen: v => `Ihr Eigenanteil nach Abzug des Zuschusses. Das Honorar ist ein Richtwert.`, zuschuss: v => `Der Zuschuss beträgt 50 % des Honorars, höchstens ${fmt(state.cap)} € ${state.cap === 650 ? 'beim Ein-/Zweifamilienhaus' : 'ab drei Wohneinheiten'}.`, weg: v => `Einmalig 250 € pro WEG, wenn wir die Ergebnisse in der Eigentümerversammlung erläutern.` };
    const draw = () => {
      const zuschuss = Math.min(state.fee * .5, state.cap), eigen = state.fee - zuschuss, weg = state.weg, total = state.fee + weg;
      const parts = [['eigen', eigen], ['zuschuss', zuschuss], ['weg', weg]]; let off = 0;
      parts.forEach(([k, v]) => { const len = C * v / total; segs[k].style.strokeDasharray = `${len} ${C}`; segs[k].style.strokeDashoffset = -off; off += len; segs[k].classList.toggle('on', state.sel === k); });
      legend.forEach(b => { const k = b.dataset.k; const v = { eigen, zuschuss, weg }[k]; $('b', b).textContent = fmt(v) + ' €'; b.hidden = k === 'weg' && !weg; b.classList.toggle('on', state.sel === k); });
      const v = { eigen, zuschuss, weg }[state.sel]; val.textContent = fmt(v) + ' €'; lbl.textContent = { eigen: 'Eigenanteil', zuschuss: 'BAFA-Zuschuss', weg: 'WEG-Zuschlag' }[state.sel]; note.textContent = texts[state.sel](v);
    };
    $$('.donut-ctl .chip').forEach(c => c.addEventListener('click', () => { $$('.donut-ctl .chip').forEach(x => x.classList.remove('on')); c.classList.add('on'); state.fee = +c.dataset.fee; state.cap = +c.dataset.cap; state.weg = +(c.dataset.weg || 0); if (state.sel === 'weg' && !state.weg) state.sel = 'eigen'; draw(); }));
    [...legend, ...Object.values(segs)].forEach(el => el.addEventListener('click', () => { state.sel = el.dataset.k; draw(); }));
    draw();
  }

  // ---------- Entscheidungsweiche: welcher Energieausweis ----------
  const weiche = $('#weiche-tool');
  if (weiche) {
    const steps = $$('.w-step', weiche), result = $('.w-result', weiche);
    const show = (k, title, text) => { result.hidden = false; $('b', result).textContent = title; $('p', result).textContent = text; };
    const next = (q, a) => {
      const st = { neubau: a => a === 'ja' ? ['R', 'Energiebedarfsausweis', 'Für Neubauten ist ein Bedarfsausweis auf Basis der energetischen Eigenschaften des fertigen Gebäudes auszustellen. Ein Verbrauchsausweis ist nicht zulässig, weil drei Jahre Verbrauchsdaten fehlen.'] : 'denkmal',
        denkmal: a => a === 'ja' ? ['R', 'Baudenkmal: bisher keine Pflicht, bald schon', 'Bei Verkauf und Vermietung war bisher kein Ausweis nötig. Mit dem GModG (Kabinettsbeschluss 13. Mai 2026) kommt die Pflicht. Wir stellen Bedarfs- oder Verbrauchsausweise für Baudenkmale schon jetzt aus.'] : 'we',
        we: a => a === 'ja' ? ['R', 'Verbrauchsausweis möglich', 'Bei fünf oder mehr Wohneinheiten darf unabhängig von Baujahr und Sanierungszustand ein Verbrauchsausweis auf Basis der letzten drei Abrechnungsperioden erstellt werden. Ein Bedarfsausweis ist ebenfalls möglich und aussagekräftiger.'] : 'alt',
        alt: a => a === 'ja' ? ['R', 'Energiebedarfsausweis', 'Für Wohngebäude mit weniger als fünf Wohnungen und Bauantrag vor dem 1. November 1977, die die Wärmeschutzverordnung von 1977 nicht erfüllen, ist ein Bedarfsausweis Pflicht. Wir nehmen das Gebäude vor Ort auf.'] : ['R', 'Verbrauchs- oder Bedarfsausweis', 'Beide Formen sind zulässig. Der Verbrauchsausweis ist günstiger und schnell erstellt, der Bedarfsausweis sagt mehr über das Gebäude aus, weil er nicht vom Heizverhalten abhängt. Wir beraten Sie, welcher sinnvoll ist.'] };
      const r = st[q](a);
      if (Array.isArray(r)) show(...r); else { const s = steps.find(x => x.dataset.q === r); s.hidden = false; setTimeout(() => $('button', s).focus(), 50); }
    };
    steps.forEach(s => $$('button', s).forEach(b => b.addEventListener('click', () => {
      const idx = steps.indexOf(s);
      steps.slice(idx + 1).forEach(x => { x.hidden = true; x.classList.remove('answered'); $$('button', x).forEach(y => y.classList.remove('on')); });
      result.hidden = true;
      $$('button', s).forEach(x => x.classList.remove('on')); b.classList.add('on'); s.classList.add('answered');
      next(s.dataset.q, b.dataset.a);
    })));
    $('.w-reset', weiche).addEventListener('click', () => { steps.forEach((x, i) => { x.hidden = i > 0; x.classList.remove('answered'); $$('button', x).forEach(y => y.classList.remove('on')); }); result.hidden = true; $('button', steps[0]).focus(); });
  }

  // ---------- Wärmebrücken: ohne/mit Nachweis ----------
  const wb = $('.wb');
  if (wb) $$('.wb-ctl .chip').forEach(c => c.addEventListener('click', () => {
    $$('.wb-ctl .chip').forEach(x => x.classList.remove('on')); c.classList.add('on');
    const add = c.dataset.wb === 'mit' ? .03 : .10;
    $$('.add', wb).forEach(i => i.style.setProperty('--v', add));
    $('.wb-add', wb).textContent = '+ ' + fmt(add, 2); $('.wb-sum', wb).textContent = fmt(.2 + add, 2); $('.wb-pct', wb).textContent = Math.round(add / .2 * 100) + ' %';
  }));

  // ---------- Taupunkt-Rechner (Magnus-Formel) ----------
  const tp = $('.tp');
  if (tp) {
    let T = 20, H = 60;
    const dew = (t, rh) => { const a = 17.62, b = 243.12; const g = Math.log(rh / 100) + a * t / (b + t); return b * g / (a - g); };
    const draw = () => {
      const d = dew(T, H);
      const mold = dew(T, Math.min(100, H / .8));
      $('#tp-dew').textContent = fmt(d, 1) + ' °C'; $('#tp-mold').textContent = fmt(mold, 1) + ' °C';
      const note = $('#tp-note'); const lai = 13;
      if (lai < d) { note.textContent = `Eine Fensterlaibung mit ${lai} °C liegt unter dem Taupunkt: Hier fällt Tauwasser aus, Schimmel ist nur eine Frage der Zeit.`; note.className = 'tp-note warn'; }
      else if (lai < mold) { note.textContent = `Eine Fensterlaibung mit ${lai} °C liegt unter der Schimmelgrenze: Hier wächst Schimmel, auch ohne sichtbares Tauwasser.`; note.className = 'tp-note warn'; }
      else { note.textContent = `Eine Fensterlaibung mit ${lai} °C bleibt oberhalb der Schimmelgrenze. Bei dieser Luftfeuchte ist die Oberfläche unkritisch.`; note.className = 'tp-note'; }
    };
    $$('.tp-ctl .chip').forEach(c => c.addEventListener('click', () => { const g = c.parentElement; $$('.chip', g).forEach(x => x.classList.remove('on')); c.classList.add('on'); if (c.dataset.t) T = +c.dataset.t; if (c.dataset.h) H = +c.dataset.h; draw(); }));
    draw();
  }

  // ---------- Wertermittlung: Faktor-Rechnung ----------
  const fk = $('.fk');
  if (fk) {
    let M = 24000, F = 22, S = 120000;
    const draw = () => { const b = M * F, n = b - S; $('#fk-brutto').textContent = fmt(b) + ' €'; $('#fk-san').textContent = '− ' + fmt(S) + ' €'; $('#fk-netto').textContent = fmt(n) + ' €';
      $('#fk-note').textContent = S ? `Der Sanierungsbedarf drückt den Wert um ${Math.round(S / b * 100)} %. Ein Gutachten setzt diese Kosten belastbar an.` : 'Ohne Sanierungsbedarf stimmt die Faktor-Rechnung. Ob das für Ihr Objekt gilt, klärt die Bestandsaufnahme.'; };
    $$('.fk-ctl .chip').forEach(c => c.addEventListener('click', () => { const g = c.parentElement; $$('.chip', g).forEach(x => x.classList.remove('on')); c.classList.add('on'); if (c.dataset.m) M = +c.dataset.m; if (c.dataset.f) F = +c.dataset.f; if (c.dataset.s !== undefined) S = +c.dataset.s; draw(); }));
    draw();
  }

  // ---------- Formular: Vorwahl per ?thema=, Prüfung, Netlify-Versand ----------
  $$('.form').forEach(form => {
    const thema = new URLSearchParams(location.search).get('thema');
    const sel = $('select[name=thema]', form);
    if (thema && sel && [...sel.options].some(o => o.value === thema)) sel.value = thema;
    const fields = $$('[required]', form);
    const check = el => { const f = el.closest('.field'); const ok = el.type === 'checkbox' ? el.checked : el.type === 'email' ? /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value) : el.value.trim().length > 1; f.classList.toggle('invalid', !ok); return ok; };
    fields.forEach(el => el.addEventListener('input', () => el.closest('.field').classList.contains('invalid') && check(el)));
    form.addEventListener('submit', e => {
      const bad = fields.filter(el => !check(el));
      if (bad.length) { e.preventDefault(); bad[0].focus(); return; }
      if (location.protocol === 'file:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1' || location.hostname.endsWith('github.io')) { e.preventDefault(); document.body.classList.add('leaving'); setTimeout(() => location.href = 'danke.html', 400); }
    });
  });

  // ---------- Karte erst per Klick ----------
  const mapBtn = $('#map-btn');
  if (mapBtn) mapBtn.addEventListener('click', () => {
    const m = $('#map'); m.classList.add('loaded');
    m.innerHTML = '<iframe title="Karte: Kortumstraße 8, 52222 Stolberg" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=6.2180%2C50.7680%2C6.2380%2C50.7770&amp;layer=mapnik&amp;marker=50.7726%2C6.2280"></iframe>';
  });

  // ---------- ScrollTrigger nach Schrift- und Bild-Load neu messen ----------
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => ScrollTrigger.refresh());
  addEventListener('load', () => setTimeout(() => ScrollTrigger.refresh(), 200));
  requestAnimationFrame(() => document.body.classList.add('ready'));
})();
