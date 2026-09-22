# Launch-Checkliste – Energieberatung Regio Stolberg

Stand: 22. September 2026 · Projektordner `Documents/website 1/eb-stolberg-web/`
Vorlage/Inhaltsquelle: https://www.eb-stolberg.de (alle Texte, Kontaktdaten, Impressum von dort übernommen und neu gegliedert)

**Wichtig: unbeauftragter Entwurf.** Vor dem Online-Stellen braucht es das Einverständnis von Renate Barlé bzw. Marijan Barlé.

---

## 1. Recht

| Punkt | Stand | Anmerkung |
|---|---|---|
| Impressum | ⚠️ fast fertig | Angaben aus dem alten Impressum übernommen (Renate Barlé Hausdienste, Kortumstraße 8, 52222 Stolberg, Telefon, E-Mail, MStV-Verantwortliche). **Offen: Umsatzsteuer-ID bzw. Hinweis auf Kleinunternehmerregelung** – im Text als „bitte ergänzen“ markiert. Berufsangaben (Ingenieurkammer-Bau NRW) ergänzt, vom Kunden bestätigen lassen. |
| Datenschutzerklärung | ⚠️ fast fertig | Neu geschrieben, an die neue Technik angepasst (Formular, jsDelivr, OpenStreetMap). **Offen: Name des Hosting-Anbieters** an zwei Stellen als „bitte ergänzen“ markiert. |
| Cookie-Banner | ✅ nicht nötig | Keine Cookies, kein Tracking, Schriften lokal, Karte erst nach Klick. |
| Kontaktformular-Einwilligung | ✅ | Pflicht-Häkchen mit Verweis auf die Datenschutzerklärung; Prüfung im Browser getestet. |
| AGB | ✅ nicht nötig | Die alte Website hat keine. |
| Bildrechte | ✅ mit Hinweis | Alle 21 Fotos von Unsplash (Unsplash-Lizenz: kostenlos, auch kommerziell, ohne Namensnennung). Fotografinnen und Fotografen in `img/BILDNACHWEIS.md` und im Impressum genannt. Von der alten Website war kein Foto verwendbar (dort gibt es nur eine Grafik). **Empfehlung: eigene Fotos von Marijan Barlé, Vor-Ort-Terminen und echten Wärmebildern nachreichen.** |
| Wärmebild-Darstellungen | ✅ gekennzeichnet | Das Wärmebild ist aus dem Foto berechnet, kein echtes Messbild. Steht als Hinweis unter der Lupe, auf der Thermografie-Seite und im Impressum. |

## 2. Inhalt und Zahlen

| Punkt | Stand | Anmerkung |
|---|---|---|
| Fördersätze | ⚠️ prüfen | Alle Beträge stammen wörtlich von der alten Website (Stand März 2025): 50 %, max. 650 € / 850 €, 250 € WEG, Baubegleitung 5.000/2.000/20.000 € bzw. 10.000/4.000/40.000 €. Disclaimer auf jeder betroffenen Seite. **Vor dem Start gegen bafa.de und kfw.de abgleichen.** |
| Beispielhonorare | ⚠️ Richtwerte | 1.300 € bzw. 1.900 € im Förder-Beleg und im Donut sind **frei gewählte Richtwerte zur Veranschaulichung**, als solche gekennzeichnet. Vom Kunden echte Werte einsetzen lassen oder weglassen. |
| Wertermittlung-Rechner | ⚠️ Richtwerte | Kaltmieten, Faktoren und Sanierungsbedarf sind Beispielwerte, gekennzeichnet. |
| Taupunkt-Rechner | ✅ | Magnus-Formel, geprüft (20 °C / 60 % → 12,0 °C Taupunkt, 15,4 °C Schimmelgrenze). Als Richtwert gekennzeichnet. |
| Wärmebrücken-Beispiel | ✅ | 0,20 + 0,10 gegen 0,20 + 0,03 W/m²K; Zahlen und Rechnung wörtlich von der alten Website. |
| GEG-Effizienzklassen | ✅ | Skala nach Anlage 10 GEG (A+ bis H, Grenzwerte in kWh/m²a). |
| GModG / Baudenkmale | ✅ | Kabinettsbeschluss vom 13.5.2026 wie auf der alten Seite; Gesetzgebungsverfahren vor dem Start noch einmal prüfen. |
| Keine erfundenen Inhalte | ✅ | Keine Kundenstimmen, keine Projektzahlen, keine Jahreszahlen ohne Quelle. |
| Porträtfoto | ⚠️ offen | Auf „Über uns“ steht ein Platzhalter „Porträt folgt“. Foto von Marijan Barlé nachreichen. |

## 3. Technik

| Punkt | Stand | Messwert |
|---|---|---|
| JS-Fehler | ✅ 0 | Alle 17 Seiten, Chromium und WebKit, je 1400 px und 390 px, komplett durchgescrollt. |
| Horizontales Scrollen | ✅ keins | `scrollWidth == clientWidth` an allen Prüfpunkten (ein gefundener Fall auf der Baubegleitungs-Seite bei 390 px wurde behoben: Silbentrennung für lange Wörter). |
| Ladegröße bis „load“ | ✅ | Startseite Desktop 246 KB, Handy 152 KB. Größte Unterseite (Thermografie) Desktop 248 KB. Ziel war < 900 KB / < 500 KB. |
| Bilder | ✅ | WebP in drei Größen (800 / 1200 / 1600–1800 px) mit `srcset`, `width`/`height`, Lazy-Loading. Szene-Fotos ab Bild 2 erst nach dem `load`-Ereignis. |
| Schriften | ✅ | Public Sans Variable lokal in `fonts/`, vorgeladen, kein Google-Fonts-Aufruf. |
| Externe Skripte | ✅ | Nur GSAP, ScrollTrigger und Lenis von jsDelivr (feste Versionen), in der Datenschutzerklärung genannt und in der CSP erlaubt. |
| Formular | ✅ | Netlify-Forms-fertig (`data-netlify`, Honeypot `firma`), Themen-Vorwahl über `?thema=`, Prüfung im Browser, Weiterleitung auf `danke.html` getestet. |
| Karte | ✅ | OpenStreetMap lädt erst nach Klick. |
| Sicherheits-Header | ✅ | `netlify.toml` mit CSP, X-Frame-Options, nosniff, Referrer-Policy, Permissions-Policy. |
| Weiterleitungen | ✅ | Alle 12 alten Adressen (`dienstleistungen-01.html`, `energieberatung-bafa-01…08.html`, `datenschutzerklaerung.html` …) auf die neuen Seiten in `netlify.toml`. |

## 4. SEO

| Punkt | Stand | Anmerkung |
|---|---|---|
| Meta-Titel ≤ 65 Zeichen | ✅ | Alle 17 Seiten geprüft. |
| Descriptions ≤ 155 Zeichen | ✅ | Alle 17 Seiten geprüft. |
| Canonical | ✅ | Auf allen Seiten, Domain `https://www.eb-stolberg.de`. |
| JSON-LD | ✅ | LocalBusiness auf allen Seiten, FAQPage auf `faq.html`, Article auf den drei Ratgeber-Artikeln. |
| OG-Tags + og.jpg | ✅ | Eigenes Bild 1200×630 (Foto + Logo + Claim). |
| sitemap.xml / robots.txt | ✅ | 15 indexierbare Seiten, `danke.html` und `404.html` auf noindex. |
| Favicon / Apple-Touch-Icon | ✅ | `favicon.svg` und `apple-touch-icon.png` (180×180). |
| 404-Seite | ✅ | Mit Links auf alle Leistungen. |
| Lokale SEO-Daten | ⚠️ prüfen | Adresse, Telefon, Koordinaten (50.7726 / 6.2280) im JSON-LD. **Koordinaten und Öffnungs-/Erreichbarkeitszeiten vom Kunden bestätigen lassen; Google-Unternehmensprofil anlegen oder aktualisieren.** |
| Interne Links | ✅ | 0 kaputte Links, 0 fehlende Anker, 0 fehlende Bilddateien (automatisch geprüft). |
| Externe Links | ✅ | jsDelivr und die EU-ODR-Plattform antworten mit 200. |

## 5. Barrierefreiheit und Bewegung

| Punkt | Stand | Anmerkung |
|---|---|---|
| Farbkontrast AA | ✅ | Alle sichtbaren Texte auf allen 17 Seiten automatisch geprüft und nachgebessert (Blau auf #0a76a6 abgedunkelt, Warnfarbe, Skalenbeschriftung). |
| Tastaturbedienung | ✅ | Sprungmarke, Menü mit Fokusfalle und Escape, Aufklappliste, alle Rechner und die Entscheidungsweiche mit echten Buttons. Tab-Reihenfolge geprüft. |
| Fokus-Ringe | ✅ | Deutlich sichtbar (3 px, blau), nie entfernt. |
| Alt-Texte | ✅ | Alle Inhaltsfotos beschrieben, Deko-Bilder `aria-hidden`. |
| `prefers-reduced-motion` | ✅ in drei Stufen | Entfernt: Szene (wird zur statischen Foto-Reihe mit Bildunterschriften), Lenis, Pins, 3D-Zitat, Lupenfahrt. Verkürzt: Reveals werden zu kurzen Einblendungen. Behalten: Fokus, Hover, Zustandswechsel. Geprüft: alle 73 Textelemente vollständig sichtbar, 0 JS-Fehler. |
| Handy | ✅ | Jede Scroll-Animation läuft bei 390 px (Szene wie am Mac), Inhaltsverzeichnis wird zur Chip-Reihe, Sticky-CTA unten. |

## 6. Sicherung und Veröffentlichung

| Punkt | Stand |
|---|---|
| Sicherung als `.tar.gz` im Ordner „website 1“ | ✅ `eb-stolberg-web_2026-09-22.tar.gz` |
| Git-Repository | ✅ lokal, alles eingecheckt |
| GitHub Pages | siehe PROJEKTE-UEBERSICHT.md |
| Eintrag in PROJEKTE-UEBERSICHT.md | ✅ |

---

## Offene Punkte für den Kunden (kurz)

1. **Einverständnis**, dass die Seite online geht (unbeauftragter Entwurf).
2. **Umsatzsteuer-ID** oder Hinweis auf Kleinunternehmerregelung fürs Impressum.
3. **Hosting-Anbieter** für die Datenschutzerklärung (zwei Stellen).
4. **Eigene Fotos**: Porträt von Marijan Barlé, Vor-Ort-Aufnahmen, echte Wärmebilder.
5. **Zahlen bestätigen**: Beispielhonorare (1.300 € / 1.900 €), aktuelle BAFA-/KfW-Fördersätze, Koordinaten und Erreichbarkeit.
