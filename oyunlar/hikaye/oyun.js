/* Türkiye’nin aile hikâyesi — altı sahnelik, kendiliğinden akan harita */
(function () {
  'use strict';
  var O = window.OYUN, R = O.R, G = window.HARITA, H = window.HIKAYE, NS = 'http://www.w3.org/2000/svg';
  var kok = document.getElementById('oyun');
  if (!G || !H) { kok.textContent = 'Veri yüklenemedi.'; return; }
  var IL = {}; G.iller.forEach(function (i) { IL[i.p] = i; });
  function v1(x, d) { return x.toFixed(d).replace('.', ','); }
  function trAd(n) { return n.toLocaleString('tr-TR'); }
  // Türkçe ekler: sayı ya da kelimenin okunuşuna göre ünlü uyumu ve sertleşme
  var BIR = ['sıfır', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz'], ON = ['', 'on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan'];
  function okunus(x) {
    if (typeof x === 'string') { var m = x.match(/(\d+)(?:,(\d+))?$/); if (!m) return x.toLocaleLowerCase('tr'); x = m[2] ? +m[2] : +m[1]; }
    x = Math.round(Math.abs(x));
    if (x % 10) return BIR[x % 10]; if (x % 100) return ON[(x % 100) / 10]; if (x % 1000) return 'yüz'; return x ? 'bin' : 'sıfır';
  }
  function ilde(n) { return n === 81 ? '81 ilin hepsinde' : '81 ilin ' + ek(n, 'inde'); }
  function ek(sozcuk, tur) {
    var w = okunus(sozcuk), un = (w.match(/[aeıioöuü](?=[^aeıioöuü]*$)/) || ['e'])[0], son = w.slice(-1);
    var ince = 'eiöü'.indexOf(un) > -1, iki = ince ? 'e' : 'a', dort = { a: 'ı', ı: 'ı', o: 'u', u: 'u', e: 'i', i: 'i', ö: 'ü', ü: 'ü' }[un];
    var unlu = 'aeıioöuü'.indexOf(son) > -1, sert = 'fstkçşhp'.indexOf(son) > -1, d = sert ? 't' : 'd';
    var e = { de: d + iki, den: d + iki + 'n', e: (unlu ? 'y' : '') + iki, inde: (unlu ? 's' : '') + dort + 'nd' + iki, i: (unlu ? 'y' : '') + dort }[tur];
    return sozcuk + '’' + e;
  }

  var SAHNE = [
    { k: 'hane', baslik: 'Haneler küçülüyor', birim: 'bir hanede ortalama kişi', d: 2, ek: ' kişi', trAd: 'Türkiye',
      renk: ['#e3ece0', '#b6cfad', '#7fa874', '#4e7b45', '#28481f'], bolum: 'Bölüm 29 · Modern Evlilik',
      metin: function (s) { return ek(s.ilk, 'de') + ' Türkiye’de bir hanede ortalama ' + v1(s.a, 2) + ' kişi yaşıyordu. ' + ek(s.son, 'de') + ' bu sayı ' + v1(s.b, 2) + '. ' + ilde(s.azalan) + ' haneler küçüldü. En hızlı küçülen il ' + s.enAz.il + ' oldu (' + v1(s.enAz.a, 2) + ' → ' + v1(s.enAz.b, 2) + ').'; } },
    { k: 'ilkK', baslik: 'Daha geç evleniyoruz', birim: 'kadınlarda ortalama ilk evlenme yaşı', d: 1, ek: ' yaş', trAd: 'Türkiye',
      renk: ['#f6e3e6', '#e8b3bd', '#d07a8b', '#a84a61', '#6b2238'], bolum: 'Bölüm 29 · Modern Evlilik',
      metin: function (s) { return 'Kadınlar ' + ek(s.ilk, 'de') + ' ortalama ' + v1(s.a, 1) + ' yaşında ilk kez evleniyordu. ' + ek(s.son, 'de') + ' ' + v1(s.b, 1) + ' yaşında. Yaklaşık ' + v1(s.b - s.a, 1) + ' yıllık bir erteleme. ' + ilde(s.artan) + ' ilk evlenme yaşı yükseldi.'; } },
    { k: 'ev', baslik: 'Daha az evleniyoruz', birim: 'bin kişide evlenme', d: 2, ek: '‰', trAd: 'Türkiye',
      renk: ['#f4e6c8', '#e3c27a', '#c99a2e', '#9a7116', '#5f4509'], bolum: 'Bölüm 15 · Evliliğin Ekonomisi',
      metin: function (s) { return ek(s.ilk, 'de') + ' bin kişiye ' + v1(s.a, 2) + ' evlilik düşüyordu. ' + ek(s.son, 'de') + ' ' + v1(s.b, 2) + '. En derin çukur ' + s.dipYil + ' (' + v1(s.dip, 2) + '), salgının ilk yılı. ' + ilde(s.azalan) + ' evlenme hızı düştü.'; } },
    { k: 'bos', baslik: 'Daha çok boşanıyoruz', birim: 'bin kişide boşanma', d: 2, ek: '‰', trAd: 'Türkiye',
      renk: ['#f3dde0', '#e2a5ad', '#c9586a', '#a3283c', '#651423'], bolum: 'Bölüm 22 · Boşanmanın Ekonomisi',
      metin: function (s) { return 'Boşanma hızı ' + ek(s.ilk, 'de') + ' binde ' + v1(s.a, 2) + ' idi, ' + ek(s.son, 'de') + ' binde ' + v1(s.b, 2) + '. ' + ilde(s.artan) + ' boşanma hızı arttı. En hızlı artış ' + ek(s.enCok.il, 'de') + ' (' + v1(s.enCok.a, 2) + ' → ' + v1(s.enCok.b, 2) + ').'; } },
    { k: 'tdh', baslik: 'Daha az çocuk', birim: 'kadın başına ortalama çocuk', d: 2, ek: ' çocuk', trAd: '81 ilin medyanı',
      renk: ['#e6e1ef', '#bfb1d8', '#8f78b8', '#634892', '#3a2560'], bolum: 'Bölüm 17 · Çocukların Ekonomisi',
      metin: function (s) { return ek(s.ilk, 'de') + ' illerin ortanca değeri kadın başına ' + v1(s.a, 2) + ' çocuktu, ' + ek(s.son, 'de') + ' ' + v1(s.b, 2) + '. Nüfusun kendini yenilemesi için gereken 2,1’in altında kalan il sayısı ' + ek(s.alt21a, 'den') + ' ' + ek(s.alt21b, 'e') + ' çıktı. (2023 ve 2024 için il verisi elimizde yok.)'; } },
    { k: 'yasli', baslik: 'Yaşlanıyoruz', birim: '65 yaş ve üstü nüfusun payı (%)', d: 1, ek: '%', trAd: 'Türkiye',
      renk: ['#eceae4', '#cfc8b8', '#a89c84', '#7a6d55', '#4a412f'], bolum: 'Bölüm 33 · Yalnızlığın Ekonomisi',
      metin: function (s) { return ek(s.ilk, 'de') + ' nüfusun ' + ek('%' + v1(s.a, 1), 'i') + ' 65 yaşın üstündeydi. ' + ek(s.son, 'de') + ' %' + v1(s.b, 1) + '. ' + ilde(s.artan) + ' nüfus yaşlandı. En yaşlı il ' + s.enYuksek.il + ' (%' + v1(s.enYuksek.b, 1) + ').'; } }
  ];
  // sahne istatistikleri (veriden hesaplanır)
  SAHNE.forEach(function (S) {
    var yl = H.yillar[S.k], tr = H.tr[S.k], n = yl.length;
    var ilkJ = 0, sonJ = n - 1;
    var ozet = H.iller.map(function (i) { var a = i[S.k][ilkJ], b = i[S.k][sonJ]; return { il: IL[i.p].il, p: i.p, a: a, b: b, d: b - a }; });
    var hepsi = []; H.iller.forEach(function (i) { i[S.k].forEach(function (x) { if (x !== null) hepsi.push(x); }); }); hepsi.sort(function (a, b) { return a - b; });
    S.sinif = [0.2, 0.4, 0.6, 0.8].map(function (q) { return hepsi[Math.floor(q * (hepsi.length - 1))]; }); S.min = hepsi[0]; S.max = hepsi[hepsi.length - 1];
    var dip = Infinity, dipYil = null; tr.forEach(function (x, j) { if (x !== null && x < dip) { dip = x; dipYil = yl[j]; } });
    var sirali = ozet.slice().sort(function (a, b) { return a.d - b.d; });
    S.ist = { ilk: yl[ilkJ], son: yl[sonJ], a: tr[ilkJ], b: tr[sonJ], artan: ozet.filter(function (x) { return x.d > 0; }).length, azalan: ozet.filter(function (x) { return x.d < 0; }).length,
      enAz: sirali[0], enCok: sirali[sirali.length - 1], dip: dip, dipYil: dipYil,
      enYuksek: ozet.slice().sort(function (a, b) { return b.b - a.b; })[0],
      alt21a: ozet.filter(function (x) { return x.a < 2.1; }).length, alt21b: ozet.filter(function (x) { return x.b < 2.1; }).length };
  });

  // ---------- iskelet ----------
  kok.innerHTML =
    '<div class="hk-sahne" id="hkSahne">' +
    '<div class="hk-ust"><div><p class="hk-no" id="hkNo"></p><h2 class="hk-baslik" id="hkBaslik"></h2></div><div class="hk-yil" id="hkYil" aria-live="off"></div></div>' +
    '<div class="hk-govde"><div class="hk-harita"><svg id="hkSvg" viewBox="' + G.viewBox + '" role="img" aria-label="Türkiye il haritası"><g id="hkIller"></g></svg>' +
    '<div class="hk-lejant" id="hkLejant"></div></div>' +
    '<div class="hk-yan"><svg id="hkGrafik" class="hk-grafik" viewBox="0 0 360 230" role="img" aria-label="Türkiye eğrisi"></svg><p class="hk-metin" id="hkMetin" aria-live="polite"></p><p class="hk-bolum" id="hkBolum"></p></div></div>' +
    '<div class="hk-ilerleme" id="hkIlerleme">' + SAHNE.map(function (S, j) { return '<button data-j="' + j + '" aria-label="' + (j + 1) + '. sahne: ' + S.baslik + '"><i></i><span>' + S.baslik + '</span></button>'; }).join('') + '</div>' +
    '<div class="hk-kontrol"><button class="hk-k" id="hkGeri" aria-label="Önceki sahne"><svg viewBox="0 0 24 24"><path d="M6 5h2v14H6zM20 5L9 12l11 7z"/></svg></button>' +
    '<button class="hk-k hk-oyna" id="hkOyna" aria-label="Oynat"></button>' +
    '<button class="hk-k" id="hkIleri" aria-label="Sonraki sahne"><svg viewBox="0 0 24 24"><path d="M16 5h2v14h-2zM4 5l11 7L4 19z"/></svg></button></div>' +
    '<div class="hk-perde" id="hkPerde"><div><p class="hk-no">Altı sahne · yaklaşık bir buçuk dakika</p><h2>Türkiye’nin aile hikâyesi</h2><p>2008’den 2025’e, 81 ilin haritası yıl yıl değişiyor: haneler, evlilikler, boşanmalar, çocuklar ve yaşlanma. Bütün sayılar TÜİK’ten.</p><button class="oy-btn" id="hkBasla">Hikâyeyi başlat</button></div></div>' +
    '</div><div id="hkSon"></div>' +
    '<p class="oy-not hk-kaynak">Kaynak: TÜİK Evlenme ve Boşanma İstatistikleri (il tabloları, 2012–2025), il ve cinsiyete göre ortalama ilk evlenme yaşı (2010–2025), Adrese Dayalı Nüfus Kayıt Sistemi (il nüfusu, hane büyüklüğü 2008–2025, yaşlı nüfus payı 2009–2024), doğurganlık 2011–2022 (araştırma arşivi) ve 2025 (TÜİK Doğum İstatistikleri, ikincil kaynak üzerinden). Kaba hızlar yıl ortası nüfusla hesaplandı. Harita sınırları: alpers/Turkey-Maps-GeoJSON, Apache 2.0.</p>';
  var gEl = document.getElementById('hkIller'), yol = {};
  G.iller.forEach(function (i) { var p = document.createElementNS(NS, 'path'); p.setAttribute('d', i.d); p.setAttribute('class', 'hk-il'); gEl.appendChild(p); yol[i.p] = p; });
  var OY = '<svg viewBox="0 0 24 24"><path d="M7 5l12 7l-12 7z"/></svg>', DU = '<svg viewBox="0 0 24 24"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z"/></svg>';
  var az = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var sj = 0, yj = 0, oynuyor = false, zam = null, ADIM = 780, BEKLE = 4200;

  function renk(S, x) { if (x === null || x === undefined) return '#ece6dc'; var k = 0; S.sinif.forEach(function (e) { if (x > e) k++; }); return S.renk[k]; }
  function f(S, x) { return x === null ? '—' : v1(x, S.d); }
  function sahneKur() {
    var S = SAHNE[sj], yl = H.yillar[S.k];
    document.getElementById('hkNo').textContent = (sj + 1) + ' / ' + SAHNE.length + ' · ' + yl[0] + '–' + yl[yl.length - 1];
    document.getElementById('hkBaslik').textContent = S.baslik;
    document.getElementById('hkBolum').textContent = 'Kitapta: ' + S.bolum;
    var sinir = [S.min].concat(S.sinif).concat([S.max]);
    document.getElementById('hkLejant').innerHTML = '<span>' + S.birim + '</span><div>' + S.renk.map(function (c, k) { return '<i style="background:' + c + '"><em>' + f(S, sinir[k]) + '</em></i>'; }).join('') + '<em class="son">' + f(S, S.max) + '</em></div>';
    document.getElementById('hkMetin').textContent = '';
    document.querySelectorAll('#hkIlerleme button').forEach(function (b, j) { b.classList.toggle('gecti', j < sj); b.classList.toggle('simdi', j === sj); b.querySelector('i').style.width = j < sj ? '100%' : '0%'; });
    yj = 0; kare();
  }
  function kare() {
    var S = SAHNE[sj], yl = H.yillar[S.k], tr = H.tr[S.k];
    var yilEl = document.getElementById('hkYil'); yilEl.textContent = yl[yj];
    if (!az) yilEl.animate([{ opacity: .3, transform: 'translateY(6px)' }, { opacity: 1, transform: 'none' }], { duration: 300 });
    H.iller.forEach(function (i) { yol[i.p].style.fill = renk(S, i[S.k][yj]); });
    grafik(S, yl, tr);
    var b = document.querySelector('#hkIlerleme button.simdi i'); if (b) b.style.width = (yj / (yl.length - 1) * 100) + '%';
    if (yj === yl.length - 1) document.getElementById('hkMetin').textContent = S.metin(S.ist);
  }
  function grafik(S, yl, tr) {
    var W = 360, Hh = 230, L = 46, Rr = 14, T0 = 30, B = 34, n = yl.length;
    var deg = tr.filter(function (x) { return x !== null; }), mn = Math.min.apply(null, deg), mx = Math.max.apply(null, deg), pay = (mx - mn) * .15 || 1; mn -= pay; mx += pay;
    var x = function (j) { return L + j * (W - L - Rr) / (n - 1); }, y = function (v) { return T0 + (1 - (v - mn) / (mx - mn)) * (Hh - T0 - B); };
    var hepsi = '', simdi = '', son = null;
    tr.forEach(function (v, j) {
      if (v === null) { son = null; return; }
      var seg = (son === null ? 'M' : 'L') + x(j).toFixed(1) + ' ' + y(v).toFixed(1);
      hepsi += seg; if (j <= yj) simdi += (son === null || son > yj ? 'M' : 'L') + x(j).toFixed(1) + ' ' + y(v).toFixed(1);
      son = j;
    });
    var bosluk = ''; tr.forEach(function (v, j) { if (v === null) bosluk += '<rect x="' + (x(j) - (W - L - Rr) / (n - 1) / 2) + '" y="' + T0 + '" width="' + (W - L - Rr) / (n - 1) + '" height="' + (Hh - T0 - B) + '" fill="url(#hkTarama)"/>'; });
    var cv = tr[yj];
    var g = '<defs><pattern id="hkTarama" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#d8ccbb" stroke-width="2"/></pattern></defs>' + bosluk +
      [mn + pay, (mn + mx) / 2, mx - pay].map(function (v) { return '<line x1="' + L + '" x2="' + (W - Rr) + '" y1="' + y(v) + '" y2="' + y(v) + '" stroke="#ece3d6"/><text x="' + (L - 6) + '" y="' + (y(v) + 4) + '" text-anchor="end" class="hk-eks">' + f(S, v) + '</text>'; }).join('') +
      '<text x="' + L + '" y="' + (Hh - 10) + '" class="hk-eks">' + yl[0] + '</text><text x="' + (W - Rr) + '" y="' + (Hh - 10) + '" text-anchor="end" class="hk-eks">' + yl[n - 1] + '</text>' +
      '<path d="' + hepsi + '" fill="none" stroke="#e6ddcf" stroke-width="3"/>' +
      '<path d="' + simdi + '" fill="none" stroke="' + S.renk[3] + '" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>' +
      (cv !== null ? '<circle cx="' + x(yj) + '" cy="' + y(cv) + '" r="6" fill="' + S.renk[3] + '" stroke="#fffaf2" stroke-width="2"/><text x="' + (x(yj) + (yj > n / 2 ? -10 : 10)) + '" y="' + (y(cv) - 12) + '" text-anchor="' + (yj > n / 2 ? 'end' : 'start') + '" class="hk-deger">' + f(S, cv) + S.ek + '</text>' : '<text x="' + x(yj) + '" y="' + (T0 + 16) + '" text-anchor="middle" class="hk-eks">veri yok</text>') +
      '<text x="' + L + '" y="16" class="hk-gb">' + S.trAd + '</text>';
    document.getElementById('hkGrafik').innerHTML = g;
  }
  function tik() {
    var S = SAHNE[sj], n = H.yillar[S.k].length;
    if (yj < n - 1) { yj++; kare(); zam = setTimeout(tik, ADIM); return; }
    zam = setTimeout(function () {
      if (sj < SAHNE.length - 1) { sj++; sahneKur(); zam = setTimeout(tik, ADIM * 1.4); }
      else { durdur(); final(); }
    }, BEKLE);
  }
  function oynat() { if (oynuyor) return; oynuyor = true; document.getElementById('hkOyna').innerHTML = DU; document.getElementById('hkOyna').setAttribute('aria-label', 'Durdur'); zam = setTimeout(tik, ADIM); }
  function durdur() { oynuyor = false; clearTimeout(zam); document.getElementById('hkOyna').innerHTML = OY; document.getElementById('hkOyna').setAttribute('aria-label', 'Oynat'); }
  function git(j, sona) { durdur(); sj = Math.max(0, Math.min(SAHNE.length - 1, j)); sahneKur(); if (sona) { yj = H.yillar[SAHNE[sj].k].length - 1; kare(); } }
  document.getElementById('hkOyna').innerHTML = OY;
  document.getElementById('hkOyna').onclick = function () { if (oynuyor) return durdur(); var n = H.yillar[SAHNE[sj].k].length; if (sj === SAHNE.length - 1 && yj === n - 1) git(0); oynat(); };
  document.getElementById('hkGeri').onclick = function () { git(sj - 1); oynat(); };
  document.getElementById('hkIleri').onclick = function () { if (sj === SAHNE.length - 1) { git(sj, true); final(); } else { git(sj + 1); oynat(); } };
  document.querySelectorAll('#hkIlerleme button').forEach(function (b) { b.onclick = function () { git(+b.dataset.j); oynat(); }; });
  document.getElementById('hkBasla').onclick = function () { git(0); document.getElementById('hkPerde').classList.add('kalk'); O.iz('oyun-basladi', { oyun: 'hikaye' }); setTimeout(function () { document.getElementById('hkPerde').hidden = true; }, 500); oynat(); };
  document.addEventListener('keydown', function (e) { if (e.target.tagName === 'INPUT') return; if (e.key === ' ' && document.getElementById('hkPerde').hidden) { e.preventDefault(); document.getElementById('hkOyna').click(); } if (e.key === 'ArrowRight') document.getElementById('hkIleri').click(); if (e.key === 'ArrowLeft') document.getElementById('hkGeri').click(); });

  // ---------- final ----------
  function final() {
    document.querySelectorAll('#hkIlerleme button').forEach(function (b) { b.classList.add('gecti'); b.classList.remove('simdi'); b.querySelector('i').style.width = '100%'; });
    O.iz('oyun-bitti', { oyun: 'hikaye' });
    var kartlar = SAHNE.map(function (S) {
      var s = S.ist, artis = s.b > s.a;
      return '<div class="hk-ozet"><small>' + S.baslik + '</small><div><span>' + s.ilk + '</span><b>' + f(S, s.a) + '</b></div><svg viewBox="0 0 40 12" aria-hidden="true"><path d="M2 6h32m-6-5l6 5l-6 5" fill="none" stroke="' + S.renk[3] + '" stroke-width="2"/></svg><div><span>' + s.son + '</span><b style="color:' + S.renk[3] + '">' + f(S, s.b) + '</b></div><em>' + S.birim + (S.trAd !== 'Türkiye' ? ' · ' + S.trAd : '') + '</em></div>';
    }).join('');
    var el = document.getElementById('hkSon');
    el.innerHTML = '<div class="oy-sahne hk-final"><p class="oy-adim">Hikâyenin özeti</p><h2 class="hk-f-b">2008’den 2025’e Türkiye’nin ailesi</h2><div class="hk-ozetler">' + kartlar + '</div>' +
      '<p>Haneler küçüldü, evlilik ertelendi ve azaldı, boşanma arttı, çocuk sayısı düştü, nüfus yaşlandı. Bu sayıların her biri milyonlarca kişisel kararın toplamı. Aşkonomi bu kararların arkasındaki iktisadı anlatıyor: Kimin, ne zaman, neden “evet” dediğini ve bunun bedelini.</p>' +
      '<div class="paylas"><button data-k="indir">Özet görselini indir</button>' + (navigator.canShare ? '<button data-k="paylas">Görseli paylaş</button>' : '') + '<a class="wa" data-k="wa" target="_blank" rel="noopener" href="#">WhatsApp</a><a data-k="x" target="_blank" rel="noopener" href="#">X</a><button data-k="kopya">Bağlantıyı kopyala</button></div>' +
      '<div class="oy-dugmeler"><a class="oy-btn" href="/oyunlar/harita/">Kendi ilini haritada bul</a><button class="oy-btn ikincil" id="hkTekrar">Hikâyeyi yeniden oynat</button></div>' + O.abone() + '</div>';
    O.paylasBagla(el, { slug: 'hikaye', mesaj: 'Türkiye’nin aile hikâyesi, 2008–2025: haneler küçüldü, evlilik ertelendi, boşanma arttı, çocuk sayısı düştü. TÜİK verisiyle akan harita:',
      kartAyar: { oyun: 'Türkiye’nin aile hikâyesi', ust: 'TÜİK verisiyle', baslik: '2008–2025: Türkiye’nin ailesi', alt: 'Haneler küçüldü, evlilik ertelendi, boşanma arttı', cagri: 'Akan haritayı izle:  askonomi.com/oyunlar/hikaye', ciz: kartCiz } });
    document.getElementById('hkTekrar').onclick = function () { el.innerHTML = ''; git(0); oynat(); kok.scrollIntoView({ behavior: 'smooth' }); };
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function kartCiz(x, X, Y, W, HH) {
    var sh = HH / 3, sw = W / 2;
    SAHNE.forEach(function (S, j) {
      var cx = X + (j % 2) * sw + 14, cy = Y + Math.floor(j / 2) * sh + 6, s = S.ist;
      x.fillStyle = '#fffaf2'; x.fillRect(cx, cy, sw - 28, sh - 16); x.strokeStyle = '#d8ccbb'; x.lineWidth = 2; x.strokeRect(cx, cy, sw - 28, sh - 16);
      x.textAlign = 'left'; x.fillStyle = R.soluk; x.font = '500 26px Fraunces, Georgia, serif'; x.fillText(S.baslik, cx + 18, cy + 40);
      x.fillStyle = R.murekkep; x.font = '600 46px Fraunces, Georgia, serif'; x.fillText(f(S, s.a), cx + 18, cy + 112);
      x.fillStyle = S.renk[3]; x.textAlign = 'right'; x.fillText(f(S, s.b), cx + sw - 46, cy + 112);
      x.fillStyle = R.soluk; x.font = 'italic 400 24px "Crimson Pro", Georgia, serif'; x.textAlign = 'left'; x.fillText(s.ilk, cx + 18, cy + 150); x.textAlign = 'right'; x.fillText(s.son, cx + sw - 46, cy + 150);
      x.strokeStyle = S.renk[3]; x.lineWidth = 4; x.beginPath(); var m = cx + (sw - 28) / 2; x.moveTo(m - 30, cy + 98); x.lineTo(m + 26, cy + 98); x.moveTo(m + 14, cy + 88); x.lineTo(m + 26, cy + 98); x.lineTo(m + 14, cy + 108); x.stroke();
    });
  }
  sahneKur(); yj = H.yillar[SAHNE[0].k].length - 1; kare(); document.getElementById('hkMetin').textContent = '';
  if (new URLSearchParams(location.search).get('s') === 'son') { document.getElementById('hkPerde').hidden = true; git(SAHNE.length - 1, true); final(); }
})();
