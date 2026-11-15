/* Türkiye's family story — a six-scene, self-playing map (English edition) */
(function () {
  'use strict';
  var O = window.OYUN, R = O.R, G = window.HARITA, H = window.HIKAYE, NS = 'http://www.w3.org/2000/svg';
  var kok = document.getElementById('oyun');
  if (!G || !H) { kok.textContent = 'Could not load the data.'; return; }
  var IL = {}; G.iller.forEach(function (i) { IL[i.p] = i; });
  function v1(x, d) { return x.toFixed(d); }
  function trAd(n) { return n.toLocaleString('en-GB'); }
  // English needs no suffix rules: "in 74 of 81 provinces" / "in all 81 provinces"
  function ilde(n) { return n === 81 ? 'in all 81 provinces' : 'in ' + n + ' of 81 provinces'; }

  var SAHNE = [
    { k: 'hane', baslik: 'Households are shrinking', birim: 'average people per household', d: 2, ek: ' people', trAd: 'Türkiye',
      renk: ['#e3ece0', '#b6cfad', '#7fa874', '#4e7b45', '#28481f'], bolum: 'Chapter 29 · Modern Marriage',
      metin: function (s) { return 'In ' + s.ilk + ', the average household in Türkiye had ' + v1(s.a, 2) + ' people. By ' + s.son + ', it was ' + v1(s.b, 2) + '. Households got smaller ' + ilde(s.azalan) + '. They shrank fastest in ' + s.enAz.il + ' (' + v1(s.enAz.a, 2) + ' → ' + v1(s.enAz.b, 2) + ').'; } },
    { k: 'ilkK', baslik: 'We marry later', birim: 'average age of women at first marriage', d: 1, ek: ' yrs', trAd: 'Türkiye',
      renk: ['#f6e3e6', '#e8b3bd', '#d07a8b', '#a84a61', '#6b2238'], bolum: 'Chapter 29 · Modern Marriage',
      metin: function (s) { return 'In ' + s.ilk + ', women first married at an average age of ' + v1(s.a, 1) + '. By ' + s.son + ', the average was ' + v1(s.b, 1) + '. That is a delay of about ' + v1(s.b - s.a, 1) + ' years. Age at first marriage went up ' + ilde(s.artan) + '.'; } },
    { k: 'ev', baslik: 'We marry less', birim: 'marriages per 1,000 people', d: 2, ek: '‰', trAd: 'Türkiye',
      renk: ['#f4e6c8', '#e3c27a', '#c99a2e', '#9a7116', '#5f4509'], bolum: 'Chapter 15 · The Economics of Marriage',
      metin: function (s) { return 'In ' + s.ilk + ', there were ' + v1(s.a, 2) + ' marriages per 1,000 people. By ' + s.son + ', there were ' + v1(s.b, 2) + '. The lowest point was ' + s.dipYil + ' (' + v1(s.dip, 2) + '), the first year of the pandemic. The marriage rate fell ' + ilde(s.azalan) + '.'; } },
    { k: 'bos', baslik: 'We divorce more', birim: 'divorces per 1,000 people', d: 2, ek: '‰', trAd: 'Türkiye',
      renk: ['#f3dde0', '#e2a5ad', '#c9586a', '#a3283c', '#651423'], bolum: 'Chapter 22 · The Economics of Divorce',
      metin: function (s) { return 'In ' + s.ilk + ', the divorce rate was ' + v1(s.a, 2) + ' per 1,000 people. In ' + s.son + ', it was ' + v1(s.b, 2) + ' per 1,000. Divorce went up ' + ilde(s.artan) + '. The steepest rise was in ' + s.enCok.il + ' (' + v1(s.enCok.a, 2) + ' → ' + v1(s.enCok.b, 2) + ').'; } },
    { k: 'tdh', baslik: 'Fewer children', birim: 'average children per woman', d: 2, ek: ' children', trAd: 'Median of 81 provinces',
      renk: ['#e6e1ef', '#bfb1d8', '#8f78b8', '#634892', '#3a2560'], bolum: 'Chapter 17 · The Economics of Children',
      metin: function (s) { return 'In ' + s.ilk + ', the median province had ' + v1(s.a, 2) + ' children per woman. In ' + s.son + ', it had ' + v1(s.b, 2) + '. A population needs about 2.1 to replace itself. The number of provinces below that line rose from ' + s.alt21a + ' to ' + s.alt21b + '. (We have no provincial data for 2023 and 2024.)'; } },
    { k: 'yasli', baslik: 'We are getting older', birim: 'share of people aged 65 and over (%)', d: 1, ek: '%', trAd: 'Türkiye',
      renk: ['#eceae4', '#cfc8b8', '#a89c84', '#7a6d55', '#4a412f'], bolum: 'Chapter 33 · The Economics of Loneliness',
      metin: function (s) { return 'In ' + s.ilk + ', ' + v1(s.a, 1) + '% of the population was over 65. By ' + s.son + ', it was ' + v1(s.b, 1) + '%. The population got older ' + ilde(s.artan) + '. The oldest province is ' + s.enYuksek.il + ' (' + v1(s.enYuksek.b, 1) + '%).'; } }
  ];
  // scene statistics (computed from the data)
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

  // ---------- layout ----------
  kok.innerHTML =
    '<div class="hk-sahne" id="hkSahne">' +
    '<div class="hk-ust"><div><p class="hk-no" id="hkNo"></p><h2 class="hk-baslik" id="hkBaslik"></h2></div><div class="hk-yil" id="hkYil" aria-live="off"></div></div>' +
    '<div class="hk-govde"><div class="hk-harita"><svg id="hkSvg" viewBox="' + G.viewBox + '" role="img" aria-label="Map of the provinces of Türkiye"><g id="hkIller"></g></svg>' +
    '<div class="hk-lejant" id="hkLejant"></div></div>' +
    '<div class="hk-yan"><svg id="hkGrafik" class="hk-grafik" viewBox="0 0 360 230" role="img" aria-label="Trend line for Türkiye"></svg><p class="hk-metin" id="hkMetin" aria-live="polite"></p><p class="hk-bolum" id="hkBolum"></p></div></div>' +
    '<div class="hk-ilerleme" id="hkIlerleme">' + SAHNE.map(function (S, j) { return '<button data-j="' + j + '" aria-label="Scene ' + (j + 1) + ': ' + S.baslik + '"><i></i><span>' + S.baslik + '</span></button>'; }).join('') + '</div>' +
    '<div class="hk-kontrol"><button class="hk-k" id="hkGeri" aria-label="Previous scene"><svg viewBox="0 0 24 24"><path d="M6 5h2v14H6zM20 5L9 12l11 7z"/></svg></button>' +
    '<button class="hk-k hk-oyna" id="hkOyna" aria-label="Play"></button>' +
    '<button class="hk-k" id="hkIleri" aria-label="Next scene"><svg viewBox="0 0 24 24"><path d="M16 5h2v14h-2zM4 5l11 7L4 19z"/></svg></button></div>' +
    '<div class="hk-perde" id="hkPerde"><div><p class="hk-no">Six scenes · about a minute and a half</p><h2>Türkiye’s family story</h2><p>From 2008 to 2025, watch the map of Türkiye’s 81 provinces change year by year: households, marriages, divorces, children and ageing. All figures come from TurkStat (TÜİK), Türkiye’s official statistics office.</p><button class="oy-btn" id="hkBasla">Start the story</button></div></div>' +
    '</div><div id="hkSon"></div>' +
    '<p class="oy-not hk-kaynak">Sources: TurkStat (TÜİK) Marriage and Divorce Statistics (provincial tables, 2012–2025); mean age at first marriage by province and sex (2010–2025); Address-Based Population Registration System, ADNKS (provincial population, household size 2008–2025, share of older people 2009–2024); fertility 2011–2022 (research archive) and 2025 (TurkStat Birth Statistics, via a secondary source). Crude rates use mid-year population. All data are official Turkish statistics. Map borders: alpers/Turkey-Maps-GeoJSON, Apache 2.0.</p>';
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
    document.getElementById('hkBolum').textContent = 'In the book (in Turkish): ' + S.bolum;
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
      (cv !== null ? '<circle cx="' + x(yj) + '" cy="' + y(cv) + '" r="6" fill="' + S.renk[3] + '" stroke="#fffaf2" stroke-width="2"/><text x="' + (x(yj) + (yj > n / 2 ? -10 : 10)) + '" y="' + (y(cv) - 12) + '" text-anchor="' + (yj > n / 2 ? 'end' : 'start') + '" class="hk-deger">' + f(S, cv) + S.ek + '</text>' : '<text x="' + x(yj) + '" y="' + (T0 + 16) + '" text-anchor="middle" class="hk-eks">no data</text>') +
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
  function oynat() { if (oynuyor) return; oynuyor = true; document.getElementById('hkOyna').innerHTML = DU; document.getElementById('hkOyna').setAttribute('aria-label', 'Pause'); zam = setTimeout(tik, ADIM); }
  function durdur() { oynuyor = false; clearTimeout(zam); document.getElementById('hkOyna').innerHTML = OY; document.getElementById('hkOyna').setAttribute('aria-label', 'Play'); }
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
    el.innerHTML = '<div class="oy-sahne hk-final"><p class="oy-adim">The story in short</p><h2 class="hk-f-b">Türkiye’s family, 2008 to 2025</h2><div class="hk-ozetler">' + kartlar + '</div>' +
      '<p>Households got smaller. Marriage came later and less often. Divorce went up, families had fewer children, and the population grew older. Each of these numbers adds up millions of personal decisions. Aşkonomi tells the economics behind those decisions: who says “yes”, when, why, and what it costs.</p>' +
      '<div class="paylas"><button data-k="indir">Download the summary image</button>' + (navigator.canShare ? '<button data-k="paylas">Share the image</button>' : '') + '<a class="wa" data-k="wa" target="_blank" rel="noopener" href="#">WhatsApp</a><a data-k="x" target="_blank" rel="noopener" href="#">X</a><a data-k="fb" target="_blank" rel="noopener" href="#">Facebook</a><button class="ig" data-k="ig">Instagram</button><button data-k="kopya">Copy link</button></div>' + O.IG_NOT + '' +
      '<div class="oy-dugmeler"><a class="oy-btn" href="/en/oyunlar/harita/">Find a province on the map</a><button class="oy-btn ikincil" id="hkTekrar">Play the story again</button></div>' + O.abone() + '</div>';
    O.paylasBagla(el, { slug: 'hikaye', url: O.SITE + '/en/oyunlar/hikaye/', mesaj: 'Türkiye’s family story, 2008–2025: smaller households, later marriage, more divorce, fewer children. A moving map built on TurkStat (TÜİK) data:',
      kartAyar: { oyun: 'Türkiye’s family story', ust: 'TurkStat (TÜİK) data', baslik: '2008–2025: Türkiye’s family', alt: 'Smaller homes, later marriage, more divorce', cagri: 'Watch the moving map:  askonomi.com/en/oyunlar/hikaye', ciz: kartCiz } });
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
