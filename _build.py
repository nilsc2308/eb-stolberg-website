# -*- coding: utf-8 -*-
"""Generator für die Website der Energieberatung Regio Stolberg: gemeinsamer Kopf/Fuß, alle Seiten, Sitemap.
Aufruf: python3 _build.py   (erzeugt die HTML-Dateien neben dieser Datei)"""
import json, os
OUT = os.path.dirname(os.path.abspath(__file__)) + '/'
DOMAIN = 'https://www.eb-stolberg.de'
TODAY = '2026-09-22'
VER = '20260922-1'
CO = dict(name='Renate Barlé Hausdienste', brand='Energieberatung Regio Stolberg', street='Kortumstraße 8', zip='52222', city='Stolberg',
          tel='0173 730 84 67', telh='+4917373084 67'.replace(' ', ''), mail='energieberatung@regio-stolberg.de', person='Dipl.-Ing. Marijan Barlé', lat='50.7726', lon='6.2280')

# Drei Kreise aus der Grafik der alten Website
MARK = '<svg viewBox="0 0 64 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="18" cy="20" r="17" fill="#2aabe2" opacity=".85"/><circle cx="32" cy="20" r="17" fill="#2aabe2" opacity=".85"/><circle cx="46" cy="20" r="17" fill="#2aabe2" opacity=".85"/></svg>'
LOGO = f'<span class="mark">{MARK}</span><span class="wordmark"><b>Energieberatung</b><i>Regio Stolberg</i></span>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.9 2z"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'

SERVICES = [  # Datei, Menütitel, Kurzbeschreibung (für Hausakte und Fußzeile)
    ('energieberatung.html', 'Energieberatung & Sanierungsfahrplan', 'Beratung'),
    ('energieausweis.html', 'Energieausweis & Baudenkmal', 'Nachweise'),
    ('baubegleitung.html', 'Baubegleitung & Wärmebrücken', 'Beratung'),
    ('thermografie-feuchteschutz.html', 'Thermografie & Feuchteschutz', 'Diagnose'),
    ('wertermittlung.html', 'Wertermittlung', 'Nachweise'),
]
NAV_L = [('leistungen', 'Leistungen'), ('ratgeber.html', 'Ratgeber'), ('ueber-uns.html', 'Über uns')]
ALLNAV = [('index.html', 'Start')] + [(f, t) for f, t, _ in SERVICES] + [('ratgeber.html', 'Ratgeber'), ('ueber-uns.html', 'Über uns'), ('faq.html', 'Häufige Fragen'), ('kontakt.html', 'Kontakt')]


def img(name, alt, w, h, cls='', lazy=True, sizes='(max-width: 820px) 100vw, 50vw'):
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ''
    return f'<img src="img/{name}-l.webp" srcset="img/{name}-m.webp 800w, img/{name}-l.webp 1200w, img/{name}.webp {w}w" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}"{load}{c}>'


def head(p):
    ld = [{
        "@context": "https://schema.org", "@type": "LocalBusiness", "@id": DOMAIN + "/#business", "name": CO['brand'], "legalName": CO['name'],
        "description": "Unabhängige Energieberatung für Wohngebäude in Stolberg und der Region Aachen: BAFA/KfW-Beratung, individueller Sanierungsfahrplan, Energieausweise, Baubegleitung, Wärmebrückenberechnung, Thermografie, Feuchteschutz und Wertermittlung.",
        "url": DOMAIN + "/", "telephone": "+49 173 7308467", "email": CO['mail'], "image": DOMAIN + "/img/og.jpg", "logo": DOMAIN + "/favicon.svg", "priceRange": "€€",
        "address": {"@type": "PostalAddress", "streetAddress": CO['street'], "postalCode": CO['zip'], "addressLocality": CO['city'], "addressRegion": "Nordrhein-Westfalen", "addressCountry": "DE"},
        "geo": {"@type": "GeoCoordinates", "latitude": float(CO['lat']), "longitude": float(CO['lon'])},
        "areaServed": ["Stolberg", "Aachen", "Eschweiler", "Alsdorf", "Roetgen", "Monschau", "Simmerath", "Düren", "Jülich", "Städteregion Aachen"],
        "employee": {"@type": "Person", "name": "Marijan Barlé", "jobTitle": "Dipl.-Ing., Gebäude-Energieberater (HWK)"},
        "memberOf": [{"@type": "Organization", "name": "Ingenieurkammer-Bau NRW"}, {"@type": "Organization", "name": "Deutsches Energieberater-Netzwerk DEN e.V."}, {"@type": "Organization", "name": "Verband Privater Bauherren e.V."}]
    }]
    if p.get('ld'): ld.append(p['ld'])
    url = DOMAIN + '/' + ('' if p['file'] == 'index.html' else p['file'])
    active = lambda f: ' class="active" aria-current="page"' if p['file'] == f or p.get('parent') == f else ''
    svc_active = ' class="active"' if p['file'] in [s[0] for s in SERVICES] else ''
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex, follow">' if p.get('noindex') else ''}
<meta property="og:type" content="{'article' if p.get('article') else 'website'}">
<meta property="og:site_name" content="{CO['brand']}">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2aabe2">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preload" href="fonts/public-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css?v={VER}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body class="{p.get('body', '')}">
<a class="skip" href="#main">Zum Inhalt springen</a>
<div class="curtain intro" aria-hidden="true"><div class="intro-mark">{MARK}<span>Energieberatung Regio Stolberg</span></div></div>
<div class="curtain leave" aria-hidden="true"></div>
<div class="progress" id="progress" aria-hidden="true"></div>
<header class="head" id="head">
  <nav class="left" aria-label="Hauptnavigation"><ul>
    <li class="has-sub"><button type="button" aria-expanded="false" aria-controls="subnav"{svc_active}>Leistungen {CHEV}</button>
      <div class="sub" id="subnav"><ul>{''.join(f'<li><a href="{f}"{active(f)}>{t}</a></li>' for f, t, _ in SERVICES)}</ul></div></li>
    <li><a href="ratgeber.html"{active('ratgeber.html')}>Ratgeber</a></li>
    <li><a href="ueber-uns.html"{active('ueber-uns.html')}>Über uns</a></li>
  </ul></nav>
  <a class="logo" href="index.html" aria-label="Energieberatung Regio Stolberg – Startseite">{LOGO}</a>
  <div class="right"><a class="tel" href="tel:{CO['telh']}" aria-label="Anrufen: {CO['tel']}">{TEL}<span>{CO['tel']}</span></a><a class="btn blue" href="kontakt.html">Anfrage</a>
  <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="lbl">Menü</span><span class="lines"><span></span><span></span></span></button></div>
</header>
<div class="menu" id="menu">
  <div class="menu-in">
    <ul>{''.join(f'<li><a href="{f}"{active(f)}>{t}</a></li>' for f, t in ALLNAV)}</ul>
    <div class="menu-foot"><span>{CO['brand']}</span><span>{CO['street']}, {CO['zip']} {CO['city']}</span><a href="tel:{CO['telh']}">{CO['tel']}</a><a href="mailto:{CO['mail']}">{CO['mail']}</a><span class="menu-sub"><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a></span></div>
  </div>
</div>
<main id="main">
'''


def foot(p):
    return f'''</main>
<div class="sticky-cta"><a class="btn blue" href="kontakt.html">Beratung anfragen {ARROW}</a></div>
<footer class="footer">
  <div class="wrap">
    <div class="top">
      <div class="brand">{LOGO}<p>Unabhängige Energieberatung für Wohngebäude: Wir sind an keinen Handwerksbetrieb und keine Baufirma gebunden und beraten nur in Ihrem Interesse.</p></div>
      <div><h4>Leistungen</h4><ul>{''.join(f'<li><a href="{f}">{t}</a></li>' for f, t, _ in SERVICES)}</ul></div>
      <div><h4>Mehr</h4><ul><li><a href="ueber-uns.html">Über uns</a></li><li><a href="ratgeber.html">Ratgeber</a></li><li><a href="faq.html">Häufige Fragen</a></li><li><a href="kontakt.html">Kontakt</a></li><li><a href="impressum.html">Impressum</a></li><li><a href="datenschutz.html">Datenschutz</a></li></ul></div>
      <div><h4>Kontakt</h4><ul><li>{CO['name']}</li><li>{CO['brand']}</li><li>{CO['street']}, {CO['zip']} {CO['city']}</li><li><a href="tel:{CO['telh']}">{CO['tel']}</a></li><li><a href="mailto:{CO['mail']}">{CO['mail']}</a></li></ul></div>
    </div>
    <div class="bottom"><span>© 2026 {CO['name']}</span><a class="totop" href="#">Nach oben <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 15 6-6 6 6"/></svg></a></div>
  </div>
</footer>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.3.11/dist/lenis.min.js"></script>
<script src="main.js?v={VER}"></script>
</body>
</html>
'''


def ph(title, lead, toc, photos=None):
    """Unterseiten-Kopf: Titel volle Breite, rechts klebendes Inhaltsverzeichnis, darunter drei Foto-Kacheln."""
    t = ''.join(f'<li><a href="#{i}">{n}</a></li>' for i, n in toc) if toc else ''
    pics = ''.join(f'<figure class="reveal">{img(n, a, 1800, h, sizes="(max-width: 820px) 50vw, 33vw")}</figure>' for n, a, h in (photos or []))
    return f'''<section class="ph"><div class="wrap">
  <div class="ph-grid">
    <div><h1 class="split">{title}</h1><p class="lead reveal">{lead}</p></div>
    {f'<nav class="toc" aria-label="Auf dieser Seite"><p>Auf dieser Seite</p><ul>{t}</ul></nav>' if t else ''}
  </div>
  {f'<div class="ph-photos">{pics}</div>' if pics else ''}
</div></section>'''


def cta(h, t, btn='Beratung anfragen', href='kontakt.html'):
    return f'''<section class="sec tight"><div class="wrap"><div class="cta-band reveal"><div><h2>{h}</h2><p class="lead">{t}</p></div><a class="btn blue big" href="{href}">{btn} {ARROW}</a></div></div></section>'''


def figure(name, alt, w, h, cap=None, cls=''):
    return f'<figure class="{cls}">{img(name, alt, w, h)}{f"<figcaption>{cap}</figcaption>" if cap else ""}</figure>'


# ============================ STARTSEITE ============================
def index():
    scene = f'''
<section class="scene" aria-label="Bildstrecke">
  <div class="stage">
    <div class="frame f1"><img src="img/haus-60er.webp" srcset="img/haus-60er-m.webp 800w, img/haus-60er-l.webp 1200w, img/haus-60er.webp 1600w" sizes="100vw" width="1600" height="1089" alt="Einfamilienhaus aus den 1960er Jahren mit Satteldach und Hecke" fetchpriority="high"><img class="warm" src="img/haus-60er-waerme.webp" srcset="img/haus-60er-waerme-m.webp 800w, img/haus-60er-waerme-l.webp 1200w, img/haus-60er-waerme.webp 1800w" sizes="100vw" width="1800" height="1225" alt="" aria-hidden="true" data-late></div>
    <div class="frame f2"><img data-src="img/handwerker-fassade-l.webp" data-srcset="img/handwerker-fassade-m.webp 800w, img/handwerker-fassade-l.webp 1200w, img/handwerker-fassade.webp 1800w" sizes="100vw" width="1800" height="1200" alt="Handwerker bohrt an einer Holzfassade" data-late></div>
    <div class="frame f3"><div class="win"><img data-src="img/plaene-tisch-l.webp" data-srcset="img/plaene-tisch-m.webp 800w, img/plaene-tisch-l.webp 1200w, img/plaene-tisch.webp 1800w" sizes="100vw" width="1800" height="1211" alt="Baupläne, Stifte und Lineal auf einem Tisch" data-late></div><img class="blur" data-src="img/plaene-tisch-blur.webp" width="900" height="606" alt="" aria-hidden="true" data-late></div>
    <div class="frame f4"><img data-src="img/fachwerk-gasse-l.webp" data-srcset="img/fachwerk-gasse-m.webp 800w, img/fachwerk-gasse-l.webp 1200w, img/fachwerk-gasse.webp 1800w" sizes="100vw" width="1800" height="1200" alt="Gasse mit Fachwerkhäusern" data-late><img class="blur" data-src="img/fachwerk-gasse-blur.webp" width="900" height="600" alt="" aria-hidden="true" data-late></div>
    <div class="frame f5"><img data-src="img/backstein-haus-l.webp" data-srcset="img/backstein-haus-m.webp 800w, img/backstein-haus-l.webp 1200w, img/backstein-haus.webp 1800w" sizes="100vw" width="1800" height="1200" alt="Backsteinhaus mit Garten" data-late></div>
    <div class="scanline" aria-hidden="true"></div>
    <div class="caps">
      <div class="cap c1"><p class="eyebrow">Energieberatung Regio Stolberg</p><h1 class="split">Wir machen sichtbar, wo Ihr Haus Wärme verliert.</h1><p class="split">Unabhängige Energieberatung für Bestandsgebäude in Stolberg und der Region Aachen.</p></div>
      <div class="cap c2"><h2 class="split">Erst die Aufnahme, dann die Berechnung.</h2><p class="split">Bauteile, U-Werte, Wärmebrücken, Anlagentechnik: sorgfältig erfasst, sonst ist jede Zahl danach unseriös.</p></div>
      <div class="cap c3"><h2 class="split">Ein Fahrplan statt Bauchgefühl.</h2><p class="split">Der individuelle Sanierungsfahrplan zeigt, welche Maßnahme wann sinnvoll ist, was sie kostet und was sie spart.</p></div>
      <div class="cap c4"><h2 class="split">Auch für Baudenkmale.</h2><p class="split">Energieausweise für denkmalgeschützte Wohngebäude, freie Beratung ohne Förderkorsett, Gutachten bei Feuchte und Schimmel.</p></div>
      <div class="cap c5"><h2 class="split">Persönlich, vor Ort, ohne Subunternehmer.</h2><p class="split">{CO['person']}, Diplom-Bauingenieur (RWTH Aachen), Gebäude-Energieberater (HWK).</p><div class="actions"><a class="btn white big" href="kontakt.html">Beratung anfragen {ARROW}</a><a class="btn ghost big" href="energieberatung.html">Leistungen ansehen</a></div></div>
    </div>
    <div class="temp" aria-hidden="true"><span class="temp-fill"></span><i>kalt</i><i>warm</i></div>
  </div>
</section>
<div class="scene-static" hidden>
  {''.join(f'<figure>{img(n, a, w, h, sizes="100vw")}<figcaption>{c}</figcaption></figure>' for n, a, w, h, c in [("haus-60er","Einfamilienhaus aus den 1960er Jahren",1600,1089,"Wir machen sichtbar, wo Ihr Haus Wärme verliert."),("handwerker-fassade","Handwerker an einer Holzfassade",1800,1200,"Erst die Aufnahme, dann die Berechnung."),("plaene-tisch","Baupläne auf einem Tisch",1800,1211,"Ein Fahrplan statt Bauchgefühl."),("fachwerk-gasse","Gasse mit Fachwerkhäusern",1800,1200,"Auch für Baudenkmale."),("backstein-haus","Backsteinhaus mit Garten",1800,1200,"Persönlich, vor Ort, ohne Subunternehmer.")])}
</div>'''

    circles = '''
<section class="sec circles" id="themen">
  <div class="wrap">
    <h2 class="split center">Drei Themen, ein Ingenieur.</h2>
    <div class="ring-wrap" aria-label="Unsere drei Themen">
      <a class="ring r1" href="energieberatung.html"><span>Energie-<br>beratung</span></a>
      <a class="ring r2" href="baubegleitung.html"><span>Wärme-<br>schutz</span></a>
      <a class="ring r3" href="thermografie-feuchteschutz.html"><span>Feuchte-<br>schutz</span></a>
    </div>
    <p class="lead center reveal">Unser Schwerpunkt ist die Beratung privater Eigentümer rund um Wärmeschutz, Feuchteschutz, Energieeffizienz und Sanierung. Wir sind weder an Handwerksbetriebe noch an Baufirmen gebunden.</p>
  </div>
</section>'''

    lens = '''
<section class="lens-sec" id="waermebild">
  <div class="lens-sticky">
    <div class="lens-photo">
      <img src="img/haus-60er.webp" srcset="img/haus-60er-m.webp 800w, img/haus-60er-l.webp 1200w, img/haus-60er.webp 1600w" sizes="100vw" width="1600" height="1089" alt="Einfamilienhaus aus den 1960er Jahren" loading="lazy" decoding="async">
      <img class="lens-warm" src="img/haus-60er-waerme.webp" srcset="img/haus-60er-waerme-m.webp 800w, img/haus-60er-waerme-l.webp 1200w, img/haus-60er-waerme.webp 1800w" sizes="100vw" width="1800" height="1225" alt="Dieselbe Fassade als Wärmebild" loading="lazy" decoding="async">
      <div class="lens-ring" aria-hidden="true"></div>
      <div class="lens-tags" aria-live="polite">
        <p class="tag t1" style="--x:63%;--y:36%">Dachanschluss: Wärme entweicht über die ungedämmte Traufe</p>
        <p class="tag t2" style="--x:34%;--y:52%">Rollladenkasten: die klassische Wärmebrücke am Fenster</p>
        <p class="tag t3" style="--x:50%;--y:58%">Fensterlaibung: kalte Oberfläche, hier bildet sich Tauwasser</p>
        <p class="tag t4" style="--x:40%;--y:78%">Sockel: aufsteigende Feuchte und fehlende Perimeterdämmung</p>
      </div>
    </div>
    <div class="lens-text">
      <h2 class="split">Die Wärmebild-Lupe</h2>
      <p class="reveal">Was mit bloßem Auge unsichtbar bleibt, zeigt die Thermografie: Wärmebrücken, Undichtigkeiten, schlecht gedämmte Bauteile. Bewegen Sie die Lupe über die Fassade.</p>
      <p class="reveal small">Darstellung nachempfunden, kein echtes Wärmebild dieses Hauses.</p>
      <a class="btn blue" href="thermografie-feuchteschutz.html">Thermografie ansehen</a>
    </div>
  </div>
</section>'''

    # GEG-Effizienzklassen (Anlage 10 GEG): Endenergie in kWh/(m²·a)
    classes = [('A+', 30), ('A', 50), ('B', 75), ('C', 100), ('D', 130), ('E', 160), ('F', 200), ('G', 250), ('H', 250)]
    bars = ''.join(f'<div class="bar k{i}" style="--w:{18 + i * 10}%"><b>{k}</b><span>{"bis " + str(v) if k != "H" else "über 250"}</span></div>' for i, (k, v) in enumerate(classes))
    scale = f'''
<section class="sec dark scale-sec" id="fahrplan">
  <div class="wrap grid2">
    <div class="scale-text">
      <h2 class="split">Vom Ist-Zustand zum Effizienzhaus, Schritt für Schritt.</h2>
      <p class="reveal">Jedes Gebäude bekommt eine Energieeffizienzklasse. Der individuelle Sanierungsfahrplan (iSFP) zeigt, mit welchen Maßnahmen Ihr Haus in eine bessere Klasse kommt, was sie kosten, was sie sparen und welche Förderung es dafür gibt. Sie haben 15 Jahre Zeit und keine Pflicht, alles umzusetzen.</p>
      <p class="reveal small">Skala nach Anlage 10 Gebäudeenergiegesetz (GEG), Endenergiebedarf in kWh je Quadratmeter und Jahr.</p>
      <a class="btn white" href="energieberatung.html">Sanierungsfahrplan {ARROW}</a>
    </div>
    <div class="scale" role="img" aria-label="Energieeffizienzklassen A+ bis H; ein Hausmarker wandert von G nach B">
      {bars}
      <div class="marker" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3 2 12h3v8h5v-5h4v5h5v-8h3z"/></svg><span>Ihr Haus</span></div>
    </div>
  </div>
</section>'''

    groups = [
        ('Beratung', [('energieberatung.html', 'Energieberatung nach BAFA/KfW', 'Die geförderte Vor-Ort-Beratung als Grundlage jeder Sanierung.'), ('energieberatung.html#isfp', 'Individueller Sanierungsfahrplan', 'Maßnahmen, Kosten, Einsparung und Förderung in einem Dokument.'), ('energieberatung.html#frei', 'Freie Energieberatung', 'Ohne Förderkorsett, angepasst an Ihre tatsächliche Nutzung.')]),
        ('Nachweise', [('energieausweis.html', 'Energieausweis', 'Bedarfs- oder Verbrauchsausweis für Wohngebäude.'), ('energieausweis.html#denkmal', 'Energieausweis für Baudenkmale', 'Neu: Ausweispflicht auch bei Denkmalschutz.'), ('baubegleitung.html#waermebruecken', 'Wärmebrückenberechnung', 'Nachweis statt Strafzuschlag, bis zur Simulation.'), ('wertermittlung.html', 'Wertermittlung', 'Gutachten für Wohngebäude mit Blick auf den energetischen Zustand.')]),
        ('Diagnose', [('thermografie-feuchteschutz.html', 'Thermografie', 'Wärmeverluste mit der Wärmebildkamera sichtbar machen.'), ('thermografie-feuchteschutz.html#feuchte', 'Feuchteschäden & Schimmel', 'Ursachen finden, Gutachten erstellen, Maßnahmen planen.'), ('baubegleitung.html', 'Baubegleitung', 'Energetische Qualität auf der Baustelle sichern.')]),
    ]
    drawers = ''.join(f'<div class="col"><h3>{g}</h3>{"".join(f"<a class=drawer href={f}><span class=knob></span><b>{t}</b><span>{d}</span></a>" for f, t, d in items)}</div>' for g, items in groups)
    akte = f'''
<section class="sec akte" id="leistungen">
  <div class="wrap">
    <h2 class="split">Die Hausakte: alles, was wir für Ihr Gebäude tun.</h2>
    <p class="lead reveal">Zehn Leistungen, ein Ansprechpartner. Beratung, Nachweise für Förderung und Gesetz, Diagnose bei Wärmeverlust und Feuchte.</p>
    <div class="drawers">{drawers}</div>
  </div>
</section>'''

    quote = '''
<section class="quote3d dark" aria-label="Leitsatz">
  <div class="q-stage"><blockquote class="q-block"><p>Nässe ist der größte Feind des Hauses.</p><footer>Aus unserer Beratungspraxis zu Feuchteschutz und Schimmel</footer></blockquote></div>
  <div class="wrap q-text"><p class="reveal">Feuchte Wände verlieren Wärme, feuchte Dämmung verliert ihre Wirkung, und Schimmel macht krank. Nach einzeln ausgeführten Maßnahmen wie einem Fenstertausch tritt Schimmel oft dort auf, wo es vorher keinen gab. Ein Gutachten klärt die Ursache, auch gegenüber Handwerksfirmen.</p><a class="btn white" href="thermografie-feuchteschutz.html#feuchte">Feuchteschutz</a></div>
</section>'''

    beleg = '''
<section class="sec beleg-sec" id="foerderung">
  <div class="wrap grid2">
    <div>
      <h2 class="split">Der Staat zahlt die Hälfte der Beratung.</h2>
      <p class="reveal">Die Energieberatung durch einen Energieeffizienz-Experten wird vom BAFA gefördert: 50 % des förderfähigen Honorars, gedeckelt je nach Gebäudegröße. Seit dem 1. Juli 2023 gilt: gefördert wird nur zusammen mit einem individuellen Sanierungsfahrplan.</p>
      <p class="reveal small">Stand März 2025. Maßgebend sind die aktuellen Vorgaben des BAFA (www.bafa.de) und der KfW (www.kfw.de). Das Honorar im Beispiel ist ein Richtwert.</p>
      <a class="btn blue" href="energieberatung.html#foerderung">Förderung im Detail</a>
    </div>
    <div class="receipt" role="img" aria-label="Beispielrechnung: Beratungshonorar 1.300 Euro, BAFA-Zuschuss 50 Prozent, höchstens 650 Euro, Eigenanteil 650 Euro">
      <div class="paper">
        <p class="r-head">Beispiel Einfamilienhaus</p>
        <div class="r-line"><span>Energieberatung mit iSFP (Richtwert)</span><b>1.300 €</b></div>
        <div class="r-line"><span>BAFA-Zuschuss 50 %</span><b>− 650 €</b></div>
        <div class="r-line"><span>Deckel bei Ein-/Zweifamilienhaus</span><b>max. 650 €</b></div>
        <div class="r-line sum"><span>Ihr Eigenanteil</span><b>650 €</b></div>
        <div class="r-line"><span>Bonus bei Umsetzung: je Einzelmaßnahme</span><b>+ 5 % Förderung</b></div>
        <div class="r-line"><span>Wohngebäude ab 3 Wohneinheiten</span><b>max. 850 €</b></div>
        <div class="r-line"><span>Erläuterung in der WEG-Versammlung</span><b>+ 250 €</b></div>
        <p class="r-foot">Stand März 2025 · ohne Gewähr</p>
      </div>
    </div>
  </div>
</section>'''

    stamps = f'''
<section class="sec stamps-sec" id="qualifikation">
  <div class="wrap grid2">
    <figure class="reveal stamps-photo">{img('plaene-hand', 'Hand mit Bleistift und Lineal über einem Bauplan', 1800, 1013)}</figure>
    <div>
      <h2 class="split">Ein Ingenieur, kein Vertrieb.</h2>
      <p class="reveal">{CO['person']} ist Diplom-Bauingenieur der RWTH Aachen, Statiker und Gebäude-Energieberater (HWK). Er führt jede Beratung selbst durch, besucht Sie vor Ort und nimmt sich Zeit. Keine Subunternehmer.</p>
      <div class="stamps" aria-label="Qualifikationen und Mitgliedschaften">
        <span class="stamp">Dipl.-Ing. RWTH Aachen</span>
        <span class="stamp">Ingenieurkammer-Bau NRW</span>
        <span class="stamp">dena-Expertenliste</span>
        <span class="stamp">DEN e.V.</span>
        <span class="stamp">Verband Privater Bauherren</span>
      </div>
      <a class="btn blue" href="ueber-uns.html">Über uns {ARROW}</a>
    </div>
  </div>
</section>'''

    anfrage = f'''
<section class="sec dark anfrage" id="anfrage">
  <div class="wrap grid2">
    <div>
      <h2 class="split">Ihr Anliegen auf einen Zettel.</h2>
      <p class="reveal">Schreiben Sie uns kurz, worum es geht. Wir melden uns innerhalb von zwei Werktagen und besprechen, was für Ihr Gebäude sinnvoll ist.</p>
      <ul class="contact-list reveal"><li>{TEL}<a href="tel:{CO['telh']}">{CO['tel']}</a></li><li>{MAIL}<a href="mailto:{CO['mail']}">{CO['mail']}</a></li><li>{PIN}<span>{CO['street']}, {CO['zip']} {CO['city']}</span></li></ul>
    </div>
    {form('zettel')}
  </div>
</section>'''
    return scene + circles + lens + scale + akte + quote + beleg + stamps + anfrage


def form(style=''):
    topics = [('energieberatung', 'Energieberatung / Sanierungsfahrplan'), ('energieausweis', 'Energieausweis'), ('baubegleitung', 'Baubegleitung / Wärmebrücken'), ('thermografie', 'Thermografie'), ('feuchte', 'Feuchteschaden / Schimmel'), ('wertermittlung', 'Wertermittlung'), ('sonstiges', 'Etwas anderes')]
    return f'''<form class="form {style}" name="anfrage" method="POST" action="danke.html" data-netlify="true" netlify-honeypot="firma" novalidate>
      <input type="hidden" name="form-name" value="anfrage">
      <p class="hp"><label>Firma <input name="firma" tabindex="-1" autocomplete="off"></label></p>
      <div class="field"><label for="f-thema">Worum geht es?</label><select id="f-thema" name="thema" required>{''.join(f'<option value="{v}">{t}</option>' for v, t in topics)}</select></div>
      <div class="row2">
        <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required><small class="err">Bitte Ihren Namen eintragen.</small></div>
        <div class="field"><label for="f-ort">Ort des Gebäudes</label><input id="f-ort" name="ort" autocomplete="address-level2" placeholder="z. B. Stolberg"></div>
      </div>
      <div class="row2">
        <div class="field"><label for="f-mail">E-Mail</label><input id="f-mail" name="email" type="email" autocomplete="email" required><small class="err">Bitte eine gültige E-Mail-Adresse eintragen.</small></div>
        <div class="field"><label for="f-tel">Telefon (optional)</label><input id="f-tel" name="telefon" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="f-msg">Ihre Nachricht</label><textarea id="f-msg" name="nachricht" rows="4" required></textarea><small class="err">Bitte kurz beschreiben, worum es geht.</small></div>
      <div class="field check"><input id="f-ds" name="datenschutz" type="checkbox" required><label for="f-ds">Ich bin einverstanden, dass meine Angaben zur Bearbeitung der Anfrage gespeichert werden. Widerruf jederzeit möglich, Details in der <a href="datenschutz.html">Datenschutzerklärung</a>.</label><small class="err">Bitte bestätigen.</small></div>
      <button class="btn blue big" type="submit">Anfrage senden {ARROW}</button>
    </form>'''


# ============================ LEISTUNGSSEITEN ============================
def energieberatung():
    return ph('Energieberatung und individueller Sanierungsfahrplan', 'Eine Energieberatung für Bestandsgebäude sollte die Grundlage jeder energetischen Sanierung sein, auch für Einzelmaßnahmen wie den Fenstertausch oder die Fassadendämmung. Wir bieten die geförderte Beratung nach BAFA/KfW-Richtlinien und die freie Energieberatung.',
              [('aufnahme', 'Die Aufnahme'), ('bafa', 'Beratung nach BAFA/KfW'), ('frei', 'Freie Beratung'), ('isfp', 'Sanierungsfahrplan'), ('foerderung', 'Förderung')],
              [('haus-60er', 'Einfamilienhaus aus den 1960ern', 1089), ('klemmbrett', 'Klemmbrett mit Notizen', 1200), ('thermostat', 'Hand am Heizkörperthermostat', 1200)]) + f'''
<section class="sec" id="aufnahme"><div class="wrap grid2">
  <div><h2 class="split">Der erste Schritt: die sorgfältige Aufnahme.</h2>
    <p class="reveal">Am Anfang steht die fachkundige Aufnahme der Gebäudehülle (Bauteildicken, Baustoffe, U-Werte), der energetischen Schwachstellen (Wärmebrücken, Luftdichtheit) und der Anlagentechnik (Heizung, Warmwasser, Leitungen, Lüftung). Wird dieser Schritt nicht ordnungsgemäß ausgeführt, ist jede nachfolgende Berechnung unseriös.</p>
    <p class="reveal">Auf dieser Basis ermitteln wir den energetischen Ist-Zustand, vergleichen ihn mit den gesetzlichen Anforderungen und ordnen das Gebäude einer Energieeffizienzklasse zu. Das ist die Grundlage für die Beratung und den Sanierungsfahrplan.</p>
    <p class="reveal">Auch wenn nur einzelne Maßnahmen geplant sind, lohnt die Beratung vorab: Ist die Maßnahme sinnvoll, oder wäre das Geld woanders besser angelegt? Und: Einzelmaßnahmen an der Gebäudehülle können die feuchtetechnische Balance stören, dann tritt Schimmel auf, wo vorher keiner war.</p></div>
  {figure('klemmbrett', 'Hände schreiben mit einem Stift auf ein Klemmbrett', 1800, 1200, 'Aufnahme vor Ort: Bauteile, Anlagentechnik, Schwachstellen.', 'reveal')}
</div></section>
<section class="sec grey" id="bafa"><div class="wrap">
  <h2 class="split">Beratung nach BAFA/KfW-Richtlinien</h2>
  <div class="grid2">
    <div><p class="reveal">Die frühere „Vor-Ort-Energieberatung“. Sie ist Voraussetzung für viele Förderprogramme und wird selbst gefördert. Seit dem 1. Juli 2023 wird sie für Wohngebäude nur noch gefördert, wenn gleichzeitig ein individueller Sanierungsfahrplan erstellt wird.</p>
    <p class="reveal">Viele Randbedingungen sind dabei strikt vorgegeben: Für jeden Raum gilt die Standardtemperatur von 20 °C, der Warmwasserbedarf wird nach Wohnfläche berechnet, auch wenn Sie nur noch zu zweit im Haus wohnen.</p></div>
    <div><p class="reveal">Wir sind in der Energieeffizienz-Expertenliste für Förderprogramme des Bundes in der Kategorie „Energieberatung für Wohngebäude“ gelistet. Damit sind unsere Beratungen, Sanierungsfahrpläne und Baubegleitungen förderfähig.</p>
    <p class="reveal">Für Wohnungseigentümergemeinschaften erläutern wir die Ergebnisse auf Wunsch in der Eigentümerversammlung; auch das wird bezuschusst.</p></div>
  </div>
</div></section>
<section class="sec" id="frei"><div class="wrap grid2">
  {figure('thermostat', 'Hand stellt einen Heizkörperthermostat ein', 1800, 1200, 'Freie Beratung: Ihre tatsächliche Nutzung zählt.', 'reveal')}
  <div><h2 class="split">Freie Energieberatung</h2>
    <p class="reveal">Ohne die oft hohen Ansprüche der staatlichen oder kommunalen Förderprogramme. Es müssen lediglich die Anforderungen des Gebäudeenergiegesetzes (GEG, vormals EnEV) eingehalten werden.</p>
    <p class="reveal">Geeignet für Eigentümer, die Sanierungskosten lieber von der Steuer absetzen, sich den Aufwand der Antragstellung sparen und nicht davon abhängig sein wollen, ob ein Förderprogramm zwischenzeitlich eingestellt wird.</p>
    <p class="reveal">Der Vorteil: Wenn Sie einzelne Räume kaum noch heizen oder wenig Warmwasser brauchen, rechnen wir mit Ihren echten Werten. Maßnahmen werden nach Ihren Bedürfnissen geplant und bringen trotzdem, oder gerade deswegen, die gewünschte Einsparung.</p></div>
</div></section>
<section class="sec dark" id="isfp"><div class="wrap">
  <h2 class="split">Der individuelle Sanierungsfahrplan (iSFP)</h2>
  <div class="grid2">
    <div><p class="reveal">Der iSFP fasst die Bestandsanalyse von Gebäudehülle und Anlagentechnik übersichtlich in Bild und Text zusammen und vergleicht den energetischen Zustand mit den aktuellen gesetzlichen Anforderungen. Dazu kommen Sanierungsmaßnahmen, mit denen das Gebäude Schritt für Schritt oder als Gesamtpaket zum Effizienzhaus wird.</p>
    <p class="reveal">Er enthält geschätzte Kosten je Maßnahme (aus Erfahrungswerten oder vorliegenden Angeboten), die berechneten Einsparungen bei Heizung und Warmwasser und Hinweise auf mögliche Fördermittel.</p></div>
    <div class="facts reveal">
      <div><b>15 Jahre</b><span>Zeit für die Umsetzung und die Nutzung der Fördermöglichkeiten</span></div>
      <div><b>Keine Pflicht</b><span>Die Maßnahmen sind Empfehlungen. Reihenfolge frei, Abbruch jederzeit, keine Rückzahlung</span></div>
      <div><b>+ 5 %</b><span>Bonus bei geförderten Einzelmaßnahmen, wenn ein iSFP vorliegt</span></div>
      <div><b>Mit Ihnen</b><span>Wir erstellen Fahrpläne nicht „von oben herab“: Jede Maßnahme wird vorher mit Ihnen besprochen</span></div>
    </div>
  </div>
</div></section>
<section class="sec" id="foerderung"><div class="wrap grid2">
  <div><h2 class="split">Förderung der Beratung</h2>
    <p class="reveal">Die Energieberatung durch einen Energieeffizienz-Experten wird vom BAFA mit 50 % des förderfähigen Beratungshonorars bezuschusst. Der Höchstbetrag hängt von der Gebäudegröße ab. Wählen Sie Ihren Gebäudetyp und klicken Sie auf die Segmente.</p>
    <div class="donut-ctl" role="group" aria-label="Gebäudetyp"><button type="button" class="chip on" data-cap="650" data-fee="1300">Ein-/Zweifamilienhaus</button><button type="button" class="chip" data-cap="850" data-fee="1900">Ab 3 Wohneinheiten</button><button type="button" class="chip" data-cap="850" data-fee="1900" data-weg="250">WEG mit Versammlung</button></div>
    <p class="reveal small">Honorare sind Richtwerte zur Veranschaulichung. Stand März 2025, maßgebend sind die aktuellen Vorgaben des BAFA (www.bafa.de) und der KfW (www.kfw.de). Die Förderhöhe hängt vom Programm ab und kann sich ändern.</p></div>
  <div class="donut reveal">
    <svg viewBox="0 0 200 200" aria-hidden="true"><circle class="d-bg" cx="100" cy="100" r="70"/><circle class="d-seg s-eigen" cx="100" cy="100" r="70" data-k="eigen"/><circle class="d-seg s-zuschuss" cx="100" cy="100" r="70" data-k="zuschuss"/><circle class="d-seg s-weg" cx="100" cy="100" r="70" data-k="weg"/><text class="d-val" x="100" y="96" text-anchor="middle">650 €</text><text class="d-lbl" x="100" y="118" text-anchor="middle">Eigenanteil</text></svg>
    <div class="d-legend"><button type="button" class="on" data-k="eigen"><i></i>Eigenanteil <b>650 €</b></button><button type="button" data-k="zuschuss"><i></i>BAFA-Zuschuss <b>650 €</b></button><button type="button" data-k="weg" hidden><i></i>WEG-Zuschlag <b>250 €</b></button></div>
    <p class="d-note" aria-live="polite">Der Zuschuss beträgt 50 % des Honorars, höchstens 650 € beim Ein-/Zweifamilienhaus.</p>
  </div>
</div></section>
''' + cta('Beratung für Ihr Gebäude?', 'Sagen Sie uns kurz, um welches Haus es geht. Wir schlagen den passenden Weg vor: gefördert mit iSFP oder frei.', href='kontakt.html?thema=energieberatung')


def energieausweis():
    return ph('Energieausweise für Wohngebäude und Baudenkmale', 'Energieausweise informieren über die energetischen Eigenschaften eines Gebäudes und machen Gebäude näherungsweise vergleichbar. In vielen Fällen ist die Ausstellung gesetzliche Pflicht. Wir stellen Bedarfs- und Verbrauchsausweise aus, auch für denkmalgeschützte Wohngebäude.',
              [('pflicht', 'Wann Pflicht?'), ('weiche', 'Welcher Ausweis?'), ('denkmal', 'Baudenkmale'), ('ablauf', 'So läuft es')],
              [('mfh-balkone', 'Mehrfamilienhaus mit Balkonen', 1200), ('fachwerk-gasse', 'Fachwerkhäuser', 1200), ('eingang-backstein', 'Eingang eines Backsteinhauses', 1200)]) + f'''
<section class="sec" id="pflicht"><div class="wrap">
  <h2 class="split">Wann ein Energieausweis Pflicht ist</h2>
  <div class="grid2">
    <div><p class="reveal">Wann und welche Art von Energieausweis Sie benötigen, regelt das Gebäudeenergiegesetz (GEG), in den Medien oft „Heizungsgesetz“ genannt. Bei Verkauf, Übertragung oder Teilungserklärung eines bestehenden Gebäudes und bei der Vermietung einer Wohnung ist ein Energieausweis vorzulegen, sofern nicht bereits ein gültiger vorliegt.</p>
    <p class="reveal">Für Neubauten ist ein Energiebedarfsausweis auf Basis der energetischen Eigenschaften des fertiggestellten Gebäudes auszustellen. Ein Verbrauchsausweis ist hier nicht zulässig, weil die Verbrauchsdaten der letzten drei Jahre fehlen.</p></div>
    <div><p class="reveal">Für Wohngebäude mit weniger als fünf Wohnungen, deren Bauantrag vor dem 1. November 1977 gestellt wurde, ist ebenfalls ein Bedarfsausweis nötig, außer das Gebäude erfüllte schon bei Fertigstellung (oder durch spätere Änderungen) das Anforderungsniveau der Wärmeschutzverordnung vom 11. August 1977. Dann darf auch ein Verbrauchsausweis ausgestellt werden.</p>
    <p class="reveal">Für Gebäude mit fünf oder mehr Wohneinheiten darf unabhängig von Baujahr und Sanierungszustand ein Verbrauchsausweis auf Basis der letzten drei Abrechnungsperioden erstellt werden.</p></div>
  </div>
</div></section>
<section class="sec grey" id="weiche"><div class="wrap">
  <h2 class="split">Welcher Ausweis passt zu Ihrem Gebäude?</h2>
  <p class="lead reveal">Beantworten Sie vier Fragen. Der Pfad zeichnet sich mit jeder Antwort weiter.</p>
  <div class="weiche reveal" id="weiche-tool">
    <div class="w-step" data-q="neubau"><p>Handelt es sich um einen Neubau?</p><div class="w-opts"><button type="button" data-a="ja">Ja</button><button type="button" data-a="nein">Nein</button></div></div>
    <div class="w-step" data-q="denkmal" hidden><p>Steht das Gebäude unter Denkmalschutz?</p><div class="w-opts"><button type="button" data-a="ja">Ja</button><button type="button" data-a="nein">Nein</button></div></div>
    <div class="w-step" data-q="we" hidden><p>Hat das Gebäude fünf oder mehr Wohnungen?</p><div class="w-opts"><button type="button" data-a="ja">Ja</button><button type="button" data-a="nein">Nein</button></div></div>
    <div class="w-step" data-q="alt" hidden><p>Wurde der Bauantrag vor dem 1. November 1977 gestellt, ohne dass das Haus die Wärmeschutzverordnung von 1977 erfüllt?</p><div class="w-opts"><button type="button" data-a="ja">Ja</button><button type="button" data-a="nein">Nein / weiß nicht</button></div></div>
    <div class="w-result" aria-live="polite" hidden><b></b><p></p><button type="button" class="btn ghost w-reset">Von vorn</button></div>
  </div>
</div></section>
<section class="sec" id="denkmal"><div class="wrap grid2">
  {figure('fachwerk-gasse', 'Gasse mit historischen Fachwerkhäusern', 1800, 1200, 'Baudenkmale: Ausweispflicht kommt mit dem GModG.', 'reveal')}
  <div><h2 class="split">Neu: Energieausweise für Baudenkmale</h2>
    <p class="reveal">Bisher musste bei Vermietung, Verpachtung und Verkauf denkmalgeschützter Wohngebäude kein Energieausweis vorgelegt werden. Mit dem neuen Gebäudemodernisierungsgesetz (GModG) wird die Ausweispflicht auch für denkmalgeschützte Gebäude eingeführt (Stand: Kabinettsbeschluss vom 13. Mai 2026).</p>
    <p class="reveal">Der Ausweis kann als Verbrauchs- oder Bedarfsausweis erstellt werden. Wir stellen schon jetzt Energieausweise für denkmalgeschützte Wohngebäude aus, für Vermietung und Verkauf ebenso wie nach einer Sanierung oder einem Umbau.</p>
    <a class="btn blue" href="ratgeber-energieausweis-baudenkmal.html">Ratgeber: Was das GModG ändert</a></div>
</div></section>
<section class="sec grey" id="ablauf"><div class="wrap">
  <h2 class="split">So läuft es</h2>
  <div class="steps reveal">
    <div><b>Anfrage</b><p>Sie nennen uns Adresse, Baujahr, Wohneinheiten und den Anlass (Verkauf, Vermietung, Sanierung).</p></div>
    <div><b>Unterlagen oder Vor-Ort-Termin</b><p>Für den Verbrauchsausweis genügen die Abrechnungen der letzten drei Jahre. Für den Bedarfsausweis nehmen wir das Gebäude vor Ort auf.</p></div>
    <div><b>Ausweis</b><p>Sie erhalten den registrierten Energieausweis mit Registriernummer, gültig zehn Jahre.</p></div>
  </div>
</div></section>
''' + cta('Energieausweis anfragen', 'Nennen Sie uns Baujahr, Zahl der Wohnungen und den Anlass. Wir sagen Ihnen, welcher Ausweis nötig ist.', 'Energieausweis anfragen', 'kontakt.html?thema=energieausweis')


def baubegleitung():
    return ph('Baubegleitung und Wärmebrückenberechnung', 'Energieeffizientes Bauen und Sanieren stellt hohe fachliche Anforderungen an alle Beteiligten. Die energetische Baubegleitung sichert, dass die Ziele erreicht und gegenüber Fördergebern nachgewiesen werden. Die Wärmebrückenberechnung holt aus der Bausubstanz die bessere Effizienzklasse heraus.',
              [('was', 'Was Baubegleitung ist'), ('foerderung', 'Förderung'), ('waermebruecken', 'Wärmebrücken'), ('rechnung', 'Strafzuschlag')],
              [('baustelle-geruest', 'Rohbau mit Gerüst', 1350), ('daemmung-team', 'Zwei Bauarbeiter prüfen Pläne auf einem Tablet', 1200), ('dachboden', 'Dachstuhl aus Holz', 1013)]) + f'''
<section class="sec" id="was"><div class="wrap grid2">
  <div><h2 class="split">Was die Baubegleitung leistet, und was nicht.</h2>
    <p class="reveal">Um Missverständnisse gleich auszuräumen: Eine Baubegleitung umfasst keine Bauplanung, keine Bauantragstellung, keine Statik und keine Bauleitung. Wir holen keine Angebote ein und beschaffen kein Material. Das ist Aufgabe von Generalunternehmern, Fachhandwerkern und anderen Fachleuten. Vor allem muss der Energieeffizienz-Experte unabhängig bleiben und darf kein wirtschaftliches Interesse an der Bauausführung haben.</p>
    <p class="reveal">Die Baubegleitung stellt sicher, dass die energetischen Ziele des Vorhabens erreicht werden: Wir überwachen die ordnungsgemäße Ausführung, dokumentieren die Übereinstimmung mit der Fachplanung und fassen alles in einer Hausakte zusammen. Je nach Stand der Vorplanung geben wir Empfehlungen und Mindestvorgaben für Bauteile, Anschlussdetails und Anlagentechnik.</p>
    <p class="reveal">Im Regelbetrieb sind wir mindestens zweimal pro Woche auf der Baustelle, je nach Fortschritt öfter. Nach Abschluss bestätigen wir gegenüber Förder- und Kreditgebern, dass die Ziele erreicht wurden, und können das bei einer Prüfung nachweisen.</p></div>
  {figure('daemmung-team', 'Zwei Bauarbeiter mit Helm prüfen Pläne auf einem Tablet vor einer gedämmten Wand', 1800, 1200, 'Engmaschig vor Ort, unabhängig von der ausführenden Firma.', 'reveal')}
</div></section>
<section class="sec grey" id="foerderung"><div class="wrap">
  <h2 class="split">Förderung der Baubegleitung</h2>
  <div class="grid3 reveal">
    <div class="fact-card"><b>BAFA-Einzelmaßnahmen (BEG)</b><p>Bei Einzelmaßnahmen an der Gebäudehülle, an der Anlagentechnik (außer Heizung) und an Wärmeerzeugern bei Gebäudenetzen: 50 % der förderfähigen Ausgaben, gedeckelt auf 5.000 € bei Ein-/Zweifamilienhäusern, 2.000 € je Wohneinheit bei Mehrfamilienhäusern, insgesamt höchstens 20.000 €.</p></div>
    <div class="fact-card"><b>KfW-Komplettsanierung (Programm 261)</b><p>Bei der Sanierung zum Effizienzhaus 85 oder besser: 50 % der förderfähigen Ausgaben, gedeckelt auf 10.000 € bei Ein-/Zweifamilienhäusern, 4.000 € je Wohneinheit ab drei Wohneinheiten (auch WEG), insgesamt höchstens 40.000 €.</p></div>
    <div class="fact-card"><b>Neubau</b><p>Über die BEG gibt es keinen Zuschuss, die Kosten können aber über die KfW-Kredite 296, 297, 298 und 300 mitfinanziert werden. Die Einbindung eines Energieeffizienz-Experten ist dort ab Antragstellung verpflichtend.</p></div>
  </div>
  <p class="small reveal">Stand März 2025, maßgebend sind die aktuellen Vorgaben von BAFA und KfW.</p>
</div></section>
<section class="sec" id="waermebruecken"><div class="wrap grid2">
  {figure('dachboden', 'Holzbalken eines Dachstuhls', 1800, 1013, 'Anschlüsse, Ecken, Rollladenkästen: die kritischen Stellen.', 'reveal')}
  <div><h2 class="split">Wärmebrückenberechnung und -simulation</h2>
    <p class="reveal">Fensteranschlüsse, Deckenanschlüsse, Gebäudeecken, Rollladenkästen: Mit einer Berechnung der Wärmebrücken lässt sich eine optimale Ausführung an diesen Stellen nachweisen. Beim Neubau wie bei der Sanierung zum Effizienzhaus ist das oft entscheidend, um die angestrebte Klasse (EH 70, EH 55, EH 40) überhaupt zu erreichen. Je niedriger die Klasse, desto höher der Tilgungszuschuss und desto niedriger die Heizkosten.</p>
    <p class="reveal">Es gibt verschiedene Qualitätsstufen, vom bildhaften Vergleich mit Regeldetails bis zur thermischen Simulation mit speziellen Programmen. Je mehr Aufwand, desto genauer die Berechnung und desto niedriger der Zuschlag. Wir führen alle Arten von Nachweisen durch, auch Simulationen für KfW-40- und Nullenergiehäuser.</p></div>
</div></section>
<section class="sec dark" id="rechnung"><div class="wrap grid2">
  <div><h2 class="split">Warum eine Berechnung die Effizienz verbessert</h2>
    <p class="reveal">Die Berechnung ändert nichts an der Bausubstanz. Aber im gesetzlichen Nachweis muss ein pauschaler Strafzuschlag für Wärmebrücken eingerechnet werden, wenn sie nicht gesondert nachgewiesen werden. Und dieser Zuschlag wiegt umso schwerer, je besser die Hülle gedämmt ist.</p>
    <p class="reveal">Beispiel: Die Gebäudehülle erreicht mit viel Dämmung einen mittleren U-Wert von 0,20 W/m²K. Ohne Nachweis kommen pauschal 0,10 W/m²K dazu, also 50 % Zuschlag. Mit Nachweis auf 0,03 W/m²K sind es nur noch 15 %. Ergebnis: bessere Klasse und höhere Förderung, oder dünnere Dämmung bei gleicher Klasse.</p>
    <div class="wb-ctl" role="group" aria-label="Nachweis wählen"><button type="button" class="chip on" data-wb="ohne">Ohne Nachweis</button><button type="button" class="chip" data-wb="mit">Mit Wärmebrückenberechnung</button></div></div>
  <div class="wb reveal" aria-live="polite">
    <div class="wb-row"><span>Gebäudehülle</span><div class="wb-bar"><i class="base" style="--v:.20"></i></div><b>0,20</b></div>
    <div class="wb-row"><span>Zuschlag Wärmebrücken</span><div class="wb-bar"><i class="add" style="--v:.10"></i></div><b class="wb-add">+ 0,10</b></div>
    <div class="wb-row sum"><span>Rechnerischer U-Wert</span><div class="wb-bar"><i class="base" style="--v:.20"></i><i class="add" style="--v:.10"></i></div><b class="wb-sum">0,30</b></div>
    <p class="wb-note">Zuschlag: <b class="wb-pct">50 %</b> auf den mühsam erreichten Wert. Angaben in W/m²K.</p>
  </div>
</div></section>
''' + cta('Baubegleitung oder Wärmebrückennachweis?', 'Schicken Sie uns Ihr Vorhaben. Wir sagen, welche Förderung greift und welche Nachweisstufe sinnvoll ist.', href='kontakt.html?thema=baubegleitung')


def thermografie():
    return ph('Thermografie, Feuchteschutz und Schimmel', 'Wärmebildaufnahmen machen Wärmeverluste sichtbar, die mit anderen Messmethoden kaum zu erfassen sind. Und wo feuchte Luft auf kalte Oberflächen trifft, entsteht Schimmel. Wir finden die Ursachen, erstellen Gutachten und planen die Maßnahmen.',
              [('thermografie', 'Thermografie'), ('taupunkt', 'Taupunkt-Rechner'), ('feuchte', 'Feuchteschäden'), ('schimmel', 'Schimmel'), ('gutachten', 'Gutachten')],
              [('fenster-alt', 'Altes Holzfenster', 1200), ('putz-feucht', 'Abblätternder Putz an einer feuchten Wand', 1013), ('mauer-feucht', 'Verwitterte Backsteinwand mit Putzresten', 1200)]) + f'''
<section class="sec" id="thermografie"><div class="wrap grid2">
  <div><h2 class="split">Thermografie: Wärmeverluste sichtbar machen</h2>
    <p class="reveal">Mit Wärmebildaufnahmen im Infrarotbereich werden Wärmebrücken, Undichtigkeiten in der Gebäudehülle und schlecht gedämmte Bauteile sichtbar. Die Aufnahmen entstehen mit einer speziellen Kamera von den Außenseiten des Gebäudes, sinnvollerweise im Winter, wenn der Temperaturunterschied zwischen innen und außen am größten ist.</p>
    <p class="reveal">Im Anschluss lassen sich die Ursachen der Energieverluste genau analysieren und Maßnahmen zielsicher planen. Innen hilft die Thermografie, Ursachen für Schimmel zu erkennen oder gefährdete Stellen vorbeugend zu finden: Raumecken, alte Kamine, Fensterlaibungen, ungedämmte Außenwände, besonders in Bädern und Küchen.</p></div>
  <figure class="reveal thermo-pair"><img src="img/haus-60er-waerme.webp" srcset="img/haus-60er-waerme-m.webp 800w, img/haus-60er-waerme-l.webp 1200w, img/haus-60er-waerme.webp 1800w" sizes="(max-width: 820px) 100vw, 50vw" width="1800" height="1225" alt="Fassade eines Einfamilienhauses in Wärmebild-Darstellung" loading="lazy" decoding="async"><figcaption>Darstellung nachempfunden. Helle Stellen zeigen, wo Wärme entweicht.</figcaption></figure>
</div></section>
<section class="sec grey" id="taupunkt"><div class="wrap grid2">
  <div><h2 class="split">Wann wird es an der Wand nass?</h2>
    <p class="reveal">Schimmel entsteht, wo feuchte Luft auf kühle Oberflächen trifft. Ab etwa 80 % relativer Feuchte an der Oberfläche wächst er, bei 100 % fällt Tauwasser aus. Wählen Sie Raumtemperatur und Luftfeuchte, der Rechner zeigt den Taupunkt und die kritische Oberflächentemperatur.</p>
    <div class="tp-ctl"><p>Raumtemperatur</p><div role="group" aria-label="Raumtemperatur">{''.join(f'<button type="button" class="chip{" on" if t == 20 else ""}" data-t="{t}">{t} °C</button>' for t in (18, 20, 22, 24))}</div>
    <p>Relative Luftfeuchte</p><div role="group" aria-label="Luftfeuchte">{''.join(f'<button type="button" class="chip{" on" if h == 60 else ""}" data-h="{h}">{h} %</button>' for h in (40, 50, 60, 70, 80))}</div></div>
    <p class="reveal small">Berechnung nach der Magnus-Formel; Richtwerte, kein Ersatz für eine Messung vor Ort.</p></div>
  <div class="tp reveal" aria-live="polite">
    <div class="tp-val"><span>Taupunkt</span><b id="tp-dew">12,0 °C</b><small>ab hier Tauwasser</small></div>
    <div class="tp-val"><span>Schimmelgrenze</span><b id="tp-mold">15,4 °C</b><small>80 % Oberflächenfeuchte</small></div>
    <p class="tp-note" id="tp-note">Eine Fensterlaibung mit 13 °C Oberflächentemperatur liegt unter der Schimmelgrenze: hier wächst Schimmel, auch ohne sichtbares Tauwasser.</p>
  </div>
</div></section>
<section class="sec" id="feuchte"><div class="wrap">
  <h2 class="split">Feuchteschäden: Nässe ist der größte Feind des Hauses.</h2>
  <div class="grid2">
    <div><p class="reveal">Sind Bauteile dauerhaft feucht, entsteht nicht nur Schimmel, auch die Bausubstanz leidet: faulende Holzbalken im Dach und in Holzbalkendecken, Holzfensterrahmen, und selbst Mauersteine, Mörtel und Stahlbeton können ihre Tragfähigkeit verlieren. Feuchte Wände verlieren mehr Wärme, feuchte Dämmung verliert ihre Wirkung. Hausschwamm und Holzfäule zerstören organische Bausubstanz.</p>
    <p class="reveal">Die Ursachen sind vielfältig: Undichtigkeiten in der Dachhaut, aufsteigende Feuchte in erdberührenden Wänden, beschädigte Regenrohre im Erdreich, tropfende Wasser- und Heizungsleitungen (vor allem, wenn die Heizung immer wieder nachgefüllt wird).</p></div>
    <div><p class="reveal">Auch Putze und Anstriche werden mit der Zeit wasserdurchlässig, durch Risse oder weil der Anstrich seine abweisende Wirkung verloren hat. Dann dringt in regenreichen Monaten bei schlagregenbeanspruchten Wänden Wasser ein, das vor dem Winter nicht mehr verdunstet. Feuchte Wände und Schimmel entstehen dann an Stellen, an denen es jahrelang keine Probleme gab, besonders hinter Schränken und an Fensterlaibungen.</p>
    {figure('putz-feucht', 'Abblätternder Putz und Farbe an einer feuchten Wand', 1800, 1013, 'Ausblühungen und abblätternder Putz: Feuchte hat einen Weg gefunden.', 'reveal')}</div>
  </div>
</div></section>
<section class="sec grey" id="schimmel"><div class="wrap grid2">
  {figure('fenster-alt', 'Altes Holzfenster mit Spiegelungen', 1800, 1200, 'Nach einem Fenstertausch verlagert sich der kälteste Punkt im Raum.', 'reveal')}
  <div><h2 class="split">Wohnungsschimmel</h2>
    <p class="reveal">Schimmelpilze wachsen, wenn genug Feuchte da ist und organisches Material (Tapetenkleister, Dispersionsfarben) als Nährboden dient. Ein hoher pH-Wert hemmt das Wachstum. Kritisch wird es, wenn die Luftfeuchte über mehrere Tage bei 70 bis 80 % liegt: An den kältesten Stellen kondensiert Wasserdampf. Im günstigen Fall an der Fensterscheibe, im ungünstigen hinter Fußleisten, Wandverkleidungen und Möbeln an Außenwänden, wo Schimmel lange unentdeckt wächst.</p>
    <p class="reveal">Feuchte kann auch im Bauteilinneren kondensieren, an Hohlräumen und Grenzschichten zu Dämmungen, und dort Dämmschichten in Dächern und Wänden durchfeuchten. Manchmal genügt eine Einzelraum-Lüftungsanlage und die Sanierung der betroffenen Bauteile; bei älteren Gebäuden kann eine Innendämmung einzelner Räume sinnvoll sein, nach vorheriger thermografischer Analyse.</p></div>
</div></section>
<section class="sec" id="gutachten"><div class="wrap grid2">
  <div><h2 class="split">Gutachten, das Ursachen klärt.</h2>
    <p class="reveal">Gerade nach einzeln ausgeführten Maßnahmen wie einem Fenstertausch tritt Schimmel auf, wenn nicht alle Einflussfaktoren betrachtet wurden. Ein fachlich fundiertes Gutachten hilft bei der Ursachenanalyse und auch dann, wenn Handwerksfirmen die Verantwortung für die Schimmelbildung nicht übernehmen wollen.</p>
    <a class="btn blue" href="ratgeber-schimmel-fenstertausch.html">Ratgeber: Schimmel nach Fenstertausch</a></div>
  {figure('mauer-feucht', 'Verwitterte Wand mit Putzresten und freiliegenden Ziegeln', 1800, 1200, None, 'reveal')}
</div></section>
''' + cta('Feuchte oder Schimmel im Haus?', 'Beschreiben Sie uns, wo und seit wann. Wir kommen vorbei, messen und klären die Ursache.', 'Gutachten anfragen', 'kontakt.html?thema=feuchte')


def wertermittlung():
    return ph('Wertermittlung von Wohngebäuden', 'Die Wertermittlung ist die Einschätzung des aktuellen Marktwertes eines Grundstücks oder Gebäudes durch einen Fachmann. Wir haben uns auf Gutachten für Wohngebäude spezialisiert und berücksichtigen dabei besonders den energetischen Zustand.',
              [('verfahren', 'Verfahren'), ('energetisch', 'Energetischer Zustand'), ('faktor', 'Faktor-Rechnung'), ('fuer-wen', 'Für wen')],
              [('backstein-haus', 'Backsteinhaus mit Garten', 1200), ('altbau-backstein', 'Altbau aus Backstein', 1200), ('daecher', 'Dächer einer Stadt von oben', 1200)]) + f'''
<section class="sec" id="verfahren"><div class="wrap grid2">
  <div><h2 class="split">Drei Verfahren, ein realistisches Gesamtbild.</h2>
    <p class="reveal">Vergleichswert-, Sachwert- und Ertragswertverfahren berücksichtigen Lage, Größe von Gebäude und Grundstück, baulichen Zustand, Ausstattung, Nutzungspotenzial und einiges mehr. Unsere Gutachten werden immer unter Berücksichtigung aller drei Verfahren erstellt, damit sich ein realistisches Gesamtbild ergibt.</p></div>
  {figure('altbau-backstein', 'Historisches Backsteingebäude mit Ziegeldach', 1800, 1200, None, 'reveal')}
</div></section>
<section class="sec grey" id="energetisch"><div class="wrap grid2">
  {figure('backstein-haus', 'Backsteinhaus mit Garten', 1800, 1200, None, 'reveal')}
  <div><h2 class="split">Der energetische Zustand entscheidet mit.</h2>
    <p class="reveal">Oft werden notwendige Maßnahmen nicht erkannt oder ihre Kosten zu niedrig angesetzt. Die bei Renditeobjekten beliebte Regel „Jahresnettokaltmiete mal Faktor 20 bis 25“ funktioniert nicht mehr, wenn aufgrund gesetzlicher Vorgaben hohe Kosten für energetische Sanierung drohen. Käufer von Renditeobjekten und besonders Erben sollten das bedenken, auch gegenüber dem Finanzamt.</p></div>
</div></section>
<section class="sec dark" id="faktor"><div class="wrap grid2">
  <div><h2 class="split">Die Faktor-Rechnung, ehrlich gerechnet.</h2>
    <p class="reveal">Wählen Sie eine Jahresnettokaltmiete und den Faktor. Darunter sehen Sie, was ein energetischer Sanierungsbedarf aus dem vermeintlichen Wert macht. Alle Beträge sind Beispiele.</p>
    <div class="fk-ctl"><p>Jahresnettokaltmiete</p><div role="group" aria-label="Kaltmiete">{''.join(f'<button type="button" class="chip{" on" if m == 24000 else ""}" data-m="{m}">{m // 1000}.000 €</button>' for m in (12000, 24000, 36000))}</div>
    <p>Faktor</p><div role="group" aria-label="Faktor">{''.join(f'<button type="button" class="chip{" on" if f == 22 else ""}" data-f="{f}">{f}</button>' for f in (20, 22, 25))}</div>
    <p>Energetischer Sanierungsbedarf</p><div role="group" aria-label="Sanierungsbedarf">{''.join(f'<button type="button" class="chip{" on" if s == 120000 else ""}" data-s="{s}">{s // 1000}.000 €</button>' for s in (0, 60000, 120000, 200000))}</div></div></div>
  <div class="fk reveal" aria-live="polite">
    <div class="r-line"><span>Kaltmiete × Faktor</span><b id="fk-brutto">528.000 €</b></div>
    <div class="r-line"><span>abzüglich Sanierungsbedarf</span><b id="fk-san">− 120.000 €</b></div>
    <div class="r-line sum"><span>Realistischer Ausgangswert</span><b id="fk-netto">408.000 €</b></div>
    <p class="small" id="fk-note">Der Sanierungsbedarf drückt den Wert um 23 %. Ein Gutachten setzt diese Kosten belastbar an.</p>
  </div>
</div></section>
<section class="sec" id="fuer-wen"><div class="wrap">
  <h2 class="split">Für wen sich das Gutachten lohnt</h2>
  <div class="steps reveal">
    <div><b>Verkäufer</b><p>Ein realistisch eingeschätzter Wert und ein ehrliches Gutachten: Es findet sich oft schneller ein Käufer, und Interessenten können die Immobilie nicht schlechtreden.</p></div>
    <div><b>Käufer</b><p>Wer ein Renditeobjekt kauft, sollte den Sanierungsbedarf kennen, bevor er den Faktor akzeptiert.</p></div>
    <div><b>Erben</b><p>Bei der Bewertung gegenüber dem Finanzamt zählt der energetische Zustand mit. Ein Gutachten belegt ihn.</p></div>
  </div>
</div></section>
''' + cta('Gutachten für Ihr Wohngebäude', 'Nennen Sie uns Objekt und Anlass. Wir erklären Umfang und Ablauf.', 'Wertermittlung anfragen', 'kontakt.html?thema=wertermittlung')


def ueber_uns():
    return ph('Wer wir sind', 'Ein Familienunternehmen aus der Baubranche mit langjähriger Erfahrung in der Sanierung von Bestandsgebäuden. Für private Eigentümer und Wohnungseigentümergemeinschaften in Stolberg und der Region.',
              [('person', 'Ihr Berater'), ('unabhaengig', 'Unabhängig'), ('region', 'Region'), ('mitglied', 'Mitgliedschaften')],
              [('plaene-hand', 'Hand mit Lineal über einem Bauplan', 1013), ('daecher', 'Dächer einer Stadt', 1200), ('eingang-backstein', 'Eingang eines Backsteinhauses', 1200)]) + f'''
<section class="sec" id="person"><div class="wrap grid2">
  <div class="portrait reveal"><div class="portrait-ph" role="img" aria-label="Platz für ein Porträtfoto von Marijan Barlé">{MARK}<span>Porträt folgt</span></div></div>
  <div><h2 class="split">{CO['person']}</h2>
    <p class="reveal">Ausgebildeter Diplom-Bauingenieur (RWTH Aachen), Statiker und Gebäude-Energieberater (HWK), langjähriges Mitglied der Ingenieurkammer-Bau NRW. Als Energieeffizienz-Experte bei der dena (Deutsche Energie-Agentur) gelistet.</p>
    <p class="reveal">Wir sind persönlich für Sie da, besuchen Sie vor Ort, nehmen uns Zeit und führen unsere Beratungen selbst aus. Wir schicken keine Subunternehmer. Durch kontinuierliche Fortbildung und laufende Projekte sind wir immer auf aktuellem Stand.</p>
    <p class="reveal">Inhaberin des Unternehmens ist Renate Barlé ({CO['name']}).</p></div>
</div></section>
<section class="sec dark" id="unabhaengig"><div class="wrap">
  <h2 class="split">Unabhängig heißt: nur Ihr Interesse zählt.</h2>
  <div class="grid2">
    <p class="reveal lead">Wir sind weder an Handwerksbetriebe noch an Baufirmen gebunden. Deshalb können Sie sich bei uns unabhängig über Möglichkeiten der energetischen Sanierung beraten oder eine energetische Baubegleitung durchführen lassen.</p>
    <p class="reveal">Unser Schwerpunkt liegt auf der Beratung privater Immobilieneigentümer rund um Wärmeschutz, Feuchteschutz, Energieeffizienz und Sanierung: Energieberatung nach KfW/BAFA-Richtlinien, Sanierungsfahrpläne, Energieausweise, Baubegleitung, Wärmebrücken, Thermografie, Feuchteschutz und Wertermittlung.</p>
  </div>
</div></section>
<section class="sec" id="region"><div class="wrap grid2">
  <div><h2 class="split">Für Stolberg und die Region</h2>
    <p class="reveal">Von der Kortumstraße in Stolberg aus sind wir in der ganzen Städteregion Aachen und im Kreis Düren unterwegs.</p>
    <ul class="places reveal">{''.join(f'<li>{o}</li>' for o in ['Stolberg', 'Aachen', 'Eschweiler', 'Alsdorf', 'Würselen', 'Roetgen', 'Simmerath', 'Monschau', 'Düren', 'Jülich', 'Langerwehe', 'Herzogenrath'])}</ul></div>
  {figure('daecher', 'Dächer einer Stadt von oben', 1800, 1200, None, 'reveal')}
</div></section>
<section class="sec grey" id="mitglied"><div class="wrap">
  <h2 class="split">Mitgliedschaften und Listungen</h2>
  <div class="steps reveal">
    <div><b>Ingenieurkammer-Bau NRW</b><p>Langjähriges Mitglied. Die Kammer steht für die Berufsordnung der Ingenieure im Bauwesen.</p></div>
    <div><b>Energieeffizienz-Expertenliste (dena)</b><p>Gelistet in der Kategorie „Energieberatung für Wohngebäude“. Voraussetzung für geförderte Beratung, iSFP und Baubegleitung.</p></div>
    <div><b>DEN e.V.</b><p>Mitglied im Deutschen Energieberater-Netzwerk, dem Berufsverband unabhängiger Energieberater.</p></div>
    <div><b>Verband Privater Bauherren</b><p>Mitglied im VPB, der die Interessen privater Bauherren vertritt.</p></div>
  </div>
</div></section>
''' + cta('Lernen wir uns kennen.', 'Ein erstes Gespräch klärt, was für Ihr Gebäude sinnvoll ist.')


POSTS = [
    dict(file='ratgeber-schimmel-fenstertausch.html', t='Schimmel nach dem Fenstertausch: warum das passiert', d='2026-09-22', img='fenster-alt', alt='Altes Holzfenster', h=1200, teaser='Neue Fenster sind dicht, die Wand bleibt kalt. Warum sich der kälteste Punkt im Raum verlagert und was vorher zu prüfen ist.'),
    dict(file='ratgeber-energieausweis-baudenkmal.html', t='Energieausweis für Baudenkmale: was das GModG ändert', d='2026-09-22', img='fachwerk-gasse', alt='Fachwerkhäuser', h=1200, teaser='Bisher waren Baudenkmale von der Ausweispflicht befreit. Mit dem Gebäudemodernisierungsgesetz ändert sich das. Was Eigentümer jetzt wissen sollten.'),
    dict(file='ratgeber-isfp-15-jahre.html', t='Der Sanierungsfahrplan: 15 Jahre Zeit, keine Pflicht', d='2026-09-22', img='plaene-tisch', alt='Baupläne auf einem Tisch', h=1211, teaser='Was im iSFP steht, was er kostet, wie er gefördert wird und warum er unverbindlich ist und trotzdem der beste Einstieg.'),
]


def ratgeber():
    cards = ''.join(f'<a class="post reveal tilt" href="{p["file"]}"><figure>{img(p["img"], p["alt"], 1800, p["h"], sizes="(max-width: 820px) 100vw, 33vw")}</figure><div><h2>{p["t"]}</h2><p>{p["teaser"]}</p><span class="more">Lesen {ARROW}</span></div></a>' for p in POSTS)
    return ph('Ratgeber', 'Drei Themen aus unserer Beratungspraxis, ohne Werbesprache erklärt.', None) + f'<section class="sec"><div class="wrap"><div class="posts">{cards}</div></div></section>' + cta('Frage zu Ihrem Haus?', 'Wir antworten gern, auch wenn es nur eine kurze Einschätzung ist.')


def article(i, body):
    p = POSTS[i]
    others = ''.join(f'<li><a href="{o["file"]}">{o["t"]}</a></li>' for j, o in enumerate(POSTS) if j != i)
    return f'''<article class="article">
<section class="ph"><div class="wrap"><p class="crumbs"><a href="ratgeber.html">Ratgeber</a></p><h1 class="split">{p['t']}</h1><p class="lead reveal">{p['teaser']}</p></div></section>
<div class="wrap"><figure class="art-img reveal">{img(p['img'], p['alt'], 1800, p['h'], sizes='(max-width: 1100px) 100vw, 1040px')}</figure></div>
<section class="sec tight"><div class="wrap prose">{body}
<aside class="more-posts"><h3>Weitere Artikel</h3><ul>{others}</ul></aside></div></section>
</article>''' + cta('Betrifft das Ihr Haus?', 'Wir schauen uns das vor Ort an.')


def art_schimmel():
    return article(0, '''
<p>Ein häufiger Fall in unserer Praxis: Ein Haus hatte jahrzehntelang keinen Schimmel. Dann wurden die alten Fenster gegen dichte, dreifach verglaste ausgetauscht. Ein Winter später zeigen sich dunkle Flecken in der Raumecke hinter dem Schrank oder an der Fensterlaibung. Der Fensterbauer sagt: Sie lüften zu wenig. Der Eigentümer sagt: Vorher ging es doch auch. Beide haben ein bisschen recht.</p>
<h2>Der kälteste Punkt wandert</h2>
<p>Schimmel entsteht dort, wo feuchte Luft auf kühle Oberflächen trifft. In einem Raum gibt es immer eine kälteste Stelle, und dort kondensiert der Wasserdampf zuerst. Bei alten Fenstern war das die Scheibe: Man konnte das Tauwasser morgens abwischen, und die undichten Rahmen sorgten nebenbei für einen ständigen Luftwechsel.</p>
<p>Nach dem Tausch ist die Scheibe warm und der Rahmen dicht. Die Feuchte bleibt im Raum, und der kälteste Punkt ist jetzt die ungedämmte Außenwand, die Fensterlaibung oder die Ecke hinter dem Schrank. Genau dort wächst der Schimmel, oft lange unentdeckt.</p>
<h2>Ab wann es kritisch wird</h2>
<p>Für Schimmelwachstum braucht es kein Tauwasser. Es reicht, wenn die relative Feuchte direkt an der Oberfläche über mehrere Tage bei 70 bis 80 % liegt. Bei 20 °C Raumluft und 60 % Luftfeuchte liegt diese Grenze schon bei rund 15 °C Oberflächentemperatur. Eine alte Fensterlaibung ohne Dämmung erreicht im Winter leicht 12 bis 13 °C.</p>
<p>Unser <a href="thermografie-feuchteschutz.html#taupunkt">Taupunkt-Rechner</a> zeigt die Zusammenhänge für verschiedene Raumtemperaturen und Luftfeuchten.</p>
<h2>Was vorher zu prüfen ist</h2>
<p>Deshalb sollte auch vor einer Einzelmaßnahme eine Energieberatung stehen. Sie bewertet, ob der Fenstertausch die feuchtetechnische Balance des Gebäudes stört, und ob eine Innendämmung der Laibungen, eine Einzelraum-Lüftung oder eine andere Reihenfolge der Maßnahmen sinnvoll ist. Manchmal ist es besser, erst die Wand zu dämmen und dann die Fenster zu tauschen.</p>
<h2>Wenn der Schimmel schon da ist</h2>
<p>Dann hilft ein fachlich fundiertes Gutachten: Es klärt die Ursache mit Messungen und Thermografie und benennt die Maßnahmen. Und es hilft, wenn Handwerksfirmen die Verantwortung nicht übernehmen wollen. Mehr dazu auf der Seite <a href="thermografie-feuchteschutz.html">Thermografie und Feuchteschutz</a>.</p>''')


def art_denkmal():
    return article(1, '''
<p>Bis heute gilt: Wer ein denkmalgeschütztes Wohngebäude vermietet, verpachtet oder verkauft, muss keinen Energieausweis vorlegen. Das Gebäudeenergiegesetz (GEG) nimmt Baudenkmale ausdrücklich aus. Diese Ausnahme fällt.</p>
<h2>Was das GModG regelt</h2>
<p>Mit dem Gesetz zur Einsparung von Energie und zur Modernisierung der Wärmeversorgung in Gebäuden, kurz Gebäudemodernisierungsgesetz (GModG), wird die Energieausweispflicht auch auf denkmalgeschützte Gebäude ausgeweitet. Stand ist der Kabinettsbeschluss vom 13. Mai 2026; das parlamentarische Verfahren läuft. Wann und welche Art von Ausweis nötig ist, regelt dann das GModG.</p>
<h2>Verbrauchs- oder Bedarfsausweis?</h2>
<p>Beide Formen sind möglich. Der Verbrauchsausweis basiert auf dem gemessenen Verbrauch der letzten drei Abrechnungsjahre und ist schnell erstellt. Der Bedarfsausweis wird aus der Bausubstanz und der Anlagentechnik berechnet und ist bei alten Gebäuden mit wenigen Wohnungen häufig vorgeschrieben. Er sagt auch mehr über das Gebäude aus, weil er nicht vom Heizverhalten der bisherigen Bewohner abhängt.</p>
<h2>Warum es sich lohnt, nicht zu warten</h2>
<p>Wir stellen schon jetzt Energieausweise für denkmalgeschützte Wohngebäude aus, für Vermietung und Verkauf ebenso wie nach einer Sanierung oder einem Umbau. Wer verkaufen oder neu vermieten will, hat den Ausweis dann in der Hand, wenn das Gesetz in Kraft tritt. Für die Bewertung der Immobilie ist der energetische Zustand ohnehin ein Faktor, siehe <a href="wertermittlung.html">Wertermittlung</a>.</p>
<h2>Besonderheit Denkmal</h2>
<p>Bei Baudenkmalen sind viele Standardmaßnahmen nicht erlaubt oder nicht sinnvoll: Außendämmung an einer Fachwerkfassade, neue Kunststofffenster, Solaranlagen auf dem Dach. Ein Energieausweis ändert daran nichts. Er stellt nur den Zustand fest. Welche Maßnahmen im Rahmen des Denkmalschutzes möglich sind, klärt eine <a href="energieberatung.html#frei">freie Energieberatung</a>.</p>''')


def art_isfp():
    return article(2, '''
<p>Der individuelle Sanierungsfahrplan, kurz iSFP, ist das Dokument, um das sich seit dem 1. Juli 2023 die geförderte Energieberatung dreht. Ohne ihn keine Förderung der Beratung. Trotzdem kursieren viele Missverständnisse.</p>
<h2>Was drinsteht</h2>
<p>Der iSFP fasst die Bestandsanalyse von Gebäudehülle und Anlagentechnik übersichtlich in Bild und Text zusammen und vergleicht den energetischen Zustand mit den aktuellen gesetzlichen Anforderungen, ähnlich einem Energiebedarfsausweis. Dazu kommen Sanierungsmaßnahmen, mit denen das Gebäude Schritt für Schritt oder als Gesamtpaket zum Effizienzhaus modernisiert werden kann: mit geschätzten Kosten, berechneten Einsparungen bei Heizung und Warmwasser und Hinweisen auf Fördermittel.</p>
<h2>Was er nicht ist: eine Pflicht</h2>
<p>Die Maßnahmen im iSFP sind Empfehlungen. Es besteht keine gesetzliche Pflicht, sie umzusetzen. Sie können an jeder beliebigen Stelle aufhören, die Reihenfolge ändern oder nur einzelne Maßnahmen umsetzen. Die Förderung für bereits umgesetzte Maßnahmen muss nicht zurückgezahlt werden, wenn Sie andere Maßnahmen des Fahrplans nicht durchführen.</p>
<h2>15 Jahre Zeit</h2>
<p>Für die Umsetzung und die Nutzung der Fördermöglichkeiten steht ein Zeitraum von insgesamt 15 Jahren zur Verfügung. Das nimmt den Druck: Erst das Dach, in fünf Jahren die Heizung, wenn das Geld da ist die Fenster.</p>
<h2>Was er bringt</h2>
<p>Der iSFP ist oft Voraussetzung für zusätzliche Fördergelder, zum Beispiel den 5-Prozent-Bonus bei geförderten Einzelmaßnahmen. Und die Erstellung selbst wird gefördert, wenn sie von einem Energieberater aus der Energieeffizienz-Expertenliste kommt. Die Beratung wird mit 50 % des Honorars bezuschusst, bis 650 € bei Ein- und Zweifamilienhäusern und bis 850 € ab drei Wohneinheiten (Stand März 2025).</p>
<h2>Wie wir ihn erstellen</h2>
<p>Nicht „von oben herab“. Alle Maßnahmen werden vorab erläutert und mit Ihnen besprochen und erst dann im Ablauf festgelegt. Die Kosten basieren auf Erfahrungswerten oder bereits vorliegenden Angeboten. Mehr auf der Seite <a href="energieberatung.html#isfp">Energieberatung und Sanierungsfahrplan</a>.</p>''')


FAQ = [
    ('Was kostet eine Energieberatung?', 'Das Honorar hängt von Gebäudegröße und Umfang ab; wir nennen es vorab. Die geförderte Beratung mit Sanierungsfahrplan bezuschusst das BAFA mit 50 % des förderfähigen Honorars, bis 650 € bei Ein- und Zweifamilienhäusern und bis 850 € ab drei Wohneinheiten (Stand März 2025).'),
    ('Brauche ich eine Beratung, wenn ich nur die Fenster tauschen will?', 'Wir empfehlen sie. Einzelmaßnahmen an der Gebäudehülle können die feuchtetechnische Balance des Hauses stören, dann entsteht Schimmel, wo vorher keiner war. Die Beratung klärt außerdem, ob das Geld woanders besser angelegt wäre.'),
    ('Was ist der Unterschied zwischen BAFA-Beratung und freier Beratung?', 'Die BAFA-Beratung folgt strikten Vorgaben (20 °C in jedem Raum, Warmwasser nach Wohnfläche) und wird gefördert. Die freie Beratung rechnet mit Ihrer tatsächlichen Nutzung, ist nicht an Förderprogramme gebunden und eignet sich, wenn Sie Kosten lieber steuerlich absetzen.'),
    ('Muss ich alle Maßnahmen aus dem Sanierungsfahrplan umsetzen?', 'Nein. Der iSFP enthält Empfehlungen, keine Pflichten. Sie können jederzeit aufhören, die Reihenfolge ändern und behalten die Förderung für schon umgesetzte Maßnahmen. Sie haben 15 Jahre Zeit.'),
    ('Welchen Energieausweis brauche ich?', 'Das regelt das GEG: Neubau und alte Gebäude mit weniger als fünf Wohnungen brauchen meist einen Bedarfsausweis, Gebäude ab fünf Wohnungen dürfen einen Verbrauchsausweis nutzen. Unsere Entscheidungsweiche auf der Seite Energieausweis führt Sie hin.'),
    ('Gilt die Ausweispflicht auch für Baudenkmale?', 'Bisher nicht. Mit dem Gebäudemodernisierungsgesetz (GModG, Kabinettsbeschluss vom 13. Mai 2026) wird sie eingeführt. Wir stellen schon jetzt Ausweise für denkmalgeschützte Wohngebäude aus.'),
    ('Übernimmt die Baubegleitung auch die Bauleitung?', 'Nein. Baubegleitung umfasst keine Planung, keinen Bauantrag, keine Statik und keine Bauleitung; sie überwacht die energetische Qualität und dokumentiert sie. Der Energieeffizienz-Experte muss unabhängig bleiben.'),
    ('Wann ist die beste Zeit für eine Thermografie?', 'Im Winter, wenn der Temperaturunterschied zwischen innen und außen am größten ist. Aufnahmen entstehen von außen; für Schimmelfragen auch innen.'),
    ('Wo sind Sie tätig?', 'In Stolberg und der Städteregion Aachen (Aachen, Eschweiler, Alsdorf, Würselen, Roetgen, Simmerath, Monschau) sowie im Kreis Düren (Düren, Jülich, Langerwehe).'),
    ('Kommen Subunternehmer?', 'Nein. Dipl.-Ing. Marijan Barlé führt jede Beratung selbst durch, vor Ort.'),
]


def faq():
    items = ''.join(f'<details class="reveal"{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(FAQ))
    return ph('Häufige Fragen', 'Kurze Antworten auf das, was uns am häufigsten gefragt wird.', None) + f'<section class="sec"><div class="wrap narrow"><div class="faq">{items}</div></div></section>' + cta('Ihre Frage war nicht dabei?', 'Rufen Sie an oder schreiben Sie uns.')


def kontakt():
    return ph('Kontakt', f'Ihr Ansprechpartner ist {CO["person"]}. Rufen Sie an, schreiben Sie eine E-Mail oder nutzen Sie das Formular.', None) + f'''
<section class="sec tight"><div class="wrap grid2 contact">
  <div>
    <ul class="contact-list big reveal"><li>{TEL}<a href="tel:{CO['telh']}">{CO['tel']}</a></li><li>{MAIL}<a href="mailto:{CO['mail']}">{CO['mail']}</a></li><li>{PIN}<span>{CO['name']}<br>{CO['brand']}<br>{CO['street']}, {CO['zip']} {CO['city']}</span></li></ul>
    <div class="map reveal" id="map"><button type="button" class="btn ghost" id="map-btn">Karte laden (OpenStreetMap)</button><p class="small">Die Karte wird erst nach Klick von openstreetmap.org geladen.</p></div>
  </div>
  {form()}
</div></section>'''


def danke():
    return f'<section class="ph"><div class="wrap"><h1 class="split">Danke für Ihre Anfrage.</h1><p class="lead reveal">Wir melden uns innerhalb von zwei Werktagen. Wenn es eilt: {TEL} <a href="tel:{CO["telh"]}">{CO["tel"]}</a>.</p><a class="btn blue" href="index.html">Zur Startseite</a></div></section>'


def err404():
    return '<section class="ph"><div class="wrap"><h1 class="split">Diese Seite gibt es nicht.</h1><p class="lead reveal">Vielleicht ist die Adresse von der alten Website. Die Leistungen finden Sie hier:</p><ul class="places">' + ''.join(f'<li><a href="{f}">{t}</a></li>' for f, t, _ in SERVICES) + '</ul><a class="btn blue" href="index.html">Zur Startseite</a></div></section>'


def impressum():
    return ph('Impressum', 'Anbieterkennzeichnung nach § 5 Digitale-Dienste-Gesetz (DDG).', None) + f'''
<section class="sec tight"><div class="wrap prose">
<h2>Anbieter</h2><p>{CO['name']}<br>Renate Barlé – {CO['brand']}<br>{CO['street']}<br>{CO['zip']} {CO['city']}</p>
<p>E-Mail: <a href="mailto:{CO['mail']}">{CO['mail']}</a><br>Telefon: <a href="tel:{CO['telh']}">{CO['tel']}</a></p>
<h2>Inhaltlich Verantwortliche i. S. d. § 18 Abs. 2 MStV</h2><p>Renate Barlé, Anschrift wie oben, <a href="mailto:{CO['mail']}">{CO['mail']}</a></p>
<h2>Berufsbezeichnung</h2><p>Energieberatung durch {CO['person']}, Diplom-Bauingenieur (verliehen in Deutschland), Mitglied der Ingenieurkammer-Bau NRW, Zollhof 2, 40221 Düsseldorf. Es gelten das Baukammerngesetz NRW und die Berufsordnung der Ingenieurkammer-Bau NRW (abrufbar unter www.ikbaunrw.de).</p>
<h2>Umsatzsteuer</h2><p>Umsatzsteuer-Identifikationsnummer bzw. Hinweis auf Kleinunternehmerregelung: <em>bitte ergänzen</em>.</p>
<h2>Streitbeilegung</h2><p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung bereit: <a href="https://ec.europa.eu/consumers/odr/" rel="noopener" target="_blank">ec.europa.eu/consumers/odr</a>. Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Bildnachweis</h2><p>Fotos von Unsplash (Unsplash-Lizenz); Fotografinnen und Fotografen sind in der Datei img/BILDNACHWEIS.md genannt. Wärmebild-Darstellungen sind nachempfunden und keine echten Messaufnahmen.</p>
</div></section>'''


def datenschutz():
    return ph('Datenschutzerklärung', 'Wie wir mit Ihren Daten umgehen, wenn Sie diese Website besuchen oder uns kontaktieren.', None) + f'''
<section class="sec tight"><div class="wrap prose">
<p>Verantwortliche für den Datenschutz: Renate Barlé, {CO['street']}, {CO['zip']} {CO['city']}, Telefon {CO['tel']}, E-Mail <a href="mailto:{CO['mail']}">{CO['mail']}</a>.</p>
<h2>1. Widerspruchsmöglichkeit</h2><p>Sofern Sie der Verarbeitung Ihrer Daten durch den Betreiber nach Maßgabe dieser Datenschutzerklärung insgesamt oder für einzelne Maßnahmen widersprechen wollen, können Sie dies unter den im Impressum angegebenen Kontaktdaten tun. Bitte beachten Sie, dass im Falle eines solchen Widerspruchs die Nutzung der Website und der Abruf der hierüber angebotenen Leistungen unter Umständen nur eingeschränkt oder überhaupt nicht möglich sind.</p>
<h2>2. Aufruf und Nutzung der Website</h2><p>Bei jedem Zugriff werden Nutzungsdaten durch den Browser übermittelt und in Protokolldateien gespeichert (Server-Logfiles): Datum und Uhrzeit des Abrufs, IP-Adresse, Betriebssystem, übertragene Datenmenge, Produkt- und Versionsinformationen des Browsers. Die Protokolldateien werden anonymisiert ausgewertet, um die Website zu verbessern, Fehler zu finden und Serverkapazitäten zu steuern. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DS-GVO (berechtigtes Interesse am Betrieb und an der Sicherheit der Website). Die Bereitstellung ist weder gesetzlich noch vertraglich vorgeschrieben. Die IP-Adresse wird nach Beendigung der Nutzung gelöscht. Hosting-Anbieter: <em>bitte ergänzen (z. B. Netlify Inc., mit Auftragsverarbeitungsvertrag)</em>.</p>
<h2>3. Kontaktformular und E-Mail</h2><p>Über das Kontaktformular können Sie uns Name, E-Mail-Adresse, Ort des Gebäudes, Telefonnummer und Ihre Nachricht übermitteln. Die Daten werden ausschließlich zur Bearbeitung Ihrer Anfrage verwendet und nach Abschluss gelöscht, sofern keine gesetzlichen Aufbewahrungspflichten bestehen. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DS-GVO (vorvertragliche Maßnahmen) sowie Ihre Einwilligung nach Art. 6 Abs. 1 lit. a DS-GVO, die Sie jederzeit widerrufen können. Die Formulardaten werden durch den Hosting-Anbieter (siehe oben) technisch entgegengenommen. Beim Klick auf eine E-Mail-Adresse öffnet sich Ihr E-Mail-Programm; dabei wird die dort hinterlegte Absenderadresse verwendet.</p>
<h2>4. Keine Cookies, keine Analyse, keine externen Schriften</h2><p>Diese Website setzt keine Cookies, verwendet keine Analyse- oder Tracking-Dienste und lädt Schriften ausschließlich vom eigenen Server. Die Animationsbibliotheken GSAP und Lenis werden vom Content-Delivery-Netzwerk jsDelivr geladen; dabei wird Ihre IP-Adresse an jsDelivr übermittelt (Art. 6 Abs. 1 lit. f DS-GVO, berechtigtes Interesse an einer schnellen Auslieferung).</p>
<h2>5. Karte (OpenStreetMap)</h2><p>Auf der Kontaktseite wird eine Karte erst geladen, wenn Sie auf „Karte laden“ klicken. Dann werden Daten (u. a. Ihre IP-Adresse) an die OpenStreetMap Foundation, St John's Innovation Centre, Cowley Road, Cambridge, CB4 0WS, Großbritannien, übermittelt. Rechtsgrundlage ist Ihre Einwilligung durch den Klick (Art. 6 Abs. 1 lit. a DS-GVO).</p>
<h2>6. Ihre Rechte</h2><p>Sie haben das Recht auf Auskunft (Art. 15 DS-GVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21). Außerdem können Sie sich bei einer Aufsichtsbehörde beschweren, zuständig ist die Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen, Kavalleriestraße 2-4, 40213 Düsseldorf.</p>
<h2>7. Datensicherheit</h2><p>Die Website wird über eine verschlüsselte Verbindung (TLS/HTTPS) ausgeliefert. Wir treffen technische und organisatorische Maßnahmen, um Ihre Daten gegen Verlust, Manipulation und unberechtigten Zugriff zu schützen.</p>
<p class="small">Stand: September 2026</p>
</div></section>'''


PAGES = [
    dict(file='index.html', title='Energieberatung Regio Stolberg – unabhängig, vor Ort', desc='Unabhängige Energieberatung für Wohngebäude in Stolberg und Region Aachen: BAFA-Beratung, Sanierungsfahrplan, Energieausweis, Thermografie, Feuchteschutz.', body=index, body_cls='home'),
    dict(file='energieberatung.html', title='Energieberatung & Sanierungsfahrplan (iSFP) – Stolberg', desc='Beratung nach BAFA/KfW und freie Beratung für Bestandsgebäude, Sanierungsfahrplan mit 50 % Förderung. Dipl.-Ing. Marijan Barlé, Stolberg.', body=energieberatung),
    dict(file='energieausweis.html', title='Energieausweis für Wohngebäude & Baudenkmale – Stolberg', desc='Bedarfs- oder Verbrauchsausweis? Pflichten nach GEG und die neue Ausweispflicht für Baudenkmale (GModG). Ausstellung in Stolberg und Region Aachen.', body=energieausweis),
    dict(file='baubegleitung.html', title='Energetische Baubegleitung & Wärmebrückenberechnung', desc='Baubegleitung durch den Energieeffizienz-Experten mit 50 % Förderung, Wärmebrückennachweis und Simulation bis KfW 40. Unabhängig, Region Aachen.', body=baubegleitung),
    dict(file='thermografie-feuchteschutz.html', title='Thermografie, Feuchteschäden & Schimmel – Gutachten Stolberg', desc='Wärmebildaufnahmen, Taupunkt-Rechner, Ursachen von Feuchteschäden und Wohnungsschimmel, fachliche Gutachten. Energieberatung Regio Stolberg.', body=thermografie),
    dict(file='wertermittlung.html', title='Wertermittlung von Wohngebäuden – Gutachten Stolberg', desc='Gutachten nach Vergleichswert-, Sachwert- und Ertragswertverfahren mit Blick auf den energetischen Zustand. Für Verkäufer, Käufer und Erben.', body=wertermittlung),
    dict(file='ueber-uns.html', title='Über uns – Dipl.-Ing. Marijan Barlé, Energieberater Stolberg', desc='Familienunternehmen aus der Baubranche: Diplom-Bauingenieur (RWTH), Gebäude-Energieberater (HWK), dena-gelistet, Ingenieurkammer-Bau NRW, DEN e.V.', body=ueber_uns),
    dict(file='ratgeber.html', title='Ratgeber – Schimmel, Energieausweis, Sanierungsfahrplan', desc='Praxiswissen aus Stolberg: Schimmel nach Fenstertausch, Energieausweis für Baudenkmale, der individuelle Sanierungsfahrplan.', body=ratgeber),
    dict(file=POSTS[0]['file'], title='Schimmel nach dem Fenstertausch: warum das passiert', desc=POSTS[0]['teaser'], body=art_schimmel, parent='ratgeber.html', article=True, ld={"@context": "https://schema.org", "@type": "Article", "headline": POSTS[0]['t'], "datePublished": POSTS[0]['d'], "author": {"@type": "Person", "name": "Marijan Barlé"}, "publisher": {"@id": DOMAIN + "/#business"}, "image": DOMAIN + "/img/fenster-alt.webp"}),
    dict(file=POSTS[1]['file'], title='Energieausweis für Baudenkmale: was das GModG ändert', desc=POSTS[1]['teaser'], body=art_denkmal, parent='ratgeber.html', article=True, ld={"@context": "https://schema.org", "@type": "Article", "headline": POSTS[1]['t'], "datePublished": POSTS[1]['d'], "author": {"@type": "Person", "name": "Marijan Barlé"}, "publisher": {"@id": DOMAIN + "/#business"}, "image": DOMAIN + "/img/fachwerk-gasse.webp"}),
    dict(file=POSTS[2]['file'], title='Sanierungsfahrplan: 15 Jahre Zeit, keine Pflicht', desc=POSTS[2]['teaser'], body=art_isfp, parent='ratgeber.html', article=True, ld={"@context": "https://schema.org", "@type": "Article", "headline": POSTS[2]['t'], "datePublished": POSTS[2]['d'], "author": {"@type": "Person", "name": "Marijan Barlé"}, "publisher": {"@id": DOMAIN + "/#business"}, "image": DOMAIN + "/img/plaene-tisch.webp"}),
    dict(file='faq.html', title='Häufige Fragen zur Energieberatung – Regio Stolberg', desc='Kosten, Förderung, BAFA oder frei, Sanierungsfahrplan, Energieausweis, Baudenkmal, Baubegleitung, Thermografie: kurz beantwortet.', body=faq, ld={"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}),
    dict(file='kontakt.html', title='Kontakt – Energieberatung Regio Stolberg, Kortumstraße 8', desc='Dipl.-Ing. Marijan Barlé: Telefon 0173 730 84 67, energieberatung@regio-stolberg.de oder Formular. Vor-Ort-Termine in Stolberg und der Region Aachen.', body=kontakt),
    dict(file='danke.html', title='Danke für Ihre Anfrage – Energieberatung Regio Stolberg', desc='Wir melden uns innerhalb von zwei Werktagen.', body=danke, noindex=True),
    dict(file='404.html', title='Seite nicht gefunden – Energieberatung Regio Stolberg', desc='Diese Seite gibt es nicht.', body=err404, noindex=True),
    dict(file='impressum.html', title='Impressum – Energieberatung Regio Stolberg', desc='Anbieterkennzeichnung der Energieberatung Regio Stolberg (Renate Barlé Hausdienste).', body=impressum),
    dict(file='datenschutz.html', title='Datenschutzerklärung – Energieberatung Regio Stolberg', desc='Datenschutzerklärung der Energieberatung Regio Stolberg.', body=datenschutz),
]

for p in PAGES:
    html = head(dict(p, body=p.get('body_cls', ''))) + p['body']() + foot(p)
    with open(OUT + p['file'], 'w', encoding='utf-8') as f:
        f.write(html)

with open(OUT + 'sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{DOMAIN}/{"" if p["file"]=="index.html" else p["file"]}</loc><lastmod>{TODAY}</lastmod></url>\n' for p in PAGES if not p.get('noindex')) + '</urlset>\n')
print('ok', len(PAGES), 'Seiten')
