# -*- coding: utf-8 -*-
"""Erzeugt die statischen Seiten der Kerzenküche-Website."""
import json, os, sys
from urllib.parse import quote
from html import escape

ROOT = sys.argv[1]
BASE = "https://www.xn--kerzenkche-geb.de"
WA = "491741941927"
TEL_DISPLAY = "0174 194 19 27"
TEL_LINK = "+491741941927"
MAIL = "monikagogoll@gmx.de"

ANLAESSE = [
    ("taufkerzen", "Taufkerzen"),
    ("kommunion-konfirmation", "Kommunion & Konfirmation"),
    ("hochzeitskerzen", "Hochzeitskerzen"),
    ("trauerkerzen", "Trauer & Gedenken"),
    ("geburtstagskerzen", "Geburtstag & Jubiläum"),
]

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>'
WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-.9 1.2-.3.2-.6.1a8 8 0 01-2.4-1.5 9 9 0 01-1.6-2c-.2-.3 0-.5.1-.6l.4-.5.3-.5v-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.1 1.1 0 00-.8.4 3.4 3.4 0 00-1 2.5 5.9 5.9 0 001.2 3.1 13.5 13.5 0 005.2 4.6c1.9.8 2.7.9 3.6.7a3.1 3.1 0 002.1-1.4 2.5 2.5 0 00.2-1.5c-.1-.1-.3-.2-.6-.3zM12 21.8a9.8 9.8 0 01-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1112 21.8zm0-21.6A11.8 11.8 0 001.9 18l-1.7 6 6.2-1.6A11.8 11.8 0 1012 .2z"/></svg>'


def wa(text):
    return f"https://wa.me/{WA}?text={quote(text)}"


def head(title, desc, path, schema=None, noindex=False):
    url = BASE + path
    schemas = ""
    for s in (schema or []):
        schemas += '\n    <script type="application/ld+json">\n' + json.dumps(s, ensure_ascii=False, indent=2) + "\n    </script>"
    robots = '\n    <meta name="robots" content="noindex">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(title)}</title>
    <meta name="description" content="{escape(desc)}">{robots}
    <link rel="canonical" href="{url}">

    <meta property="og:type" content="website">
    <meta property="og:locale" content="de_DE">
    <meta property="og:site_name" content="Kerzenküche Balingen">
    <meta property="og:title" content="{escape(title)}">
    <meta property="og:description" content="{escape(desc)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}/og-image.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <link rel="preload" href="/fonts/playfair-display-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="/css/style.css?v=17">
    <script>document.documentElement.classList.add('js');</script>{schemas}
</head>
<body>
    <a class="skip-link" href="#inhalt">Zum Inhalt springen</a>
"""


def header(active=""):
    def cur(key):
        return ' aria-current="page"' if key == active else ""
    drop = "\n".join(
        f'                            <li><a href="/{slug}/"{cur(slug)}>{escape(name)}</a></li>' for slug, name in ANLAESSE)
    mob = "\n".join(
        f'                    <li class="sub"><a href="/{slug}/">{escape(name)}</a></li>' for slug, name in ANLAESSE)
    return f"""
    <header class="site-header">
        <div class="container">
            <nav class="nav" aria-label="Hauptnavigation">
                <a href="/" class="logo">Kerzenküche</a>

                <ul class="nav-links">
                    <li class="has-dropdown">
                        <a href="/#anlaesse"{' aria-current="page"' if active in [s for s, _ in ANLAESSE] else ''}>Anlässe</a>
                        <ul class="dropdown">
{drop}
                        </ul>
                    </li>
                    <li><a href="/galerie/"{cur("galerie")}>Galerie</a></li>
                    <li><a href="/#manufaktur">Manufaktur</a></li>
                    <li><a href="/#material">Material</a></li>
                    <li><a href="/#sammelstellen">Sammelstellen</a></li>
                </ul>

                <a href="#kontakt" class="nav-cta">Kontakt</a>

                <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Menü öffnen">
                    <svg class="icon-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
                    <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
                </button>
            </nav>

            <div class="mobile-menu" id="mobile-menu">
                <ul>
                    <li><a href="/#anlaesse">Anlässe</a></li>
{mob}
                    <li><a href="/galerie/">Galerie</a></li>
                    <li><a href="/#manufaktur">Manufaktur</a></li>
                    <li><a href="/#material">Material</a></li>
                    <li><a href="/#sammelstellen">Sammelstellen</a></li>
                </ul>
                <a href="#kontakt" class="btn btn--primary">Kontakt &amp; Anfrage</a>
            </div>
        </div>
    </header>

    <main id="inhalt">
"""


ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5.5A2.5 2.5 0 015.5 3h1.6a1 1 0 01.95.68l1.2 3.6a1 1 0 01-.27 1.05l-1.5 1.4a12 12 0 006.8 6.8l1.4-1.5a1 1 0 011.05-.27l3.6 1.2a1 1 0 01.68.95v1.6A2.5 2.5 0 0118.5 21h-1C9.5 21 3 14.5 3 6.5v-1z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path stroke-linecap="round" stroke-linejoin="round" d="M3.5 6.5l8.5 6 8.5-6"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 21s-7-6.1-7-11.5a7 7 0 0114 0C19 14.9 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
MAPS = "https://www.google.com/maps/search/?api=1&query=" + quote("Hebsackstraße 3, 72336 Balingen-Dürrwangen")


def contact(wa_text, title="Wunschkerze anfragen?", text="Wir beraten euch persönlich – damit eure Kerze genau so wird, wie ihr sie euch vorstellt."):
    return f"""
        <section id="kontakt" class="section bg-dark contact">
            <div class="container contact-grid">
                <div class="contact-intro reveal">
                    <span class="eyebrow">Kontakt</span>
                    <h2>{title}</h2>
                    <p class="lead">{text}</p>
                    <a href="{wa(wa_text)}" class="btn btn--light" target="_blank" rel="noopener">{WA_ICON}<span>Per WhatsApp anfragen</span></a>
                    <p class="contact-tip">Am schnellsten geht's per WhatsApp – wir freuen uns auf eure Nachricht.</p>
                </div>
                <ul class="contact-cards reveal">
                    <li>
                        <div class="contact-box">
                            <span class="contact-icon">{WA_ICON}</span>
                            <span class="contact-label">WhatsApp &amp; Telefon</span>
                            <span class="contact-actions">
                                <a href="{wa(wa_text)}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a>
                                <a href="tel:{TEL_LINK}">{ICON_PHONE}Anrufen</a>
                            </span>
                            <span class="contact-value">{TEL_DISPLAY}</span>
                        </div>
                    </li>
                    <li>
                        <a href="mailto:{MAIL}">
                            <span class="contact-icon">{ICON_MAIL}</span>
                            <span class="contact-label">E-Mail</span>
                            <span class="contact-value">{MAIL}</span>
                            <span class="contact-hint">E-Mail schreiben</span>
                        </a>
                    </li>
                    <li class="contact-card--wide">
                        <a href="{MAPS}" target="_blank" rel="noopener">
                            <span class="contact-icon">{ICON_PIN}</span>
                            <span class="contact-label">Laden &amp; Werkstatt</span>
                            <span class="contact-value">Kerzenküche</span>
                            <span class="contact-address">Armin und Monika Gogoll<br>Hebsackstr. 3<br>72336 Balingen-Dürrwangen</span>
                            <span class="contact-hint">Besuch &amp; Abholung nach Absprache · Route planen</span>
                        </a>
                    </li>
                </ul>
            </div>
        </section>
"""


def footer(gallery=False):
    links = "\n".join(f'                        <li><a href="/{s}/">{escape(n)}</a></li>' for s, n in ANLAESSE)
    gal = '\n    <script src="/galerie/bilder.js?v=3"></script>' if gallery else ""
    return f"""    </main>

    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="/" class="logo">Kerzenküche</a>
                    <p class="footer-sign">Armin &amp; Monika Gogoll</p>
                    <address>
                        Hebsackstr. 3<br>
                        72336 Balingen-Dürrwangen<br>
                        <span class="footer-note">Laden: Besuch nach Absprache</span>
                    </address>
                    <ul class="footer-contact">
                        <li><a href="{wa('Hallo Monika und Armin, ich interessiere mich für eine Wunschkerze.')}" target="_blank" rel="noopener">{WA_ICON}<span>WhatsApp schreiben</span></a></li>
                        <li><a href="mailto:{MAIL}">{ICON_MAIL}<span>{MAIL}</span></a></li>
                        <li><a href="tel:{TEL_LINK}">{ICON_PHONE}<span>{TEL_DISPLAY}</span></a></li>
                        <li><a href="{MAPS}" target="_blank" rel="noopener">{ICON_PIN}<span>Route planen</span></a></li>
                    </ul>
                </div>
                <nav aria-label="Anlässe">
                    <h4>Anlässe</h4>
                    <ul>
{links}
                    </ul>
                </nav>
                <nav aria-label="Entdecken">
                    <h4>Entdecken</h4>
                    <ul>
                        <li><a href="/galerie/">Galerie</a></li>
                        <li><a href="/#manufaktur">Manufaktur</a></li>
                        <li><a href="/#material">Material</a></li>
                        <li><a href="/#sammelstellen">Sammelstellen</a></li>
                    </ul>
                </nav>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2026 Kerzenküche Balingen</span>
                <ul>
                    <li><a href="/impressum/">Impressum</a></li>
                    <li><a href="/datenschutz/">Datenschutz</a></li>
                    <li><a href="/widerruf/">Bestellung &amp; Widerruf</a></li>
                </ul>
            </div>
        </div>
    </footer>
{gal}
    <script src="/js/main.js?v=10"></script>
</body>
</html>
"""


def steps_html(items):
    lis = "\n".join(f"""                    <li>
                        <h3>{t}</h3>
                        <p>{p}</p>
                    </li>""" for t, p in items)
    return f"""                <ol class="steps">
{lis}
                </ol>"""


def faq_html(items):
    out = []
    for q, a in items:
        out.append(f"""                <details>
                    <summary>{q}</summary>
                    <div><p>{a}</p></div>
                </details>""")
    return "\n".join(out)


def faq_schema(items):
    import re
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{
            "@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}
        } for q, a in items]
    }


BUSINESS = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": BASE + "/#kerzenkueche",
    "name": "Kerzenküche",
    "description": "Handgegossene und personalisierte Kerzen aus Balingen: Taufkerzen, Kommunion- und Konfirmationskerzen, Hochzeitskerzen, Trauerkerzen und Wunschkerzen.",
    "url": BASE + "/",
    "image": BASE + "/og-image.jpg",
    "telephone": TEL_LINK,
    "email": MAIL,
    "founder": [{"@type": "Person", "name": "Monika Gogoll"}, {"@type": "Person", "name": "Armin Gogoll"}],
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Hebsackstraße 3",
        "postalCode": "72336",
        "addressLocality": "Balingen-Dürrwangen",
        "addressRegion": "Baden-Württemberg",
        "addressCountry": "DE"
    },
    "areaServed": ["Balingen", "Albstadt", "Hechingen", "Geislingen", "Rosenfeld", "Meßstetten", "Haigerloch", "Rottweil", "Zollernalbkreis"],
    "knowsAbout": ["Taufkerzen", "Kommunionkerzen", "Konfirmationskerzen", "Hochzeitskerzen", "Trauerkerzen", "Bienenwachskerzen"]
}

STEPS = [
    ("Anfrage", "Schreibt uns per WhatsApp oder E-Mail: Anlass, Termin, Namen und eure Ideen. Gerne mit Fotos von Einladung, Deko oder Lieblingsmotiv."),
    ("Entwurf", "Wir besprechen mit euch Form, Farben, Schrift und Motiv – und nennen euch den Preis. Unverbindlich."),
    ("Handarbeit", "Wir gießen und verzieren eure Kerze in Ruhe von Hand – jede ein Unikat."),
    ("Abholung", "Ihr holt eure Kerze in unserem kleinen Laden in Balingen-Dürrwangen ab – Termin nach Absprache. Versand auf Anfrage."),
]


import subprocess, re as _re
_js = os.path.join(ROOT, "galerie", "bilder.js").replace("\\", "/")
GALERIE = json.loads(subprocess.run(["node", "-e", "global.window={};require('" + _js + "');process.stdout.write(JSON.stringify(window.GALERIE))"],
                                    capture_output=True, text=True, encoding="utf-8", check=True).stdout)
KURZ = {"taufe": "Taufe", "kommunion": "Kommunion", "hochzeit": "Hochzeit", "trauer": "Gedenken",
        "geburtstag": "Geburtstag", "deko": "Deko & Form", "duft": "Duft", "weitere": "Kerze"}


def thumb(datei):
    return datei.replace("/galerie/bilder/", "/galerie/bilder/thumbs/", 1) if datei.startswith("/galerie/bilder/") else datei


def static_gallery(key, limit):
    items = [b for b in GALERIE if key in ("alle", "") or b["anlass"] == key]
    if limit:
        items = items[:limit]
    out = []
    for b in items:
        t = escape(b.get("titel", ""))
        k = escape(b.get("kurz") or b.get("titel", ""))
        out.append('<figure style="margin:0"><button type="button" class="gallery-item" aria-label="Bild vergrößern: ' + t + '">'
                   '<img src="' + thumb(b["datei"]) + '" alt="' + t + '" loading="lazy" decoding="async"></button>'
                   '<figcaption class="gallery-caption"><span class="gallery-cat">' + KURZ.get(b["anlass"], "") + '</span>'
                   '<span class="gallery-name">' + k + '</span></figcaption></figure>')
    return "".join(out)


def fill_galleries(html):
    def sub(m):
        attrs = m.group(1)
        key = _re.search(r'data-galerie="([^"]*)"', attrs).group(1)
        lim = _re.search(r'data-limit="(\d+)"', attrs)
        return "<div" + attrs + ">" + static_gallery(key, int(lim.group(1)) if lim else 0) + "</div>"
    return _re.sub(r'<div( class="gallery[^"]*" data-galerie="[^"]*"(?: data-limit="\d+")?)></div>', sub, html)


def write(rel, content):
    if rel.endswith(".html"):
        content = fill_galleries(content)
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("geschrieben:", rel)


# ==========================================================================
# Startseite
# ==========================================================================

FAQ_HOME = [
    ("Was kostet eine persönliche Kerze?",
     "Das hängt von Größe, Wachs und Aufwand der Gestaltung ab. Schreibt uns eure Wünsche – ihr bekommt ein unverbindliches Angebot, bevor wir loslegen."),
    ("Wie früh sollte ich bestellen?",
     "Am besten einige Wochen vor eurem Termin, damit genug Zeit für Absprache und Handarbeit bleibt. Es ist knapp? Fragt trotzdem – wir sagen euch ehrlich, ob es klappt."),
    ("Ich habe schon eine Idee. Kann ich euch Fotos schicken?",
     "Gerne! Schickt uns Fotos von Kerzen oder Motiven, die euch gefallen – wir sagen euch, was sich umsetzen lässt."),
]

index = head(
    "Taufkerzen & Wunschkerzen aus Balingen | Kerzenküche",
    "Persönlich gestaltete Taufkerzen, Kommunion-, Hochzeits- und Trauerkerzen – von Hand gegossen von Armin & Monika in Balingen. Für den ganzen Zollernalbkreis.",
    "/", [BUSINESS, faq_schema(FAQ_HOME)]
) + header() + f"""
        <section class="hero">
            <div class="container split">
                <div>
                    <span class="eyebrow">Kerzenmanufaktur in Balingen</span>
                    <h1 class="display">Kerzen für eure <br><em>besonderen Momente.</em></h1>
                    <p class="lead">Taufkerzen, Kommunionkerzen und Wunschkerzen – von Hand gegossen und ganz persönlich gestaltet von Armin &amp; Monika.</p>
                    <ul class="tags">
                        <li>Personalisiert</li>
                        <li>Handarbeit</li>
                        <li>Bienenwachs</li>
                        <li>Upcycling</li>
                    </ul>
                    <div class="btn-row">
                        <a href="#anlaesse" class="btn btn--primary">Anlässe entdecken</a>
                        <a href="/galerie/" class="btn btn--outline">Galerie ansehen</a>
                    </div>
                </div>
                <div>
                    <div class="media">
                        <img src="/galerie/bilder/kerzen-titelbild.jpg" width="1500" height="1200" alt="Persönlich gestaltete Kommunionkerzen und eine Herz-Kerze aus der Kerzenküche Balingen" fetchpriority="high">
                    </div>
                </div>
            </div>
        </section>

        <section id="anlaesse" class="section bg-sand" style="padding-top:0">
            <div class="container">
                <div class="section-head reveal">
                    <span class="eyebrow">Lebensbegleiter</span>
                    <h2 class="title">Kerzen für Meilensteine.</h2>
                    <p class="muted text-light">Jede Kerze gestalten wir einzeln – mit Namen, Datum und Verzierungen, ganz nach euren Wünschen.</p>
                </div>
                <div class="cards">
                    <a href="/taufkerzen/" class="card reveal">
                        <div class="media"><img src="/galerie/bilder/taufkerzen-blau-kreuz-lebensbaum.jpg" width="1600" height="1600" loading="lazy" alt="Drei persönlich gestaltete Taufkerzen in Blau mit Kreuz und Lebensbaum"></div>
                        <div class="card-body">
                            <h3>Taufkerzen</h3>
                            <p>Mit Name, Taufdatum und Symbolen wie Kreuz, Taube oder Lebensbaum – eine Kerze, die ein Leben lang begleitet.</p>
                            <span class="link-arrow">Mehr erfahren</span>
                        </div>
                    </a>
                    <a href="/kommunion-konfirmation/" class="card reveal">
                        <div class="media"><img src="/galerie/bilder/kommunionkerzen-collage.jpg" width="1500" height="1200" loading="lazy" alt="Drei individuell gestaltete Kommunionkerzen"></div>
                        <div class="card-body">
                            <h3>Kommunion &amp; Konfirmation</h3>
                            <p>Schlank und festlich – mit Namen, Datum und Symbolen wie Kelch, Kreuz und Fisch.</p>
                            <span class="link-arrow">Mehr erfahren</span>
                        </div>
                    </a>
                    <a href="/hochzeitskerzen/" class="card reveal">
                        <div class="media"><img src="/galerie/bilder/windlicht-gepresste-blueten.jpg" width="1600" height="1600" loading="lazy" alt="Windlicht aus Wachs mit gepressten Blüten"></div>
                        <div class="card-body">
                            <h3>Hochzeitskerzen</h3>
                            <p>Mit euren Namen und eurem Datum – für die Trauung und jeden Hochzeitstag danach.</p>
                            <span class="link-arrow">Mehr erfahren</span>
                        </div>
                    </a>
                    <a href="/trauerkerzen/" class="card reveal">
                        <div class="media"><img src="/galerie/bilder/kerze-herz-haende-quer.jpg" width="1500" height="1200" loading="lazy" alt="Kerze „Herz in Händen“ in warmem Apricot"></div>
                        <div class="card-body">
                            <h3>Trauer &amp; Gedenken</h3>
                            <p>Behutsam gestaltete Kerzen, die an einen geliebten Menschen erinnern.</p>
                            <span class="link-arrow">Mehr erfahren</span>
                        </div>
                    </a>
                    <a href="/geburtstagskerzen/" class="card reveal">
                        <div class="media"><img src="/galerie/bilder/geburtstagskerzen-jubilaeum.jpg" width="1600" height="1600" loading="lazy" alt="Persönliche Geburtstagskerzen zum 60., 77., 80. und 84. Geburtstag"></div>
                        <div class="card-body">
                            <h3>Geburtstag &amp; Jubiläum</h3>
                            <p>Zum runden Geburtstag oder Jubiläum – mit Name, Zahl und Lieblingsblumen.</p>
                            <span class="link-arrow">Mehr erfahren</span>
                        </div>
                    </a>
                    <a href="#kontakt" class="card card--text reveal">
                        <div class="card-body">
                            <span class="eyebrow">Eure Idee</span>
                            <h3>Und alles andere.</h3>
                            <p>Deko- und Formkerzen oder ein ganz eigener Anlass – erzählt uns eure Idee, wir sagen euch, was möglich ist.</p>
                            <span class="link-arrow">Idee schicken</span>
                        </div>
                    </a>
                </div>
            </div>
        </section>

        <section class="section section--tight bg-paper region">
            <div class="container reveal">
                <span class="eyebrow">Aus der Region, für die Region</span>
                <h2 class="title">Persönliche Kerzen aus Balingen.</h2>
                <p class="muted text-light">Individuell gestaltete Spezialkerzen findet man im Zollernalbkreis kaum. Bei uns entstehen sie in Handarbeit – für Familien aus Balingen und der ganzen Umgebung.</p>
                <ul class="places">
                    <li>Balingen</li><li>Albstadt</li><li>Hechingen</li><li>Geislingen</li><li>Rosenfeld</li>
                    <li>Meßstetten</li><li>Haigerloch</li><li>Dotternhausen</li><li>Rottweil</li><li>Zollernalbkreis</li>
                </ul>
            </div>
        </section>

        <section class="section bg-sand">
            <div class="container">
                <div class="section-head reveal">
                    <span class="eyebrow">Galerie</span>
                    <h2 class="title">Frisch aus der Kerzenküche.</h2>
                    <p class="muted text-light">Ein kleiner Einblick in Kerzen, die wir für unsere Kundinnen und Kunden gestaltet haben.</p>
                </div>
                <div class="gallery" data-galerie="alle" data-limit="6"></div>
                <p class="center" style="margin-top:2.5rem"><a href="/galerie/" class="btn btn--outline">Zur ganzen Galerie</a></p>
            </div>
        </section>

        <section class="section bg-paper">
            <div class="container">
                <div class="section-head reveal">
                    <span class="eyebrow">So einfach geht's</span>
                    <h2 class="title">So entsteht eure Kerze.</h2>
                </div>
                <div class="reveal">
{steps_html(STEPS)}
                </div>
            </div>
        </section>

        <section id="manufaktur" class="section bg-sand">
            <div class="container split split--reverse">
                <div class="reveal">
                    <span class="eyebrow">Die Macher</span>
                    <h2 class="title">Vier Hände, <br>eine Werkstatt.</h2>
                    <p class="lead">Wir sind Armin und Monika. In unserer Werkstatt in Balingen gießen wir jede Kerze von Hand.</p>
                    <p class="lead">Keine Fließbandware. Jede Kerze entsteht in Ruhe, mit der Zeit, die sie braucht. Das macht den Unterschied, wenn ihr sie anzündet.</p>
                    <p class="lead">Und weil man Kerzen am schönsten mit eigenen Augen sieht: Unser kleiner Laden in Balingen-Dürrwangen ist nach Absprache für euch geöffnet.</p>
                    <a href="#kontakt" class="link-arrow">Besuch vereinbaren</a>
                </div>
                <div class="reveal">
                    <div class="media">
                        <img src="/team.jpg" width="1500" height="1200" loading="lazy" alt="Armin und Monika von der Kerzenküche Balingen">
                    </div>
                </div>
            </div>
        </section>

        <section id="material" class="section bg-paper">
            <div class="container container--narrow reveal">
                <span class="eyebrow">Rohstoffe</span>
                <h2 class="title">Ehrliche Materialien.</h2>
                <p class="lead">Wir arbeiten mit dem, was die Natur hergibt – und dem, was andere wegwerfen.</p>

                <h3 style="font-size:1.6rem;margin-top:3rem">Bienen- &amp; Rapswachs</h3>
                <p class="muted text-light">100 % reines Bienenwachs duftet natürlich nach Honig. Rapswachs aus der Region ist die vegane Alternative – es brennt sauber, rußarm und ohne Eigengeruch.</p>

                <hr class="divider">
                <div class="media">
                    <img src="/bienenwachs.jpg" width="1080" height="1091" loading="lazy" alt="Handgegossene Formkerzen in Creme und Honiggelb">
                </div>

                <h3 style="font-size:1.6rem;margin-top:3rem">Upcycling &amp; Paraffin</h3>
                <p class="muted text-light">Wir sammeln Kerzenreste und gießen daraus neue Kerzen. Für klare, klassische Formen nutzen wir hochwertiges Paraffin.</p>
            </div>
        </section>

        <section id="design" class="section bg-sand">
            <div class="container split">
                <div class="reveal">
                    <span class="eyebrow">Atmosphäre</span>
                    <h2 class="title">Duft &amp; Design.</h2>
                    <div class="stack">
                        <div class="panel">
                            <h3>Duftwachsmelts</h3>
                            <p>Passend zur Jahreszeit in verschiedenen Duftnoten. Frische im Frühling, Wärme im Winter.</p>
                        </div>
                        <div class="panel">
                            <h3>Keraflott Deko</h3>
                            <p>Untersetzer, Teelichthalter und Figuren aus Keramikgießmasse. Schlicht, matt, modern.</p>
                        </div>
                    </div>
                </div>
                <div class="reveal">
                    <div class="media">
                        <img src="/galerie/bilder/duftwachsmelts-duftlampe.jpg" width="1512" height="1512" loading="lazy" alt="Duftwachsmelts mit Duftlampe aus Keramik">
                    </div>
                </div>
            </div>
        </section>

        <section class="section bg-paper">
            <div class="container">
                <div class="section-head reveal">
                    <span class="eyebrow">Gut zu wissen</span>
                    <h2 class="title">Häufige Fragen.</h2>
                </div>
                <div class="faq reveal">
{faq_html(FAQ_HOME)}
                </div>
            </div>
        </section>

        <section id="sammelstellen" class="section bg-paper" style="padding-top:0">
            <div class="container container--narrow center reveal">
                <span class="eyebrow">Gemeinsam handeln</span>
                <h2 class="title">Wachs ist wertvoll.</h2>
                <div class="collect">
                    <div>
                        <h3>Sammelstellen</h3>
                        <p class="muted text-light">Kerzenreste? Bringt sie vorbei. <br>Wir gießen daraus etwas Neues.</p>
                    </div>
                    <div>
                        <h4>📍 Bei uns im Laden</h4>
                        <p class="muted">In Balingen-Dürrwangen – einfach vorbeibringen, gern nach kurzer Absprache.</p>
                        <h4 style="opacity:.5">📍 Weitere Sammelstellen</h4>
                        <p class="muted" style="opacity:.7;margin:0">Bald verfügbar</p>
                    </div>
                </div>
            </div>
        </section>
""" + contact("Hallo Monika und Armin, ich interessiere mich für eine Wunschkerze.\n\nAnlass:\nTermin:\nMeine Idee:") + footer(gallery=True)

write("index.html", index)

# ==========================================================================
# Anlass-Seiten
# ==========================================================================

PAGES = [
    dict(
        slug="taufkerzen", key="taufe", name="Taufkerzen",
        title="Taufkerze individuell gestalten in Balingen | Kerzenküche",
        desc="Persönliche Taufkerzen mit Name, Taufdatum und Symbolen wie Kreuz, Taube oder Lebensbaum – handgefertigt in Balingen für den ganzen Zollernalbkreis.",
        eyebrow="Taufe",
        h1="Taufkerzen mit <em>Namen &amp; Datum.</em>",
        intro="Die Taufkerze begleitet ein ganzes Leben – zur Erstkommunion oder Konfirmation, zur Hochzeit und an jedem Tauftag. Deshalb gestalten wir jede Taufkerze einzeln, genau für euer Kind.",
        img=("/galerie/bilder/taufkerzen-blau-kreuz-lebensbaum.jpg", 1600, 1600, "Persönlich gestaltete Taufkerzen aus der Kerzenküche Balingen"),
        options=[
            ("Name &amp; Datum", "Der Name eures Kindes, auf Wunsch mit Geburts- und Taufdatum."),
            ("„Zur Taufe“", "Der klassische Schriftzug in Silber."),
            ("Symbole", "Kreuz, Taube, Fisch, Lebensbaum, Alpha &amp; Omega, Engel, Herz, Schmetterling oder Babyfüßchen."),
            ("Farben", "Zartes Rosa, kräftiges Blau oder Grün – mit Silber und kleinen Glitzersteinen."),
            ("Band &amp; Spitze", "Ein Zierband oder eine Spitzenborte rund um die Kerze."),
            ("Material", "Wir beraten euch, welches Wachs zu eurer Kerze passt."),
        ],
        note="Die Taufkerze wird bei der Taufe traditionell an der Osterkerze entzündet. Viele Familien zünden sie später an jedem Tauftag wieder an – eine schöne Erinnerung.",
        faq=[
            ("Wie früh sollten wir die Taufkerze bestellen?",
             "Am besten einige Wochen vor der Taufe, damit genug Zeit für Absprache und Handarbeit bleibt. Wenn es knapp wird: Fragt trotzdem – wir sagen euch ehrlich, ob es bis zu eurem Termin klappt."),
            ("Was kostet eine Taufkerze?",
             "Der Preis hängt von Größe, Wachs und Aufwand der Verzierung ab. Schreibt uns eure Wünsche, dann bekommt ihr ein unverbindliches Angebot."),
            ("Wir haben schon eine Idee. Können wir euch Fotos schicken?",
             "Gerne! Schickt uns Fotos von Kerzen oder Motiven, die euch gefallen – wir sagen euch, was sich umsetzen lässt."),
            ("Was brauchen wir für die Anfrage?",
             "Den Namen eures Kindes, das Taufdatum und eure Wünsche zu Farben und Symbolen. Alles Weitere besprechen wir gemeinsam."),
        ],
        wa="Hallo Monika und Armin, ich interessiere mich für eine Taufkerze.\n\nName des Kindes:\nTauftermin:\nWunschfarben/Symbole:",
        cta_title="Eure Taufkerze anfragen",
    ),
    dict(
        slug="kommunion-konfirmation", key="kommunion", name="Kommunion & Konfirmation",
        title="Kommunionkerzen & Konfirmationskerzen in Balingen | Kerzenküche",
        desc="Individuelle Kommunionkerzen und Konfirmationskerzen mit Name, Datum und Symbolen wie Kelch, Kreuz und Fisch – handgefertigt in Balingen.",
        eyebrow="Kommunion &amp; Konfirmation",
        h1="Kerzen zur Kommunion <em>&amp; Konfirmation.</em>",
        intro="Zur Erstkommunion oder Konfirmation gehört eine eigene Kerze. Wir gestalten sie für euer Kind – mit Namen, Datum und christlichen Symbolen.",
        img=("/galerie/bilder/kommunionkerzen-collage.jpg", 1500, 1200, "Individuell gestaltete Kommunionkerzen aus der Kerzenküche Balingen"),
        options=[
            ("Name &amp; Datum", "Der Name eures Kindes und das Datum des Festes."),
            ("Schriftzug", "Zum Beispiel „Zur Kommunion“ oder „Holy Communion“."),
            ("Symbole", "Kelch, Kreuz, Fische, Alpha &amp; Omega, Taube, Herzen oder Wellen."),
            ("Rosen &amp; Steine", "Kleine Rosen und glitzernde Steine als Verzierung."),
            ("Farben", "Von Blau und Grün bis Rosa und Lila – gern auch in Regenbogenfarben."),
            ("Schlanke Form", "Die klassisch hohe, schlanke Kommunionkerze – auf Wunsch mit Tropfschutz."),
        ],
        note="Eure Gemeinde gibt eine Kerzengröße oder ein Motiv vor? Sagt es uns bei der Anfrage – wir sagen euch, was möglich ist.",
        faq=[
            ("Wann sollten wir bestellen?",
             "Kommunion und Konfirmation sind meist im Frühjahr. Am besten fragt ihr frühzeitig an, damit genug Zeit für Absprache und Handarbeit bleibt."),
            ("Was kostet eine Kommunion- oder Konfirmationskerze?",
             "Das hängt von Größe, Wachs und Verzierung ab. Ihr bekommt von uns vorab ein unverbindliches Angebot."),
            ("Wir haben schon eine Idee. Können wir euch Fotos schicken?",
             "Gerne! Schickt uns Fotos von Kerzen oder Motiven, die euch gefallen – wir sagen euch, was sich umsetzen lässt."),
        ],
        wa="Hallo Monika und Armin, ich interessiere mich für eine Kerze zur Kommunion/Konfirmation.\n\nName:\nDatum des Festes:\nWunschfarben/Symbole:",
        cta_title="Kerze zur Kommunion oder Konfirmation anfragen",
    ),
    dict(
        slug="hochzeitskerzen", key="hochzeit", name="Hochzeitskerzen",
        title="Hochzeitskerze mit Namen in Balingen gestalten | Kerzenküche",
        desc="Persönliche Hochzeitskerzen mit euren Namen und eurem Hochzeitsdatum – von Hand gegossen und gestaltet in Balingen. Jetzt unverbindlich anfragen.",
        eyebrow="Hochzeit",
        h1="Hochzeitskerzen <em>mit euren Namen.</em>",
        intro="Eure Hochzeitskerze brennt bei der Trauung – und danach an jedem Hochzeitstag. Wir gestalten sie mit euren Namen und eurem Datum.",
        img=("/galerie/bilder/windlicht-gepresste-blueten.jpg", 1600, 1600, "Windlicht aus Wachs mit gepressten Blüten"),
        options=[
            ("Namen &amp; Datum", "Eure Vornamen und euer Hochzeitsdatum."),
            ("Verzierung", "Herzen, Blüten, Ranken oder ein Kreuz."),
            ("Farben", "Schlichtes Weiß mit Silber oder Gold – oder in euren Farben."),
            ("Für jede Trauung", "Für die kirchliche Trauung, das Standesamt oder die freie Trauung."),
        ],
        note="Ihr habt schon eine Vorstellung? Schickt uns gern Fotos von Ideen, die euch gefallen – wir sagen euch, was sich umsetzen lässt.",
        faq=[
            ("Wie früh sollten wir die Hochzeitskerze bestellen?",
             "Am besten einige Wochen vor der Hochzeit. Dann bleibt in Ruhe Zeit für die Absprache – und ihr habt einen Punkt weniger auf der Liste."),
            ("Was kostet eine Hochzeitskerze?",
             "Das hängt von Größe, Wachs und Gestaltung ab. Erzählt uns eure Wünsche, ihr bekommt ein unverbindliches Angebot."),
        ],
        wa="Hallo Monika und Armin, wir interessieren uns für eine Hochzeitskerze.\n\nNamen:\nHochzeitsdatum:\nWunschfarben:",
        cta_title="Eure Hochzeitskerze anfragen",
    ),
    dict(
        slug="trauerkerzen", key="trauer", name="Trauer & Gedenken",
        title="Trauerkerzen & Gedenkkerzen in Balingen | Kerzenküche",
        desc="Persönliche Trauerkerzen und Gedenkkerzen mit Name und Lebensdaten – behutsam von Hand gestaltet in Balingen für die Trauerfeier oder das Zuhause.",
        eyebrow="Trauer &amp; Gedenken",
        h1="Kerzen, die <em>erinnern.</em>",
        intro="Eine Kerze kann Trost spenden und an einen geliebten Menschen erinnern. Wir gestalten Trauer- und Gedenkkerzen behutsam und persönlich – für die Trauerfeier, das Grab oder einen Platz im Zuhause.",
        img=("/galerie/bilder/kerze-herz-haende-quer.jpg", 1500, 1200, "Kerze „Herz in Händen“ in warmem Apricot"),
        options=[
            ("Name &amp; Lebensdaten", "Name, Geburts- und Sterbedatum."),
            ("Symbole", "Kreuz, Engel, Lebensbaum, Rosen, Herz oder Schmetterling."),
            ("Farben", "Schlicht und ruhig – oder in den Lieblingsfarben des Verstorbenen."),
            ("Für die Trauerfeier", "Als Kerze für die Trauerfeier oder Beisetzung."),
            ("Zum Gedenken", "Für den Jahrestag, Allerheiligen oder einen Erinnerungsplatz zu Hause."),
        ],
        note="Wir wissen, dass es in dieser Zeit oft schnell gehen muss. Meldet euch einfach – wir sagen euch ehrlich, ob wir es bis zu eurem Termin schaffen.",
        faq=[
            ("Wie schnell ist eine Trauerkerze fertig?",
             "Das hängt von der Gestaltung ab. Ruft uns an oder schreibt uns – wir finden gemeinsam heraus, was bis zu eurem Termin möglich ist."),
            ("Was kostet eine Trauerkerze?",
             "Der Preis richtet sich nach Größe und Gestaltung. Ihr bekommt vorab ein unverbindliches Angebot."),
            ("Können wir die Kerze auch später zum Gedenken bestellen?",
             "Ja – zum Beispiel zum Jahrestag oder für einen Erinnerungsplatz zu Hause."),
        ],
        wa="Hallo Monika und Armin, ich interessiere mich für eine Trauerkerze/Gedenkkerze.\n\nName:\nLebensdaten:\nTermin:",
        cta_title="Trauer- oder Gedenkkerze anfragen",
    ),
]

PAGES.append(dict(
    slug="geburtstagskerzen", key="geburtstag", name="Geburtstag & Jubiläum",
    title="Geburtstagskerzen & Jubiläumskerzen mit Namen | Kerzenküche Balingen",
    desc="Persönliche Geburtstagskerzen mit Name, Zahl und Blumen – zum 60., 70., 80. oder 90. und zum Jubiläum. Handgefertigt in Balingen.",
    eyebrow="Geburtstag &amp; Jubiläum",
    h1="Kerzen für <em>runde Tage.</em>",
    intro="Zum runden Geburtstag oder Jubiläum: Eine persönlich gestaltete Kerze ist ein Geschenk, das in Erinnerung bleibt – mit Name, Zahl und den Lieblingsblumen des Geburtstagskindes.",
    img=("/galerie/bilder/geburtstagskerzen-jubilaeum.jpg", 1600, 1600, "Persönliche Geburtstagskerzen zum 60., 77., 80. und 84. Geburtstag"),
    options=[
        ("Name &amp; Zahl", "Der Name des Geburtstagskindes und die große Zahl – der Blickfang jeder Geburtstagskerze."),
        ("Datum", "Das Geburtsdatum oder das Datum des Festes."),
        ("Kurzer Gruß", "Zum Beispiel „Zum 80. Geburtstag“ oder „Herzlichen Glückwunsch“."),
        ("Blumen", "Rosen, Sonnenblumen oder kleine blaue Blüten."),
        ("Herz &amp; Ranken", "Ein Herz um die Zahl, Ranken oder Schmetterlinge."),
        ("Verschiedene Formen", "Klassisch rund, geschwungen oder als spitze Bogenkerze."),
    ],
    note="Ein schönes Geschenk von der ganzen Familie: Erzählt uns ein bisschen über das Geburtstagskind – zum Beispiel seine Lieblingsfarben und -blumen.",
    faq=[
        ("Wie früh sollte ich eine Geburtstagskerze bestellen?",
         "Am besten ein bis zwei Wochen vor dem Fest. Es ist knapp? Fragt trotzdem – wir sagen euch ehrlich, ob es klappt."),
        ("Was kostet eine Geburtstagskerze?",
         "Das hängt von Größe und Gestaltung ab. Schreibt uns eure Wünsche, ihr bekommt vorab ein unverbindliches Angebot."),
        ("Macht ihr auch Kerzen zum Jubiläum?",
         "Ja – ebenfalls mit Namen, Datum und der passenden Zahl."),
    ],
    wa="Hallo Monika und Armin, ich interessiere mich für eine Geburtstags-/Jubiläumskerze.\n\nName:\nWelcher Geburtstag/Anlass:\nDatum:\nLieblingsfarben/-blumen:",
    cta_title="Geburtstags- oder Jubiläumskerze anfragen",
))

for p in PAGES:
    opts = "\n".join(f"                    <li><strong>{t}</strong><span>{d}</span></li>" for t, d in p["options"])
    src, w, h, alt = p["img"]
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Start", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": p["name"], "item": f"{BASE}/{p['slug']}/"},
        ]
    }
    service = {
        "@context": "https://schema.org", "@type": "Service",
        "name": p["name"], "serviceType": p["name"],
        "provider": {"@id": BASE + "/#kerzenkueche"},
        "areaServed": BUSINESS["areaServed"],
        "description": p["desc"],
    }
    html = head(p["title"], p["desc"], f"/{p['slug']}/", [BUSINESS, service, crumbs, faq_schema(p["faq"])]) + header(p["slug"]) + f"""
        <section class="hero hero--page">
            <div class="container">
                <nav class="breadcrumb" aria-label="Brotkrümelnavigation"><a href="/">Start</a><span>/</span>{escape(p['name'])}</nav>
                <div class="split">
                    <div>
                        <span class="eyebrow">{p['eyebrow']}</span>
                        <h1 class="display">{p['h1']}</h1>
                        <p class="lead">{p['intro']}</p>
                        <div class="btn-row">
                            <a href="{wa(p['wa'])}" class="btn btn--primary" target="_blank" rel="noopener">{WA_ICON}<span>Jetzt anfragen</span></a>
                            <a href="#beispiele" class="btn btn--outline">Beispiele ansehen</a>
                        </div>
                    </div>
                    <div>
                        <div class="media">
                            <img src="{src}" width="{w}" height="{h}" alt="{alt}" fetchpriority="high">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="section bg-paper">
            <div class="container container--narrow">
                <div class="reveal">
                    <span class="eyebrow">Eure Gestaltung</span>
                    <h2 class="title">Was wir für euch gestalten.</h2>
                    <p class="muted text-light" style="margin-bottom:2.5rem">Jede Kerze ist ein Unikat. Ihr entscheidet, was darauf kommt – wir beraten euch gern.</p>
                </div>
                <ul class="checklist reveal">
{opts}
                </ul>
                <div class="note reveal"><p class="muted">{p['note']}</p></div>
            </div>
        </section>

        <section id="beispiele" class="section bg-sand">
            <div class="container">
                <div class="section-head reveal">
                    <span class="eyebrow">Beispiele</span>
                    <h2 class="title">Frisch aus der Kerzenküche.</h2>
                </div>
                <div class="gallery" data-galerie="{p['key']}" data-limit="6"></div>
                <p class="center" style="margin-top:2.5rem"><a href="/galerie/#{p['key']}" class="link-arrow">Alle Bilder in der Galerie</a></p>
            </div>
        </section>

        <section class="section bg-paper">
            <div class="container">
                <div class="section-head reveal">
                    <span class="eyebrow">So einfach geht's</span>
                    <h2 class="title">So entsteht eure Kerze.</h2>
                </div>
                <div class="reveal">
{steps_html(STEPS)}
                </div>
            </div>
        </section>

        <section class="section bg-sand">
            <div class="container">
                <div class="section-head reveal">
                    <span class="eyebrow">Gut zu wissen</span>
                    <h2 class="title">Häufige Fragen.</h2>
                </div>
                <div class="faq reveal">
{faq_html(p['faq'])}
                </div>
            </div>
        </section>
""" + contact(p["wa"], title=p["cta_title"]) + footer(gallery=True)
    write(f"{p['slug']}/index.html", html)

# ==========================================================================
# Galerie
# ==========================================================================

galerie = head(
    "Galerie: Taufkerzen, Hochzeitskerzen & mehr | Kerzenküche Balingen",
    "Bilder unserer personalisierten Kerzen: Taufkerzen, Kommunion- und Konfirmationskerzen, Hochzeitskerzen und Gedenkkerzen – handgefertigt in Balingen.",
    "/galerie/"
) + header("galerie") + f"""
        <section class="hero hero--page">
            <div class="container">
                <nav class="breadcrumb" aria-label="Brotkrümelnavigation"><a href="/">Start</a><span>/</span>Galerie</nav>
                <div class="section-head" style="margin-bottom:0">
                    <span class="eyebrow">Galerie</span>
                    <h1 class="display">Unsere <em>Kerzen.</em></h1>
                    <p class="lead" style="margin:0 auto">Jede Kerze ist ein Unikat – hier seht ihr eine Auswahl dessen, was in der Kerzenküche entstanden ist. Tippt auf ein Bild, um es groß anzusehen.</p>
                </div>
            </div>
        </section>

        <section class="section bg-paper" style="padding-top:3rem">
            <div class="container">
                <ul class="filter" aria-label="Nach Anlass filtern"></ul>
                <div class="gallery gallery--4" data-galerie="alle"></div>
                <noscript><p class="center muted">Bitte aktiviert JavaScript, um die Galerie zu sehen.</p></noscript>
            </div>
        </section>
""" + contact("Hallo Monika und Armin, ich habe eure Galerie gesehen und interessiere mich für eine Kerze.\n\nAnlass:\nTermin:\nMeine Idee:", title="Gefällt euch, was ihr seht?") + footer(gallery=True)
write("galerie/index.html", galerie)

# ==========================================================================
# Rechtliches
# ==========================================================================

def legal(slug, title, desc, body):
    return head(title, desc, f"/{slug}/") + header() + f"""
        <section class="section bg-paper">
            <div class="container">
                <div class="prose">
{body}
                </div>
            </div>
        </section>
""" + contact("Hallo Monika und Armin, ich habe eine Frage:\n", title="Fragen?", text="Schreibt uns einfach – wir helfen gern weiter.") + footer()


impressum = f"""
                    <h1>Impressum</h1>

                    <h2>Angaben gemäß § 5 DDG</h2>
                    <p>Monika Gogoll<br>
                    Kerzenküche<br>
                    Hebsackstr. 3<br>
                    72336 Balingen-Dürrwangen</p>

                    <h2>Kontakt</h2>
                    <p>Telefon / WhatsApp: <a href="tel:{TEL_LINK}">{TEL_DISPLAY}</a><br>
                    E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>

                    <h2>Umsatzsteuer</h2>
                    <p>Kleinunternehmerin gemäß § 19 UStG. Es wird keine Umsatzsteuer ausgewiesen.</p>

                    <h2>Verbraucherstreitbeilegung</h2>
                    <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

                    <h2>Bildnachweis</h2>
                    <p>Alle Fotos: Kerzenküche Balingen.</p>
"""
write("impressum/index.html", legal("impressum", "Impressum | Kerzenküche Balingen", "Impressum der Kerzenküche, Monika Gogoll, Hebsackstr. 3, 72336 Balingen-Dürrwangen.", impressum))

datenschutz = f"""
                    <h1>Datenschutzerklärung</h1>

                    <div class="box">
                        <p><strong>Kurz gesagt:</strong> Diese Website setzt keine Cookies, verwendet keine Analyse- oder Tracking-Werkzeuge und bindet keine Inhalte von Google, Facebook o.&nbsp;ä. ein. Schriften und alle anderen Dateien werden direkt von unserem Webspace geladen. Daten von euch erhalten wir nur, wenn ihr uns selbst kontaktiert.</p>
                    </div>

                    <h2>1. Verantwortliche</h2>
                    <p>Monika Gogoll, Kerzenküche<br>
                    Hebsackstr. 3, 72336 Balingen-Dürrwangen<br>
                    Telefon: {TEL_DISPLAY}<br>
                    E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>

                    <h2>2. Hosting und Server-Logfiles</h2>
                    <p>Diese Website wird über <strong>GitHub Pages</strong> bereitgestellt, einen Dienst der GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Website verarbeitet GitHub technisch notwendige Daten, insbesondere eure IP-Adresse, Datum und Uhrzeit des Zugriffs, die aufgerufene Seite sowie Informationen zu Browser und Betriebssystem. Diese Daten werden benötigt, um die Website auszuliefern und ihre Sicherheit zu gewährleisten.</p>
                    <p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO; unser berechtigtes Interesse liegt in der sicheren und zuverlässigen Bereitstellung der Website. Dabei kann eine Übermittlung in die USA stattfinden. GitHub ist als Tochterunternehmen der Microsoft Corporation unter dem EU-US Data Privacy Framework zertifiziert; damit besteht ein Angemessenheitsbeschluss der EU-Kommission (Art. 45 DSGVO). Weitere Informationen: <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">Datenschutzerklärung von GitHub</a>.</p>
                    <p>Unsere Domain ist bei der STRATO GmbH, Otto-Ostrowski-Straße 7, 10249 Berlin, registriert. STRATO stellt die Namensauflösung (DNS) bereit, damit eure Anfrage an die Website weitergeleitet wird.</p>

                    <h2>3. Keine Cookies, kein Tracking</h2>
                    <p>Wir setzen keine Cookies und verwenden keine Analyse-, Werbe- oder Tracking-Dienste. Schriftarten werden lokal von unserem Webspace geladen; es findet keine Verbindung zu Google Fonts oder anderen Drittanbietern statt.</p>

                    <h2>4. Kontakt per E-Mail oder Telefon</h2>
                    <p>Wenn ihr uns per E-Mail oder Telefon kontaktiert, verarbeiten wir eure Angaben (z.&nbsp;B. Name, Kontaktdaten, Nachricht), um eure Anfrage zu beantworten und ggf. eine Bestellung abzuwickeln. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (Anbahnung bzw. Durchführung eines Vertrags) bzw. Art. 6 Abs. 1 lit. f DSGVO bei allgemeinen Anfragen. Für unser E-Mail-Postfach nutzen wir den Dienst GMX (1&amp;1 Mail &amp; Media GmbH, Brauerstraße 48, 76135 Karlsruhe).</p>

                    <h2>5. Kontakt per WhatsApp</h2>
                    <p>Auf unserer Website verlinken wir auf WhatsApp. Erst wenn ihr auf einen WhatsApp-Button klickt, wird WhatsApp geöffnet bzw. die Seite wa.me aufgerufen; vorher werden keine Daten an WhatsApp übertragen. Anbieter ist die WhatsApp Ireland Limited, Merrion Road, Dublin 4, D04 X2K5, Irland. Wenn ihr uns über WhatsApp schreibt, verarbeitet WhatsApp eure Daten nach eigenen Bestimmungen; dabei kann eine Übermittlung in die USA stattfinden (die Muttergesellschaft Meta Platforms, Inc. ist unter dem EU-US Data Privacy Framework zertifiziert). Rechtsgrundlage für unsere Verarbeitung ist Art. 6 Abs. 1 lit. b bzw. lit. f DSGVO. Wer WhatsApp nicht nutzen möchte, erreicht uns jederzeit per E-Mail oder Telefon.</p>
                    <p>Datenschutzhinweise von WhatsApp: <a href="https://www.whatsapp.com/legal/privacy-policy-eea" target="_blank" rel="noopener">whatsapp.com/legal/privacy-policy-eea</a></p>

                    <h2>6. Bestellungen</h2>
                    <p>Für eine Bestellung benötigen wir eure Kontaktdaten sowie die Angaben zur Gestaltung der Kerze (z.&nbsp;B. Namen und Daten). Diese verwenden wir ausschließlich zur Herstellung und Übergabe der Kerze (Art. 6 Abs. 1 lit. b DSGVO). Rechnungsrelevante Unterlagen bewahren wir entsprechend den gesetzlichen Aufbewahrungsfristen (bis zu 10 Jahre nach HGB/AO) auf; alle übrigen Daten löschen wir, sobald sie nicht mehr benötigt werden.</p>

                    <h2>7. Fotos in der Galerie</h2>
                    <p>Fotos von Kerzen, auf denen persönliche Angaben wie Namen oder Daten zu sehen sind, veröffentlichen wir nur mit Einwilligung der jeweiligen Kundinnen und Kunden (Art. 6 Abs. 1 lit. a DSGVO) oder machen diese Angaben unkenntlich. Eine Einwilligung kann jederzeit mit Wirkung für die Zukunft widerrufen werden – eine kurze Nachricht genügt, dann entfernen wir das Bild.</p>

                    <h2>8. Speicherdauer</h2>
                    <p>Wir speichern personenbezogene Daten nur so lange, wie es für den jeweiligen Zweck erforderlich ist oder gesetzliche Aufbewahrungspflichten bestehen.</p>

                    <h2>9. Eure Rechte</h2>
                    <p>Ihr habt das Recht auf</p>
                    <ul>
                        <li>Auskunft über eure gespeicherten Daten (Art. 15 DSGVO),</li>
                        <li>Berichtigung unrichtiger Daten (Art. 16 DSGVO),</li>
                        <li>Löschung (Art. 17 DSGVO) und Einschränkung der Verarbeitung (Art. 18 DSGVO),</li>
                        <li>Datenübertragbarkeit (Art. 20 DSGVO),</li>
                        <li>Widerspruch gegen die Verarbeitung auf Grundlage berechtigter Interessen (Art. 21 DSGVO),</li>
                        <li>Widerruf einer erteilten Einwilligung mit Wirkung für die Zukunft (Art. 7 Abs. 3 DSGVO).</li>
                    </ul>
                    <p>Wendet euch dazu einfach an die oben genannten Kontaktdaten.</p>
                    <p>Außerdem habt ihr das Recht, euch bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Für uns zuständig ist: Der Landesbeauftragte für den Datenschutz und die Informationsfreiheit Baden-Württemberg, Lautenschlagerstraße 20, 70173 Stuttgart, <a href="https://www.baden-wuerttemberg.datenschutz.de" target="_blank" rel="noopener">www.baden-wuerttemberg.datenschutz.de</a>.</p>

                    <p class="small muted" style="margin-top:3rem">Stand: Oktober 2026</p>
"""
write("datenschutz/index.html", legal("datenschutz", "Datenschutz | Kerzenküche Balingen", "Datenschutzerklärung der Kerzenküche Balingen: keine Cookies, kein Tracking.", datenschutz))

widerruf = f"""
                    <h1>Bestellung &amp; Widerruf</h1>

                    <h2>So kauft ihr bei uns</h2>
                    <p>Wir betreiben keinen Online-Shop. Kerzen könnt ihr direkt in unserem kleinen Laden in Balingen-Dürrwangen kaufen (Besuch nach Absprache) oder per WhatsApp, Telefon bzw. E-Mail anfragen und bestellen. Unsere Preise sind Endpreise; als Kleinunternehmerin gemäß § 19 UStG weisen wir keine Umsatzsteuer aus.</p>

                    <h2>Wann gibt es ein Widerrufsrecht?</h2>
                    <ul>
                        <li><strong>Kauf vor Ort in unserem Laden:</strong> Hier besteht kein gesetzliches Widerrufsrecht.</li>
                        <li><strong>Personalisierte Kerzen</strong> (z.&nbsp;B. mit Namen und Datum): Diese fertigen wir eigens nach euren Vorgaben an. Ein Widerrufsrecht besteht daher nicht – auch nicht bei Bestellung per WhatsApp, Telefon oder E-Mail (§ 312g Abs. 2 Nr. 1 BGB).</li>
                        <li><strong>Nicht personalisierte Ware, die ihr ausschließlich per WhatsApp, Telefon oder E-Mail bestellt</strong> und euch zuschicken lasst: Hierfür gilt das folgende Widerrufsrecht.</li>
                    </ul>

                    <h2>Widerrufsbelehrung</h2>
                    <h3>Widerrufsrecht</h3>
                    <p>Sie haben das Recht, binnen vierzehn Tagen ohne Angabe von Gründen diesen Vertrag zu widerrufen.</p>
                    <p>Die Widerrufsfrist beträgt vierzehn Tage ab dem Tag, an dem Sie oder ein von Ihnen benannter Dritter, der nicht der Beförderer ist, die Waren in Besitz genommen haben bzw. hat.</p>
                    <p>Um Ihr Widerrufsrecht auszuüben, müssen Sie uns (Monika Gogoll, Kerzenküche, Hebsackstr. 3, 72336 Balingen-Dürrwangen, Telefon: {TEL_DISPLAY}, E-Mail: <a href="mailto:{MAIL}">{MAIL}</a>) mittels einer eindeutigen Erklärung (z.&nbsp;B. ein mit der Post versandter Brief oder eine E-Mail) über Ihren Entschluss, diesen Vertrag zu widerrufen, informieren. Sie können dafür das beigefügte Muster-Widerrufsformular verwenden, das jedoch nicht vorgeschrieben ist.</p>
                    <p>Zur Wahrung der Widerrufsfrist reicht es aus, dass Sie die Mitteilung über die Ausübung des Widerrufsrechts vor Ablauf der Widerrufsfrist absenden.</p>

                    <h3>Folgen des Widerrufs</h3>
                    <p>Wenn Sie diesen Vertrag widerrufen, haben wir Ihnen alle Zahlungen, die wir von Ihnen erhalten haben, einschließlich der Lieferkosten (mit Ausnahme der zusätzlichen Kosten, die sich daraus ergeben, dass Sie eine andere Art der Lieferung als die von uns angebotene, günstigste Standardlieferung gewählt haben), unverzüglich und spätestens binnen vierzehn Tagen ab dem Tag zurückzuzahlen, an dem die Mitteilung über Ihren Widerruf dieses Vertrags bei uns eingegangen ist. Für diese Rückzahlung verwenden wir dasselbe Zahlungsmittel, das Sie bei der ursprünglichen Transaktion eingesetzt haben, es sei denn, mit Ihnen wurde ausdrücklich etwas anderes vereinbart; in keinem Fall werden Ihnen wegen dieser Rückzahlung Entgelte berechnet.</p>
                    <p>Wir können die Rückzahlung verweigern, bis wir die Waren wieder zurückerhalten haben oder bis Sie den Nachweis erbracht haben, dass Sie die Waren zurückgesandt haben, je nachdem, welches der frühere Zeitpunkt ist.</p>
                    <p>Sie haben die Waren unverzüglich und in jedem Fall spätestens binnen vierzehn Tagen ab dem Tag, an dem Sie uns über den Widerruf dieses Vertrags unterrichten, an uns zurückzusenden oder zu übergeben. Die Frist ist gewahrt, wenn Sie die Waren vor Ablauf der Frist von vierzehn Tagen absenden.</p>
                    <p>Sie tragen die unmittelbaren Kosten der Rücksendung der Waren.</p>
                    <p>Sie müssen für einen etwaigen Wertverlust der Waren nur aufkommen, wenn dieser Wertverlust auf einen zur Prüfung der Beschaffenheit, Eigenschaften und Funktionsweise der Waren nicht notwendigen Umgang mit ihnen zurückzuführen ist.</p>

                    <h3>Ausschluss des Widerrufsrechts</h3>
                    <p>Das Widerrufsrecht besteht nicht bei Verträgen zur Lieferung von Waren, die nicht vorgefertigt sind und für deren Herstellung eine individuelle Auswahl oder Bestimmung durch den Verbraucher maßgeblich ist oder die eindeutig auf die persönlichen Bedürfnisse des Verbrauchers zugeschnitten sind.</p>

                    <h2>Muster-Widerrufsformular</h2>
                    <div class="box">
                        <p>(Wenn Sie den Vertrag widerrufen wollen, dann füllen Sie bitte dieses Formular aus und senden Sie es zurück.)</p>
                        <p>An: Monika Gogoll, Kerzenküche, Hebsackstr. 3, 72336 Balingen-Dürrwangen, E-Mail: {MAIL}</p>
                        <p>Hiermit widerrufe(n) ich/wir (*) den von mir/uns (*) abgeschlossenen Vertrag über den Kauf der folgenden Waren (*) / die Erbringung der folgenden Dienstleistung (*)</p>
                        <p>_______________________________________________</p>
                        <p>Bestellt am (*) / erhalten am (*): ____________________</p>
                        <p>Name des/der Verbraucher(s): ____________________</p>
                        <p>Anschrift des/der Verbraucher(s): ____________________</p>
                        <p>Unterschrift des/der Verbraucher(s) (nur bei Mitteilung auf Papier): ____________________</p>
                        <p>Datum: ____________________</p>
                        <p class="small">(*) Unzutreffendes streichen.</p>
                    </div>
"""
write("widerruf/index.html", legal("widerruf", "Bestellung & Widerruf | Kerzenküche Balingen", "Hinweise zur Bestellung und Widerrufsbelehrung der Kerzenküche Balingen.", widerruf))

# ==========================================================================
# 404
# ==========================================================================

nf = head("Seite nicht gefunden | Kerzenküche", "Diese Seite gibt es leider nicht.", "/404.html", noindex=True) + header() + """
        <section class="hero hero--page" style="min-height:50vh">
            <div class="container center">
                <span class="eyebrow">Fehler 404</span>
                <h1 class="display">Hier brennt <em>leider nichts.</em></h1>
                <p class="lead" style="margin:0 auto 2.5rem">Diese Seite gibt es nicht (mehr). Vielleicht findet ihr hier, was ihr sucht:</p>
                <div class="btn-row btn-row--center">
                    <a href="/" class="btn btn--primary">Zur Startseite</a>
                    <a href="/galerie/" class="btn btn--outline">Zur Galerie</a>
                </div>
            </div>
        </section>
""" + contact("Hallo Monika und Armin, ich interessiere mich für eine Wunschkerze.\n") + footer()
write("404.html", nf)


# ==========================================================================
# Ratgeber: Taufsprüche
# Abgeschaltet, bis belegt ist, welche Texte auf die Kerzen passen.
# Zum Aktivieren auf True setzen (Link im Footer/Taufe-Seite wieder ergänzen).
# ==========================================================================
RATGEBER_AKTIV = False

VERSE = [
    ("Licht – passend zur Kerze", [
        ("Dein Wort ist meines Fußes Leuchte und ein Licht auf meinem Wege.", "Psalm 119,105"),
        ("Ich bin das Licht der Welt.", "Johannes 8,12"),
        ("Ihr seid das Licht der Welt.", "Matthäus 5,14"),
        ("Der HERR ist mein Licht und mein Heil.", "Psalm 27,1"),
    ]),
    ("Schutz & Segen", [
        ("Denn er hat seinen Engeln befohlen, dass sie dich behüten auf allen deinen Wegen.", "Psalm 91,11"),
        ("Ich will dich segnen, und du sollst ein Segen sein.", "1. Mose 12,2"),
        ("Der HERR segne dich und behüte dich.", "4. Mose 6,24"),
        ("Der HERR behüte deinen Ausgang und Eingang von nun an bis in Ewigkeit.", "Psalm 121,8"),
        ("Fürchte dich nicht, denn ich habe dich erlöst; ich habe dich bei deinem Namen gerufen; du bist mein.", "Jesaja 43,1"),
        ("Siehe, ich bin bei euch alle Tage bis an der Welt Ende.", "Matthäus 28,20"),
    ]),
    ("Liebe & Vertrauen", [
        ("Nun aber bleiben Glaube, Hoffnung, Liebe, diese drei; aber die Liebe ist die größte unter ihnen.", "1. Korinther 13,13"),
        ("Der HERR ist mein Hirte, mir wird nichts mangeln.", "Psalm 23,1"),
        ("Ich danke dir dafür, dass ich wunderbar gemacht bin.", "Psalm 139,14"),
        ("Alle eure Dinge lasst in der Liebe geschehen.", "1. Korinther 16,14"),
        ("Sei getrost und unverzagt.", "Josua 1,9"),
    ]),
    ("Segenswünsche ohne Bibelvers", [
        ("Kleines Licht, leuchte hell auf deinem Weg.", ""),
        ("Möge dein Weg immer behütet sein – und dein Herz voller Licht.", ""),
        ("Willkommen auf der Welt. Schön, dass es dich gibt.", ""),
        ("Ein Licht für dich – heute und an jedem Tag deines Lebens.", ""),
        ("Wurzeln, die halten, und Flügel, die tragen.", ""),
    ]),
]

FAQ_TAUF = [
    ("Wie lang darf ein Taufspruch auf der Kerze sein?",
     "Am schönsten wirken ein bis drei kurze Zeilen. Bei längeren Versen setzen wir nur einen Teil oder die Bibelstelle allein auf die Kerze – das besprechen wir gemeinsam mit euch."),
    ("Muss der Taufspruch aus der Bibel sein?",
     "In vielen Gemeinden ist ein Bibelvers üblich, oft sucht ihn die Pfarrerin oder der Pfarrer gemeinsam mit euch aus. Fragt am besten in eurer Gemeinde nach. Auf die Kerze kann aber jeder Spruch, der euch gefällt."),
    ("Kommt die Bibelstelle mit auf die Kerze?",
     "Wenn ihr möchtet, ja – meist klein unter dem Spruch, zum Beispiel „Psalm 91,11“."),
]

cards = []
for gruppe, verse in VERSE:
    items = []
    for text, stelle in verse:
        wa_text = "Hallo Monika und Armin, ich interessiere mich für eine Taufkerze mit diesem Taufspruch:\n\n„" + text + "“" + (" (" + stelle + ")" if stelle else "") + "\n\nName des Kindes:\nTauftermin:"
        ref = f'<cite>{stelle}</cite>' if stelle else ''
        items.append(f"""                    <li class="verse">
                        <blockquote>„{text}“</blockquote>
                        {ref}
                        <a href="{wa(wa_text)}" class="verse-link" target="_blank" rel="noopener">Für meine Taufkerze</a>
                    </li>""")
    cards.append(f"""                <h2 class="verse-group">{gruppe}</h2>
                <ul class="verse-grid">
{chr(10).join(items)}
                </ul>""")

TIPPS = [
    ("Kurz ist schöner", "Ein bis drei kurze Zeilen passen gut auf eine Taufkerze und bleiben gut lesbar."),
    ("Mit der Gemeinde absprechen", "Wird bei der Taufe ein Taufspruch vorgelesen, nehmt am besten genau diesen auch für die Kerze."),
    ("Zum Motiv passend", "Licht-Verse passen wunderbar zur Kerze, Engel-Verse zu einem Engel- oder Tauben-Motiv."),
    ("Bibelstelle dazu", "Auf Wunsch setzen wir die Bibelstelle klein unter den Spruch."),
]
tipps = "\n".join(f"                    <li><strong>{t}</strong><span>{d}</span></li>" for t, d in TIPPS)

article = {
    "@context": "https://schema.org", "@type": "Article",
    "headline": "Taufsprüche für die Taufkerze",
    "author": {"@type": "Organization", "name": "Kerzenküche"},
    "publisher": {"@id": BASE + "/#kerzenkueche"},
    "mainEntityOfPage": BASE + "/ratgeber/taufsprueche/",
    "image": BASE + "/galerie/bilder/taufkerzen-blau-kreuz-lebensbaum.jpg",
    "dateModified": "2026-10-08",
}
crumbs_t = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Start", "item": BASE + "/"},
    {"@type": "ListItem", "position": 2, "name": "Taufsprüche", "item": BASE + "/ratgeber/taufsprueche/"},
]}

tauf_wa = "Hallo Monika und Armin, ich interessiere mich für eine Taufkerze.\n\nName des Kindes:\nTauftermin:\nTaufspruch:\nWunschfarben/Motiv:"
ratgeber = head(
    "Taufsprüche für die Taufkerze – schöne Bibelverse & Ideen | Kerzenküche",
    "Die schönsten Taufsprüche für die Taufkerze: Bibelverse über Licht, Schutz und Segen, moderne Segenswünsche und Tipps, wie der Spruch gut auf die Kerze passt.",
    "/ratgeber/taufsprueche/", [article, crumbs_t, faq_schema(FAQ_TAUF)]
) + header() + f"""
        <section class="hero hero--page">
            <div class="container">
                <nav class="breadcrumb" aria-label="Brotkrümelnavigation"><a href="/">Start</a><span>/</span><a href="/taufkerzen/">Taufkerzen</a><span>/</span>Taufsprüche</nav>
                <div class="split">
                    <div>
                        <span class="eyebrow">Ratgeber</span>
                        <h1 class="display">Taufsprüche für <em>die Taufkerze.</em></h1>
                        <p class="lead">Der Taufspruch begleitet euer Kind ein Leben lang – und auf der Taufkerze ist er an jedem Tauftag wieder zu sehen. Hier findet ihr bewährte Bibelverse, schöne Segenswünsche und Tipps, wie der Spruch gut auf die Kerze passt.</p>
                        <div class="btn-row">
                            <a href="#sprueche" class="btn btn--primary">Zu den Sprüchen</a>
                            <a href="/taufkerzen/" class="btn btn--outline">Unsere Taufkerzen</a>
                        </div>
                    </div>
                    <div>
                        <div class="media">
                            <img src="/galerie/bilder/taufkerzen-blau-kreuz-lebensbaum.jpg" width="1600" height="1600" alt="Persönlich gestaltete Taufkerzen mit Kreuz und Lebensbaum" fetchpriority="high">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="section bg-paper">
            <div class="container container--narrow">
                <div class="reveal">
                    <span class="eyebrow">Gut zu wissen</span>
                    <h2 class="title">So passt der Spruch auf die Kerze.</h2>
                </div>
                <ul class="checklist reveal">
{tipps}
                </ul>
            </div>
        </section>

        <section id="sprueche" class="section bg-sand">
            <div class="container">
                <div class="section-head reveal">
                    <span class="eyebrow">Ideen</span>
                    <h2 class="title">Die schönsten Taufsprüche.</h2>
                    <p class="muted text-light">Einen gefunden? Tippt auf „Für meine Taufkerze“ – dann ist der Spruch in eurer WhatsApp-Nachricht schon eingetragen.</p>
                </div>
{chr(10).join(cards)}
                <p class="small muted center" style="margin-top:2.5rem">Bibelverse nach der Lutherübersetzung, teils leicht gekürzt.</p>
            </div>
        </section>

        <section class="section bg-paper">
            <div class="container">
                <div class="section-head reveal">
                    <span class="eyebrow">Häufige Fragen</span>
                    <h2 class="title">Rund um den Taufspruch.</h2>
                </div>
                <div class="faq reveal">
{faq_html(FAQ_TAUF)}
                </div>
            </div>
        </section>
""" + contact(tauf_wa, title="Euren Taufspruch auf eure Kerze?", text="Schickt uns euren Spruch, den Namen und das Taufdatum – wir gestalten daraus eure Taufkerze.") + footer()
if RATGEBER_AKTIV:
    write("ratgeber/taufsprueche/index.html", ratgeber)

# ==========================================================================
# Sitemap
# ==========================================================================

urls = [("/", "1.0"), ("/taufkerzen/", "0.9"), ("/kommunion-konfirmation/", "0.9"), ("/hochzeitskerzen/", "0.9"),
        ("/trauerkerzen/", "0.9"), ("/geburtstagskerzen/", "0.9"), ("/galerie/", "0.8"),
        ("/impressum/", "0.2"), ("/datenschutz/", "0.2"), ("/widerruf/", "0.2")]
SEITEN_KEY = {"/taufkerzen/": "taufe", "/kommunion-konfirmation/": "kommunion", "/hochzeitskerzen/": "hochzeit",
              "/trauerkerzen/": "trauer", "/geburtstagskerzen/": "geburtstag", "/galerie/": "alle"}
if RATGEBER_AKTIV:
    urls.insert(7, ("/ratgeber/taufsprueche/", "0.7"))
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
for u, prio in urls:
    sm += f"  <url>\n    <loc>{BASE}{u}</loc>\n    <lastmod>2026-10-08</lastmod>\n    <priority>{prio}</priority>\n"
    key = SEITEN_KEY.get(u)
    if key:
        for b in GALERIE:
            if key == "alle" or b["anlass"] == key:
                sm += f"    <image:image><image:loc>{BASE}{quote(b['datei'])}</image:loc></image:image>\n"
    sm += "  </url>\n"
sm += "</urlset>\n"
write("sitemap.xml", sm)

write("robots.txt", f"# robots.txt für Kerzenküche\n# {BASE}\n\nUser-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
