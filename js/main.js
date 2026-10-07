/* Kerzenküche – Skripte (ohne externe Bibliotheken) */
(function () {
    'use strict';

    // ---------- Scroll-Animation ----------
    var revealEls = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        revealEls.forEach(function (el) { observer.observe(el); });
    } else {
        revealEls.forEach(function (el) { el.classList.add('visible'); });
    }

    // ---------- Mobiles Menü ----------
    var header = document.querySelector('.site-header');
    var toggle = document.querySelector('.menu-toggle');
    if (header && toggle) {
        toggle.addEventListener('click', function () {
            var open = header.classList.toggle('menu-open');
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            toggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
        });
        header.querySelectorAll('.mobile-menu a').forEach(function (a) {
            a.addEventListener('click', function () {
                header.classList.remove('menu-open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // ---------- Schwebender WhatsApp-Button ----------
    // Übernimmt die vorausgefüllte Nachricht aus dem Kontaktbereich der jeweiligen Seite.
    var kontakt = document.getElementById('kontakt');
    var waLink = kontakt && kontakt.querySelector('a[href*="wa.me"]');
    if (waLink) {
        var fab = document.createElement('a');
        fab.className = 'wa-fab';
        fab.href = waLink.href;
        fab.target = '_blank';
        fab.rel = 'noopener';
        fab.setAttribute('aria-label', 'Per WhatsApp anfragen');
        fab.innerHTML = waLink.querySelector('svg').outerHTML + '<span>Anfragen</span>';
        document.body.appendChild(fab);

        var kontaktSichtbar = false;
        function updateFab() {
            var zeigen = window.scrollY > 400 && !kontaktSichtbar &&
                !(header && header.classList.contains('menu-open'));
            fab.classList.toggle('is-visible', zeigen);
        }
        if ('IntersectionObserver' in window) {
            new IntersectionObserver(function (entries) {
                kontaktSichtbar = entries[0].isIntersecting;
                updateFab();
            }).observe(kontakt);
        }
        window.addEventListener('scroll', updateFab, { passive: true });
        if (toggle) toggle.addEventListener('click', updateFab);
        updateFab();
    }

    // ---------- Galerie ----------
    var BILDER = window.GALERIE || [];
    var ANLAESSE = {
        taufe: 'Taufe',
        kommunion: 'Kommunion & Konfirmation',
        hochzeit: 'Hochzeit',
        trauer: 'Trauer & Gedenken',
        geburtstag: 'Geburtstag & Jubiläum',
        deko: 'Deko- & Formkerzen',
        duft: 'Duft & Keramik',
        weitere: 'Weitere'
    };
    var WHATSAPP = 'https://wa.me/491741941927?text=' +
        encodeURIComponent('Hallo Monika und Armin, habt ihr ein paar Beispielbilder für mich? Ich interessiere mich für eine Kerze zum Anlass: ');

    var lightbox = null, lbImg, lbCap, lbList = [], lbIndex = 0;

    function buildLightbox() {
        lightbox = document.createElement('dialog');
        lightbox.className = 'lightbox';
        lightbox.setAttribute('aria-label', 'Bildansicht');
        lightbox.innerHTML =
            '<figure><img alt=""><figcaption></figcaption></figure>' +
            '<button class="lb-btn lb-close" type="button" aria-label="Schließen"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg></button>' +
            '<button class="lb-btn lb-prev" type="button" aria-label="Vorheriges Bild"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 6l-6 6 6 6"/></svg></button>' +
            '<button class="lb-btn lb-next" type="button" aria-label="Nächstes Bild"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg></button>';
        document.body.appendChild(lightbox);
        lbImg = lightbox.querySelector('img');
        lbCap = lightbox.querySelector('figcaption');
        lightbox.querySelector('.lb-close').addEventListener('click', closeLightbox);
        lightbox.querySelector('.lb-prev').addEventListener('click', function () { step(-1); });
        lightbox.querySelector('.lb-next').addEventListener('click', function () { step(1); });
        lightbox.addEventListener('click', function (e) { if (e.target === lightbox || e.target.tagName === 'FIGURE') closeLightbox(); });
        lightbox.addEventListener('keydown', function (e) {
            if (e.key === 'ArrowLeft') step(-1);
            if (e.key === 'ArrowRight') step(1);
        });
        lightbox.addEventListener('close', function () { document.body.style.overflow = ''; });
        // Wischen auf dem Handy
        var startX = null;
        lightbox.addEventListener('touchstart', function (e) { startX = e.touches[0].clientX; }, { passive: true });
        lightbox.addEventListener('touchend', function (e) {
            if (startX === null) return;
            var dx = e.changedTouches[0].clientX - startX;
            if (Math.abs(dx) > 50) step(dx < 0 ? 1 : -1);
            startX = null;
        });
    }

    function show() {
        var b = lbList[lbIndex];
        lbImg.src = b.datei;
        lbImg.alt = b.titel || 'Kerze aus der Kerzenküche';
        lbCap.textContent = (b.titel || '') + (lbList.length > 1 ? '  ·  ' + (lbIndex + 1) + ' / ' + lbList.length : '');
        var multi = lbList.length > 1;
        lightbox.querySelector('.lb-prev').hidden = !multi;
        lightbox.querySelector('.lb-next').hidden = !multi;
    }
    function step(d) { lbIndex = (lbIndex + d + lbList.length) % lbList.length; show(); }
    function openLightbox(list, i) {
        if (!lightbox) buildLightbox();
        lbList = list; lbIndex = i; show();
        document.body.style.overflow = 'hidden';
        if (lightbox.showModal) lightbox.showModal(); else lightbox.setAttribute('open', '');
    }
    function closeLightbox() {
        if (lightbox.close) lightbox.close(); else lightbox.removeAttribute('open');
        document.body.style.overflow = '';
    }

    function render(container, anlass) {
        var limit = parseInt(container.getAttribute('data-limit') || '0', 10);
        var list = BILDER.filter(function (b) { return !anlass || anlass === 'alle' || b.anlass === anlass; });
        if (limit) list = list.slice(0, limit);
        container.innerHTML = '';

        if (!list.length) {
            var empty = document.createElement('div');
            empty.className = 'gallery-empty';
            empty.innerHTML = '<p>Hier zeigen wir bald weitere Beispiele.<br>Gerne schicken wir euch vorab Fotos per WhatsApp.</p>' +
                '<a class="btn btn--outline" href="' + WHATSAPP + '" target="_blank" rel="noopener">Beispiele anfragen</a>';
            container.appendChild(empty);
            return;
        }

        list.forEach(function (b, i) {
            var fig = document.createElement('figure');
            fig.style.margin = '0';
            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'gallery-item';
            btn.setAttribute('aria-label', 'Bild vergrößern: ' + (b.titel || ''));
            var img = document.createElement('img');
            img.src = b.datei;
            img.alt = b.titel || 'Kerze aus der Kerzenküche';
            img.loading = 'lazy';
            img.decoding = 'async';
            btn.appendChild(img);
            if (b.titel) {
                var cap = document.createElement('figcaption');
                cap.textContent = b.titel;
                btn.appendChild(cap);
            }
            btn.addEventListener('click', function () { openLightbox(list, i); });
            fig.appendChild(btn);
            container.appendChild(fig);
        });
    }

    document.querySelectorAll('[data-galerie]').forEach(function (container) {
        var fixed = container.getAttribute('data-galerie'); // z. B. "taufe" oder "alle"
        var filterBar = container.parentNode.querySelector('.filter');

        if (!filterBar) { render(container, fixed); return; }

        // Galerie-Seite mit Filter: nur Anlässe anzeigen, die Bilder haben
        var vorhanden = {};
        BILDER.forEach(function (b) { vorhanden[b.anlass] = true; });
        var keys = ['alle'].concat(Object.keys(ANLAESSE).filter(function (k) { return vorhanden[k]; }));

        function setActive(key) {
            filterBar.querySelectorAll('button').forEach(function (bt) {
                bt.setAttribute('aria-pressed', bt.getAttribute('data-key') === key ? 'true' : 'false');
            });
            render(container, key);
        }

        keys.forEach(function (key) {
            var li = document.createElement('li');
            var bt = document.createElement('button');
            bt.type = 'button';
            bt.setAttribute('data-key', key);
            bt.textContent = key === 'alle' ? 'Alle' : ANLAESSE[key];
            bt.addEventListener('click', function () {
                setActive(key);
                if (history.replaceState) history.replaceState(null, '', key === 'alle' ? location.pathname : '#' + key);
            });
            li.appendChild(bt);
            filterBar.appendChild(li);
        });

        var start = location.hash.replace('#', '');
        setActive(vorhanden[start] ? start : 'alle');
    });
})();
