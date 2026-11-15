/* Aşkonomi quiz engine (English edition) — data: /en/testler/veri.js (ASKV) */
(function () {
  'use strict';
  var V = window.ASKV, SITE = 'https://askonomi.com';
  // Special chapter quizzes (Chemistry of Love) sit outside the series: not counted, not queued, not in the report card.
  var TUM = V.testler;
  V.testler = TUM.filter(function (t) { return !t.ozel; });
  var AY = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  var GUN = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  var ACILIS_SAATI = 'T09:00:00+03:00';
  var KARNE_ESIK = 5;

  function iz(n, d) { try { if (window.umami) umami.track(n, d); } catch (e) {} }
  function $(s, r) { return (r || document).querySelector(s); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  // ---- saved results (in the browser) ----
  // Stored value includes the result name (shown again), so the EN site uses its own key (brief rule 6).
  var ANAHTAR = 'askonomiTestler_en';
  function kayitlar() { try { return JSON.parse(localStorage.getItem(ANAHTAR)) || {}; } catch (e) { return {}; } }
  function kaydet(slug, k, ad) {
    var r = kayitlar(); r[slug] = { k: k, ad: ad, t: Date.now() };
    try { localStorage.setItem(ANAHTAR, JSON.stringify(r)); } catch (e) {}
  }
  function cozulenSayisi() { var r = kayitlar(); return V.testler.filter(function (t) { return t.tur !== 'karne' && r[t.slug] && r[t.slug].k !== 'bekliyor'; }).length; }

  // ---- time ----
  function acilisZamani(t) { return new Date(t.acilis + ACILIS_SAATI); }
  function icerikVar(t) { return t.tur === 'karne' || !!(t.sorular && t.sorular.length); }
  function acik(t) {
    if (t.tur === 'karne') return true;
    return icerikVar(t) && Date.now() >= acilisZamani(t).getTime();
  }
  function tarihMetni(t) { var d = acilisZamani(t); return GUN[d.getDay()] + ', ' + d.getDate() + ' ' + AY[d.getMonth()]; }
  function siradaki() {
    var gelecek = V.testler.filter(function (t) { return t.tur !== 'karne' && Date.now() < acilisZamani(t).getTime(); });
    gelecek.sort(function (a, b) { return acilisZamani(a) - acilisZamani(b); });
    return gelecek[0] || null;
  }
  function sayacHTML(hedef) {
    var ms = Math.max(0, hedef - Date.now()), g = Math.floor(ms / 864e5), s = Math.floor(ms / 36e5) % 24, d = Math.floor(ms / 6e4) % 60, sn = Math.floor(ms / 1e3) % 60;
    return '<div><b>' + g + '</b><span>days</span></div><div><b>' + s + '</b><span>hrs</span></div><div><b>' + d + '</b><span>min</span></div><div><b>' + sn + '</b><span>sec</span></div>';
  }
  function sayacBaslat(el, hedef) {
    if (!el) return;
    var f = function () { el.innerHTML = sayacHTML(hedef); if (Date.now() >= hedef) { clearInterval(z); location.reload(); } };
    f(); var z = setInterval(f, 1000);
  }
  function testBul(slug) { for (var i = 0; i < TUM.length; i++) if (TUM[i].slug === slug) return TUM[i]; return null; }
  function bolumAd(n) { return V.bolum[n] ? 'Chapter ' + parseInt(n, 10) + ' · ' + V.bolum[n] : ''; }
  function testUrl(t) { return '/en/test/' + t.slug + '/'; }

  // ================= MERKEZ =================
  function merkez() {
    var kok = $('#uygulama'), r = kayitlar(), n = cozulenSayisi(), sira = siradaki();
    var toplam = V.testler.length - 1;
    var h = '<div class="durum">';
    h += '<div class="kutu"><div class="k-ust">Your progress</div><div class="siradaki">' + n + ' / ' + toplam + ' quizzes done</div>' +
      '<div class="cubuk"><i style="width:' + (n / toplam * 100) + '%"></i></div>' +
      '<div style="font-size:16px;color:var(--soluk)">' + (n >= KARNE_ESIK ? 'Your Aşkonomi Report Card is unlocked. <a href="/en/test/karne/">See your report card →</a>' : (KARNE_ESIK - n) + ' more ' + (KARNE_ESIK - n === 1 ? 'quiz' : 'quizzes') + ' to unlock your report card.') + '</div></div>';
    if (sira) h += '<div class="kutu"><div class="k-ust">Next quiz · ' + tarihMetni(sira) + '</div><div class="siradaki">' + esc(sira.ad) + '</div><div class="sayac" id="sayac"></div></div>';
    h += '</div>';
    V.sezonlar.forEach(function (s) {
      h += '<section class="sezon"><div class="sezon-bas"><span class="etiket" style="margin:0">Season ' + s.no + '</span><h2>' + esc(s.ad) + '</h2><span>' + esc(s.alt) + '</span></div><div class="izgara">';
      V.testler.filter(function (t) { return t.sezon === s.no; }).forEach(function (t) { h += kartHTML(t, r, n); });
      h += '</div></section>';
    });
    kok.innerHTML = h;
    if (sira) sayacBaslat($('#sayac'), acilisZamani(sira).getTime());
  }
  function kartHTML(t, r, n) {
    var no = (t.no < 10 ? '0' : '') + t.no, tur = V.turAd[t.tur] || '';
    if (t.tur === 'karne') {
      return '<a class="tk karne" href="/en/test/karne/"><div class="no"><span>' + no + ' · Final</span></div><h3>' + esc(t.ad) + '</h3><div class="alt">' + (n >= KARNE_ESIK ? 'Unlocked. All your results on one page.' : 'Finish ' + KARNE_ESIK + ' quizzes to unlock your report card (' + n + '/' + KARNE_ESIK + ')') + '</div></a>';
    }
    if (!acik(t)) {
      var gecti = Date.now() >= acilisZamani(t).getTime();
      return '<div class="tk kilitli"><div class="no"><span>' + no + ' · ' + tur + '</span></div><h3>' + esc(t.ad) + '</h3><div class="alt">' + (gecti ? 'Coming very soon' : 'Opens ' + tarihMetni(t)) + '</div></div>';
    }
    var c = r[t.slug], yeni = (Date.now() - acilisZamani(t).getTime()) < 4 * 864e5;
    var rozet = c ? '<span class="rozet cozuldu">Done</span>' : (yeni ? '<span class="rozet">New</span>' : '');
    return '<a class="tk" href="' + testUrl(t) + '"><div class="no"><span>' + no + ' · ' + tur + '</span>' + rozet + '</div><h3>' + esc(t.ad) + '</h3><div class="alt">' + (c ? 'Your result: <b>' + esc(c.ad) + '</b>' : (t.bolum ? bolumAd(t.bolum) : '')) + '</div></a>';
  }

  // ================= TEST =================
  function test(slug) {
    var t = testBul(slug), kok = $('#uygulama');
    if (!t) { kok.innerHTML = '<p>Quiz not found.</p>'; return; }
    if (t.tur === 'karne') return karne(kok);
    if (!acik(t)) {
      var gecti = Date.now() >= acilisZamani(t).getTime();
      kok.innerHTML = '<div class="kart kilit-ekran"><span class="etiket">Locked quiz</span><h2 style="font-size:28px">' + esc(t.ad) + '</h2>' +
        (gecti ? '<p>This quiz opens very soon.</p>' : '<p>Opens on ' + tarihMetni(t) + ' at 09:00 (Turkey time).</p><div class="sayac" id="sayac"></div>') +
        '<p style="margin-top:22px"><a class="btn" href="/en/testler/">Try the open quizzes</a></p></div>';
      if (!gecti) sayacBaslat($('#sayac'), acilisZamani(t).getTime());
      return;
    }
    if (t.tur === 'mit') return mitTest(t, kok);
    if (t.tur === 'cift') return ciftTest(t, kok);
    if (t.tur === 'hesap') return hesapTest(t, kok);
    return profilTest(t, kok);
  }

  function ilerleme(i, n) { return '<div class="ilerleme"><i style="width:' + (i / n * 100) + '%"></i></div><div class="sayi">Question ' + (i + 1) + ' / ' + n + '</div>'; }

  function profilTest(t, kok) {
    var i = 0, puan = {}, son = {};
    function ciz() {
      if (i < t.sorular.length) {
        var q = t.sorular[i];
        kok.innerHTML = '<div class="kart">' + ilerleme(i, t.sorular.length) + '<p class="soru">' + esc(q[0]) + '</p>' +
          q[1].map(function (a) { return '<button class="secenek" data-k="' + a[0] + '">' + esc(a[1]) + '</button>'; }).join('') + '</div>';
        kok.querySelectorAll('.secenek').forEach(function (b) {
          b.onclick = function () {
            if (i === 0) iz('test-basladi', { test: t.slug });
            var k = b.dataset.k; puan[k] = (puan[k] || 0) + 1; son[k] = i; i++; ciz(); scrollUst();
          };
        });
        return;
      }
      var mx = Math.max.apply(null, Object.keys(puan).map(function (k) { return puan[k]; }));
      var aday = Object.keys(puan).filter(function (k) { return puan[k] === mx; });
      aday.sort(function (a, b) { return son[b] - son[a]; });
      var k = aday[0], s = t.sonuclar[k];
      kaydet(t.slug, k, s[0]); iz('test-bitti', { test: t.slug, sonuc: s[0] });
      sonucCiz(kok, t, k, s[0], s[1], s[2], function () { i = 0; puan = {}; son = {}; ciz(); });
    }
    ciz();
  }

  function mitTest(t, kok) {
    var i = 0, dogru = 0;
    function ciz() {
      if (i < t.sorular.length) {
        var q = t.sorular[i];
        kok.innerHTML = '<div class="kart">' + ilerleme(i, t.sorular.length) + '<p class="soru">“' + esc(q[0]) + '”</p>' +
          '<div class="ikili"><button class="secenek" data-v="1">True</button><button class="secenek" data-v="0">False</button></div><div id="gb"></div></div>';
        kok.querySelectorAll('.secenek').forEach(function (b) {
          b.onclick = function () {
            if (i === 0) iz('test-basladi', { test: t.slug });
            var cevap = b.dataset.v === '1', isabet = cevap === q[1];
            if (isabet) dogru++;
            kok.querySelectorAll('.secenek').forEach(function (x) { x.disabled = true; if ((x.dataset.v === '1') === q[1]) x.classList.add('dogru'); });
            if (!isabet) b.classList.add('hatali');
            $('#gb').innerHTML = '<div class="geri-bildirim' + (isabet ? '' : ' yanlis') + '"><b>' + (isabet ? 'Got it.' : 'Not quite.') + '</b> ' + esc(q[2]) + '</div>' +
              '<p style="margin:16px 0 0"><button class="btn" id="ileri">' + (i + 1 < t.sorular.length ? 'Next claim' : 'See your result') + '</button></p>';
            $('#ileri').onclick = function () { i++; ciz(); scrollUst(); };
          };
        });
        return;
      }
      var sv = 0; t.seviyeler.forEach(function (s, j) { if (dogru >= s[0]) sv = j; });
      var s = t.seviyeler[sv], ad = s[1] + ' · ' + dogru + '/' + t.sorular.length;
      kaydet(t.slug, 's' + sv, ad); iz('test-bitti', { test: t.slug, sonuc: s[1], puan: dogru });
      sonucCiz(kok, t, 's' + sv, s[1], s[2], t.bolum, function () { i = 0; dogru = 0; ciz(); }, dogru + ' / ' + t.sorular.length + ' correct');
    }
    ciz();
  }

  // ---- calculator: points are summed and converted to a 0–100 index ----
  function hesapTest(t, kok) {
    var i = 0, top = 0, mx = 0;
    function ciz() {
      if (i < t.sorular.length) {
        var q = t.sorular[i];
        kok.innerHTML = '<div class="kart">' + ilerleme(i, t.sorular.length) + '<p class="soru">' + esc(q[0]) + '</p>' +
          q[1].map(function (a) { return '<button class="secenek" data-p="' + a[0] + '">' + esc(a[1]) + '</button>'; }).join('') + '</div>';
        kok.querySelectorAll('.secenek').forEach(function (b) {
          b.onclick = function () {
            if (i === 0) iz('test-basladi', { test: t.slug });
            top += +b.dataset.p; mx += Math.max.apply(null, q[1].map(function (a) { return a[0]; })); i++; ciz(); scrollUst();
          };
        });
        return;
      }
      var e = mx ? Math.round(top / mx * 100) : 0, sv = 0;
      t.seviyeler.forEach(function (s, j) { if (e >= s[0]) sv = j; });
      var s = t.seviyeler[sv];
      kaydet(t.slug, 's' + sv, s[1] + ' · ' + e + '/100'); iz('test-bitti', { test: t.slug, sonuc: s[1], puan: e });
      sonucCiz(kok, t, 's' + sv, s[1], s[2], t.bolum, function () { i = 0; top = 0; mx = 0; ciz(); }, (t.birim || 'Index') + ': ' + e + ' / 100');
    }
    ciz();
  }

  // ---- couple quiz: answers travel inside the link, never sent to a server ----
  function ciftTest(t, kok) {
    var p = new URLSearchParams(location.search), a = p.get('a'), b = p.get('b'), an = p.get('an') || '', bn = p.get('bn') || '';
    var gecerli = function (x) { return x && x.length === t.sorular.length && /^[01]+$/.test(x); };
    if (gecerli(a) && gecerli(b)) return ciftSonuc(t, kok, a, b, an, bn, false);
    var davet = gecerli(a), cevap = '', i = -1, ad = '';
    function ciz() {
      if (i < 0) {
        kok.innerHTML = '<div class="kart">' + (davet ? '<div class="davet"><b>' + esc(an || 'Your partner') + '</b> took this quiz and invited you. Now it is your turn; at the end you will both see your answers side by side.</div>' :
          '<p>Ten short questions. You answer first, then send the link to your partner. When they finish, your answers appear side by side.</p>') +
          '<label for="ad" class="sayi">Your name (optional)</label><input id="ad" class="ad" maxlength="20" autocomplete="given-name" placeholder="For example: Alex"><button class="btn" id="basla">Start</button></div>';
        $('#basla').onclick = function () { ad = $('#ad').value.trim().slice(0, 20); i = 0; iz('test-basladi', { test: t.slug, davet: davet ? 1 : 0 }); ciz(); };
        return;
      }
      if (i < t.sorular.length) {
        var q = t.sorular[i];
        kok.innerHTML = '<div class="kart">' + ilerleme(i, t.sorular.length) + '<p class="soru">' + esc(q[0]) + '</p><div class="ikili">' +
          q[1].map(function (x, j) { return '<button class="secenek" data-j="' + j + '">' + esc(x) + '</button>'; }).join('') + '</div></div>';
        kok.querySelectorAll('.secenek').forEach(function (bt) { bt.onclick = function () { cevap += bt.dataset.j; i++; ciz(); scrollUst(); }; });
        return;
      }
      if (davet) return ciftSonuc(t, kok, a, cevap, an, ad, true);
      var link = SITE + testUrl(t) + '?a=' + cevap + (ad ? '&an=' + encodeURIComponent(ad) : '');
      var msg = 'I took the Aşkonomi couple quiz: “' + t.ad + '” Your turn, then we can see our answers side by side: ' + link;
      kaydet(t.slug, 'bekliyor', 'Waiting for your partner');
      kok.innerHTML = '<div class="kart sonuc"><span class="bolumno">Halfway there</span><h2>Now it is your partner’s turn</h2>' +
        '<p>Send this link to your partner only. When they finish, your answers appear side by side and your match score is calculated.</p>' +
        '<div class="paylas"><a class="wa" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent(msg) + '">Send on WhatsApp</a><button id="kopya">Copy link</button></div>' +
        '<p class="not">Your answers are never saved on any server; they travel only inside this link.</p>' + altBaglar() + '</div>';
      $('#kopya').onclick = function (e) { kopyala(link, e.target); };
      iz('cift-davet-olustu');
    }
    ciz();
  }
  function ciftSonuc(t, kok, a, b, an, bn, yeniBitti) {
    var es = 0; for (var j = 0; j < a.length; j++) if (a[j] === b[j]) es++;
    var sv = 0; t.seviyeler.forEach(function (s, k) { if (es >= s[0]) sv = k; });
    var s = t.seviyeler[sv], A = an || 'Partner 1', B = bn || 'Partner 2';
    if (yeniBitti) { kaydet(t.slug, 's' + sv, s[1] + ' · ' + es * 10 + '%'); iz('test-bitti', { test: t.slug, sonuc: s[1], uyum: es * 10 }); }
    var tablo = '<table class="karsilastir"><tr><th></th><th>' + esc(A) + '</th><th>' + esc(B) + '</th></tr>' + t.sorular.map(function (q, j) {
      var e = a[j] === b[j];
      return '<tr><td>' + esc(q[0]) + '</td><td class="' + (e ? 'e' : 'f') + '">' + esc(q[1][+a[j]]) + '</td><td class="' + (e ? 'e' : 'f') + '">' + esc(q[1][+b[j]]) + '</td></tr>';
    }).join('') + '</table>';
    var ikisi = SITE + testUrl(t) + '?a=' + a + '&b=' + b + (an ? '&an=' + encodeURIComponent(an) : '') + (bn ? '&bn=' + encodeURIComponent(bn) : '');
    var msg = 'Our match in the Aşkonomi couple quiz: ' + es * 10 + '%, ' + s[1] + '. Our answers: ' + ikisi;
    kok.innerHTML = '<div class="kart sonuc"><span class="bolumno">' + esc(A) + ' & ' + esc(B) + '</span><div class="yuzde">' + es * 10 + '%</div><h2>' + esc(s[1]) + '</h2><p>' + esc(s[2]) + '</p>' + tablo +
      '<div class="paylas"><a class="wa" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent(msg) + '">Send the result to your partner</a><button id="kopya">Copy link</button></div>' +
      '<p class="not">' + bolumAd(t.bolum) + ' covers this topic.</p>' +
      '<div class="paylas"><a target="_blank" rel="noopener" href="https://x.com/intent/tweet?via=askonomikitap&text=' + encodeURIComponent('Our match in the Aşkonomi couple quiz: ' + es * 10 + '%, ' + s[1] + '. What is yours? ' + SITE + testUrl(t) + '?utm_source=x') + '">Share on X (without answers)</a>' + igHTML() + '</div>' + igNotHTML() +
      fragmanHTML(t) + aboneHTML() + altBaglar() + '</div>';
    $('#kopya').onclick = function (e) { kopyala(ikisi, e.target); };
    igHazirla({ ust: t.ad, etiket: 'Our match in the Aşkonomi couple quiz', baslik: es * 10 + '% · ' + s[1], alt: 'What is yours?' }, SITE + testUrl(t));
    fragmanSayac();
  }


  // ---- Instagram Story image (1080×1920, drawn in the browser) ----
  var IG = { blob: null, o: null, url: '' };
  function satirla(c, metin, maxw) {
    var w = String(metin).split(' '), out = [], cur = '';
    w.forEach(function (k) { var d = cur ? cur + ' ' + k : k; if (c.measureText(d).width <= maxw) cur = d; else { if (cur) out.push(cur); cur = k; } });
    if (cur) out.push(cur); return out;
  }
  function igCiz(o) {
    var cv = document.createElement('canvas'); cv.width = 1080; cv.height = 1920;
    var c = cv.getContext('2d'), M = '#262028', B = '#B3263A', S = '#6b6070';
    c.fillStyle = '#F2EBE0'; c.fillRect(0, 0, 1080, 1920);
    c.strokeStyle = '#d8ccbb'; c.lineWidth = 2; c.strokeRect(60, 60, 960, 1800);
    c.textAlign = 'center'; c.textBaseline = 'alphabetic';
    function yaz(m, font, renk, y, maxw, lh) { c.font = font; c.fillStyle = renk; lh = lh || Math.round(parseInt(font.match(/(\d+)px/)[1], 10) * 1.15); var ls = satirla(c, m, maxw || 860); ls.forEach(function (l, i) { c.fillText(l, 540, y + i * lh); }); return y + ls.length * lh; }
    yaz('A Ş K O N O M İ   Q U I Z', '500 34px Fraunces, Georgia, serif', B, 290);
    var y = yaz(o.ust, 'italic 400 54px Fraunces, Georgia, serif', M, 390, 860, 66);
    // heart
    var hy = Math.max(y + 230, 760), hs = 9.5;
    c.beginPath();
    for (var k = 0; k <= 200; k++) { var a = Math.PI * 2 * k / 200, x = 16 * Math.pow(Math.sin(a), 3), yy = 13 * Math.cos(a) - 5 * Math.cos(2 * a) - 2 * Math.cos(3 * a) - Math.cos(4 * a); if (k) c.lineTo(540 + x * hs, hy - yy * hs); else c.moveTo(540 + x * hs, hy - yy * hs); }
    c.strokeStyle = B; c.lineWidth = 7; c.stroke();
    y = yaz(o.etiket || 'My result', 'italic 400 46px "Crimson Pro", Georgia, serif', S, hy + 290);
    y = yaz(o.baslik, '600 88px Fraunces, Georgia, serif', B, y + 50, 860, 98);
    yaz(o.alt || 'What is yours?', '600 56px Fraunces, Georgia, serif', M, Math.max(y + 90, 1440));
    yaz('askonomi.com/en', '600 50px Fraunces, Georgia, serif', M, 1600);
    yaz('Aşkonomi: The Economics of the Heart’s Decisions · Prof. Dr. Mehmet Şahin', '400 30px "Crimson Pro", Georgia, serif', S, 1652);
    return cv;
  }
  function igHazirla(o, url) {
    IG.blob = null; IG.o = o; IG.url = url + (url.indexOf('?') < 0 ? '?' : '&') + 'utm_source=instagram';
    var fl = ['500 34px Fraunces', '600 88px Fraunces', 'italic 400 54px Fraunces', 'italic 400 46px "Crimson Pro"', '400 30px "Crimson Pro"'];
    var bekle = (document.fonts && document.fonts.load) ? Promise.all(fl.map(function (f) { return document.fonts.load(f).catch(function () {}); })) : Promise.resolve();
    bekle.then(function () { igCiz(o).toBlob(function (b) { IG.blob = b; }, 'image/png'); });
    var bt = $('#ig'); if (bt) bt.onclick = function () { igPaylas(bt); };
  }
  function igPaylas(bt) {
    var not = $('#ig-not');
    if (!IG.blob) { bt.textContent = 'Preparing…'; setTimeout(function () { bt.textContent = 'Instagram Story'; }, 900); return; }
    var dosya = null; try { dosya = new File([IG.blob], 'askonomi-my-result.png', { type: 'image/png' }); } catch (e) {}
    if (not) not.hidden = false;
    if (dosya && navigator.canShare && navigator.canShare({ files: [dosya] })) {
      navigator.share({ files: [dosya] }).catch(function () {});
    } else {
      var a = document.createElement('a'); a.href = URL.createObjectURL(IG.blob); a.download = 'askonomi-my-result.png';
      document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1500);
      if (not) not.innerHTML = 'Image downloaded. Share it as a <b>Story</b> on Instagram from your phone and add the quiz with a <b>link sticker</b>. <button id="ig-kopya">Copy link</button>';
    }
    var k = $('#ig-kopya'); if (k) k.onclick = function (e) { kopyala(IG.url, e.target); };
  }
  function igHTML() {
    return '<button class="ig" id="ig">Instagram Story</button>';
  }
  function igNotHTML() {
    return '<p class="not ig-not" id="ig-not" hidden>On Instagram choose <b>Story</b>, then add the quiz link with a <b>link sticker</b> so your followers can take it in one tap. <button id="ig-kopya">Copy link</button></p>';
  }

  // ---- shared result screen ----
  function sonucCiz(kok, t, k, ad, metin, bolum, yeniden, ek) {
    var url = SITE + testUrl(t) + 's/' + k + '/';
    var msg = 'My Aşkonomi quiz result: “' + ad + '”. What is yours?';
    kok.innerHTML = '<div class="kart sonuc"><span class="bolumno">' + (ek ? esc(ek) : 'Your result') + '</span><h2>' + esc(ad) + '</h2><p>' + esc(metin) + '</p>' +
      (bolum ? '<p class="not">In the book: ' + bolumAd(bolum) + '</p>' : '') +
      '<div class="paylas"><a class="wa" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent(msg + ' ' + url + '?utm_source=whatsapp') + '">WhatsApp</a>' +
      '<a target="_blank" rel="noopener" href="https://x.com/intent/tweet?via=askonomikitap&text=' + encodeURIComponent(msg + ' ' + url + '?utm_source=x') + '">X</a>' +
      '<a target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(url + '?utm_source=facebook') + '">Facebook</a>' +
      igHTML() + '<button id="kopya">Copy link</button></div>' + igNotHTML() +
      fragmanHTML(t) + aboneHTML() + altBaglar(true) + '</div>';
    $('#kopya').onclick = function (e) { kopyala(url, e.target); };
    igHazirla({ ust: t.ad, baslik: ad }, url);
    var y = $('#yeniden'); if (y) y.onclick = function () { yeniden(); scrollUst(); };
    fragmanSayac();
    scrollUst();
  }
  var fragmanHedef = null;
  function fragmanHTML(t) {
    var r = kayitlar();
    var acikCozulmemis = V.testler.filter(function (x) { return x.tur !== 'karne' && x.slug !== t.slug && acik(x) && !r[x.slug]; });
    var sira = siradaki(), h = '';
    if (sira) {
      fragmanHedef = acilisZamani(sira).getTime();
      h += '<div class="fragman"><div class="k-ust">Next quiz · ' + tarihMetni(sira) + '</div><b>' + esc(sira.ad) + '</b><div class="zaman" id="fz"></div></div>';
    }
    if (acikCozulmemis.length) {
      var n = acikCozulmemis[0];
      h += '<p style="margin:14px 0 0"><a class="btn" href="' + testUrl(n) + '">Next quiz: ' + esc(n.ad) + ' →</a></p>';
    } else if (cozulenSayisi() >= KARNE_ESIK) {
      h += '<p style="margin:14px 0 0"><a class="btn" href="/en/test/karne/">See your Aşkonomi Report Card →</a></p>';
    }
    return h;
  }
  function fragmanSayac() {
    var el = $('#fz'); if (!el || !fragmanHedef) return;
    var f = function () { var ms = Math.max(0, fragmanHedef - Date.now()), g = Math.floor(ms / 864e5), s = Math.floor(ms / 36e5) % 24, d = Math.floor(ms / 6e4) % 60; el.textContent = 'Opens in ' + (g ? g + (g === 1 ? ' day ' : ' days ') : '') + s + (s === 1 ? ' hour ' : ' hours ') + d + (d === 1 ? ' minute' : ' minutes'); };
    f(); setInterval(f, 30000);
  }
  function aboneHTML() {
    return '<div class="abone-kutu"><p>New quizzes open every Monday and Thursday. The book Aşkonomi is out now (in Turkish) on Kitapyurdu.</p><a class="btn al" target="_blank" rel="noopener" data-umami-event="kitapyurdu-testler" href="https://www.kitapyurdu.com/kitap/askonomi-kalbin-kararlarinin-ekonomisi/774343.html">Buy the book (in Turkish)</a> <a class="btn ikincil abone-git" href="/#takip">Join the email list</a></div>';
  }
  function altBaglar(yeniden) {
    var oz = testBul(document.body.dataset.slug || '');
    if (oz && oz.ozel) return '<div class="alt-baglar"><a href="/en/kimya/">← The Chemistry of Love</a>' + (yeniden ? '<button id="yeniden">Retake this quiz</button>' : '') + '<a href="/en/testler/">The 40-quiz series</a><a href="https://www.instagram.com/profmehmetsahin/" target="_blank" rel="noopener">@profmehmetsahin</a></div>';
    return '<div class="alt-baglar"><a href="/en/testler/">All quizzes (' + cozulenSayisi() + '/' + (V.testler.length - 1) + ')</a>' + (yeniden ? '<button id="yeniden">Retake this quiz</button>' : '') + '<a href="https://www.instagram.com/profmehmetsahin/" target="_blank" rel="noopener">@profmehmetsahin</a></div>';
  }
  function kopyala(s, el) { try { navigator.clipboard.writeText(s); el.textContent = 'Copied'; } catch (e) { prompt('Link:', s); } }
  function scrollUst() { var u = $('.test-ust'); if (u && u.getBoundingClientRect().top < -40) window.scrollTo({ top: 0, behavior: 'smooth' }); }

  // ================= KARNE =================
  function karne(kok) {
    var r = kayitlar(), n = cozulenSayisi();
    if (n < KARNE_ESIK) {
      kok.innerHTML = '<div class="kart kilit-ekran"><span class="etiket">Locked</span><h2 style="font-size:30px">Your report card unlocks after ' + (KARNE_ESIK - n) + ' more ' + (KARNE_ESIK - n === 1 ? 'quiz' : 'quizzes') + '</h2>' +
        '<div class="cubuk" style="max-width:360px;margin:20px auto"><i style="width:' + (n / KARNE_ESIK * 100) + '%"></i></div><p>' + n + ' / ' + KARNE_ESIK + ' quizzes done.</p>' +
        '<p style="margin-top:22px"><a class="btn" href="/en/testler/">Back to the quizzes</a></p></div>';
      return;
    }
    var liste = V.testler.filter(function (t) { return r[t.slug] && t.tur !== 'karne' && r[t.slug].k !== 'bekliyor'; });
    var sayim = {};
    liste.forEach(function (t) {
      var b = t.bolum; var k = r[t.slug].k;
      if (t.sonuclar && t.sonuclar[k]) b = t.sonuclar[k][2];
      if (b) sayim[b] = (sayim[b] || 0) + 1;
    });
    var ilk = Object.keys(sayim).sort(function (x, y) { return sayim[y] - sayim[x]; }).slice(0, 3);
    var msg = 'My Aşkonomi Report Card is unlocked: ' + liste.length + ' quizzes, my top chapter is “' + (V.bolum[ilk[0]] || '') + '”. What is yours?';
    kok.innerHTML = '<div class="kart sonuc"><span class="bolumno">' + liste.length + ' quizzes</span><h2>Your Aşkonomi Report Card</h2>' +
      '<p>The chapters of the book that suit you best:</p><ol>' + ilk.map(function (b) { return '<li><b>' + bolumAd(b) + '</b></li>'; }).join('') + '</ol>' +
      '<div class="karne-liste">' + liste.map(function (t) { return '<div><small>' + esc(t.ad) + '</small><b>' + esc(r[t.slug].ad) + '</b></div>'; }).join('') + '</div>' +
      '<div class="paylas"><a class="wa" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent(msg + ' ' + SITE + '/en/testler/?utm_source=whatsapp') + '">WhatsApp</a><a target="_blank" rel="noopener" href="https://x.com/intent/tweet?via=askonomikitap&text=' + encodeURIComponent(msg + ' ' + SITE + '/en/testler/?utm_source=x') + '">X</a>' + igHTML() + '</div>' + igNotHTML() +
      '<p class="not">Your report card updates with every new quiz. Your results are saved only in this browser.</p>' + aboneHTML() + altBaglar() + '</div>';
    igHazirla({ ust: 'I took ' + liste.length + ' quizzes', etiket: 'Top chapter on my Aşkonomi Report Card', baslik: V.bolum[ilk[0]] || 'My Aşkonomi Report Card', alt: 'What is yours?' }, SITE + '/en/testler/');
    iz('karne-goruldu', { test: liste.length });
  }

  // ================= RESULT SHARE PAGE =================
  function sonucSayfasi(slug) {
    var t = testBul(slug), r = kayitlar(), el = $('#kendi');
    if (el && t && r[slug]) el.innerHTML = 'Your result: <b>' + esc(r[slug].ad) + '</b>';
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('.paylas a, .paylas button');
    if (a) iz('sonuc-paylas', { kanal: a.textContent.trim(), sayfa: document.body.dataset.slug || 'merkez' });
    if (e.target.closest && e.target.closest('.abone-git')) iz('abone-cagrisi', { kaynak: 'test' });
  });

  var sayfa = document.body.dataset.sayfa, slug = document.body.dataset.slug;
  if (sayfa === 'merkez') merkez();
  else if (sayfa === 'test') test(slug);
  else if (sayfa === 'sonuc') sonucSayfasi(slug);
})();
