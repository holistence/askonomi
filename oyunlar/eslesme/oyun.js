/* Eşleşme köyü — Gale–Shapley ertelenmiş kabul algoritması (Gale ve Shapley, 1962) */
(function () {
  'use strict';
  var O = window.OYUN, R = O.R, NS = 'http://www.w3.org/2000/svg';
  var kok = document.getElementById('oyun');
  var SOL = ['Sen', 'Deniz', 'Umut', 'Evren'], SAG = ['Ada', 'Ege', 'Yağmur', 'Derin'];
  // Diğerlerinin tercihleri sabit. Bu düzen bilgisayarla arandı: Her iki yönde de birkaç tur ret yaşanıyor,
  // oyuncunun 24 olası sıralamasının hepsinde kimin teklif ettiği eşleşmeyi değiştiriyor.
  var TERCIH = {
    Deniz: ['Ege', 'Yağmur', 'Derin', 'Ada'], Umut: ['Ada', 'Derin', 'Yağmur', 'Ege'], Evren: ['Derin', 'Ege', 'Ada', 'Yağmur'],
    Ada: ['Evren', 'Deniz', 'Sen', 'Umut'], Ege: ['Umut', 'Evren', 'Sen', 'Deniz'], 'Yağmur': ['Evren', 'Umut', 'Sen', 'Deniz'], Derin: ['Sen', 'Deniz', 'Umut', 'Evren']
  };
  var NOT = { Ada: 'kitap kurdu', Ege: 'gece kuşu', 'Yağmur': 'yol arkadaşı', Derin: 'şakacı', Deniz: 'aşçı', Umut: 'müzisyen', Evren: 'dağcı' };
  var senSira = [], sonuc = {};
  var hareketAz = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function bekle(ms) { return new Promise(function (r) { setTimeout(r, hareketAz ? 0 : ms); }); }

  // ---- algoritma: tur tur kayıt ----
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

  // ---- sahne ----
  var Y = [90, 190, 290, 390], XL = 180, XR = 620;
  function poz(ad) { var i = SOL.indexOf(ad); return i > -1 ? [XL, Y[i]] : [XR, Y[SAG.indexOf(ad)]]; }
  function sahneSVG() {
    var h = '<svg id="esSahne" class="es-sahne" viewBox="0 0 800 470" role="img" aria-label="Köyün iki yakası ve aralarındaki eşleşmeler">' +
      '<defs><linearGradient id="esNehir" x1="0" x2="1"><stop offset="0" stop-color="#cfe2df"/><stop offset=".5" stop-color="#b9d6d2"/><stop offset="1" stop-color="#cfe2df"/></linearGradient>' +
      '<marker id="esOk" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="13" markerHeight="13" orient="auto"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>' +
      '<path d="M360 0C330 80 420 150 380 235S330 390 380 470H440C390 390 470 320 440 235S380 80 420 0Z" fill="url(#esNehir)" opacity=".75"/>' +
      '<path d="M372 60q12-8 24 0M398 160q12-8 24 0M382 300q12-8 24 0M396 410q12-8 24 0" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".8"/>' +
      '<text x="' + XL + '" y="30" text-anchor="middle" class="es-yaka" fill="' + R.bordo + '">Sol yaka</text><text x="' + XR + '" y="30" text-anchor="middle" class="es-yaka" fill="' + R.petrol + '">Sağ yaka</text>' +
      '<g id="esCizgiler"></g><g id="esKisiler">';
    SOL.concat(SAG).forEach(function (ad) {
      var p = poz(ad), sol = SOL.indexOf(ad) > -1, renk = sol ? R.bordo : R.petrol, ben = ad === 'Sen';
      h += '<g class="es-kisi" data-ad="' + ad + '"><circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + (ben ? 32 : 28) + '" fill="' + (ben ? renk : '#fffaf2') + '" stroke="' + renk + '" stroke-width="4"/>' +
        '<text x="' + p[0] + '" y="' + (p[1] + 8) + '" text-anchor="middle" class="es-bas" fill="' + (ben ? '#fff' : renk) + '">' + (ben ? 'Sen' : ad.charAt(0)) + '</text>' +
        '<text x="' + (p[0] + (sol ? -46 : 46)) + '" y="' + (p[1] - 2) + '" text-anchor="' + (sol ? 'end' : 'start') + '" class="es-ad">' + (ben ? '' : ad) + '</text>' +
        '<text x="' + (p[0] + (sol ? -46 : 46)) + '" y="' + (p[1] + 20) + '" text-anchor="' + (sol ? 'end' : 'start') + '" class="es-not">' + (NOT[ad] || '') + '</text>' +
        '<text class="es-rozet" x="' + (p[0] + (sol ? 42 : -42)) + '" y="' + (p[1] - 26) + '" text-anchor="middle"></text></g>';
    });
    return h + '</g><text id="esTur" x="400" y="458" text-anchor="middle" class="es-tur"></text></svg>';
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

  // ---- 1. adım: sen sırala ----
  function bas() {
    senSira = [];
    kok.innerHTML = '<p class="oy-adim">1. adım · Tercihlerini sırala</p>' + sahneSVG() +
      '<p class="oy-buyuk" style="margin-top:10px">Sağ yakadan kimi ne kadar istiyorsun? En çok istediğinden başlayarak dokun.</p>' +
      '<div class="es-secim" id="esSecim">' + SAG.map(function (ad) { return '<button data-ad="' + ad + '"><b>' + ad + '</b><span>' + NOT[ad] + '</span><i></i></button>'; }).join('') + '</div>' +
      '<div class="oy-dugmeler"><button class="oy-btn" id="esBasla" disabled>Köyü eşleştir</button><button class="oy-btn ikincil" id="esSifirla">Sıfırla</button></div>' +
      tercihTablosu(false);
    kok.querySelectorAll('#esSecim button').forEach(function (b) {
      b.onclick = function () {
        if (senSira.indexOf(b.dataset.ad) > -1) return;
        senSira.push(b.dataset.ad); b.classList.add('secili'); b.querySelector('i').textContent = senSira.length + '.';
        if (senSira.length === 3) { var son = SAG.filter(function (x) { return senSira.indexOf(x) < 0; })[0]; senSira.push(son); var bb = kok.querySelector('#esSecim button[data-ad="' + son + '"]'); bb.classList.add('secili'); bb.querySelector('i').textContent = '4.'; }
        document.getElementById('esBasla').disabled = senSira.length < 4;
        rozetler();
      };
    });
    document.getElementById('esSifirla').onclick = bas;
    document.getElementById('esBasla').onclick = function () { O.iz('oyun-basladi', { oyun: 'eslesme' }); calistir('sol'); };
  }
  function rozetler() {
    SAG.forEach(function (ad) { var r = document.querySelector('.es-kisi[data-ad="' + ad + '"] .es-rozet'); var i = senSira.indexOf(ad); r.textContent = i > -1 ? (i + 1) + '.' : ''; });
  }
  function tercihTablosu(acik) {
    var satir = function (ad) { var l = ad === 'Sen' ? (senSira.length === 4 ? senSira : ['?', '?', '?', '?']) : TERCIH[ad]; return '<tr><th class="' + (SOL.indexOf(ad) > -1 ? 'sen-r' : 'o-r') + '">' + ad + '</th>' + l.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr>'; };
    return '<details class="es-tablo"' + (acik ? ' open' : '') + '><summary>Herkesin tercih sırası</summary><div class="es-tablo-ic"><table><tr><th></th><th>1.</th><th>2.</th><th>3.</th><th>4.</th></tr>' +
      SOL.map(satir).join('') + SAG.map(satir).join('') + '</table><p class="oy-not">Köydekilerin tercihleri sabit. Senin sıran değiştikçe sonuç da değişebilir.</p></div></details>';
  }

  // ---- 2–3. adım: algoritmayı oynat ----
  function calistir(taraf) {
    var tek = taraf === 'sol' ? SOL : SAG, al = taraf === 'sol' ? SAG : SOL, g = gs(tek, al);
    sonuc[taraf] = g;
    var baslik = taraf === 'sol' ? '2. adım · Sol yaka teklif ediyor' : '3. adım · Şimdi sağ yaka teklif ediyor';
    var acik = taraf === 'sol' ? 'Sol yakadaki herkes, listesinin başındakine teklif eder. Teklif alan, gelenler arasından en çok istediğini “şimdilik” tutar, diğerlerini reddeder. Reddedilen, listesindeki sıradakine gider.' :
      'Bu kez sağ yaka teklif ediyor, sol yaka bekliyor. Tercihler aynı, yalnızca ilk adımı atan taraf değişti.';
    kok.innerHTML = '<p class="oy-adim">' + baslik + '</p><p class="oy-not" style="margin:0 0 6px">' + acik + '</p>' + sahneSVG() + '<div class="es-gunluk" id="esGunluk" aria-live="polite"></div><div id="esAlt"></div>';
    rozetler();
    var gun = document.getElementById('esGunluk'), turYazi = document.getElementById('esTur');
    var p = Promise.resolve();
    g.turlar.forEach(function (tur, i) {
      p = p.then(function () {
        turYazi.textContent = 'Tur ' + (i + 1);
        tur.teklif.forEach(function (t) { yay(t[0], t[1], 'teklif ' + (SOL.indexOf(t[0]) > -1 ? 'sol' : 'sag')); });
        gun.insertAdjacentHTML('beforeend', '<p><b>Tur ' + (i + 1) + '.</b> ' + tur.teklif.map(function (t) { return t[0] + ' → ' + t[1]; }).join(', ') + '</p>');
        return bekle(900);
      }).then(function () {
        tur.ret.forEach(function (r) {
          document.querySelectorAll('.es-yay').forEach(function (e) { if (e.dataset.ab === r[0] + '|' + r[1] || e.dataset.ab === r[1] + '|' + r[0]) { e.classList.add('ret'); e.animate([{ opacity: 1 }, { opacity: 0 }], { duration: hareketAz ? 1 : 700, delay: 250, fill: 'forwards' }).finished.then(function () { e.remove(); }); } });
        });
        tur.tut.forEach(function (t) { document.querySelectorAll('.es-yay').forEach(function (e) { if (e.dataset.ab === t[0] + '|' + t[1]) e.classList.add('tut'); }); });
        if (tur.ret.length) gun.insertAdjacentHTML('beforeend', '<p class="ret">Reddedilen: ' + tur.ret.map(function (r) { return r[0] + (r[2] ? ' (önceki turda tutulmuştu)' : ''); }).join(', ') + '</p>');
        else gun.insertAdjacentHTML('beforeend', '<p class="tamam">Kimse reddedilmedi. Eşleşme tamamlandı.</p>');
        gun.scrollTop = gun.scrollHeight;
        return bekle(1100);
      });
    });
    p.then(function () {
      turYazi.textContent = g.turlar.length + ' turda tamamlandı';
      document.querySelectorAll('.es-yay.tut').forEach(function (e) { e.classList.add('son'); });
      var ben = g.es.Sen, siram = siraNo(g.T, 'Sen', ben);
      var alt = document.getElementById('esAlt');
      alt.innerHTML = '<p class="oy-buyuk" style="margin-top:14px">Sen <span class="o-r">' + ben + '</span> ile eşleştin. Bu, listendeki <b>' + siram + '. tercihin</b>.</p>' +
        '<div class="oy-dugmeler">' + (taraf === 'sol' ? '<button class="oy-btn petrol" id="esTers">Tersini dene: Sağ yaka teklif etsin</button>' : '<button class="oy-btn" id="esKarsilastir">Sonuçları karşılaştır</button>') + '</div>';
      if (taraf === 'sol') document.getElementById('esTers').onclick = function () { calistir('sag'); kok.scrollIntoView({ behavior: 'smooth' }); };
      else document.getElementById('esKarsilastir').onclick = karsilastir;
    });
  }

  // ---- karşılaştırma ----
  function ort(g, grup) { return grup.reduce(function (a, p) { return a + siraNo(g.T, p, g.es[p]); }, 0) / grup.length; }
  function sayi(x) { return (Math.round(x * 10) / 10).toFixed(1).replace('.', ','); }
  function karsilastir() {
    var A = sonuc.sol, B = sonuc.sag, sA = siraNo(A.T, 'Sen', A.es.Sen), sB = siraNo(B.T, 'Sen', B.es.Sen);
    var baslik = sA < sB ? 'İlk adımın değeri: ' + (sB - sA) + ' sıra' : sA === sB ? 'Teklif etsen de beklesen de aynı' : 'Beklemek sana yaradı';
    O.iz('oyun-bitti', { oyun: 'eslesme', sonuc: baslik });
    var rozet = function (n) { return '<i class="es-r r' + n + '">' + n + '.</i>'; };
    var tablo = '<table class="es-karsi"><tr><th>Kişi</th><th>Sol yaka teklif edince</th><th>Sağ yaka teklif edince</th></tr>' +
      SOL.concat(SAG).map(function (p) {
        var a = A.es[p], b = B.es[p];
        return '<tr' + (p === 'Sen' ? ' class="ben"' : '') + '><th class="' + (SOL.indexOf(p) > -1 ? 'sen-r' : 'o-r') + '">' + p + '</th><td>' + a + ' ' + rozet(siraNo(A.T, p, a)) + '</td><td>' + b + ' ' + rozet(siraNo(B.T, p, b)) + '</td></tr>';
      }).join('') + '</table>';
    var metin = sA < sB ?
      'Sol yaka teklif ettiğinde sen ' + sA + '. tercihinle, beklediğinde ' + sB + '. tercihinle eşleştin. Tercihler değişmedi, yalnızca ilk adımı atan taraf değişti.' :
      sA === sB ? 'Senin sonucun değişmedi, ama tabloya bak: Köyün geri kalanında teklif eden taraf hep daha iyi sonuç aldı.' :
      'Bu sefer beklemek senin işine yaradı, çünkü kendi tercih sıran köyün geri kalanıyla farklı kesişti. Tabloda genel eğilim yine teklif edenin lehine.';
    kok.innerHTML = '<div class="oy-sonuc"><p class="oy-adim">Karşılaştırma</p><h2>' + baslik + '</h2>' +
      '<div class="oy-olcu"><div><small>Sol yaka, teklif edince</small><b class="sen-r">' + sayi(ort(A, SOL)) + '</b><span>ortalama tercih sırası</span></div><div><small>Sol yaka, beklerken</small><b class="sen-r">' + sayi(ort(B, SOL)) + '</b><span>ortalama tercih sırası</span></div>' +
      '<div><small>Sağ yaka, beklerken</small><b class="o-r">' + sayi(ort(A, SAG)) + '</b><span>ortalama tercih sırası</span></div><div><small>Sağ yaka, teklif edince</small><b class="o-r">' + sayi(ort(B, SAG)) + '</b><span>ortalama tercih sırası</span></div></div>' +
      '<p>' + metin + '</p>' + tablo +
      '<p>Bu yöntemin adı ertelenmiş kabul algoritması. Gale ve Shapley 1962’de gösterdi: Sonuçta oluşan eşleşme <b>kararlıdır</b>, yani hiçbir iki kişi mevcut eşlerini bırakıp birbirlerine kaçmak istemez. Ve teklif eden taraf, mümkün kararlı eşleşmeler arasında kendisi için en iyisini alır. Bu fikir, okul yerleştirmeden yeni hekimlerin hastanelere yerleştirilmesine kadar pek çok piyasada kullanılıyor ve 2012 Nobel İktisat Ödülü’nü getirdi. Bir sınır da var: Gerçek hayatta tercihler sabit değildir ve kimse listesini açıkça yazmaz.</p>' +
      '<p class="not">Kitapta: Bölüm 05 · Aşk Piyasası (Arz, Talep ve İki Taraflı Eşleşme).</p>' +
      O.paylasHTML() + O.abone() +
      '<div class="oy-dugmeler"><button class="oy-btn ikincil" id="esYeniden">Farklı bir sırayla yeniden oyna</button></div></div>';
    O.paylasBagla(kok, { slug: 'eslesme', mesaj: 'Aşkonomi eşleşme köyünde: “' + baslik + '”. Teklif ettiğimde ' + sA + '. tercihimle, beklediğimde ' + sB + '. tercihimle eşleştim.',
      kartAyar: { oyun: 'Eşleşme köyü', baslik: baslik, alt: 'Teklif edince ' + sA + '. tercih · beklerken ' + sB + '. tercih', ciz: function (x, X, Y0, W, H) { kartCiz(x, X, Y0, W, H, A, B); } } });
    document.getElementById('esYeniden').onclick = function () { bas(); window.scrollTo({ top: 0, behavior: 'smooth' }); };
    kok.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function kartCiz(x, X, Y0, W, H, A, B) {
    var yarim = W / 2 - 20;
    [[A, 'Sol yaka teklif edince', X], [B, 'Sağ yaka teklif edince', X + W / 2 + 20]].forEach(function (z) {
      var g = z[0], x0 = z[2], xl = x0 + 60, xr = x0 + yarim - 60;
      x.fillStyle = R.soluk; x.textAlign = 'center'; x.font = 'italic 400 30px "Crimson Pro", Georgia, serif'; x.fillText(z[1], x0 + yarim / 2, Y0 + 30);
      SOL.forEach(function (p, i) {
        var q = g.es[p], j = SAG.indexOf(q), y1 = Y0 + 110 + i * 130, y2 = Y0 + 110 + j * 130;
        x.strokeStyle = p === 'Sen' ? R.bordo : '#c7b9a6'; x.lineWidth = p === 'Sen' ? 8 : 4;
        x.beginPath(); x.moveTo(xl, y1); x.bezierCurveTo((xl + xr) / 2, y1, (xl + xr) / 2, y2, xr, y2); x.stroke();
      });
      SOL.forEach(function (p, i) { var y = Y0 + 110 + i * 130; x.fillStyle = p === 'Sen' ? R.bordo : '#fffaf2'; x.strokeStyle = R.bordo; x.lineWidth = 5; x.beginPath(); x.arc(xl, y, 30, 0, 7); x.fill(); x.stroke(); x.fillStyle = p === 'Sen' ? '#fff' : R.bordo; x.font = '600 26px Fraunces, Georgia, serif'; x.fillText(p === 'Sen' ? 'Sen' : p.charAt(0), xl, y + 9); });
      SAG.forEach(function (p, i) { var y = Y0 + 110 + i * 130; x.fillStyle = '#fffaf2'; x.strokeStyle = R.petrol; x.lineWidth = 5; x.beginPath(); x.arc(xr, y, 30, 0, 7); x.fill(); x.stroke(); x.fillStyle = R.petrol; x.font = '600 26px Fraunces, Georgia, serif'; x.fillText(p.charAt(0), xr, y + 9); });
    });
  }
  bas();
})();
