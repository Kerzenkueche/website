# website
Offizielle Website der Kerzenküche – https://www.kerzenküche.de

## Aufbau

| Seite | Datei |
|---|---|
| Startseite | `index.html` |
| Taufkerzen | `taufkerzen/index.html` |
| Kommunion & Konfirmation | `kommunion-konfirmation/index.html` |
| Hochzeitskerzen | `hochzeitskerzen/index.html` |
| Trauer & Gedenken | `trauerkerzen/index.html` |
| Geburtstag & Jubiläum | `geburtstagskerzen/index.html` |
| Galerie | `galerie/index.html` |
| Ratgeber Taufsprüche | `ratgeber/taufsprueche/index.html` |
| Impressum / Datenschutz / Widerruf | `impressum/`, `datenschutz/`, `widerruf/` |

Gestaltung: `css/style.css` · Skripte: `js/main.js` · Schriften liegen lokal in `fonts/` (keine Google-Dienste).

## Neues Bild in die Galerie

1. Bild auf ca. 1500 px Breite verkleinern.
2. In den Ordner `galerie/bilder/` hochladen (Dateiname klein, ohne Leerzeichen/Umlaute).
3. In `galerie/bilder.js` eine Zeile ergänzen, z. B.
   `{ datei: "/galerie/bilder/taufkerze-regenbogen.jpg", anlass: "taufe", titel: "Taufkerze mit Regenbogen und Taube", kurz: "Regenbogen" },`

   `titel` = ausführliche Beschreibung (Großansicht, Google) · `kurz` = 2–3 Wörter unter dem Vorschaubild

Anlass: `taufe`, `kommunion`, `hochzeit`, `trauer`, `geburtstag`, `deko`, `duft` oder `weitere`. Die Bilder erscheinen automatisch in der Galerie **und** auf der passenden Anlass-Seite.

Bei Kerzen mit Namen/Datum nur mit Einverständnis der Kunden veröffentlichen.

**Vorschaubild (optional):** Dieselbe Datei auf 640 px Breite verkleinert unter `galerie/bilder/thumbs/` ablegen (gleicher Dateiname). Fehlt sie, wird automatisch das große Bild verwendet.

## Seiten neu erzeugen

Alle HTML-Seiten, die Sitemap und die Galerie-Vorschau im HTML werden von `_werkzeug/build.py` erzeugt:

```
python _werkzeug/build.py .
```

Texte, Anlass-Seiten und Ratgeber stehen dort. Der Ordner `_werkzeug/` wird von GitHub Pages nicht veröffentlicht.
