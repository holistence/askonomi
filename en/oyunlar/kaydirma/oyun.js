/* Swipe simulator — attention and selectiveness in your own data (Chapter 30 in the book) */
(function () {
  'use strict';
  var O = window.OYUN, R = O.R;
  var kok = document.getElementById('oyun');
  var N = 30;
  // seeded random: every visitor sees the same 30 profiles, so comparisons are fair
  // (list lengths must stay the same as the Turkish file; names and cities stay Turkish)
  var tohum = 20261021;
  function rnd() { tohum = (tohum * 1664525 + 1013904223) % 4294967296; return tohum / 4294967296; }
  function sec(a) { return a[Math.floor(rnd() * a.length)]; }
  var KADIN = ['Selin', 'Zeynep', 'Elif', 'İpek', 'Defne', 'Ece', 'Nil', 'Asya', 'Lal', 'Duru', 'Melis', 'Ceren', 'Damla', 'Gizem', 'Pelin', 'Buse', 'Derya', 'Eylül', 'Ezgi', 'Irmak', 'Naz', 'Yasemin', 'Beren', 'Öykü', 'Aslı', 'Burcu', 'Tuğçe', 'Sinem', 'Ayça', 'Gamze'];
  var ERKEK = ['Kerem', 'Mert', 'Can', 'Arda', 'Bora', 'Emre', 'Kaan', 'Ozan', 'Tuna', 'Efe', 'Onur', 'Sarp', 'Barış', 'Cem', 'Eren', 'Furkan', 'Gökhan', 'Hakan', 'İlker', 'Kerim', 'Levent', 'Murat', 'Oğuz', 'Serkan', 'Tolga', 'Volkan', 'Yiğit', 'Alp', 'Berk', 'Doruk'];
  var MESLEK = ['architect', 'nurse', 'software developer', 'teacher', 'chef', 'graphic designer', 'lawyer', 'physiotherapist', 'musician', 'vet', 'engineer', 'librarian', 'pilot', 'pharmacist', 'photographer', 'academic'];
  var SEHIR = ['Çanakkale', 'İzmir', 'İstanbul', 'Ankara', 'Eskişehir', 'Bursa', 'Antalya', 'Trabzon', 'Muğla', 'Edirne'];
  var ILGI = ['camping', 'chess', 'morning runs', 'old films', 'fermented food', 'birdwatching', 'ceramics', 'tango', 'crime novels', 'diving', 'puzzles', 'cycling', 'jazz', 'gardening', 'yoga', 'sci-fi', 'history', 'stand-up', 'photography', 'mountaineering'];
  var CUMLE = ['I take my coffee plain, not my life.', 'First date: museum or meyhane (tavern)? Both.', 'I find my way without a map. Sometimes.', 'I want to meet someone who recommends books.', 'If my cat says no, it’s a no.', 'Sunday breakfast is on me.', 'Three languages, one instrument, zero recipes.', 'The longer the walk, the longer the chat.', 'Looking for something serious, but I love to laugh.', 'Always ready to escape the city.', 'I love making plans, and I love it when they fall apart.', 'Slow to reply to messages, never late for dates.'];
  var TEN = ['#f3d2b8', '#e9c19f', '#d9a57e', '#c48a62', '#a8704c', '#8a5638', '#6e4129'];
  var SAC = ['#1e1612', '#3a2618', '#5b3a22', '#8a5a33', '#b07a42', '#d7b07a', '#7a7672', '#2b2a33'];
  var ZEMIN = [['#f6d9c9', '#e8a990'], ['#d6e7e3', '#9cc5bf'], ['#f1e2b8', '#d9b968'], ['#e3d8ef', '#b5a3d1'], ['#dfe8d2', '#a9c48c'], ['#f4d6dc', '#d996a4'], ['#d7e1ee', '#93aecb']];
  var GIYSI = ['#B3263A', '#1E6B70', '#C99A2E', '#3d3550', '#5f7a4a', '#c46a3c', '#2f4f7a', '#8a3b5e'];
  var profiller = [], cins = null;
  function uret(c) {
    tohum = 20261021; profiller = [];
    for (var i = 0; i < N; i++) {
      var k = c === 'kadin' ? 'e' : c === 'erkek' ? 'k' : (i % 2 ? 'e' : 'k');
      var ilg = []; while (ilg.length < 3) { var x = sec(ILGI); if (ilg.indexOf(x) < 0) ilg.push(x); }
      var ad = k === 'k' ? KADIN[i] : ERKEK[i];
      profiller.push({ ad: ad, yas: 24 + Math.floor(rnd() * 15), meslek: sec(MESLEK), sehir: sec(SEHIR), ilgi: ilg, cumle: sec(CUMLE),
        ten: sec(TEN), sac: sec(SAC), zemin: sec(ZEMIN), giysi: sec(GIYSI),
        sacTip: k === 'k' ? [1, 3, 1, 3, 0][Math.floor(rnd() * 5)] : [0, 2, 4, 4, 0][Math.floor(rnd() * 5)],
        gozluk: rnd() < .22, sakal: k === 'e' && rnd() < .4, kupe: k === 'k' ? rnd() < .55 : rnd() < .06 });
    }
  }
  function portre(p, id) {
    var g = 'g' + id, sacArka = ['', '<path d="M112 120c-8 60 8 120 30 150h116c22-30 38-90 30-150z" fill="' + p.sac + '"/>', '', '<path d="M118 110c-14 40-14 90 4 120h156c18-30 18-80 4-120z" fill="' + p.sac + '"/>', ''][p.sacTip];
    var sacOn = [
      '<path d="M132 118c8-44 46-62 74-60c36 2 62 26 64 62c-20-18-58-30-96-24c-20 4-34 12-42 22z" fill="' + p.sac + '"/>',
      '<path d="M126 132c0-52 40-78 78-76c42 2 72 32 70 80c-18-30-50-44-80-44c-30 0-52 14-68 40z" fill="' + p.sac + '"/>',
      '<path d="M134 108c14-34 50-44 78-38c28 6 46 26 50 48c-6-6-16-10-26-10c-4-12-24-16-40-8c-18-8-48-6-62 8z" fill="' + p.sac + '"/><circle cx="200" cy="58" r="22" fill="' + p.sac + '"/>',
      '<path d="M124 140c-4-56 34-86 80-84c46 2 76 36 72 86c-14-40-44-56-74-56c-36 0-60 20-78 54z" fill="' + p.sac + '"/>',
      '<path d="M136 112c10-30 40-46 66-44c30 2 54 20 60 44c-30-12-82-14-126 0z" fill="' + p.sac + '"/>'][p.sacTip];
    return '<svg viewBox="0 0 400 400" class="ky-portre" aria-hidden="true"><defs><linearGradient id="' + g + '" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="' + p.zemin[0] + '"/><stop offset="1" stop-color="' + p.zemin[1] + '"/></linearGradient></defs>' +
      '<rect width="400" height="400" fill="url(#' + g + ')"/><circle cx="320" cy="80" r="60" fill="#fff" opacity=".18"/><circle cx="60" cy="330" r="90" fill="#fff" opacity=".12"/>' + sacArka +
      '<path d="M90 400c8-70 54-104 110-104s102 34 110 104z" fill="' + p.giysi + '"/><path d="M176 300l24 30l24-30" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="5"/>' +
      '<rect x="180" y="250" width="40" height="52" rx="16" fill="' + p.ten + '"/><ellipse cx="200" cy="168" rx="70" ry="84" fill="' + p.ten + '"/>' +
      '<ellipse cx="132" cy="174" rx="10" ry="16" fill="' + p.ten + '"/><ellipse cx="268" cy="174" rx="10" ry="16" fill="' + p.ten + '"/>' +
      (p.kupe ? '<circle cx="132" cy="196" r="5" fill="#C99A2E"/><circle cx="268" cy="196" r="5" fill="#C99A2E"/>' : '') + sacOn +
      '<path d="M166 166q10-7 20 0M214 166q10-7 20 0" fill="none" stroke="#2a1d16" stroke-width="5" stroke-linecap="round"/>' +
      '<path d="M200 178q-6 22 0 26q4 2 8 0" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="4" stroke-linecap="round"/>' +
      '<path d="M178 222q22 16 44 0" fill="none" stroke="#7a2e2a" stroke-width="5" stroke-linecap="round"/>' +
      '<ellipse cx="160" cy="200" rx="14" ry="8" fill="#e06a6a" opacity=".18"/><ellipse cx="240" cy="200" rx="14" ry="8" fill="#e06a6a" opacity=".18"/>' +
      (p.sakal ? '<path d="M136 196c6 46 34 66 64 66s58-20 64-66c-10 20-34 22-64 22s-54-2-64-22z" fill="' + p.sac + '" opacity=".85"/><path d="M180 224q20 10 40 0" fill="none" stroke="#7a2e2a" stroke-width="5" stroke-linecap="round"/>' : '') +
      (p.gozluk ? '<g fill="none" stroke="#262028" stroke-width="5"><circle cx="176" cy="170" r="20"/><circle cx="224" cy="170" r="20"/><path d="M196 170h8M156 168l-22-6M244 168l22-6"/></g>' : '') + '</svg>';
  }

  // ---------- flow ----------
  var kayit = [], idx = 0, t0 = 0, mesgul = false, ilk = 0;
  var CO = { oyun: 'kaydirma', aciklama: 'The profiles you see depend on your choice.', kadin: 'You will see men’s profiles', erkek: 'You will see women’s profiles', belirsiz: 'You will see a mix of profiles' };
  var GOR = { kadin: 'men’s', erkek: 'women’s', belirsiz: 'mixed' };
  function bas() {
    kok.innerHTML = '<div class="ky-giris">' + O.C.kaydirma + '<div><p class="oy-buyuk">Thirty profiles, your call.</p><p>On each profile, swipe right (like) or left (pass). You can drag on the screen, use the buttons, or press the ← → arrow keys. The page will measure how long you look before each decision. All profiles are fictional.</p>' +
      '<p class="oy-not">You will be shown ' + GOR[cins] + ' profiles. <button class="ky-degis" id="kyCins">Change</button></p>' +
      '<div class="oy-dugmeler"><button class="oy-btn" id="kyBasla">Start swiping</button></div></div></div>';
    document.getElementById('kyCins').onclick = function () { O.cinsSor(kok, CO, function (c) { cins = c; uret(c); bas(); }); };
    document.getElementById('kyBasla').onclick = function () { O.iz('oyun-basladi', { oyun: 'kaydirma' }); idx = 0; kayit = []; deste(); var y = kok.getBoundingClientRect().top + window.scrollY - 66; window.scrollTo({ top: y, behavior: 'smooth' }); };
  }
  function kartHTML(p, i, ust) {
    return '<div class="ky-kart' + (ust ? ' ust' : '') + '" data-i="' + i + '">' + portre(p, i) +
      '<div class="ky-bilgi"><b>' + p.ad + ', ' + p.yas + '</b><span>' + p.meslek + ' · ' + p.sehir + '</span><p>“' + p.cumle + '”</p><div class="ky-ilgi">' + p.ilgi.map(function (x) { return '<em>' + x + '</em>'; }).join('') + '</div></div>' +
      '<i class="ky-dam evet">LIKE</i><i class="ky-dam hayir">PASS</i></div>';
  }
  function deste() {
    kok.innerHTML = '<div class="ky-ust"><span class="oy-adim" id="kySay"></span><div class="ky-ilerleme"><i id="kyIl"></i></div></div>' +
      '<div class="ky-deste" id="kyDeste"></div>' +
      '<div class="ky-dugmeler"><button class="ky-btn hayir" id="kyHayir" aria-label="Pass">' + '<svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button>' +
      '<button class="ky-btn evet" id="kyEvet" aria-label="Like"><svg viewBox="0 0 24 24"><path d="M12 20C5 15 3 11.5 3 8.5C3 6 5 4 7.5 4c1.9 0 3.4 1.1 4.5 2.7C13.1 5.1 14.6 4 16.5 4C19 4 21 6 21 8.5c0 3-2 6.5-9 11.5z"/></svg></button></div>';
    goster();
    document.getElementById('kyHayir').onclick = function () { karar(false); };
    document.getElementById('kyEvet').onclick = function () { karar(true); };
    document.onkeydown = function (e) { if (!document.getElementById('kyDeste')) return; if (e.key === 'ArrowLeft') karar(false); if (e.key === 'ArrowRight') karar(true); };
  }
  function goster() {
    var d = document.getElementById('kyDeste');
    d.innerHTML = (idx + 1 < N ? kartHTML(profiller[idx + 1], idx + 1, false) : '') + kartHTML(profiller[idx], idx, true);
    document.getElementById('kySay').textContent = (idx + 1) + ' / ' + N;
    document.getElementById('kyIl').style.width = (idx / N * 100) + '%';
    t0 = performance.now(); mesgul = false; surukle(d.querySelector('.ky-kart.ust'));
  }
  function surukle(k) {
    var x0 = null, dx = 0;
    k.addEventListener('pointerdown', function (e) { x0 = e.clientX; dx = 0; k.setPointerCapture(e.pointerId); k.style.transition = 'none'; });
    k.addEventListener('pointermove', function (e) {
      if (x0 === null) return; dx = e.clientX - x0;
      k.style.transform = 'translateX(' + dx + 'px) rotate(' + dx / 18 + 'deg)';
      k.querySelector('.evet').style.opacity = Math.max(0, Math.min(1, dx / 90));
      k.querySelector('.hayir').style.opacity = Math.max(0, Math.min(1, -dx / 90));
    });
    var bit = function () {
      if (x0 === null) return; x0 = null; k.style.transition = '';
      if (Math.abs(dx) > 90) karar(dx > 0);
      else { k.style.transform = ''; k.querySelectorAll('.ky-dam').forEach(function (d) { d.style.opacity = 0; }); }
    };
    k.addEventListener('pointerup', bit); k.addEventListener('pointercancel', bit);
  }
  function karar(evet) {
    if (mesgul) return; mesgul = true;
    var sure = (performance.now() - t0) / 1000;
    kayit.push({ i: idx, evet: evet, s: Math.min(sure, 30) });
    var k = document.querySelector('.ky-kart.ust');
    k.querySelector(evet ? '.evet' : '.hayir').style.opacity = 1;
    k.style.transition = 'transform .38s cubic-bezier(.4,0,.6,1), opacity .38s';
    k.style.transform = 'translateX(' + (evet ? 520 : -520) + 'px) rotate(' + (evet ? 24 : -24) + 'deg)'; k.style.opacity = 0;
    setTimeout(function () { idx++; if (idx < N) goster(); else sonuc(); }, 330);
  }

  // ---------- result ----------
  function sayi(x, d) { return (Math.round(x * Math.pow(10, d || 1)) / Math.pow(10, d || 1)).toFixed(d === undefined ? 1 : d); }
  function ortalama(a) { return a.reduce(function (s, x) { return s + x; }, 0) / (a.length || 1); }
  function sonuc() {
    document.onkeydown = null;
    var ilk10 = kayit.slice(0, 10).map(function (k) { return k.s; }), son10 = kayit.slice(-10).map(function (k) { return k.s; });
    var a1 = ortalama(ilk10), a2 = ortalama(son10), dusus = a1 ? Math.round((1 - a2 / a1) * 100) : 0;
    var b1 = kayit.slice(0, 10).filter(function (k) { return k.evet; }).length, b2 = kayit.slice(-10).filter(function (k) { return k.evet; }).length;
    var toplamB = kayit.filter(function (k) { return k.evet; }).length;
    var tur, metin;
    if (dusus >= 35) { tur = 'Melting attention'; metin = 'You looked at the first ten profiles for ' + sayi(a1) + ' seconds on average, and at the last ten for ' + sayi(a2) + ' seconds. Your attention dropped by about ' + dusus + '%. The more options there are, the less attention each one gets. The book sees this as one of the core dilemmas of platform love: more choice can come at the price of getting to know each person less.'; }
    else if (dusus <= -15) { tur = 'The warming-up chooser'; metin = 'Something interesting happened: towards the end you looked at profiles for longer. ' + sayi(a1) + ' seconds in the first ten, ' + sayi(a2) + ' seconds in the last ten. Either your criteria got clearer, or the fear of missing out kicked in as the end came closer. Both are traces of an abundance of choice showing up in behaviour.'; }
    else { tur = 'The steady pacer'; metin = 'Your attention stayed about the same from start to finish: ' + sayi(a1) + ' seconds in the first ten, ' + sayi(a2) + ' in the last ten. Most people speed up as they swipe; you did not. This may show that you gave every profile a chance. Or thirty profiles were just not enough to tire you out.'; }
    if (b2 < b1 - 2) metin += ' Your like rate dropped too: ' + b1 + ' likes in the first ten, ' + b2 + ' in the last ten. As you get pickier, the door gets narrower.';
    else if (b2 > b1 + 2) metin += ' Your number of likes went up, though: ' + b1 + ' in the first ten, ' + b2 + ' in the last ten. You got more generous towards the end.';
    O.iz('oyun-bitti', { oyun: 'kaydirma', sonuc: tur, dusus: dusus, begeni: toplamB });
    var mx = Math.max.apply(null, kayit.map(function (k) { return k.s; })) || 1, W = 760, H = 220, bw = W / N;
    var svg = '<svg class="ky-grafik" viewBox="0 0 ' + (W + 50) + ' ' + (H + 50) + '" role="img" aria-label="How many seconds you looked at each profile">' +
      [0, .5, 1].map(function (f) { var y = 10 + H - f * H; return '<line x1="40" x2="' + (W + 40) + '" y1="' + y + '" y2="' + y + '" stroke="#ece3d6"/><text x="34" y="' + (y + 5) + '" text-anchor="end" class="gv-eks">' + sayi(f * mx) + ' s</text>'; }).join('') +
      kayit.map(function (k, i) { var h = k.s / mx * H; return '<rect x="' + (40 + i * bw + 2) + '" y="' + (10 + H - h) + '" width="' + (bw - 4) + '" height="' + h + '" fill="' + (k.evet ? R.bordo : '#b9ad9c') + '"><title>Profile ' + (i + 1) + ': ' + sayi(k.s) + ' s, ' + (k.evet ? 'liked' : 'passed') + '</title></rect>'; }).join('') +
      '<line x1="40" x2="' + (40 + 10 * bw) + '" y1="' + (10 + H - a1 / mx * H) + '" y2="' + (10 + H - a1 / mx * H) + '" stroke="' + R.petrol + '" stroke-width="3" stroke-dasharray="6 5"/>' +
      '<line x1="' + (40 + 20 * bw) + '" x2="' + (40 + W) + '" y1="' + (10 + H - a2 / mx * H) + '" y2="' + (10 + H - a2 / mx * H) + '" stroke="' + R.petrol + '" stroke-width="3" stroke-dasharray="6 5"/>' +
      '<text x="40" y="' + (H + 40) + '" class="gv-eks">profile 1</text><text x="' + (W + 40) + '" y="' + (H + 40) + '" text-anchor="end" class="gv-eks">profile 30</text></svg>';
    var begenilen = kayit.filter(function (k) { return k.evet; }).slice(0, 8);
    kok.innerHTML = '<div class="oy-sonuc"><p class="oy-adim">Thirty profiles done</p><h2>' + tur + '</h2>' +
      '<div class="oy-olcu"><div><small>First ten profiles</small><b class="o-r">' + sayi(a1) + '</b><span>seconds / profile</span></div><div><small>Last ten profiles</small><b class="o-r">' + sayi(a2) + '</b><span>seconds / profile</span></div>' +
      '<div><small>Change in attention</small><b class="alt-r">' + (dusus >= 0 ? '−' + dusus + '%' : '+' + (-dusus) + '%') + '</b><span>first ten to last ten</span></div><div><small>You liked</small><b class="sen-r">' + toplamB + '</b><span>/ 30 profiles</span></div></div>' +
      svg + '<p class="gv-lejant"><i style="background:' + R.bordo + '"></i>liked <i style="background:#b9ad9c"></i>passed <i class="cizgi" style="background:' + R.petrol + '"></i>average of the first and last ten</p>' +
      '<p>' + metin + '</p>' +
      (begenilen.length ? '<div class="ky-galeri"><small>The ones you liked</small><div>' + begenilen.map(function (k) { return '<figure>' + portre(profiller[k.i], 'g' + k.i) + '<figcaption>' + profiller[k.i].ad + '</figcaption></figure>'; }).join('') + '</div></div>' : '') +
      '<p class="not">In the book: Chapter 30 · Before and After Tinder (Love on Platforms). This is not an experiment, just a small mirror held up to your own behaviour. The times were measured in this browser and sent nowhere.</p>' +
      O.paylasHTML() + O.abone() +
      '<div class="oy-dugmeler"><button class="oy-btn ikincil" id="kyYeniden">Swipe again</button></div></div>';
    O.paylasBagla(kok, { slug: 'kaydirma', mesaj: 'In the Aşkonomi swipe simulator: “' + tur + '”. From the first ten profiles to the last ten, my attention ' + (dusus >= 0 ? 'dropped by ' + dusus + '%' : 'rose by ' + (-dusus) + '%') + '.',
      kartAyar: { oyun: 'The swipe simulator', baslik: tur, alt: 'First ten ' + sayi(a1) + ' s → last ten ' + sayi(a2) + ' s · ' + toplamB + '/30 likes', ciz: function (x, X, Y, W2, H2) {
        var m2 = mx, b2w = W2 / N;
        kayit.forEach(function (k, i) { var h = k.s / m2 * (H2 - 40); x.fillStyle = k.evet ? R.bordo : '#b9ad9c'; x.fillRect(X + i * b2w + 3, Y + H2 - h, b2w - 6, h); });
        x.strokeStyle = R.petrol; x.lineWidth = 6; x.setLineDash([14, 10]);
        x.beginPath(); x.moveTo(X, Y + H2 - a1 / m2 * (H2 - 40)); x.lineTo(X + 10 * b2w, Y + H2 - a1 / m2 * (H2 - 40)); x.stroke();
        x.beginPath(); x.moveTo(X + 20 * b2w, Y + H2 - a2 / m2 * (H2 - 40)); x.lineTo(X + W2, Y + H2 - a2 / m2 * (H2 - 40)); x.stroke(); x.setLineDash([]);
      } } });
    document.getElementById('kyYeniden').onclick = function () { idx = 0; kayit = []; deste(); window.scrollTo({ top: 0, behavior: 'smooth' }); };
    kok.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  O.cinsBaslat(kok, CO, function (c) { cins = c; uret(c); bas(); });
})();
