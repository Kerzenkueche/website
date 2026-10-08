/*
  ==========================================================================
  GALERIE – hier tragt ihr eure Bilder ein
  ==========================================================================

  So kommt ein neues Bild in die Galerie:
  1. Bild auf ca. 1500 Pixel Breite verkleinern (spart Ladezeit am Handy).
  2. Bild in den Ordner  galerie/bilder/  hochladen,
     z. B. als  taufkerze-regenbogen.jpg  (Kleinbuchstaben, keine Leerzeichen/Umlaute).
  3. Unten eine neue Zeile nach dem gleichen Muster einfügen.
     titel = ausführliche Beschreibung (Großansicht + Google)
     kurz  = kurzer Name unter dem Vorschaubild (2–3 Wörter)

  anlass: taufe | kommunion | hochzeit | trauer | geburtstag | schule | deko | duft | weitere
  auswahl: true  = erscheint in der Bilderauswahl auf der Startseite (am besten 6 Stück)
  Die Reihenfolge hier ist die Reihenfolge in der Galerie.

  WICHTIG – Datenschutz: Auf Taufkerzen o. ä. stehen Name und Datum.
  Nur Bilder zeigen, wenn die Kunden einverstanden sind – oder Nachnamen
  bzw. Daten vorher unkenntlich machen.
*/

window.GALERIE = [
    // Taufe
    { datei: "/galerie/bilder/taufkerze-lebensbaum-blau.jpg",         anlass: "taufe",      titel: "Taufkerze mit blauem Lebensbaum und Taube", kurz: "Lebensbaum in Blau", auswahl: true },
    { datei: "/galerie/bilder/taufkerze-blaue-rosen-sonne-fische.jpg", anlass: "taufe",     titel: "Taufkerze mit blauen Rosen, Sonne, Lebensbaum und Fischen", kurz: "Blaue Rosen & Sonne" },
    { datei: "/galerie/bilder/taufkerze-bordeaux-kreuz-taube.jpg",    anlass: "taufe",      titel: "Taufkerze mit bordeauxrotem Kreuz, Taube und Röschen", kurz: "Bordeaux mit Taube" },
    { datei: "/galerie/bilder/taufkerzen-blau-kreuz-lebensbaum.jpg",  anlass: "taufe",      titel: "Taufkerzen in Blau mit Kreuz, Lebensbaum und Fisch", kurz: "Kreuz & Lebensbaum" },
    { datei: "/galerie/bilder/taufkerzen-rosa-maedchen.jpg",          anlass: "taufe",      titel: "Taufkerzen in Rosa mit Kreuz, Herz und Engel", kurz: "Rosa mit Herz & Engel" },

    // Kommunion & Konfirmation
    { datei: "/galerie/bilder/kommunionkerze-rosen-blau.jpg",         anlass: "kommunion",  titel: "Kommunionkerze mit blauen Rosen und Strasskreuz", kurz: "Blaue Rosen", auswahl: true },
    { datei: "/galerie/bilder/kommunionkerze-holy-communion.jpg",     anlass: "kommunion",  titel: "Kommunionkerze „Holy Communion“ in Rosa und Lila", kurz: "Holy Communion" },
    { datei: "/galerie/bilder/kommunionkerze-gruen-kelch-fische.jpg", anlass: "kommunion",  titel: "Kommunionkerze in Grün mit Kelch, Alpha & Omega und Fischen", kurz: "Kelch & Fische" },
    { datei: "/galerie/bilder/kommunionkerze-regenbogen-kreuz.jpg",   anlass: "kommunion",  titel: "Kommunionkerze mit Regenbogenkreuz und Fischband", kurz: "Regenbogenkreuz" },

    // Hochzeit
    { datei: "/galerie/bilder/hochzeitskerze-blaetterkranz.jpg",      anlass: "hochzeit",   titel: "Hochzeitskerze mit Namen, Datum und Blätterkranz in Blaugrün und Gold", kurz: "Blätterkranz & Gold", auswahl: true },

    // Geburtstag & Jubiläum
    { datei: "/galerie/bilder/geburtstagskerzen-jubilaeum.jpg",       anlass: "geburtstag", titel: "Geburtstagskerzen zum 60., 77., 80. und 84.", kurz: "Runde Geburtstage", auswahl: true },
    { datei: "/galerie/bilder/jubilaeumskerze-fotodruck.jpg",         anlass: "geburtstag", titel: "Jubiläumskerze „Zum Jubiläum“ mit gedrucktem Bild", kurz: "Jubiläum mit Bild" },

    // Schulanfang
    { datei: "/galerie/bilder/schulanfangskerze-abc-schultueten.jpg", anlass: "schule",     titel: "Kerze zum Schulanfang mit ABC, Schultüten, Name und Datum", kurz: "ABC & Schultüten", auswahl: true },

    // Trauer & Gedenken
    { datei: "/galerie/bilder/trauerkerze-fuer-immer-in-unserem-herzen.jpg", anlass: "trauer", titel: "Trauerkerze mit goldenem Kreuz: „Für immer in unserem Herzen“", kurz: "Für immer im Herzen", auswahl: true },
    { datei: "/galerie/bilder/trauerkerze-stiller-abschied.jpg",      anlass: "trauer",     titel: "Trauerkerze mit silbernem Kreuz: „Stiller Abschied“", kurz: "Stiller Abschied" },

    // Deko- & Formkerzen
    { datei: "/galerie/bilder/kerze-herz-haende.jpg",                 anlass: "deko",       titel: "Kerze „Herz in Händen“ – handmade with love", kurz: "Herz in Händen" },
    { datei: "/galerie/bilder/windlicht-gepresste-blueten.jpg",       anlass: "deko",       titel: "Windlicht aus Wachs mit gepressten Blüten", kurz: "Windlicht mit Blüten" },
    { datei: "/galerie/bilder/formkerze-spirale.jpg",                 anlass: "deko",       titel: "Spiralkerze in Creme", kurz: "Spiralkerze" },
    { datei: "/galerie/bilder/formkerzen-creme-geflochten.jpg",          anlass: "deko",       titel: "Formkerzen in Creme und Natur – geflochten und gedreht", kurz: "Geflochtene Formkerzen" },
    { datei: "/galerie/bilder/formkerzen-pink.jpg",                   anlass: "deko",       titel: "Formkerzen in Pink", kurz: "Formkerzen in Pink" },
    { datei: "/galerie/bilder/kugelkerzen-blau-weiss.jpg",         anlass: "deko",       titel: "Kugelkerzen in Blau-Weiß", kurz: "Kugeln in Blau-Weiß" },
    { datei: "/galerie/bilder/schichtkerzen-tuerkis-gruen.jpg",       anlass: "deko",       titel: "Schichtkerzen in Türkis und Grün", kurz: "Schichtkerzen" },
    { datei: "/galerie/bilder/perlenkerzen-rot-weiss.jpg",            anlass: "deko",       titel: "Perlenkerzen in Rot, Weiß und Anthrazit", kurz: "Perlenkerzen" },
    { datei: "/galerie/bilder/sechseckkerze-blau-weiss.jpg",          anlass: "deko",       titel: "Sechseckkerze in Blau-Weiß", kurz: "Sechseckkerze" },
    { datei: "/galerie/bilder/formkerzen-weiss-kugel-blau.jpg",       anlass: "deko",       titel: "Weiße Formkerzen mit blauer Kugelkerze", kurz: "Weiße Formkerzen" },

    // Duft & Keramik
    { datei: "/galerie/bilder/duftwachsmelts-duftlampe.jpg",          anlass: "duft",       titel: "Duftwachsmelts mit Duftlampe", kurz: "Duftwachsmelts" },
    { datei: "/galerie/bilder/duftwachswuerfel-duftlampen.jpg",       anlass: "duft",       titel: "Duftwachswürfel und Duftlampen", kurz: "Duftwachswürfel" },

    // Beispiel für ein neues Bild:
    // { datei: "/galerie/bilder/hochzeitskerze-ringe.jpg", anlass: "hochzeit", titel: "Hochzeitskerze mit Ringen und Initialen", kurz: "Ringe & Initialen" },
];
