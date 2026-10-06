/* Aşkonomi test motoru — veri: /testler/veri.js (ASKV) */
(function () {
  'use strict';
  var V = window.ASKV, SITE = 'https://askonomi.com';
  var AY = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
  var GUN = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'];
  var ACILIS_SAATI = 'T09:00:00+03:00';
  var KARNE_ESIK = 5;

  function iz(n, d) { try { if (window.umami) umami.track(n, d); } catch (e) {} }
  function $(s, r) { return (r || document).querySelector(s); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  // ---- kayıt (tarayıcıda) ----
  var ANAHTAR = 'askonomiTestler';
  function kayitlar() { try { return JSON.parse(localStorage.getItem(ANAHTAR)) || {}; } catch (e) { return {}; } }
  function kaydet(slug, k, ad) {
    var r = kayitlar(); r[slug] = { k: k, ad: ad, t: Date.now() };
    try { localStorage.setItem(ANAHTAR, JSON.stringify(r)); } catch (e) {}
  }
  function cozulenSayisi() { var r = kayitlar(); return V.testler.filter(function (t) { return t.tur !== 'karne' && r[t.slug] && r[t.slug].k !== 'bekliyor'; }).length; }

  // ---- zaman ----
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
    return '<div><b>' + g + '</b><span>gün</span></div><div><b>' + s + '</b><span>saat</span></div><div><b>' + d + '</b><span>dk</span></div><div><b>' + sn + '</b><span>sn</span></div>';
  }
  function sayacBaslat(el, hedef) {
    if (!el) return;
    var f = function () { el.innerHTML = sayacHTML(hedef); if (Date.now() >= hedef) { clearInterval(z); location.reload(); } };
    f(); var z = setInterval(f, 1000);
  }
  function testBul(slug) { for (var i = 0; i < V.testler.length; i++) if (V.testler[i].slug === slug) return V.testler[i]; return null; }
  function bolumAd(n) { return V.bolum[n] ? 'Bölüm ' + parseInt(n, 10) + ' · ' + V.bolum[n] : ''; }
  function testUrl(t) { return '/test/' + t.slug + '/'; }

  // ================= MERKEZ =================
  function merkez() {
    var kok = $('#uygulama'), r = kayitlar(), n = cozulenSayisi(), sira = siradaki();
    var toplam = V.testler.length - 1;
    var h = '<div class="durum">';
    h += '<div class="kutu"><div class="k-ust">Senin ilerlemen</div><div class="siradaki">' + n + ' / ' + toplam + ' test çözdün</div>' +
      '<div class="cubuk"><i style="width:' + (n / toplam * 100) + '%"></i></div>' +
      '<div style="font-size:16px;color:var(--soluk)">' + (n >= KARNE_ESIK ? 'Aşkonomi Karnen açıldı. <a href="/test/karne/">Karneni gör →</a>' : 'Karnenin açılmasına ' + (KARNE_ESIK - n) + ' test kaldı.') + '</div></div>';
    if (sira) h += '<div class="kutu"><div class="k-ust">Sıradaki test · ' + tarihMetni(sira) + '</div><div class="siradaki">' + esc(sira.ad) + '</div><div class="sayac" id="sayac"></div></div>';
    h += '</div>';
    V.sezonlar.forEach(function (s) {
      h += '<section class="sezon"><div class="sezon-bas"><span class="etiket" style="margin:0">Sezon ' + s.no + '</span><h2>' + esc(s.ad) + '</h2><span>' + esc(s.alt) + '</span></div><div class="izgara">';
      V.testler.filter(function (t) { return t.sezon === s.no; }).forEach(function (t) { h += kartHTML(t, r, n); });
      h += '</div></section>';
    });
    kok.innerHTML = h;
    if (sira) sayacBaslat($('#sayac'), acilisZamani(sira).getTime());
  }
  function kartHTML(t, r, n) {
    var no = (t.no < 10 ? '0' : '') + t.no, tur = V.turAd[t.tur] || '';
    if (t.tur === 'karne') {
      return '<a class="tk karne" href="/test/karne/"><div class="no"><span>' + no + ' · Final</span></div><h3>' + esc(t.ad) + '</h3><div class="alt">' + (n >= KARNE_ESIK ? 'Açıldı. Bütün sonuçların tek sayfada.' : KARNE_ESIK + ' test çöz, karnen açılsın (' + n + '/' + KARNE_ESIK + ')') + '</div></a>';
    }
    if (!acik(t)) {
      var gecti = Date.now() >= acilisZamani(t).getTime();
      return '<div class="tk kilitli"><div class="no"><span>' + no + ' · ' + tur + '</span></div><h3>' + esc(t.ad) + '</h3><div class="alt">' + (gecti ? 'Çok yakında' : tarihMetni(t) + ' açılıyor') + '</div></div>';
    }
    var c = r[t.slug], yeni = (Date.now() - acilisZamani(t).getTime()) < 4 * 864e5;
    var rozet = c ? '<span class="rozet cozuldu">Çözüldü</span>' : (yeni ? '<span class="rozet">Yeni</span>' : '');
    return '<a class="tk" href="' + testUrl(t) + '"><div class="no"><span>' + no + ' · ' + tur + '</span>' + rozet + '</div><h3>' + esc(t.ad) + '</h3><div class="alt">' + (c ? 'Sonucun: <b>' + esc(c.ad) + '</b>' : (t.bolum ? bolumAd(t.bolum) : '')) + '</div></a>';
  }

  // ================= TEST =================
  function test(slug) {
    var t = testBul(slug), kok = $('#uygulama');
    if (!t) { kok.innerHTML = '<p>Test bulunamadı.</p>'; return; }
    if (t.tur === 'karne') return karne(kok);
    if (!acik(t)) {
      var gecti = Date.now() >= acilisZamani(t).getTime();
      kok.innerHTML = '<div class="kart kilit-ekran"><span class="etiket">Kilitli test</span><h2 style="font-size:28px">' + esc(t.ad) + '</h2>' +
        (gecti ? '<p>Bu test çok yakında açılıyor.</p>' : '<p>' + tarihMetni(t) + ', saat 09:00’da açılıyor.</p><div class="sayac" id="sayac"></div>') +
        '<p style="margin-top:22px"><a class="btn" href="/testler/">Açık testleri çöz</a></p></div>';
      if (!gecti) sayacBaslat($('#sayac'), acilisZamani(t).getTime());
      return;
    }
    if (t.tur === 'mit') return mitTest(t, kok);
    if (t.tur === 'cift') return ciftTest(t, kok);
    return profilTest(t, kok);
  }

  function ilerleme(i, n) { return '<div class="ilerleme"><i style="width:' + (i / n * 100) + '%"></i></div><div class="sayi">Soru ' + (i + 1) + ' / ' + n + '</div>'; }

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
          '<div class="ikili"><button class="secenek" data-v="1">Doğru</button><button class="secenek" data-v="0">Yanlış</button></div><div id="gb"></div></div>';
        kok.querySelectorAll('.secenek').forEach(function (b) {
          b.onclick = function () {
            if (i === 0) iz('test-basladi', { test: t.slug });
            var cevap = b.dataset.v === '1', isabet = cevap === q[1];
            if (isabet) dogru++;
            kok.querySelectorAll('.secenek').forEach(function (x) { x.disabled = true; if ((x.dataset.v === '1') === q[1]) x.classList.add('dogru'); });
            if (!isabet) b.classList.add('hatali');
            $('#gb').innerHTML = '<div class="geri-bildirim' + (isabet ? '' : ' yanlis') + '"><b>' + (isabet ? 'Bildin.' : 'Bilemedin.') + '</b> ' + esc(q[2]) + '</div>' +
              '<p style="margin:16px 0 0"><button class="btn" id="ileri">' + (i + 1 < t.sorular.length ? 'Sonraki iddia' : 'Sonucu gör') + '</button></p>';
            $('#ileri').onclick = function () { i++; ciz(); scrollUst(); };
          };
        });
        return;
      }
      var sv = 0; t.seviyeler.forEach(function (s, j) { if (dogru >= s[0]) sv = j; });
      var s = t.seviyeler[sv], ad = s[1] + ' · ' + dogru + '/' + t.sorular.length;
      kaydet(t.slug, 's' + sv, ad); iz('test-bitti', { test: t.slug, sonuc: s[1], puan: dogru });
      sonucCiz(kok, t, 's' + sv, s[1], s[2], t.bolum, function () { i = 0; dogru = 0; ciz(); }, dogru + ' / ' + t.sorular.length + ' doğru');
    }
    ciz();
  }

  // ---- çift testi: cevaplar bağlantıda taşınır, sunucuya gitmez ----
  function ciftTest(t, kok) {
    var p = new URLSearchParams(location.search), a = p.get('a'), b = p.get('b'), an = p.get('an') || '', bn = p.get('bn') || '';
    var gecerli = function (x) { return x && x.length === t.sorular.length && /^[01]+$/.test(x); };
    if (gecerli(a) && gecerli(b)) return ciftSonuc(t, kok, a, b, an, bn, false);
    var davet = gecerli(a), cevap = '', i = -1, ad = '';
    function ciz() {
      if (i < 0) {
        kok.innerHTML = '<div class="kart">' + (davet ? '<div class="davet"><b>' + esc(an || 'Partnerin') + '</b> bu testi çözdü ve seni davet etti. Şimdi sen çöz; sonunda ikinizin cevaplarını yan yana göreceksiniz.</div>' :
          '<p>On kısa soru. Önce sen çöz, sonra bağlantıyı partnerine gönder. O da çözünce ikinizin “fiyat listesi” yan yana çıkacak.</p>') +
          '<label for="ad" class="sayi">Adın (isteğe bağlı)</label><input id="ad" class="ad" maxlength="20" autocomplete="given-name" placeholder="Örneğin: Deniz"><button class="btn" id="basla">Başla</button></div>';
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
      var msg = 'Aşkonomi çift testini çözdüm. Bakalım birbirimizi ne kadar doğru “fiyatlıyoruz”? Sen de çöz: ' + link;
      kaydet(t.slug, 'bekliyor', 'Partnerini bekliyor');
      kok.innerHTML = '<div class="kart sonuc"><span class="bolumno">Yarısı tamam</span><h2>Şimdi sıra partnerinde</h2>' +
        '<p>Bu bağlantıyı yalnızca partnerine gönder. O çözünce ikinizin cevapları yan yana çıkacak ve uyum puanınız hesaplanacak.</p>' +
        '<div class="paylas"><a class="wa" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent(msg) + '">WhatsApp ile gönder</a><button id="kopya">Bağlantıyı kopyala</button></div>' +
        '<p class="not">Cevapların hiçbir sunucuya kaydedilmez; yalnızca bu bağlantının içinde taşınır.</p>' + altBaglar() + '</div>';
      $('#kopya').onclick = function (e) { kopyala(link, e.target); };
      iz('cift-davet-olustu');
    }
    ciz();
  }
  function ciftSonuc(t, kok, a, b, an, bn, yeniBitti) {
    var es = 0; for (var j = 0; j < a.length; j++) if (a[j] === b[j]) es++;
    var sv = 0; t.seviyeler.forEach(function (s, k) { if (es >= s[0]) sv = k; });
    var s = t.seviyeler[sv], A = an || 'Partner 1', B = bn || 'Partner 2';
    if (yeniBitti) { kaydet(t.slug, 's' + sv, s[1] + ' · %' + es * 10); iz('test-bitti', { test: t.slug, sonuc: s[1], uyum: es * 10 }); }
    var tablo = '<table class="karsilastir"><tr><th></th><th>' + esc(A) + '</th><th>' + esc(B) + '</th></tr>' + t.sorular.map(function (q, j) {
      var e = a[j] === b[j];
      return '<tr><td>' + esc(q[0]) + '</td><td class="' + (e ? 'e' : 'f') + '">' + esc(q[1][+a[j]]) + '</td><td class="' + (e ? 'e' : 'f') + '">' + esc(q[1][+b[j]]) + '</td></tr>';
    }).join('') + '</table>';
    var ikisi = SITE + testUrl(t) + '?a=' + a + '&b=' + b + (an ? '&an=' + encodeURIComponent(an) : '') + (bn ? '&bn=' + encodeURIComponent(bn) : '');
    var msg = 'Aşkonomi çift testinde uyumumuz %' + es * 10 + ' çıktı: ' + s[1] + '. Sonuçlarımız: ' + ikisi;
    kok.innerHTML = '<div class="kart sonuc"><span class="bolumno">' + esc(A) + ' & ' + esc(B) + '</span><div class="yuzde">%' + es * 10 + '</div><h2>' + esc(s[1]) + '</h2><p>' + esc(s[2]) + '</p>' + tablo +
      '<div class="paylas"><a class="wa" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent(msg) + '">Sonucu partnerine gönder</a><button id="kopya">Bağlantıyı kopyala</button></div>' +
      '<p class="not">' + bolumAd(t.bolum) + ' bu konuyu ele alıyor.</p>' +
      '<div class="paylas"><a target="_blank" rel="noopener" href="https://x.com/intent/tweet?via=askonomikitap&text=' + encodeURIComponent('Aşkonomi çift testinde uyumumuz %' + es * 10 + ': ' + s[1] + '. Sizinki kaç? ' + SITE + testUrl(t) + '?utm_source=x') + '">X’te paylaş (cevaplar olmadan)</a></div>' +
      fragmanHTML(t) + aboneHTML() + altBaglar() + '</div>';
    $('#kopya').onclick = function (e) { kopyala(ikisi, e.target); };
    fragmanSayac();
  }

  // ---- ortak sonuç ekranı ----
  function sonucCiz(kok, t, k, ad, metin, bolum, yeniden, ek) {
    var url = SITE + testUrl(t) + 's/' + k + '/';
    var msg = 'Aşkonomi testine göre sonucum: “' + ad + '”. Seninki ne?';
    kok.innerHTML = '<div class="kart sonuc"><span class="bolumno">' + (ek ? esc(ek) : 'Sonucun') + '</span><h2>' + esc(ad) + '</h2><p>' + esc(metin) + '</p>' +
      (bolum ? '<p class="not">Kitapta: ' + bolumAd(bolum) + '</p>' : '') +
      '<div class="paylas"><a class="wa" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent(msg + ' ' + url + '?utm_source=whatsapp') + '">WhatsApp</a>' +
      '<a target="_blank" rel="noopener" href="https://x.com/intent/tweet?via=askonomikitap&text=' + encodeURIComponent(msg + ' ' + url + '?utm_source=x') + '">X</a>' +
      '<a target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(url + '?utm_source=facebook') + '">Facebook</a>' +
      '<button id="kopya">Bağlantıyı kopyala</button></div>' +
      fragmanHTML(t) + aboneHTML() + altBaglar(true) + '</div>';
    $('#kopya').onclick = function (e) { kopyala(url, e.target); };
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
      h += '<div class="fragman"><div class="k-ust">Sıradaki test · ' + tarihMetni(sira) + '</div><b>' + esc(sira.ad) + '</b><div class="zaman" id="fz"></div></div>';
    }
    if (acikCozulmemis.length) {
      var n = acikCozulmemis[0];
      h += '<p style="margin:14px 0 0"><a class="btn" href="' + testUrl(n) + '">Sonraki testi çöz: ' + esc(n.ad) + ' →</a></p>';
    } else if (cozulenSayisi() >= KARNE_ESIK) {
      h += '<p style="margin:14px 0 0"><a class="btn" href="/test/karne/">Aşkonomi Karneni gör →</a></p>';
    }
    return h;
  }
  function fragmanSayac() {
    var el = $('#fz'); if (!el || !fragmanHedef) return;
    var f = function () { var ms = Math.max(0, fragmanHedef - Date.now()), g = Math.floor(ms / 864e5), s = Math.floor(ms / 36e5) % 24, d = Math.floor(ms / 6e4) % 60; el.textContent = 'Açılmasına ' + (g ? g + ' gün ' : '') + s + ' saat ' + d + ' dakika'; };
    f(); setInterval(f, 30000);
  }
  function aboneHTML() {
    return '<div class="abone-kutu"><p>Yeni testler her Pazartesi ve Perşembe açılıyor. Haber almak ve kitap çıktığında ilk duymak için:</p><a class="btn abone-git" href="/#takip">E-posta listesine katıl</a></div>';
  }
  function altBaglar(yeniden) {
    return '<div class="alt-baglar"><a href="/testler/">Tüm testler (' + cozulenSayisi() + '/' + (V.testler.length - 1) + ')</a>' + (yeniden ? '<button id="yeniden">Bu testi yeniden çöz</button>' : '') + '<a href="https://instagram.com/askonomikitap" target="_blank" rel="noopener">@askonomikitap</a></div>';
  }
  function kopyala(s, el) { try { navigator.clipboard.writeText(s); el.textContent = 'Kopyalandı'; } catch (e) { prompt('Bağlantı:', s); } }
  function scrollUst() { var u = $('.test-ust'); if (u && u.getBoundingClientRect().top < -40) window.scrollTo({ top: 0, behavior: 'smooth' }); }

  // ================= KARNE =================
  function karne(kok) {
    var r = kayitlar(), n = cozulenSayisi();
    if (n < KARNE_ESIK) {
      kok.innerHTML = '<div class="kart kilit-ekran"><span class="etiket">Kilitli</span><h2 style="font-size:30px">Karnen ' + (KARNE_ESIK - n) + ' test sonra açılacak</h2>' +
        '<div class="cubuk" style="max-width:360px;margin:20px auto"><i style="width:' + (n / KARNE_ESIK * 100) + '%"></i></div><p>' + n + ' / ' + KARNE_ESIK + ' test çözdün.</p>' +
        '<p style="margin-top:22px"><a class="btn" href="/testler/">Testlere dön</a></p></div>';
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
    var msg = 'Aşkonomi karnem açıldı: ' + liste.length + ' test, en çok çıkan bölümüm “' + (V.bolum[ilk[0]] || '') + '”. Seninki ne?';
    kok.innerHTML = '<div class="kart sonuc"><span class="bolumno">' + liste.length + ' test</span><h2>Aşkonomi Karnen</h2>' +
      '<p>Kitapta seni en çok bekleyen bölümler:</p><ol>' + ilk.map(function (b) { return '<li><b>' + bolumAd(b) + '</b></li>'; }).join('') + '</ol>' +
      '<div class="karne-liste">' + liste.map(function (t) { return '<div><small>' + esc(t.ad) + '</small><b>' + esc(r[t.slug].ad) + '</b></div>'; }).join('') + '</div>' +
      '<div class="paylas"><a class="wa" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent(msg + ' ' + SITE + '/testler/?utm_source=whatsapp') + '">WhatsApp</a><a target="_blank" rel="noopener" href="https://x.com/intent/tweet?via=askonomikitap&text=' + encodeURIComponent(msg + ' ' + SITE + '/testler/?utm_source=x') + '">X</a></div>' +
      '<p class="not">Karnen her yeni testle güncellenir. Kayıtlar yalnızca bu tarayıcıda tutulur.</p>' + aboneHTML() + altBaglar() + '</div>';
    iz('karne-goruldu', { test: liste.length });
  }

  // ================= SONUÇ PAYLAŞIM SAYFASI =================
  function sonucSayfasi(slug) {
    var t = testBul(slug), r = kayitlar(), el = $('#kendi');
    if (el && t && r[slug]) el.innerHTML = 'Senin sonucun: <b>' + esc(r[slug].ad) + '</b>';
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
