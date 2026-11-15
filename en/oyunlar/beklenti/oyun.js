/* Expectation budget — expectation inflation (Chapter 28 in the book) */
(function () {
  'use strict';
  var O = window.OYUN, R = O.R;
  var kok = document.getElementById('oyun');
  var I = { // 32×32 single-line icons
    sevgili: '<path d="M16 27C6 20 3 15 3 10.5C3 7 5.6 4.5 9 4.5c2.9 0 5.2 1.8 7 4.4c1.8-2.6 4.1-4.4 7-4.4c3.4 0 6 2.5 6 6c0 4.5-3 9.5-13 16.5z"/>',
    arkadas: '<circle cx="11" cy="10" r="4.5"/><circle cx="22" cy="10" r="4.5"/><path d="M3 26c1.5-6 5-8.5 8-8.5s6.5 2.5 8 8.5M14 26c1.5-6 5-8.5 8-8.5s6.5 2.5 8 8.5"/>',
    dert: '<path d="M5 6h22v14H14l-6 6v-6H5z"/><path d="M10 12h12M10 16h8"/>',
    eglence: '<path d="M16 3l3.4 7.6l8.1.8l-6.1 5.4l1.8 8l-7.2-4.2l-7.2 4.2l1.8-8l-6.1-5.4l8.1-.8z"/>',
    koc: '<circle cx="16" cy="16" r="12"/><circle cx="16" cy="16" r="7"/><circle cx="16" cy="16" r="2"/><path d="M16 16L28 4M24 4h4v4"/>',
    ev: '<path d="M4 15L16 5l12 10M7 13v14h18V13"/><path d="M13 27v-8h6v8"/>',
    guvence: '<path d="M16 3l11 4v8c0 7-5 12-11 14C10 27 5 22 5 15V7z"/><path d="M11 16l4 4l7-8"/>',
    macera: '<path d="M2 27l9-15l6 9l4-6l9 12z"/><circle cx="24" cy="7" r="3"/>',
    entelektuel: '<path d="M4 7c4-2 8-2 12 1v19c-4-3-8-3-12-1zM28 7c-4-2-8-2-12 1v19c4-3 8-3 12-1z"/>',
    sefkat: '<path d="M4 20c3 0 5 1 7 3h6c1.5 0 2.5-1 2.5-2.2S18.5 18.5 17 18.5h-4M4 27h9l9-3l6-5c.8-.8.6-2-.4-2.4c-.8-.3-1.6 0-2.2.5L21 21"/><path d="M19 13c-4-3-6-5-6-7c0-1.6 1.2-3 2.8-3c1.3 0 2.3.8 3.2 2c.9-1.2 1.9-2 3.2-2c1.6 0 2.8 1.4 2.8 3c0 2-2 4-6 7z"/>'
  };
  var ROL = [
    ['sevgili', 'Lover', 'passion, romance'], ['arkadas', 'Best friend', 'sharing everything'], ['dert', 'Confidant', 'listening, comfort'],
    ['eglence', 'Fun partner', 'laughter, lightness'], ['koc', 'Life coach', 'pushing you towards your goals'], ['ev', 'Housemate', 'daily routine, sharing chores'],
    ['guvence', 'Safety net', 'financial and emotional backing'], ['macera', 'Adventure buddy', 'novelty, discovery'], ['entelektuel', 'Thinking partner', 'deep conversation'], ['sefkat', 'Source of care', 'looking after you, attention']
  ];
  var bek = ROL.map(function () { return 5; }), ver = ROL.map(function () { return 5; }), asama = 1;
  function ikon(k, renk) { return '<svg viewBox="0 0 32 32" class="bk-ikon" aria-hidden="true"><g fill="none" stroke="' + renk + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + I[k] + '</g></svg>'; }
  function top(a) { return a.reduce(function (s, x) { return s + x; }, 0); }

  function satirHTML(i) {
    var r = ROL[i], dizi = asama === 1 ? bek : ver, renk = asama === 1 ? R.bordo : R.petrol;
    var seg = '';
    for (var k = 1; k <= 10; k++) {
      var dolu = k <= dizi[i], hayalet = asama === 2 && k <= bek[i];
      seg += '<button class="bk-seg' + (dolu ? ' dolu' : '') + (hayalet ? ' hayalet' : '') + '" data-i="' + i + '" data-k="' + k + '" aria-label="' + r[1] + ': ' + k + '"></button>';
    }
    return '<div class="bk-satir"><div class="bk-rol">' + ikon(r[0], renk) + '<div><b>' + r[1] + '</b><span>' + r[2] + '</span></div></div>' +
      '<div class="bk-segler ' + (asama === 1 ? 'b' : 'v') + '" role="slider" aria-label="' + r[1] + '" aria-valuemin="0" aria-valuemax="10" aria-valuenow="' + dizi[i] + '" tabindex="0" data-i="' + i + '">' + seg + '</div><b class="bk-deger">' + dizi[i] + '</b></div>';
  }
  function ciz() {
    var dizi = asama === 1 ? bek : ver;
    var ust = asama === 1 ?
      '<p class="oy-adim">Step 1 · Your expectations</p><p class="oy-buyuk">How much would you want from your dream partner in each of these roles?</p><p class="oy-not" style="margin:-6px 0 14px">0 means not at all, 10 means completely. There is no limit: mark what your heart wants.</p>' :
      '<p class="oy-adim">Step 2 · Capacity</p><p class="oy-buyuk">Now look at yourself. How much can you give a partner in each of these roles?</p><p class="oy-not" style="margin:-6px 0 14px">The faded red bars are what you expected in step 1. Be honest: think of a real week in your life.</p>';
    kok.innerHTML = ust + '<div class="bk-toplam"><span>' + (asama === 1 ? 'Your total expectation' : 'Total you can give') + '</span><b class="' + (asama === 1 ? 'sen-r' : 'o-r') + '" id="bkTop">' + top(dizi) + '</b><span>/ 100</span>' +
      (asama === 2 ? '<span class="bk-kiyas">expectation: <b class="sen-r">' + top(bek) + '</b></span>' : '') + '</div>' +
      '<div class="bk-liste">' + ROL.map(function (_, i) { return satirHTML(i); }).join('') + '</div>' +
      '<div class="oy-dugmeler"><button class="oy-btn' + (asama === 1 ? '' : ' petrol') + '" id="bkIleri">' + (asama === 1 ? 'Continue' : 'Calculate my inflation') + '</button>' + (asama === 2 ? '<button class="oy-btn ikincil" id="bkGeri">Back to expectations</button>' : '') + '</div>';
    kok.querySelectorAll('.bk-seg').forEach(function (b) {
      b.onclick = function () { var i = +b.dataset.i, k = +b.dataset.k; dizi[i] = dizi[i] === k ? k - 1 : k; satirYenile(i); };
    });
    kok.querySelectorAll('.bk-segler').forEach(function (el) {
      el.addEventListener('keydown', function (e) {
        var i = +el.dataset.i, d = { ArrowRight: 1, ArrowUp: 1, ArrowLeft: -1, ArrowDown: -1 }[e.key];
        if (d) { e.preventDefault(); dizi[i] = Math.max(0, Math.min(10, dizi[i] + d)); satirYenile(i); kok.querySelector('.bk-segler[data-i="' + i + '"]').focus(); }
      });
    });
    document.getElementById('bkIleri').onclick = function () { if (asama === 1) { asama = 2; O.iz('oyun-basladi', { oyun: 'beklenti' }); ciz(); kok.scrollIntoView({ behavior: 'smooth' }); } else sonuc(); };
    var g = document.getElementById('bkGeri'); if (g) g.onclick = function () { asama = 1; ciz(); };
  }
  function satirYenile(i) {
    var eski = kok.querySelectorAll('.bk-satir')[i], tmp = document.createElement('div'); tmp.innerHTML = satirHTML(i);
    var yeni = tmp.firstChild; eski.replaceWith(yeni);
    yeni.querySelectorAll('.bk-seg').forEach(function (b) {
      b.onclick = function () { var dizi = asama === 1 ? bek : ver, k = +b.dataset.k; dizi[i] = dizi[i] === k ? k - 1 : k; satirYenile(i); };
    });
    var el = yeni.querySelector('.bk-segler');
    el.addEventListener('keydown', function (e) {
      var dizi = asama === 1 ? bek : ver, d = { ArrowRight: 1, ArrowUp: 1, ArrowLeft: -1, ArrowDown: -1 }[e.key];
      if (d) { e.preventDefault(); dizi[i] = Math.max(0, Math.min(10, dizi[i] + d)); satirYenile(i); kok.querySelector('.bk-segler[data-i="' + i + '"]').focus(); }
    });
    document.getElementById('bkTop').textContent = top(asama === 1 ? bek : ver);
  }

  var SEVIYE = [
    [0, 'Balanced budget', 'What you expect from a partner does not exceed what you can give yourself. In economists’ language, your budget is balanced. This does not mean low expectations. You set what you ask for by what you can offer in return. The book’s warning still applies: even with a balanced budget, loading certain roles onto one person is fragile.'],
    [101, 'Moderate inflation', 'Your expectations are a little above what you can give. That is normal for most people: dreaming is easier than measuring. But as the gap grows, every partner gets weighed on a scale that nobody could really meet. Look at the roles with the biggest deficit. Some of them could also be covered by friends, family or yourself.'],
    [131, 'High inflation', 'What you expect from a partner is far above what you could give yourself. The book calls this expectation inflation: in modern relationships, expecting one person to be lover, best friend, therapist and life coach all at once. If even you cannot do this, it may be hard for the other person too. There are two ways to close the deficit: spread your expectations around, or grow your capacity.'],
    [171, 'Hyperinflation', 'Your expectations are almost double what you can give, or even more. At this scale no real person can meet the budget, and every relationship may feel like one long disappointment. The good news: just as in monetary policy, inflation can be brought down in a relationship too. The first step is to stop expecting one person to fill the roles with the biggest deficit.']
  ];
  function sonuc() {
    var B = top(bek), V = top(ver), oran = V ? Math.round(B / V * 100) : 999;
    var sv = SEVIYE[0]; SEVIYE.forEach(function (s) { if (oran >= s[0]) sv = s; });
    var aciklar = ROL.map(function (r, i) { return { i: i, f: bek[i] - ver[i] }; }).filter(function (x) { return x.f > 0; }).sort(function (a, b) { return b.f - a.f; }).slice(0, 3);
    O.iz('oyun-bitti', { oyun: 'beklenti', sonuc: sv[1], oran: oran });
    var balon = Math.min(1.55, Math.max(.75, oran / 100));
    var cizelge = '<div class="bk-sonuc-liste">' + ROL.map(function (r, i) {
      return '<div class="bk-s"><span>' + ikon(r[0], R.murekkep) + r[1] + '</span><div class="bk-cift"><i class="b" style="width:' + bek[i] * 10 + '%"></i><i class="v" style="width:' + ver[i] * 10 + '%"></i></div><small>' + bek[i] + ' / ' + ver[i] + '</small></div>';
    }).join('') + '</div>';
    kok.innerHTML = '<div class="oy-sonuc"><div class="bk-ust"><div><p class="oy-adim">Your expectation inflation</p><h2>' + sv[1] + '</h2></div>' +
      '<svg class="bk-balon" viewBox="0 -50 200 300" aria-hidden="true"><path d="M100 ' + (110 + 58 * balon).toFixed(1) + 'C100 220 94 232 104 248" fill="none" stroke="#262028" stroke-width="2"/>' +
      '<g style="transform-origin:100px 110px;transform:scale(' + balon.toFixed(2) + ')" class="bk-sis"><ellipse cx="100" cy="100" rx="52" ry="60" fill="' + R.bordo + '"/><path d="M94 159l6 9l6-9z" fill="#8f1c2d"/><path d="M76 72q10-18 28-20" stroke="#fff" stroke-opacity=".55" stroke-width="7" fill="none" stroke-linecap="round"/></g>' +
      '<text x="100" y="' + (118) + '" text-anchor="middle" class="bk-yuzde">' + oran + '%</text></svg></div>' +
      '<div class="oy-olcu"><div><small>Expectation</small><b class="sen-r">' + B + '</b><span>points</span></div><div><small>What you can give</small><b class="o-r">' + V + '</b><span>points</span></div>' +
      '<div><small>Inflation</small><b class="alt-r">' + oran + '%</b><span>expectation ÷ capacity</span></div><div><small>Deficit</small><b>' + Math.max(0, B - V) + '</b><span>points</span></div></div>' +
      '<p>' + sv[2] + '</p>' +
      (aciklar.length ? '<div class="bk-acik"><small>Biggest deficits</small>' + aciklar.map(function (a) { return '<span>' + ikon(ROL[a.i][0], R.bordo) + ROL[a.i][1] + ' <b>+' + a.f + '</b></span>'; }).join('') + '<p class="oy-not">Think about sharing these roles with your friends, your family or yourself.</p></div>' : '') +
      cizelge + '<p class="gv-lejant"><i style="background:' + R.bordo + '"></i>what you expect <i style="background:' + R.petrol + '"></i>what you can give</p>' +
      '<p class="not">In the book: Chapter 28 · Expectation Inflation (Expecting Everything from One Partner).</p>' +
      O.paylasHTML() + O.abone() +
      '<div class="oy-dugmeler"><button class="oy-btn ikincil" id="bkYeniden">Play again</button></div></div>';
    O.paylasBagla(kok, { slug: 'beklenti', mesaj: 'According to Aşkonomi, my expectation inflation is ' + oran + '%: “' + sv[1] + '”. What’s yours?',
      kartAyar: { oyun: 'The expectation budget', ust: 'My expectation inflation', baslik: oran + '% · ' + sv[1], alt: 'Expectation ' + B + ' · what I can give ' + V, ciz: function (x, X, Y, W, H) { kartCiz(x, X, Y, W, H); } } });
    document.getElementById('bkYeniden').onclick = function () { asama = 1; ciz(); window.scrollTo({ top: 0, behavior: 'smooth' }); };
    kok.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function kartCiz(x, X, Y, W, H) {
    var sh = H / ROL.length;
    ROL.forEach(function (r, i) {
      var y = Y + i * sh + 8, bw = W - 300;
      x.fillStyle = R.murekkep; x.textAlign = 'right'; x.font = '500 30px Fraunces, Georgia, serif'; x.fillText(r[1], X + 270, y + 34);
      x.fillStyle = '#ece3d6'; x.fillRect(X + 290, y + 6, bw, 20); x.fillRect(X + 290, y + 30, bw, 20);
      x.fillStyle = R.bordo; x.fillRect(X + 290, y + 6, bw * bek[i] / 10, 20);
      x.fillStyle = R.petrol; x.fillRect(X + 290, y + 30, bw * ver[i] / 10, 20);
    });
  }
  ciz();
})();
