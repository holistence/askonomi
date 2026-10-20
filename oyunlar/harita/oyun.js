/* Türkiye’nin aşk haritası — TÜİK il verileri, 2014–2025 zaman serisi ve 2025 kesitleri */
(function () {
  'use strict';
  var O = window.OYUN, R = O.R, H = window.HARITA, NS = 'http://www.w3.org/2000/svg';
  var kok = document.getElementById('oyun');
  if (!H) { kok.textContent = 'Harita verisi yüklenemedi.'; return; }
  var Y = H.yillar, SON = Y.length - 1;
  // seri: 2014–2025 dizisi; diğerleri yalnız 2025
  var GOS = {
    ev: { ad: 'Evlenme hızı', grup: 'Evlilik', seri: true, birim: 'bin kişide evlenme', ek: '‰', d: 2, renk: ['#f4e6c8', '#e3c27a', '#c99a2e', '#9a7116', '#5f4509'] },
    ilkK: { ad: 'İlk evlenme yaşı', grup: 'Evlilik', seri: true, birim: 'kadınlarda ortalama ilk evlenme yaşı', ek: ' yaş', d: 1, renk: ['#f6e3e6', '#e8b3bd', '#d07a8b', '#a84a61', '#6b2238'], cins: 'K' },
    ilkE: { ad: 'İlk evlenme yaşı', grup: 'Evlilik', seri: true, birim: 'erkeklerde ortalama ilk evlenme yaşı', ek: ' yaş', d: 1, renk: ['#e2ecf0', '#aecbd6', '#6fa2b6', '#3b7690', '#1c4a5e'], cins: 'E', gizli: true },
    kadinB: { ad: 'Kadın daha büyük', grup: 'Evlilik', seri: false, birim: 'kadının erkekten büyük olduğu evliliklerin payı (%)', ek: '%', d: 1, renk: ['#f2e5ef', '#dcb7d1', '#bd82ad', '#8f4f80', '#5a2a51'] },
    bos: { ad: 'Boşanma hızı', grup: 'Boşanma', seri: true, birim: 'bin kişide boşanma', ek: '‰', d: 2, renk: ['#f3dde0', '#e2a5ad', '#c9586a', '#a3283c', '#651423'] },
    oran: { ad: 'Boşanma / evlenme', grup: 'Boşanma', seri: true, birim: 'her 100 evlenmeye karşı boşanma', ek: '', d: 0, renk: ['#dbecea', '#a2cbc6', '#5e9e9a', '#2b726f', '#13403e'] },
    hizli: { ad: 'Hızlı boşanma', grup: 'Boşanma', seri: false, birim: '2 aydan kısa sürede sonuçlanan boşanma davalarının payı (%)', ek: '%', d: 1, renk: ['#eee8dc', '#d6c6a4', '#b39a62', '#86703a', '#54451f'] },
    tdh: { ad: 'Çocuk sayısı', grup: 'Aile', seri: false, birim: 'kadın başına ortalama çocuk (toplam doğurganlık hızı)', ek: ' çocuk', d: 2, renk: ['#e6e1ef', '#bfb1d8', '#8f78b8', '#634892', '#3a2560'] },
    hane: { ad: 'Hane büyüklüğü', grup: 'Aile', seri: false, birim: 'bir hanede ortalama kişi', ek: ' kişi', d: 2, renk: ['#e3ece0', '#b6cfad', '#7fa874', '#4e7b45', '#28481f'] }
  };
  var KAYNAK = {
    ev: 'TÜİK Evlenme İstatistikleri, il evlenme sayıları 2014–2025; nüfus TÜİK ADNKS', ilkK: 'TÜİK, il ve cinsiyete göre ortalama ilk evlenme yaşı', ilkE: 'TÜİK, il ve cinsiyete göre ortalama ilk evlenme yaşı',
    kadinB: 'TÜİK, il ve eşlerin yaş farkına göre evlilikler, 2025', bos: 'TÜİK Boşanma İstatistikleri, il boşanma sayıları 2014–2025; nüfus TÜİK ADNKS', oran: 'TÜİK il evlenme ve boşanma sayıları 2014–2025',
    hizli: 'TÜİK, il ve dava süresine göre boşanmalar, 2025', tdh: 'TÜİK Doğum İstatistikleri 2025 (ikincil kaynak üzerinden)', hane: 'TÜİK ADNKS 2025, ortalama hanehalkı büyüklüğü'
  };
  var gos = 'ev', yi = SON, secili = null, hover = null, oynuyor = null;
  function g() { return GOS[gos]; }
  function deger(i, k, y) { k = k || gos; var v = i[k]; return GOS[k].seri ? v[y === undefined ? yi : y] : v; }
  function trDeger(k, y) { k = k || gos; var v = H.tr[k]; return GOS[k].seri ? v[y === undefined ? yi : y] : v; }
  function f(x, k) { k = k || gos; var d = GOS[k].d; return d === 0 ? String(Math.round(x)) : x.toFixed(d).replace('.', ','); }
  function fe(x, k) { return f(x, k) + GOS[k || gos].ek; }
  function cinsAd(k) { k = k || gos; return GOS[k].cins ? (GOS[k].cins === 'K' ? ' (kadın)' : ' (erkek)') : ''; }

  // renk sınıfları: seri göstergelerde bütün yılların havuzundan, böylece renkler yıllar arasında karşılaştırılabilir
  var SINIF = {};
  Object.keys(GOS).forEach(function (k) {
    var v = [];
    H.iller.forEach(function (i) { if (GOS[k].seri) i[k].forEach(function (x) { v.push(x); }); else v.push(i[k]); });
    v.sort(function (a, b) { return a - b; });
    SINIF[k] = { s: [0.2, 0.4, 0.6, 0.8].map(function (q) { return v[Math.floor(q * (v.length - 1))]; }), min: v[0], max: v[v.length - 1] };
  });
  function renk(i) { var x = deger(i), k = 0; SINIF[gos].s.forEach(function (e) { if (x > e) k++; }); return g().renk[k]; }
  function sira(i) { var l = H.iller.slice().sort(function (a, b) { return deger(b) - deger(a); }); return l.indexOf(i) + 1; }

  // ---------- iskelet ----------
  var gruplar = ['Evlilik', 'Boşanma', 'Aile'];
  kok.innerHTML =
    '<div class="hr-gos" role="tablist" aria-label="Gösterge">' + gruplar.map(function (gr) {
      return '<div class="hr-grup"><small>' + gr + '</small><div>' + Object.keys(GOS).filter(function (k) { return GOS[k].grup === gr && !GOS[k].gizli; }).map(function (k) {
        return '<button role="tab" data-g="' + k + '" aria-selected="false">' + GOS[k].ad + (GOS[k].seri ? '' : ' <em>2025</em>') + '</button>';
      }).join('') + '</div></div>';
    }).join('') + '</div>' +
    '<div class="hr-ara-satir"><div class="hr-cins" id="hrCins" hidden><span>Kimin yaşı?</span><button data-c="K">Kadın</button><button data-c="E">Erkek</button></div>' +
    '<label class="hr-ara"><span class="gizli">İl ara</span><input id="hrAra" list="hrListe" placeholder="İlini yaz, örneğin Çanakkale" autocomplete="off"><datalist id="hrListe">' + H.iller.slice().sort(function (a, b) { return a.il.localeCompare(b.il, 'tr'); }).map(function (i) { return '<option value="' + i.il + '">'; }).join('') + '</datalist></label></div>' +
    '<div class="hr-cerceve"><div class="hr-yil-buyuk" id="hrYilB" aria-hidden="true"></div><svg id="hrSvg" class="hr-svg" viewBox="' + H.viewBox + '" role="img" aria-label="Türkiye il haritası"><g id="hrIller"></g><g id="hrVurgu"></g></svg>' +
    '<div class="hr-ipucu" id="hrIpucu" hidden></div></div>' +
    '<div class="hr-zaman" id="hrZaman"><button class="hr-oynat" id="hrOynat" aria-label="Yılları oynat"><svg viewBox="0 0 24 24"><path d="M7 5l12 7l-12 7z"/></svg></button>' +
    '<div class="hr-kaydir"><input type="range" id="hrYil" min="0" max="' + SON + '" step="1" value="' + SON + '" aria-label="Yıl"><div class="hr-yillar">' + Y.map(function (y, k) { return '<span' + (k % 2 && k !== SON ? ' class="ara"' : '') + '>' + y + '</span>'; }).join('') + '</div></div></div>' +
    '<div class="hr-lejant" id="hrLejant"></div>' +
    '<div class="hr-alt"><div class="hr-kart" id="hrKart" aria-live="polite"></div><div class="hr-uclar" id="hrUclar"></div></div>' +
    '<p class="oy-not hr-kaynak" id="hrKaynak"></p><div id="hrSon"></div>';

  var gEl = document.getElementById('hrIller');
  H.iller.forEach(function (i) {
    var p = document.createElementNS(NS, 'path'); p.setAttribute('d', i.d); p.setAttribute('class', 'hr-il'); p.dataset.p = i.p;
    p.setAttribute('tabindex', '0'); p.setAttribute('role', 'button'); p.setAttribute('aria-label', i.il);
    p.addEventListener('pointerenter', function (e) { hover = i; ipucu(e); });
    p.addEventListener('pointermove', ipucu);
    p.addEventListener('pointerleave', function () { hover = null; document.getElementById('hrIpucu').hidden = true; });
    p.addEventListener('click', function () { sec(i); });
    p.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sec(i); } });
    gEl.appendChild(p); i.el = p;
  });
  function ipucu(e) {
    if (!hover || e.pointerType === 'touch') return;
    var t = document.getElementById('hrIpucu'), c = t.parentNode.getBoundingClientRect();
    t.hidden = false; t.innerHTML = '<b>' + hover.il + '</b> ' + fe(deger(hover)) + ' <span>' + (g().seri ? Y[yi] : 2025) + '</span>';
    var x = e.clientX - c.left + 14, y = e.clientY - c.top - 36;
    t.style.left = Math.min(x, c.width - t.offsetWidth - 4) + 'px'; t.style.top = Math.max(0, y) + 'px';
  }

  // ---------- çizim ----------
  function boya() {
    H.iller.forEach(function (i) { i.el.style.fill = renk(i); });
    var S = SINIF[gos], sinir = [S.min].concat(S.s).concat([S.max]);
    document.getElementById('hrLejant').innerHTML = '<span>' + g().birim + ', ' + (g().seri ? Y[yi] : 2025) + '</span><div>' + g().renk.map(function (c, k) { return '<i style="background:' + c + '"><em>' + f(sinir[k]) + '–' + f(sinir[k + 1]) + '</em></i>'; }).join('') + '</div><span class="hr-tr">Türkiye: <b>' + fe(trDeger()) + '</b></span>';
    document.getElementById('hrYilB').textContent = g().seri ? Y[yi] : '2025';
    document.getElementById('hrZaman').classList.toggle('kapali', !g().seri);
    document.getElementById('hrYil').disabled = !g().seri; document.getElementById('hrOynat').disabled = !g().seri;
    var l = H.iller.slice().sort(function (a, b) { return deger(b) - deger(a); });
    var li = function (i) { return '<li><button data-p="' + i.p + '">' + i.il + '</button><b>' + f(deger(i)) + '</b></li>'; };
    var h = '<div><small>En yüksek</small><ol>' + l.slice(0, 5).map(li).join('') + '</ol></div><div><small>En düşük</small><ol>' + l.slice(-5).reverse().map(li).join('') + '</ol></div>';
    if (g().seri) {
      var dg = H.iller.map(function (i) { return { i: i, d: i[gos][SON] - i[gos][0] }; }).sort(function (a, b) { return b.d - a.d; });
      var lc = function (x) { return '<li><button data-p="' + x.i.p + '">' + x.i.il + '</button><b>' + (x.d >= 0 ? '+' : '−') + f(Math.abs(x.d)) + '</b></li>'; };
      var ust = dg[0].d > 0 ? '2014’ten 2025’e en çok artan' : '2014’ten 2025’e en az azalan';
      var alt = dg[dg.length - 1].d < 0 ? 'En çok azalan' : 'En az artan';
      h += '<div class="hr-degisim"><small>' + ust + '</small><ol>' + dg.slice(0, 3).map(lc).join('') + '</ol></div><div class="hr-degisim"><small>' + alt + '</small><ol>' + dg.slice(-3).reverse().map(lc).join('') + '</ol></div>';
    }
    document.getElementById('hrUclar').innerHTML = h;
    document.querySelectorAll('#hrUclar button').forEach(function (b) { b.onclick = function () { sec(H.iller.filter(function (i) { return i.p === +b.dataset.p; })[0]); }; });
    document.getElementById('hrKaynak').innerHTML = 'Kaynak: ' + KAYNAK[gos] + '. ' + (gos === 'ev' || gos === 'bos' ? 'Kaba hız, olay sayısının yıl ortası il nüfusuna bölünüp binle çarpılmasıyla hesaplandı. Bu yöntem TÜİK’in yayımladığı il kaba boşanma hızlarını tekrar eder. ' : '') + 'Harita sınırları: alpers/Turkey-Maps-GeoJSON, Apache 2.0 lisansı.';
    kart();
  }
  function spark(i, k) {
    var W = 300, Hh = 92, P = 6, a = i[k], t = H.tr[k], hepsi = a.concat(t), yy = GOS[gos].seri ? yi : SON;
    var mn = Math.min.apply(null, hepsi), mx = Math.max.apply(null, hepsi); if (mx - mn < 1e-6) mx = mn + 1;
    var x = function (j) { return P + j * (W - 2 * P) / SON; }, y = function (v) { return P + 16 + (1 - (v - mn) / (mx - mn)) * (Hh - 2 * P - 16); };
    var yol = function (s) { return s.map(function (v, j) { return (j ? 'L' : 'M') + x(j).toFixed(1) + ' ' + y(v).toFixed(1); }).join(''); };
    return '<div class="hr-sp-kap"><small>' + GOS[k].ad + cinsAd(k) + ', 2014–2025</small><svg class="hr-spark" viewBox="0 0 ' + W + ' ' + (Hh + 16) + '" role="img" aria-label="' + i.il + ' ve Türkiye, 2014–2025">' +
      '<path d="' + yol(t) + '" fill="none" stroke="#b9ad9c" stroke-width="2" stroke-dasharray="4 4"/>' +
      '<path d="' + yol(a) + '" fill="none" stroke="' + GOS[k].renk[3] + '" stroke-width="3" stroke-linejoin="round"/>' +
      '<line x1="' + x(yy) + '" x2="' + x(yy) + '" y1="' + (P + 12) + '" y2="' + (Hh - P) + '" stroke="#262028" stroke-width="1" opacity=".35"/>' +
      '<circle cx="' + x(yy) + '" cy="' + y(a[yy]) + '" r="4.5" fill="' + GOS[k].renk[3] + '"/>' +
      '<text x="' + x(0) + '" y="' + (Hh + 13) + '" class="hr-sp-e">2014</text><text x="' + x(SON) + '" y="' + (Hh + 13) + '" text-anchor="end" class="hr-sp-e">2025</text>' +
      '<text x="' + (x(yy) + (yy > SON / 2 ? -6 : 6)) + '" y="' + (P + 9) + '" text-anchor="' + (yy > SON / 2 ? 'end' : 'start') + '" class="hr-sp-d">' + Y[yy] + ': ' + fe(a[yy], k) + '</text></svg>' +
      '<p class="hr-sp-l"><i style="background:' + GOS[k].renk[3] + '"></i>' + i.il + ' <i class="kesik"></i>Türkiye</p></div>';
  }
  function satir(ad, k, i) {
    var yy = GOS[gos].seri ? yi : SON, v = GOS[k].seri ? i[k][yy] : i[k], t = GOS[k].seri ? H.tr[k][yy] : H.tr[k], d = v - t, S = SINIF[k];
    var w = (v - S.min) / (S.max - S.min) * 100, tw = (t - S.min) / (S.max - S.min) * 100;
    return '<div class="hr-c"><span>' + ad + '</span><div class="hr-c-ic"><i style="width:' + Math.max(3, w) + '%;background:' + GOS[k].renk[3] + '"></i><u style="left:' + tw + '%"></u></div><b>' + f(v, k) + '</b><small>' + (d >= 0 ? '+' : '−') + f(Math.abs(d), k) + '</small></div>';
  }
  function cocukSatir(i) {
    var ikon = '';
    for (var j = 0; j < 5; j++) {
      var dol = Math.max(0, Math.min(1, i.tdh - j));
      ikon += '<svg viewBox="0 0 24 24" class="hr-cocuk"><defs><clipPath id="hc' + i.p + j + '"><rect width="' + (24 * dol) + '" height="24"/></clipPath></defs><g fill="none" stroke="#634892" stroke-width="1.6"><circle cx="12" cy="7" r="3.6"/><path d="M5.5 21c.6-5.4 3.2-8.2 6.5-8.2s5.9 2.8 6.5 8.2z"/></g><g clip-path="url(#hc' + i.p + j + ')" fill="#634892"><circle cx="12" cy="7" r="3.6"/><path d="M5.5 21c.6-5.4 3.2-8.2 6.5-8.2s5.9 2.8 6.5 8.2z"/></g></svg>';
    }
    var d = i.tdh - H.tr.tdh;
    return '<div class="hr-c hr-c-cocuk"><span>Çocuk (2025)</span><div class="hr-ikonlar">' + ikon + '</div><b>' + f(i.tdh, 'tdh') + '</b><small>' + (d >= 0 ? '+' : '−') + f(Math.abs(d), 'tdh') + '</small></div>';
  }
  function kart() {
    var k = document.getElementById('hrKart');
    if (!secili) { k.innerHTML = '<p class="oy-buyuk" style="margin:0">Haritada bir ile dokun ya da ilini ara.</p><p class="oy-not">Yıl çubuğunu kaydır ya da oynat düğmesiyle 2014’ten 2025’e izle. Renk ölçeği bütün yıllar için aynıdır, böylece zaman içindeki değişim görünür.</p>'; return; }
    var i = secili, yy = g().seri ? yi : SON, yil = Y[yy];
    var degisim = g().seri ? (function () { var d = i[gos][SON] - i[gos][0], dt = H.tr[gos][SON] - H.tr[gos][0]; return '<p class="hr-deg">2014’ten 2025’e: <b>' + (d >= 0 ? '+' : '−') + f(Math.abs(d)) + g().ek + '</b> <span>(Türkiye ' + (dt >= 0 ? '+' : '−') + f(Math.abs(dt)) + g().ek + ')</span></p>'; })() : '';
    var n = function (a) { return a.toLocaleString('tr-TR'); };
    k.innerHTML = '<p class="oy-adim">' + i.p + ' plaka · 81 il arasında ' + sira(i) + '. · ' + (g().seri ? yil : 2025) + '</p><h3 class="hr-il-ad">' + i.il + '</h3>' +
      '<div class="hr-buyuk"><b>' + fe(deger(i)) + '</b><span>' + g().birim + '</span></div>' + degisim +
      spark(i, g().seri ? gos : 'ev') +
      '<div class="hr-cubuklar"><small class="hr-yil-not">' + yil + ' değerleri · dikey çizgi Türkiye</small>' +
      satir('Evlenme ‰', 'ev', i) + satir('Boşanma ‰', 'bos', i) + satir('İlk evlilik, K', 'ilkK', i) + satir('İlk evlilik, E', 'ilkE', i) + cocukSatir(i) + satir('Hane (2025)', 'hane', i) + '</div>' +
      '<p class="hr-oran">' + yil + '’te ' + n(i.nE[yy]) + ' evlilik, ' + n(i.nB[yy]) + ' boşanma. Her 100 evliliğe karşı <b>' + Math.round(i.oran[yy]) + '</b> boşanma.</p>' +
      '<div class="paylas"><a class="wa" data-k="wa" target="_blank" rel="noopener" href="#">WhatsApp</a><a data-k="x" target="_blank" rel="noopener" href="#">X</a><button data-k="indir">Görseli indir</button><button data-k="kopya">Bağlantıyı kopyala</button></div>';
    O.paylasBagla(k, { slug: 'harita', url: O.SITE + '/oyunlar/harita/?il=' + i.p + '&g=' + gos + (g().seri ? '&y=' + yil : ''),
      mesaj: 'Türkiye’nin aşk haritasında ' + i.il + ' (' + (g().seri ? yil : 2025) + '): ' + g().ad.toLowerCase() + cinsAd() + ' ' + fe(deger(i)) + ', Türkiye ' + fe(trDeger()) + '. Senin ilin?',
      kartAyar: { oyun: 'Türkiye’nin aşk haritası', ust: g().ad + cinsAd() + ' · ' + (g().seri ? yil : 2025) + ' · TÜİK', baslik: i.il + ' · ' + fe(deger(i)), alt: 'Türkiye ' + fe(trDeger()), ciz: function (x, X, Yy, W, HH) { kartCiz(x, X, Yy, W, HH, i); } } });
  }
  function kartCiz(x, X, Yy, W, HH, i) {
    var vb = H.viewBox.split(' ').map(Number), sc = W / vb[2], oy = Yy + (g().seri ? 0 : 120);
    H.iller.forEach(function (il) {
      var p = new Path2D(il.d); x.save(); x.translate(X, oy); x.scale(sc, sc);
      x.fillStyle = renk(il); x.fill(p); x.strokeStyle = '#fffaf2'; x.lineWidth = 1.2 / sc; x.stroke(p); x.restore();
    });
    x.save(); x.translate(X, oy); x.scale(sc, sc); x.strokeStyle = R.murekkep; x.lineWidth = 4 / sc; x.stroke(new Path2D(i.d)); x.restore();
    if (!g().seri) return;
    var a = i[gos], t = H.tr[gos], all = a.concat(t), mn = Math.min.apply(null, all), mx = Math.max.apply(null, all);
    var top = oy + vb[3] * sc + 40, hh = HH - (top - Yy) - 50;
    var px = function (j) { return X + 40 + j * (W - 80) / SON; }, py = function (v) { return top + (1 - (v - mn) / ((mx - mn) || 1)) * hh; };
    x.setLineDash([10, 10]); x.strokeStyle = '#b9ad9c'; x.lineWidth = 4; x.beginPath(); t.forEach(function (v, j) { j ? x.lineTo(px(j), py(v)) : x.moveTo(px(j), py(v)); }); x.stroke(); x.setLineDash([]);
    x.strokeStyle = g().renk[3]; x.lineWidth = 8; x.lineJoin = 'round'; x.beginPath(); a.forEach(function (v, j) { j ? x.lineTo(px(j), py(v)) : x.moveTo(px(j), py(v)); }); x.stroke();
    x.fillStyle = R.soluk; x.font = 'italic 400 28px "Crimson Pro", Georgia, serif'; x.textAlign = 'left'; x.fillText('2014', X + 30, top + hh + 38); x.textAlign = 'right'; x.fillText('2025 · kesikli çizgi Türkiye', X + W - 30, top + hh + 38);
  }
  function sec(i) {
    if (!i) return; secili = i;
    document.querySelectorAll('.hr-il.secili').forEach(function (p) { p.classList.remove('secili'); });
    i.el.classList.add('secili'); i.el.parentNode.appendChild(i.el);
    document.getElementById('hrVurgu').innerHTML = '<circle cx="' + i.cx + '" cy="' + i.cy + '" r="5" class="hr-nokta"/><circle cx="' + i.cx + '" cy="' + i.cy + '" r="5" class="hr-dalga"/>';
    document.getElementById('hrAra').value = i.il;
    adres(); kart(); O.iz('harita-il', { il: i.il, g: gos });
    if (window.innerWidth < 760 && !oynuyor) document.getElementById('hrKart').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
  function adres() { try { history.replaceState(null, '', '?' + (secili ? 'il=' + secili.p + '&' : '') + 'g=' + gos + (g().seri && yi !== SON ? '&y=' + Y[yi] : '')); } catch (e) {} }
  function yilAyarla(k) { yi = k; document.getElementById('hrYil').value = k; boya(); adres(); }
  var OY = '<svg viewBox="0 0 24 24"><path d="M7 5l12 7l-12 7z"/></svg>', DU = '<svg viewBox="0 0 24 24"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z"/></svg>';
  function durdur() { if (oynuyor) { clearInterval(oynuyor); oynuyor = null; var b = document.getElementById('hrOynat'); b.classList.remove('oynuyor'); b.innerHTML = OY; b.setAttribute('aria-label', 'Yılları oynat'); } }
  document.getElementById('hrOynat').onclick = function () {
    if (oynuyor) return durdur();
    if (yi === SON) yilAyarla(0);
    this.classList.add('oynuyor'); this.innerHTML = DU; this.setAttribute('aria-label', 'Durdur');
    O.iz('harita-oynat', { g: gos });
    oynuyor = setInterval(function () { if (yi >= SON) return durdur(); yilAyarla(yi + 1); }, 850);
  };
  document.getElementById('hrYil').addEventListener('input', function (e) { durdur(); yilAyarla(+e.target.value); });
  function gosSec(k) {
    gos = k; durdur();
    var gorunen = GOS[k].gizli ? 'ilkK' : k;
    document.querySelectorAll('.hr-gos button').forEach(function (x) { var on = x.dataset.g === gorunen; x.classList.toggle('secili', on); x.setAttribute('aria-selected', on); });
    var c = document.getElementById('hrCins'); c.hidden = !GOS[k].cins;
    c.querySelectorAll('button').forEach(function (b) { b.classList.toggle('secili', b.dataset.c === GOS[k].cins); });
    boya(); adres(); O.iz('harita-gosterge', { g: k });
  }
  document.querySelectorAll('.hr-gos button').forEach(function (b) { b.onclick = function () { gosSec(b.dataset.g); }; });
  document.querySelectorAll('#hrCins button').forEach(function (b) { b.onclick = function () { gosSec(b.dataset.c === 'K' ? 'ilkK' : 'ilkE'); }; });
  var ara = document.getElementById('hrAra');
  function bul() {
    var q = ara.value.trim().toLocaleLowerCase('tr'); if (!q) return;
    var i = H.iller.filter(function (x) { return x.il.toLocaleLowerCase('tr') === q; })[0] || H.iller.filter(function (x) { return x.il.toLocaleLowerCase('tr').indexOf(q) === 0; })[0];
    if (i) sec(i);
  }
  ara.addEventListener('change', bul);
  ara.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); bul(); } });
  document.getElementById('hrSon').outerHTML = '<div class="hr-son">' + O.abone() + '<p class="not">Kitapta: Bölüm 15 · Evliliğin Ekonomisi, Bölüm 17 · Çocukların Ekonomisi, Bölüm 22 · Boşanmanın Ekonomisi ve Bölüm 29 · Modern Evlilik.</p></div>';

  // adresten başla: ?il=17&g=bos&y=2019
  var q = new URLSearchParams(location.search);
  if (q.get('g') && GOS[q.get('g')]) gos = q.get('g');
  if (q.get('y')) { var yk = Y.indexOf(+q.get('y')); if (yk > -1) yi = yk; }
  gosSec(gos); yilAyarla(yi);
  if (q.get('il')) sec(H.iller.filter(function (i) { return i.p === +q.get('il'); })[0]);
  O.iz('oyun-basladi', { oyun: 'harita' });
})();
