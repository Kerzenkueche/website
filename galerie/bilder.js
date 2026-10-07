/*
  ==========================================================================
  GALERIE – hier tragt ihr eure Bilder ein
  ==========================================================================

  So kommt ein neues Bild in die Galerie:
  1. Bild auf ca. 1500 Pixel Breite verkleinern (spart Ladezeit am Handy).
  2. Bild in den Ordner  galerie/bilder/  hochladen,
     z. B. als  taufkerze-regenbogen.jpg  (Kleinbuchstaben, keine Leerzeichen/Umlaute).
  3. Unten eine neue Zeile nach dem gleichen Muster einfügen.

  anlass: taufe | kommunion | hochzeit | trauer | geburtstag | deko | duft | weitere
  Die Reihenfolge hier ist die Reihenfolge in der Galerie.

  WICHTIG – Datenschutz: Auf Taufkerzen o. ä. stehen Name und Datum.
  Nur Bilder zeigen, wenn die Kunden einverstanden sind – oder Nachnamen
  bzw. Daten vorher unkenntlich machen.
*/

window.GALERIE = [
    // Taufe
    { datei: "/galerie/bilder/taufkerze-lebensbaum-blau.jpg",         anlass: "taufe",      titel: "Taufkerze mit blauem Lebensbaum und Taube" },
    { datei: "/galerie/bilder/taufkerzen-blau-kreuz-lebensbaum.jpg",  anlass: "taufe",      titel: "Taufkerzen in Blau mit Kreuz, Lebensbaum und Fisch" },
    { datei: "/galerie/bilder/taufkerzen-rosa-maedchen.jpg",          anlass: "taufe",      titel: "Taufkerzen in Rosa mit Kreuz, Herz und Engel" },

    // Kommunion & Konfirmation
    { datei: "/galerie/bilder/kommunionkerze-rosen-blau.jpg",         anlass: "kommunion",  titel: "Kommunionkerze mit blauen Rosen und Strasskreuz" },
    { datei: "/galerie/bilder/kommunionkerze-gruen-kelch-fische.jpg", anlass: "kommunion",  titel: "Kommunionkerze in Grün mit Kelch, Alpha & Omega und Fischen" },
    { datei: "/galerie/bilder/kommunionkerze-regenbogen-kreuz.jpg",   anlass: "kommunion",  titel: "Kommunionkerze mit Regenbogenkreuz und Fischband" },
    { datei: "/galerie/bilder/kommunionkerze-holy-communion.jpg",     anlass: "kommunion",  titel: "Kommunionkerze „Holy Communion“ in Rosa und Lila" },

    // Geburtstag & Jubiläum
    { datei: "/galerie/bilder/geburtstagskerzen-jubilaeum.jpg",       anlass: "geburtstag", titel: "Geburtstagskerzen zum 60., 77., 80. und 84." },

    // Deko- & Formkerzen
    { datei: "/galerie/bilder/kerze-herz-haende.jpg",                 anlass: "deko",       titel: "Kerze „Herz in Händen“ – handmade with love" },
    { datei: "/galerie/bilder/windlicht-gepresste-blueten.jpg",       anlass: "deko",       titel: "Windlicht aus Wachs mit gepressten Blüten" },
    { datei: "/galerie/bilder/formkerzen-creme-gedreht.jpg",          anlass: "deko",       titel: "Formkerzen in Creme – gedreht, geflochten, gewellt" },
    { datei: "/galerie/bilder/formkerzen-pink.jpg",                   anlass: "deko",       titel: "Formkerzen in Pink" },
    { datei: "/galerie/bilder/kugelkerzen-blau-pyramide.jpg",         anlass: "deko",       titel: "Kugelkerzen und Pyramide in Blau-Weiß" },
    { datei: "/galerie/bilder/schichtkerzen-tuerkis-gruen.jpg",       anlass: "deko",       titel: "Schichtkerzen in Türkis und Grün" },
    { datei: "/galerie/bilder/perlenkerzen-rot-weiss.jpg",            anlass: "deko",       titel: "Perlenkerzen in Rot, Weiß und Anthrazit" },
    { datei: "/galerie/bilder/formkerze-spirale.jpg",                 anlass: "deko",       titel: "Spiralkerze in Creme" },
    { datei: "/galerie/bilder/formkerzen-kugel-pyramide-bunt.jpg",    anlass: "deko",       titel: "Kugel- und Pyramidenkerzen" },
    { datei: "/galerie/bilder/kerzen-petrol-kugel-sechseck.jpg",      anlass: "deko",       titel: "Kerzen in Petrol – Kugel und Sechseck" },
    { datei: "/galerie/bilder/sechseckkerze-blau-weiss.jpg",          anlass: "deko",       titel: "Sechseckkerze in Blau-Weiß" },
    { datei: "/galerie/bilder/kugelkerzen-dekoschale.jpg",            anlass: "deko",       titel: "Kugelkerzen in der Dekoschale" },
    { datei: "/galerie/bilder/muschelkerze-pink.jpg",                 anlass: "deko",       titel: "Muschelkerze in Pink" },
    { datei: "/galerie/bilder/formkerzen-weiss.jpg",                  anlass: "deko",       titel: "Formkerzen in Weiß" },
    { datei: "/galerie/bilder/formkerzen-weiss-kugel-blau.jpg",       anlass: "deko",       titel: "Weiße Formkerzen mit blauer Kugelkerze" },
    { datei: "/galerie/bilder/kerze-herz-haende-satin.jpg",           anlass: "deko",       titel: "Kerze „Herz in Händen“ auf Satin" },

    // Duft & Keramik
    { datei: "/galerie/bilder/duftwachsmelts-duftlampe.jpg",          anlass: "duft",       titel: "Duftwachsmelts mit Duftlampe" },
    { datei: "/galerie/bilder/duftwachswuerfel-duftlampen.jpg",       anlass: "duft",       titel: "Duftwachswürfel und Duftlampen" },

    // Beispiel für ein neues Bild:
    // { datei: "/galerie/bilder/hochzeitskerze-ringe.jpg", anlass: "hochzeit", titel: "Hochzeitskerze mit Ringen" },
];
