/* Matching village — Gale–Shapley deferred acceptance algorithm (Gale and Shapley, 1962) */
(function () {
  'use strict';
  var O = window.OYUN, R = O.R, NS = 'http://www.w3.org/2000/svg';
  var kok = document.getElementById('oyun');
  var SOL = ['Sen', 'Deniz', 'Umut', 'Evren'], SAG = ['Ada', 'Ege', 'Yağmur', 'Derin'];
  // The others' preferences are fixed. This set-up was found by computer search: in both directions there are a few rounds of rejection,
  // and in all 24 possible rankings of the player, who proposes changes the matching.
  // Internal ids (Sen, Deniz, ...) are Turkish names and stay unchanged; 'Sen' (= 'you') is shown as 'You'.
  var TERCIH = {
    Deniz: ['Ege', 'Yağmur', 'Derin', 'Ada'], Umut: ['Ada', 'Derin', 'Yağmur', 'Ege'], Evren: ['Derin', 'Ege', 'Ada', 'Yağmur'],
    Ada: ['Evren', 'Deniz', 'Sen', 'Umut'], Ege: ['Umut', 'Evren', 'Sen', 'Deniz'], 'Yağmur': ['Evren', 'Umut', 'Sen', 'Deniz'], Derin: ['Sen', 'Deniz', 'Umut', 'Evren']
  };
  var NOT = { Ada: 'bookworm', Ege: 'night owl', 'Yağmur': 'travel buddy', Derin: 'joker', Deniz: 'cook', Umut: 'musician', Evren: 'mountaineer' };
  // Internal ids stay fixed (the algorithm and preferences use them); on screen, names are shown according to gender.
  var ISIM = {
    kadin: { Deniz: 'Elif', Umut: 'Zeynep', Evren: 'Selin', Ada: 'Kerem', Ege: 'Mert', 'Yağmur': 'Emre', Derin: 'Arda' },
    erkek: { Deniz: 'Kerem', Umut: 'Mert', Evren: 'Emre', Ada: 'Elif', Ege: 'Zeynep', 'Yağmur': 'Selin', Derin: 'Defne' },
    belirsiz: {}
  };
  var cins = null;
  function A(id) { return id === 'Sen' ? 'You' : ((cins && ISIM[cins][id]) || id); }
  function sira(n) { return n + (n === 1 ? 'st' : n === 2 ? 'nd' : n === 3 ? 'rd' : 'th'); }
  var senSira = [], sonuc = {};
  var hareketAz = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function bekle(ms) { return new Promise(function (r) { setTimeout(r, hareketAz ? 0 : ms); }); }

  // ---- algorithm: round-by-round log ----
  function gs(teklifci, alici) {
    var T = {}; Object.keys(TERCIH).forEach(function (k) { T[k] = TERCIH[k]; }); T.Sen = senSira.slice();
    var sira = {}; teklifci.forEach(function (p) { sira[p] = 0; });
    var tutulan = {}, serbest = teklifci.slice(), turlar = [];
    while (serbest.length) {
      var tur = { teklif: [], tut: [], ret: [] }, buTur = {};
      serbest.forEach(function (p) { var q = T[p][sira[p]]; tur.teklif.push([p, q]); (buTur[q] = buTur[q] || []).push(p); sira[p]++; });
      var yeniSerbest = [];
      Object.keys(buTur).forEach(function (q) {
        var adaylar = buTur[q].slice(); if (tutulan[q]) adaylar.push(tutulan[q]);
        adaylar.sort(function (a, b) { return T[q].indexOf(a) - T[q].indexOf(b); });
        var eski = tutulan[q]; tutulan[q] = adaylar[0];
        adaylar.slice(1).forEach(function (p) { tur.ret.push([p, q, p === eski]); yeniSerbest.push(p); });
        tur.tut.push([adaylar[0], q]);
      });
      turlar.push(tur); serbest = yeniSerbest;
    }
    var es = {}; Object.keys(tutulan).forEach(function (q) { es[q] = tutulan[q]; es[tutulan[q]] = q; });
    return { turlar: turlar, es: es, T: T };
  }
  function siraNo(T, a, b) { return T[a].indexOf(b) + 1; }

  // ---- scene ----
  var Y = [90, 190, 290, 390], XL = 180, XR = 620, VW = 800, DAR = false;
  var VH = 470;
  function olcu() { DAR = (kok.clientWidth || 800) < 560; VW = DAR ? 440 : 800; XL = DAR ? 90 : 180; XR = DAR ? 350 : 620; Y = DAR ? [80, 196, 312, 428] : [90, 190, 290, 390]; VH = DAR ? 520 : 470; }
  // a person's first choice (for 'Sen' what the player picked, empty if not yet chosen)
  function ilk(ad) { return ad === 'Sen' ? (senSira[0] ? A(senSira[0]) : '') : A(TERCIH[ad][0]); }
  function poz(ad) { var i = SOL.indexOf(ad); return i > -1 ? [XL, Y[i]] : [XR, Y[SAG.indexOf(ad)]]; }
  function sahneSVG() {
    olcu();
    var h = '<svg id="esSahne" class="es-sahne' + (DAR ? ' dar' : '') + '" viewBox="0 0 ' + VW + ' ' + VH + '" role="img" aria-label="The two banks of the village and the matches between them">' +
      '<defs><linearGradient id="esNehir" x1="0" x2="1"><stop offset="0" stop-color="#cfe2df"/><stop offset=".5" stop-color="#b9d6d2"/><stop offset="1" stop-color="#cfe2df"/></linearGradient>' +
      '<marker id="esOk" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="13" markerHeight="13" orient="auto"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>' +
      '<g transform="translate(' + (VW / 2 - 400) + ' 0)"><path d="M360 0C330 80 420 150 380 235S330 390 380 470H440C390 390 470 320 440 235S380 80 420 0Z" fill="url(#esNehir)" opacity=".75"/>' +
      '<path d="M372 60q12-8 24 0M398 160q12-8 24 0M382 300q12-8 24 0M396 410q12-8 24 0" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".8"/></g>' +
      '<text x="' + XL + '" y="30" text-anchor="middle" class="es-yaka" fill="' + R.bordo + '">Left bank</text><text x="' + XR + '" y="30" text-anchor="middle" class="es-yaka" fill="' + R.petrol + '">Right bank</text>' +
      '<g id="esCizgiler"></g><g id="esKisiler">';
    SOL.concat(SAG).forEach(function (ad) {
      var p = poz(ad), sol = SOL.indexOf(ad) > -1, renk = sol ? R.bordo : R.petrol, ben = ad === 'Sen';
      h += '<g class="es-kisi" data-ad="' + ad + '"><circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + (ben ? 32 : 28) + '" fill="' + (ben ? renk : '#fffaf2') + '" stroke="' + renk + '" stroke-width="4"/>' +
        '<text x="' + p[0] + '" y="' + (p[1] + 8) + '" text-anchor="middle" class="es-bas" fill="' + (ben ? '#fff' : renk) + '">' + (ben ? 'You' : A(ad).charAt(0)) + '</text>' +
        (DAR ? '<text x="' + p[0] + '" y="' + (p[1] + 52) + '" text-anchor="middle" class="es-ad">' + (ben ? '' : A(ad)) + '</text>' +
        '<text x="' + p[0] + '" y="' + (p[1] + (ben ? 54 : 76)) + '" text-anchor="middle" class="es-not es-ilk" data-ilk="' + ad + '">' + (ilk(ad) ? '♥ ' + ilk(ad) : '') + '</text>' :
        '<text x="' + (p[0] + (sol ? -46 : 46)) + '" y="' + (p[1] - 2) + '" text-anchor="' + (sol ? 'end' : 'start') + '" class="es-ad">' + (ben ? '' : A(ad)) + '</text>' +
        '<text x="' + (p[0] + (sol ? -46 : 46)) + '" y="' + (p[1] + 20) + '" text-anchor="' + (sol ? 'end' : 'start') + '" class="es-not es-ilk" data-ilk="' + ad + '">' + (ilk(ad) ? '♥ ' + ilk(ad) : '') + '</text>') +
        '<text class="es-rozet" x="' + (p[0] + (sol ? 42 : -42)) + '" y="' + (p[1] - 26) + '" text-anchor="middle"></text></g>';
    });
    return h + '</g><text id="esTur" x="' + VW / 2 + '" y="' + (VH - 4) + '" text-anchor="middle" class="es-tur"></text></svg>';
  }
  function yay(a, b, cls) {
    var p = poz(a), q = poz(b), sol = SOL.indexOf(a) > -1;
    var x1 = p[0] + (sol ? 34 : -34), x2 = q[0] + (sol ? -34 : 34);
    var mx = (x1 + x2) / 2, d = 'M' + x1 + ' ' + p[1] + 'C' + mx + ' ' + p[1] + ' ' + mx + ' ' + q[1] + ' ' + x2 + ' ' + q[1];
    var e = document.createElementNS(NS, 'path'); e.setAttribute('d', d); e.setAttribute('class', 'es-yay ' + cls);
    e.dataset.ab = a + '|' + b; document.getElementById('esCizgiler').appendChild(e);
    if (!hareketAz) { var L = e.getTotalLength(); e.style.strokeDasharray = L; e.style.strokeDashoffset = L; e.animate([{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: 520, fill: 'forwards', easing: 'ease-out' }); }
    return e;
  }

  // ---- step 1: you rank ----
  function bas() {
    senSira = [];
    kok.innerHTML = '<p class="oy-adim">Step 1 · Rank your choices</p>' + sahneSVG() +
      '<p class="oy-not" style="margin:6px 0 0">The ♥ shows each person’s first choice on the other bank. The full rankings are in the table below.</p>' +
      '<p class="oy-buyuk" style="margin-top:10px">How much do you want each person on the right bank? Tap them in order, starting with the one you want most.</p>' +
      '<div class="es-secim" id="esSecim">' + SAG.map(function (ad) { return '<button data-ad="' + ad + '"><b>' + A(ad) + '</b><span>' + NOT[ad] + '</span><i></i></button>'; }).join('') + '</div>' +
      '<div class="oy-dugmeler"><button class="oy-btn" id="esBasla" disabled>Match the village</button><button class="oy-btn ikincil" id="esSifirla">Reset</button><button class="oy-btn ikincil" id="esCins">Change gender choice</button></div>' +
      tercihTablosu(true);
    kok.querySelectorAll('#esSecim button').forEach(function (b) {
      b.onclick = function () {
        if (senSira.indexOf(b.dataset.ad) > -1) return;
        senSira.push(b.dataset.ad); b.classList.add('secili'); b.querySelector('i').textContent = senSira.length + '.';
        if (senSira.length === 3) { var son = SAG.filter(function (x) { return senSira.indexOf(x) < 0; })[0]; senSira.push(son); var bb = kok.querySelector('#esSecim button[data-ad="' + son + '"]'); bb.classList.add('secili'); bb.querySelector('i').textContent = '4.'; }
        document.getElementById('esBasla').disabled = senSira.length < 4;
        var tb = kok.querySelector('.es-tablo'); if (tb) tb.outerHTML = tercihTablosu(true);
        rozetler();
      };
    });
    document.getElementById('esSifirla').onclick = bas;
    var dc = document.getElementById('esCins'); if (dc) dc.onclick = cinsiyet;
    document.getElementById('esBasla').onclick = function () { O.iz('oyun-basladi', { oyun: 'eslesme' }); calistir('sol'); };
  }
  function rozetler() {
    var e = document.querySelector('.es-ilk[data-ilk="Sen"]'); if (e) e.textContent = ilk('Sen') ? '♥ ' + ilk('Sen') : '';
    SAG.forEach(function (ad) { var r = document.querySelector('.es-kisi[data-ad="' + ad + '"] .es-rozet'); var i = senSira.indexOf(ad); r.textContent = i > -1 ? (i + 1) + '.' : ''; });
  }
  function tercihTablosu(acik) {
    var satir = function (ad) { var l = ad === 'Sen' ? [0, 1, 2, 3].map(function (k) { return senSira[k] || '?'; }) : TERCIH[ad]; return '<tr><th class="' + (SOL.indexOf(ad) > -1 ? 'sen-r' : 'o-r') + '">' + A(ad) + '</th>' + l.map(function (x) { return '<td>' + A(x) + '</td>'; }).join('') + '</tr>'; };
    return '<details class="es-tablo"' + (acik ? ' open' : '') + '><summary>Everyone’s ranking</summary><div class="es-tablo-ic"><table><tr><th></th><th>1.</th><th>2.</th><th>3.</th><th>4.</th></tr>' +
      SOL.map(satir).join('') + SAG.map(satir).join('') + '</table><p class="oy-not">The villagers’ rankings are fixed. If you change your ranking, the result may change too.</p></div></details>';
  }

  // ---- steps 2–3: run the algorithm ----
  function calistir(taraf) {
    var tek = taraf === 'sol' ? SOL : SAG, al = taraf === 'sol' ? SAG : SOL, g = gs(tek, al);
    sonuc[taraf] = g;
    var baslik = taraf === 'sol' ? 'Step 2 · The left bank proposes' : 'Step 3 · Now the right bank proposes';
    var acik = taraf === 'sol' ? 'Everyone on the left bank proposes to the person at the top of their list. Whoever gets proposals keeps the one they like best “for now” and rejects the rest. Anyone rejected moves on to the next person on their list.' :
      'This time the right bank proposes and the left bank waits. The rankings are the same; only the side that makes the first move has changed.';
    kok.innerHTML = '<p class="oy-adim">' + baslik + '</p><p class="oy-not" style="margin:0 0 6px">' + acik + '</p>' + sahneSVG() + '<div class="es-gunluk" id="esGunluk" aria-live="polite"></div><div id="esAlt"></div>';
    rozetler();
    var gun = document.getElementById('esGunluk'), turYazi = document.getElementById('esTur');
    var p = Promise.resolve();
    g.turlar.forEach(function (tur, i) {
      p = p.then(function () {
        turYazi.textContent = 'Round ' + (i + 1);
        tur.teklif.forEach(function (t) { yay(t[0], t[1], 'teklif ' + (SOL.indexOf(t[0]) > -1 ? 'sol' : 'sag')); });
        gun.insertAdjacentHTML('beforeend', '<p><b>Round ' + (i + 1) + '.</b> ' + tur.teklif.map(function (t) { return A(t[0]) + ' → ' + A(t[1]); }).join(', ') + '</p>');
        return bekle(900);
      }).then(function () {
        tur.ret.forEach(function (r) {
          document.querySelectorAll('.es-yay').forEach(function (e) { if (e.dataset.ab === r[0] + '|' + r[1] || e.dataset.ab === r[1] + '|' + r[0]) { e.classList.add('ret'); e.animate([{ opacity: 1 }, { opacity: 0 }], { duration: hareketAz ? 1 : 700, delay: 250, fill: 'forwards' }).finished.then(function () { e.remove(); }); } });
        });
        tur.tut.forEach(function (t) { document.querySelectorAll('.es-yay').forEach(function (e) { if (e.dataset.ab === t[0] + '|' + t[1]) e.classList.add('tut'); }); });
        if (tur.ret.length) gun.insertAdjacentHTML('beforeend', '<p class="ret">Rejected: ' + tur.ret.map(function (r) { return A(r[0]) + (r[2] ? ' (had been kept in an earlier round)' : ''); }).join(', ') + '</p>');
        else gun.insertAdjacentHTML('beforeend', '<p class="tamam">Nobody was rejected. The matching is complete.</p>');
        gun.scrollTop = gun.scrollHeight;
        return bekle(1100);
      });
    });
    p.then(function () {
      turYazi.textContent = 'Done in ' + g.turlar.length + (g.turlar.length === 1 ? ' round' : ' rounds');
      document.querySelectorAll('.es-yay.tut').forEach(function (e) { e.classList.add('son'); });
      var ben = g.es.Sen, siram = siraNo(g.T, 'Sen', ben);
      var alt = document.getElementById('esAlt');
      alt.innerHTML = '<p class="oy-buyuk" style="margin-top:14px">You were matched with <span class="o-r">' + A(ben) + '</span>. That is your <b>' + sira(siram) + ' choice</b>.</p>' +
        '<div class="oy-dugmeler">' + (taraf === 'sol' ? '<button class="oy-btn petrol" id="esTers">Flip it: let the right bank propose</button>' : '<button class="oy-btn" id="esKarsilastir">Compare the results</button>') + '</div>';
      if (taraf === 'sol') document.getElementById('esTers').onclick = function () { calistir('sag'); kok.scrollIntoView({ behavior: 'smooth' }); };
      else document.getElementById('esKarsilastir').onclick = karsilastir;
    });
  }

  // ---- comparison ----
  function ort(g, grup) { return grup.reduce(function (a, p) { return a + siraNo(g.T, p, g.es[p]); }, 0) / grup.length; }
  function sayi(x) { return (Math.round(x * 10) / 10).toFixed(1); }
  function karsilastir() {
    var Asol = sonuc.sol, Bsag = sonuc.sag, sA = siraNo(Asol.T, 'Sen', Asol.es.Sen), sB = siraNo(Bsag.T, 'Sen', Bsag.es.Sen);
    var baslik = sA < sB ? 'The first move was worth ' + (sB - sA) + ((sB - sA) === 1 ? ' place' : ' places') : sA === sB ? 'Propose or wait, same result' : 'Waiting paid off for you';
    O.iz('oyun-bitti', { oyun: 'eslesme', sonuc: baslik });
    var rozet = function (n) { return '<i class="es-r r' + n + '">' + n + '.</i>'; };
    var tablo = '<table class="es-karsi"><tr><th>Person</th><th>When the left bank proposes</th><th>When the right bank proposes</th></tr>' +
      SOL.concat(SAG).map(function (p) {
        var a = Asol.es[p], b = Bsag.es[p];
        return '<tr' + (p === 'Sen' ? ' class="ben"' : '') + '><th class="' + (SOL.indexOf(p) > -1 ? 'sen-r' : 'o-r') + '">' + A(p) + '</th><td>' + A(a) + ' ' + rozet(siraNo(Asol.T, p, a)) + '</td><td>' + A(b) + ' ' + rozet(siraNo(Bsag.T, p, b)) + '</td></tr>';
      }).join('') + '</table>';
    var metin = sA < sB ?
      'When the left bank proposed, you got your ' + sira(sA) + ' choice; when you waited, you got your ' + sira(sB) + ' choice. The rankings did not change; only the side that made the first move did.' :
      sA === sB ? 'Your result did not change, but look at the table: for the rest of the village, the proposing side always did better.' :
      'This time waiting worked in your favour, because your own ranking crossed with the rest of the village in an unusual way. In the table, the overall trend still favours the side that proposes.';
    kok.innerHTML = '<div class="oy-sonuc"><p class="oy-adim">Comparison</p><h2>' + baslik + '</h2>' +
      '<div class="oy-olcu"><div><small>Left bank, proposing</small><b class="sen-r">' + sayi(ort(Asol, SOL)) + '</b><span>average rank of match</span></div><div><small>Left bank, waiting</small><b class="sen-r">' + sayi(ort(Bsag, SOL)) + '</b><span>average rank of match</span></div>' +
      '<div><small>Right bank, waiting</small><b class="o-r">' + sayi(ort(Asol, SAG)) + '</b><span>average rank of match</span></div><div><small>Right bank, proposing</small><b class="o-r">' + sayi(ort(Bsag, SAG)) + '</b><span>average rank of match</span></div></div>' +
      '<p>' + metin + '</p>' + tablo +
      '<p>This method is called the deferred acceptance algorithm. Gale and Shapley showed in 1962 that the resulting matching is <b>stable</b>: no two people would rather leave their partners and run off with each other. And the proposing side gets the best outcome for itself among all possible stable matchings. The idea is used in many markets, from school admissions to placing new doctors in hospitals, and it led to the 2012 Nobel Prize in Economics. There is a limit, too: in real life, preferences are not fixed and nobody writes down their list openly.</p>' +
      '<p class="not">In the book: Chapter 05 · The Love Market (Supply, Demand and Two-Sided Matching).</p>' +
      O.paylasHTML() + O.abone() +
      '<div class="oy-dugmeler"><button class="oy-btn ikincil" id="esYeniden">Play again with a different ranking</button></div></div>';
    O.paylasBagla(kok, { slug: 'eslesme', mesaj: 'In the Aşkonomi matching village: “' + baslik + '”. When I proposed I got my ' + sira(sA) + ' choice; when I waited, my ' + sira(sB) + ' choice.',
      kartAyar: { oyun: 'The matching village', baslik: baslik, alt: 'Proposing: ' + sira(sA) + ' choice · waiting: ' + sira(sB) + ' choice', ciz: function (x, X, Y0, W, H) { kartCiz(x, X, Y0, W, H, Asol, Bsag); } } });
    document.getElementById('esYeniden').onclick = function () { bas(); window.scrollTo({ top: 0, behavior: 'smooth' }); };
    kok.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function kartCiz(x, X, Y0, W, H, KA, KB) {
    var yarim = W / 2 - 20;
    [[KA, 'Left bank proposes', X], [KB, 'Right bank proposes', X + W / 2 + 20]].forEach(function (z) {
      var g = z[0], x0 = z[2], xl = x0 + 60, xr = x0 + yarim - 60;
      x.fillStyle = R.soluk; x.textAlign = 'center'; x.font = 'italic 400 30px "Crimson Pro", Georgia, serif'; x.fillText(z[1], x0 + yarim / 2, Y0 + 30);
      SOL.forEach(function (p, i) {
        var q = g.es[p], j = SAG.indexOf(q), y1 = Y0 + 110 + i * 130, y2 = Y0 + 110 + j * 130;
        x.strokeStyle = p === 'Sen' ? R.bordo : '#c7b9a6'; x.lineWidth = p === 'Sen' ? 8 : 4;
        x.beginPath(); x.moveTo(xl, y1); x.bezierCurveTo((xl + xr) / 2, y1, (xl + xr) / 2, y2, xr, y2); x.stroke();
      });
      SOL.forEach(function (p, i) { var y = Y0 + 110 + i * 130; x.fillStyle = p === 'Sen' ? R.bordo : '#fffaf2'; x.strokeStyle = R.bordo; x.lineWidth = 5; x.beginPath(); x.arc(xl, y, 30, 0, 7); x.fill(); x.stroke(); x.fillStyle = p === 'Sen' ? '#fff' : R.bordo; x.font = '600 26px Fraunces, Georgia, serif'; x.fillText(p === 'Sen' ? 'You' : A(p).charAt(0), xl, y + 9); });
      SAG.forEach(function (p, i) { var y = Y0 + 110 + i * 130; x.fillStyle = '#fffaf2'; x.strokeStyle = R.petrol; x.lineWidth = 5; x.beginPath(); x.arc(xr, y, 30, 0, 7); x.fill(); x.stroke(); x.fillStyle = R.petrol; x.font = '600 26px Fraunces, Georgia, serif'; x.fillText(A(p).charAt(0), xr, y + 9); });
    });
  }
  var CO = { oyun: 'eslesme', aciklama: 'The villagers’ (Turkish) names change with your choice. The game uses the classic two-sided matching model: you are on one bank, and the people you can be matched with are on the other.', kadin: 'Men on the other bank', erkek: 'Women on the other bank', belirsiz: 'Gender-neutral names' };
  function cinsiyet() { O.cinsSor(kok, CO, function (c) { cins = c; bas(); }); }
  O.cinsBaslat(kok, CO, function (c) { cins = c; bas(); });
})();
