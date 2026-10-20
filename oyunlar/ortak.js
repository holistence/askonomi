/* Aşkonomi Oyunları — ortak yardımcılar, çizimler ve paylaşım kartı */
(function () {
  'use strict';
  var R = { bordo: '#B3263A', petrol: '#1E6B70', altin: '#C99A2E', murekkep: '#262028', soluk: '#6b6070', zemin: '#F2EBE0', kagit: '#fffaf2', cizgi: '#d8ccbb' };
  var SITE = 'https://askonomi.com';

  // ---- tek çizgili vektör çizimler (viewBox 0 0 320 180) ----
  var C = {
    guven: '<svg viewBox="0 0 320 180" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round">' +
      '<circle cx="64" cy="70" r="20" stroke="#B3263A" stroke-width="4"/><path d="M30 140q34-44 68 0" stroke="#B3263A" stroke-width="4"/>' +
      '<circle cx="256" cy="70" r="20" stroke="#1E6B70" stroke-width="4"/><path d="M222 140q34-44 68 0" stroke="#1E6B70" stroke-width="4"/>' +
      '<path d="M96 58q64-54 128 0" stroke="#C99A2E" stroke-width="3" stroke-dasharray="2 9"/><path d="M224 104q-64 40-128 0" stroke="#1E6B70" stroke-width="3" stroke-dasharray="2 9"/></g>' +
      '<g fill="#C99A2E" stroke="#a87f1f" stroke-width="2"><circle cx="128" cy="38" r="7"/><circle cx="160" cy="31" r="10"/><circle cx="194" cy="38" r="13"/></g>' +
      '<path d="M160 150c-9-6-14-10-14-16c0-4 3-7 7-7c3 0 5 2 7 4c2-2 4-4 7-4c4 0 7 3 7 7c0 6-5 10-14 16z" fill="#B3263A"/></svg>',
    eslesme: '<svg viewBox="0 0 320 180" aria-hidden="true"><g stroke-linecap="round" fill="none" stroke-width="3">' +
      '<path d="M84 36C160 36 160 104 236 104" stroke="#d8ccbb"/><path d="M84 70C160 70 160 36 236 36" stroke="#d8ccbb"/><path d="M84 104C160 104 160 138 236 138" stroke="#d8ccbb"/>' +
      '<path d="M84 138C130 138 140 100 160 84c14-12 34-14 34-30c0-12-10-18-18-18c-8 0-14 6-16 12c-2-6-8-12-16-12c-8 0-18 6-18 18c0 16 20 18 34 30c20 16 30 54 76 54" stroke="#B3263A" stroke-width="4.5"/></g>' +
      '<g fill="#B3263A"><circle cx="72" cy="36" r="10"/><circle cx="72" cy="70" r="10"/><circle cx="72" cy="104" r="10"/><circle cx="72" cy="138" r="10" stroke="#262028" stroke-width="3"/></g>' +
      '<g fill="#1E6B70"><circle cx="248" cy="36" r="10"/><circle cx="248" cy="70" r="10"/><circle cx="248" cy="104" r="10"/><circle cx="248" cy="138" r="10"/></g></svg>',
    beklenti: '<svg viewBox="0 0 320 180" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M40 150h160" stroke="#b9ad9c" stroke-width="2"/>' +
      '<g stroke-width="14"><path d="M58 150v-26" stroke="#1E6B70"/><path d="M86 150v-40" stroke="#1E6B70"/><path d="M114 150v-22" stroke="#1E6B70"/><path d="M142 150v-34" stroke="#1E6B70"/><path d="M170 150v-18" stroke="#1E6B70"/></g>' +
      '<g stroke="#B3263A" stroke-width="3" stroke-dasharray="1 7"><path d="M51 118h14M79 86h14M107 112h14M135 92h14M163 104h14"/></g>' +
      '<path d="M200 150c20-30 30-50 44-68" stroke="#262028" stroke-width="2"/>' +
      '<ellipse cx="252" cy="54" rx="40" ry="46" fill="#B3263A" stroke="#8f1c2d" stroke-width="3"/><path d="M246 99l6 8l6-8" fill="#8f1c2d"/>' +
      '<path d="M236 36q8-12 20-12" stroke="#fff" stroke-opacity=".6" stroke-width="5"/></g>' +
      '<text x="252" y="62" text-anchor="middle" font-family="Fraunces,Georgia,serif" font-weight="600" font-size="22" fill="#fff">%170</text></svg>',
    kaydirma: '<svg viewBox="0 0 320 180" aria-hidden="true"><g stroke-linejoin="round">' +
      '<g transform="rotate(-14 120 96)"><rect x="80" y="30" width="80" height="120" rx="8" fill="#fbf5ea" stroke="#d8ccbb" stroke-width="2"/><circle cx="120" cy="72" r="20" fill="#e9c6a8"/></g>' +
      '<g transform="rotate(10 200 96)"><rect x="160" y="30" width="80" height="120" rx="8" fill="#fbf5ea" stroke="#d8ccbb" stroke-width="2"/><circle cx="200" cy="72" r="20" fill="#c9a07e"/></g>' +
      '<rect x="120" y="22" width="80" height="124" rx="8" fill="#fffaf2" stroke="#262028" stroke-width="2.5"/><circle cx="160" cy="64" r="22" fill="#B3263A"/><path d="M138 104h44M138 116h30M138 128h38" stroke="#d8ccbb" stroke-width="5" stroke-linecap="round"/></g>' +
      '<g fill="none" stroke-linecap="round" stroke-width="4"><path d="M56 160h-26m10-9l-10 9l10 9" stroke="#1E6B70"/><path d="M264 160h26m-10-9l10 9l-10 9" stroke="#B3263A"/></g>' +
      '<g fill="#C99A2E"><circle cx="232" cy="28" r="3"/><circle cx="246" cy="40" r="2"/><circle cx="84" cy="26" r="2.5"/></g></svg>',
    harita: '<svg viewBox="0 0 320 180" aria-hidden="true"><path d="M25.3 60.2L29.7 56.3L29.7 50.5L34.2 48.4L33.6 43.6L30.3 41.5L30.4 39.2L32.9 39.0L34.0 36.4L43.2 33.9L47.4 37.6L54.6 36.2L55.0 38.2L53.7 38.8L56.2 44.1L65.5 49.5L81.4 52.7L87.2 51.2L97.6 54.0L102.8 52.8L103.8 49.3L121.0 39.3L132.1 35.5L153.3 36.8L155.6 34.0L159.2 35.1L157.7 37.5L160.5 41.5L164.6 43.1L171.8 42.1L172.9 46.5L176.8 50.5L180.6 48.0L193.4 55.0L195.5 52.8L198.5 55.7L205.4 57.1L220.9 53.3L232.7 56.8L245.0 51.2L252.0 45.2L256.0 46.9L258.0 45.2L265.9 46.9L267.4 44.1L270.8 44.1L270.5 45.9L276.2 49.6L276.7 51.9L279.6 52.0L280.1 54.8L283.1 56.8L284.2 61.6L281.4 65.6L283.6 71.5L282.9 72.6L286.5 74.3L292.0 73.7L299.7 80.8L296.7 79.0L295.1 80.5L294.0 85.8L288.6 86.7L292.4 96.7L292.5 104.9L295.3 106.1L291.4 114.3L296.7 116.8L296.8 122.4L300.0 125.6L299.6 127.9L297.1 127.3L292.5 131.3L290.8 128.9L291.9 126.3L289.9 124.9L282.9 126.4L270.3 123.7L267.2 128.0L263.9 128.6L263.7 126.3L261.5 125.3L252.2 129.1L240.8 128.5L227.1 135.1L218.1 136.8L210.9 136.0L208.4 133.6L203.1 132.4L192.7 137.2L186.9 137.5L186.1 135.5L181.1 133.6L179.1 139.9L181.3 144.3L176.9 145.0L176.5 148.8L174.0 149.8L173.4 152.1L169.8 150.0L170.6 148.3L167.8 143.4L173.9 137.8L173.9 134.5L171.3 132.0L166.0 135.0L166.9 135.9L164.6 138.6L161.3 139.1L151.3 134.2L145.8 138.2L141.2 144.6L139.8 143.2L137.2 146.4L129.3 146.3L124.3 148.5L116.9 144.6L112.9 139.1L102.7 134.1L93.5 132.8L91.7 134.5L91.1 142.8L89.3 145.6L89.1 144.0L86.3 143.1L77.9 146.9L70.2 141.8L70.5 139.1L68.8 139.0L68.4 135.7L66.5 138.2L65.6 136.4L63.1 136.1L62.7 134.0L60.5 133.6L54.6 138.8L53.5 137.9L54.8 137.6L54.1 135.0L50.2 135.0L49.4 136.9L44.8 136.4L48.9 134.1L54.6 134.5L54.4 132.0L57.1 130.3L42.4 130.8L43.2 128.2L47.2 127.4L44.9 123.9L42.3 124.2L41.5 119.2L39.5 118.7L42.9 117.3L43.2 112.7L39.3 110.9L37.8 111.9L35.9 108.3L33.5 110.3L27.9 106.8L29.0 105.2L31.4 105.7L31.4 103.5L30.6 104.4L29.4 104.5L30.7 103.7L31.0 99.6L34.0 102.4L34.3 105.3L35.1 102.1L36.6 105.5L38.7 104.8L35.2 98.9L37.9 98.4L40.0 95.6L36.7 95.1L37.7 91.8L33.3 88.4L33.2 86.3L36.5 86.3L38.4 82.6L25.8 84.6L27.5 74.8L30.2 72.9L27.4 73.8L29.0 70.5L28.1 68.5L36.2 64.1L36.8 62.3L26.7 63.3L25.3 60.2ZM20.0 72.3L24.1 70.0L25.1 71.5L21.1 72.9L20.0 72.3ZM47.2 63.2L48.8 61.8L50.4 62.5L48.4 63.6L47.2 63.2Z" fill="#fbf5ea" stroke="#262028" stroke-width="2" stroke-linejoin="round"/>' +
      '<g fill="#B3263A" opacity=".85"><circle cx="41.5" cy="104.4" r="9"/><circle cx="93.5" cy="132.5" r="8.5"/><circle cx="30.7" cy="71.8" r="7"/><circle cx="125" cy="76" r="6.5"/><circle cx="175.8" cy="49.8" r="5.5"/><circle cx="119.5" cy="114.6" r="5"/></g>' +
      '<g fill="#1E6B70" opacity=".85"><circle cx="191.1" cy="129.4" r="3.5"/><circle cx="278.8" cy="102.9" r="2.5"/><circle cx="284" cy="120" r="2"/><circle cx="225.3" cy="55.4" r="3.5"/></g>' +
      '<path d="M30.7 66c-9-6-13-10-13-15c0-4 3-7 7-7c3 0 5 2 6 4c1-2 3-4 6-4c4 0 7 3 7 7c0 5-4 9-13 15z" transform="translate(0 -12)" fill="#B3263A"/><path d="M30.7 54v17" stroke="#B3263A" stroke-width="2.5"/></svg>',
    grafik: '<svg viewBox="0 0 320 180" aria-hidden="true"><path d="M40 20v134h250" fill="none" stroke="#b9ad9c" stroke-width="2"/>' +
      '<path d="M52 140l22 2l20-14l18 4l22-12l20 2l22-8l18 0l14-4c-30-26-52-40-52-62c0-14 11-24 24-24c10 0 18 6 22 14c4-8 12-14 22-14c13 0 24 10 24 24c0 22-22 36-52 62l14 8l16-10l14 8l16-10l14 12l10-28l14 10l14-50" fill="none" stroke="#B3263A" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/></svg>'
  };

  var OYUNLAR = [
    { slug: 'guven', ad: 'Güven oyunu', kisa: 'Bir partnerle on tur. Yatırdığın her jeton üçe katlanır, peki geri gelir mi?', sure: '3 dk', bolum: 'Bölüm 24 · Güven Sermayesi', cizim: 'guven' },
    { slug: 'eslesme', ad: 'Eşleşme köyü', kisa: 'Sekiz kişilik bir köyü eşleştir. Kimin teklif ettiği, kimin kiminle kalacağını nasıl değiştiriyor?', sure: '4 dk', bolum: 'Bölüm 05 · Aşk Piyasası', cizim: 'eslesme' },
    { slug: 'beklenti', ad: 'Beklenti bütçesi', kisa: 'Önce hayalindeki partnerden ne beklediğini işaretle, sonra bir insanın gerçek kapasitesiyle karşılaştır.', sure: '2 dk', bolum: 'Bölüm 28 · Beklenti Enflasyonu', cizim: 'beklenti' },
    { slug: 'kaydirma', ad: 'Kaydırma simülatörü', kisa: 'Otuz profil kaydır. Sonunda dikkatinin nasıl eridiğini kendi verinle gör.', sure: '3 dk', bolum: 'Bölüm 30 · Tinder’dan Önce ve Sonra', cizim: 'kaydirma' },
    { slug: 'harita', ad: 'Türkiye’nin aşk haritası', kisa: 'Hangi ilde insanlar daha erken evleniyor, nerede boşanma daha sık? İlini bul.', sure: '2 dk', bolum: 'Bölüm 22 ve 29', cizim: 'harita' },
    { slug: '../grafik', ad: 'Aşkının grafiği', kisa: 'Kapaktaki değer–zaman eğrisini kendi ilişkin için çiz, piyasa yorumunu al.', sure: '1 dk', bolum: 'Bölüm 24–28', cizim: 'grafik' }
  ];

  function iz(n, d) { try { if (window.umami) umami.track(n, d); } catch (e) {} }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function karistir(a, rnd) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor((rnd || Math.random)() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

  function kartHTML(o, genis, tam) {
    var href = o.slug.indexOf('..') === 0 ? '/grafik/' : '/oyunlar/' + o.slug + '/';
    return '<a class="oy-kart' + (genis ? ' genis' : '') + (tam ? ' tam' : '') + '" href="' + href + '"><div class="resim">' + C[o.cizim] + '</div><div class="yazi"><h2>' + esc(o.ad) + '</h2><p>' + esc(o.kisa) + '</p><div class="kunye"><span><b>' + o.sure + '</b></span><span>' + esc(o.bolum) + '</span></div></div></a>';
  }
  function digerleri(slug, n) {
    var l = OYUNLAR.filter(function (o) { return o.slug !== slug; }).slice(0, n || 3);
    return '<section class="oy-diger"><h2>Başka bir oyun</h2><div class="oy-liste">' + l.map(function (o) { return kartHTML(o); }).join('') + '</div></section>';
  }

  // ---- paylaşım kartı 1080×1350 ----
  function kart(o, cb) {
    var c = document.createElement('canvas'); c.width = 1080; c.height = 1350;
    var x = c.getContext('2d');
    (document.fonts ? document.fonts.ready : Promise.resolve()).then(function () {
      x.fillStyle = R.zemin; x.fillRect(0, 0, 1080, 1350);
      x.strokeStyle = R.cizgi; x.lineWidth = 3; x.strokeRect(36, 36, 1008, 1278);
      x.textAlign = 'center'; x.fillStyle = R.murekkep;
      x.font = '600 30px Fraunces, Georgia, serif'; x.fillText('A Ş K O N O M İ   O Y U N L A R I', 540, 120);
      x.font = 'italic 400 54px Fraunces, Georgia, serif'; x.fillStyle = R.bordo; x.fillText(o.oyun, 540, 210);
      x.save(); o.ciz(x, 110, 270, 860, 640); x.restore();
      x.textAlign = 'center'; x.fillStyle = R.soluk; x.font = 'italic 400 38px "Crimson Pro", Georgia, serif'; x.fillText(o.ust || 'Sonucum', 540, 1000);
      var b = o.baslik, fs = 84; x.font = '600 ' + fs + 'px Fraunces, Georgia, serif';
      while (x.measureText(b).width > 940 && fs > 48) { fs -= 4; x.font = '600 ' + fs + 'px Fraunces, Georgia, serif'; }
      x.fillStyle = R.murekkep; x.fillText(b, 540, 1090);
      if (o.alt) { x.font = '400 40px "Crimson Pro", Georgia, serif'; x.fillStyle = R.murekkep; x.fillText(o.alt, 540, 1160); }
      x.fillStyle = R.bordo; x.font = '500 36px Fraunces, Georgia, serif'; x.fillText('Seninki ne?  askonomi.com/oyunlar', 540, 1262);
      c.toBlob(cb, 'image/png');
    });
  }
  function paylasHTML(id) {
    return '<div class="paylas"><button data-k="indir">Görseli indir</button>' + (navigator.canShare ? '<button data-k="paylas">Görseli paylaş</button>' : '') +
      '<a class="wa" data-k="wa" target="_blank" rel="noopener" href="#">WhatsApp</a><a data-k="x" target="_blank" rel="noopener" href="#">X</a><button data-k="kopya">Bağlantıyı kopyala</button></div>';
  }
  // o: {kok, slug, mesaj, url, kartAyar}
  function paylasBagla(kok, o) {
    var url = o.url || (SITE + '/oyunlar/' + o.slug + '/');
    var m = o.mesaj + ' ' + url;
    var wa = kok.querySelector('[data-k="wa"]'); if (wa) wa.href = 'https://wa.me/?text=' + encodeURIComponent(m + (url.indexOf('?') > -1 ? '&' : '?') + 'utm_source=whatsapp');
    var xx = kok.querySelector('[data-k="x"]'); if (xx) xx.href = 'https://x.com/intent/tweet?via=askonomikitap&text=' + encodeURIComponent(m + (url.indexOf('?') > -1 ? '&' : '?') + 'utm_source=x');
    function indir(b) { var a = document.createElement('a'); a.href = URL.createObjectURL(b); a.download = 'askonomi-' + o.slug + '.png'; document.body.appendChild(a); a.click(); a.remove(); }
    var i = kok.querySelector('[data-k="indir"]'); if (i) i.onclick = function () { kart(o.kartAyar, indir); iz('oyun-gorsel', { oyun: o.slug }); };
    var p = kok.querySelector('[data-k="paylas"]'); if (p) p.onclick = function () {
      kart(o.kartAyar, function (b) {
        var f = new File([b], 'askonomi-' + o.slug + '.png', { type: 'image/png' });
        if (navigator.canShare && navigator.canShare({ files: [f] })) navigator.share({ files: [f], text: m }).catch(function () {}); else indir(b);
      });
      iz('oyun-paylas', { oyun: o.slug });
    };
    var k = kok.querySelector('[data-k="kopya"]'); if (k) k.onclick = function () { try { navigator.clipboard.writeText(url); k.textContent = 'Kopyalandı'; } catch (e) { prompt('Bağlantı:', url); } };
  }
  function abone() {
    return '<div class="abone-kutu"><p>Bu oyunun arkasındaki fikir kitapta. Aşkonomi çıktığında ilk duymak için:</p><a class="btn abone-git" href="/#takip">E-posta listesine katıl</a></div>';
  }

  window.OYUN = { R: R, C: C, OYUNLAR: OYUNLAR, iz: iz, esc: esc, karistir: karistir, kartHTML: kartHTML, digerleri: digerleri, kart: kart, paylasHTML: paylasHTML, paylasBagla: paylasBagla, abone: abone, SITE: SITE };

  // merkez sayfa
  var liste = document.getElementById('oyListe');
  if (liste) liste.innerHTML = OYUNLAR.map(function (o, i) { return kartHTML(o, i === 0, i === OYUNLAR.length - 1); }).join('');
  var dg = document.getElementById('oyDiger');
  if (dg) dg.outerHTML = digerleri(dg.dataset.slug, 3);
})();
