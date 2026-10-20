/* Türkiye’nin aşk haritası — il bazında kaba evlenme ve boşanma hızları, 2025 */
(function () {
  'use strict';
  var O = window.OYUN, R = O.R, H = window.HARITA, NS = 'http://www.w3.org/2000/svg';
  var kok = document.getElementById('oyun');
  if (!H) { kok.textContent = 'Harita verisi yüklenemedi.'; return; }
  var GOS = {
    ev: { ad: 'Evlenme hızı', birim: 'bin kişide evlenme', renk: ['#f4e6c8', '#e3c27a', '#c99a2e', '#9a7116', '#5f4509'] },
    bos: { ad: 'Boşanma hızı', birim: 'bin kişide boşanma', renk: ['#f3dde0', '#e2a5ad', '#c9586a', '#a3283c', '#651423'] },
    oran: { ad: 'Boşanma / evlenme', birim: 'her 100 evlenmeye karşı boşanma', renk: ['#dbecea', '#a2cbc6', '#5e9e9a', '#2b726f', '#13403e'] },
    tdh: { ad: 'Çocuk sayısı', birim: 'kadın başına ortalama çocuk (toplam doğurganlık hızı)', renk: ['#e6e1ef', '#bfb1d8', '#8f78b8', '#634892', '#3a2560'] }
  };
  if (!(H.iller[0] && typeof H.iller[0].tdh === 'number')) delete GOS.tdh;
  if (H.iller[0] && typeof H.iller[0].hane === 'number') GOS.hane = { ad: 'Hane büyüklüğü', birim: 'bir hanede ortalama kişi', renk: ['#e3ece0', '#b6cfad', '#7fa874', '#4e7b45', '#28481f'] };
  var gos = 'ev', secili = null, hover = null;
  H.iller.forEach(function (i) { i.oran = Math.round(i.bos / i.ev * 100); });
  H.tr.oran = Math.round(H.tr.bos / H.tr.ev * 100);
  function deger(i) { return i[gos]; }
  function siniflar() {
    var v = H.iller.map(deger).sort(function (a, b) { return a - b; });
    return [0.2, 0.4, 0.6, 0.8].map(function (q) { return v[Math.floor(q * (v.length - 1))]; });
  }
  function renk(i, s) { var x = deger(i), k = 0; s.forEach(function (e) { if (x > e) k++; }); return GOS[gos].renk[k]; }
  function f(x) { return gos === 'oran' ? String(Math.round(x)) : (gos === 'tdh' || gos === 'hane') ? x.toFixed(2).replace('.', ',') : x.toFixed(1).replace('.', ','); }
  function sira(i) { var l = H.iller.slice().sort(function (a, b) { return deger(b) - deger(a); }); return l.indexOf(i) + 1; }

  kok.innerHTML =
    '<div class="hr-ust"><div class="hr-sek" role="tablist">' + Object.keys(GOS).map(function (k) { return '<button role="tab" data-g="' + k + '"' + (k === gos ? ' aria-selected="true" class="secili"' : ' aria-selected="false"') + '>' + GOS[k].ad + '</button>'; }).join('') + '</div>' +
    '<label class="hr-ara"><span class="gizli">İl ara</span><input id="hrAra" list="hrListe" placeholder="İlini yaz, örneğin Çanakkale" autocomplete="off"><datalist id="hrListe">' + H.iller.slice().sort(function (a, b) { return a.il.localeCompare(b.il, 'tr'); }).map(function (i) { return '<option value="' + i.il + '">'; }).join('') + '</datalist></label></div>' +
    '<div class="hr-cerceve"><svg id="hrSvg" class="hr-svg" viewBox="' + H.viewBox + '" role="img" aria-label="Türkiye il haritası"><g id="hrIller"></g><g id="hrVurgu"></g></svg>' +
    '<div class="hr-ipucu" id="hrIpucu" hidden></div></div>' +
    '<div class="hr-lejant" id="hrLejant"></div>' +
    '<div class="hr-alt"><div class="hr-kart" id="hrKart" aria-live="polite"></div><div class="hr-uclar" id="hrUclar"></div></div>' +
    '<p class="oy-not hr-kaynak">Veri: TÜİK, Evlenme ve Boşanma İstatistikleri 2025 (24 Şubat 2026)' + (H.dogumKaynak ? '; TÜİK, ' + H.dogumKaynak : '') + (H.haneKaynak ? '; TÜİK, ' + H.haneKaynak : '') + '. Kaba hız, il nüfusunun bin kişisi başına düşen evlenme ya da boşanma sayısıdır. Harita sınırları: alpers/Turkey-Maps-GeoJSON, Apache 2.0 lisansı.</p>' +
    '<div id="hrSon"></div>';
  var g = document.getElementById('hrIller');
  H.iller.forEach(function (i) {
    var p = document.createElementNS(NS, 'path'); p.setAttribute('d', i.d); p.setAttribute('class', 'hr-il'); p.dataset.p = i.p;
    p.setAttribute('tabindex', '0'); p.setAttribute('role', 'button'); p.setAttribute('aria-label', i.il);
    p.addEventListener('pointerenter', function (e) { hover = i; ipucu(e); });
    p.addEventListener('pointermove', ipucu);
    p.addEventListener('pointerleave', function () { hover = null; document.getElementById('hrIpucu').hidden = true; });
    p.addEventListener('click', function () { sec(i); });
    p.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sec(i); } });
    p.addEventListener('focus', function () { p.parentNode.appendChild(p); });
    g.appendChild(p); i.el = p;
  });
  function ipucu(e) {
    if (!hover || e.pointerType === 'touch') return;
    var t = document.getElementById('hrIpucu'), c = t.parentNode.getBoundingClientRect();
    t.hidden = false; t.innerHTML = '<b>' + hover.il + '</b> ' + f(deger(hover)) + (gos === 'oran' ? '' : gos === 'tdh' ? ' çocuk' : gos === 'hane' ? ' kişi' : '‰');
    var x = e.clientX - c.left + 14, y = e.clientY - c.top - 34;
    t.style.left = Math.min(x, c.width - t.offsetWidth - 4) + 'px'; t.style.top = Math.max(0, y) + 'px';
  }
  function boya() {
    var s = siniflar();
    H.iller.forEach(function (i) { i.el.style.fill = renk(i, s); });
    var r = GOS[gos].renk, sinir = [H.iller.map(deger).reduce(function (a, b) { return Math.min(a, b); })].concat(s).concat([H.iller.map(deger).reduce(function (a, b) { return Math.max(a, b); })]);
    document.getElementById('hrLejant').innerHTML = '<span>' + GOS[gos].birim + (gos === 'oran' || gos === 'tdh' || gos === 'hane' ? '' : ' (‰)') + '</span><div>' + r.map(function (c, k) { return '<i style="background:' + c + '"><em>' + f(sinir[k]) + '–' + f(sinir[k + 1]) + '</em></i>'; }).join('') + '</div><span class="hr-tr">Türkiye: <b>' + f(H.tr[gos]) + '</b></span>';
    var l = H.iller.slice().sort(function (a, b) { return deger(b) - deger(a); });
    var li = function (i) { return '<li><button data-p="' + i.p + '">' + i.il + '</button><b>' + f(deger(i)) + '</b></li>'; };
    document.getElementById('hrUclar').innerHTML = '<div><small>En yüksek</small><ol>' + l.slice(0, 5).map(li).join('') + '</ol></div><div><small>En düşük</small><ol>' + l.slice(-5).reverse().map(li).join('') + '</ol></div>';
    document.querySelectorAll('#hrUclar button').forEach(function (b) { b.onclick = function () { sec(H.iller.filter(function (i) { return i.p === +b.dataset.p; })[0]); }; });
    kart();
  }
  function kart() {
    var k = document.getElementById('hrKart');
    if (!secili) { k.innerHTML = '<p class="oy-buyuk" style="margin:0">Haritada bir ile dokun ya da yukarıdan ilini ara.</p><p class="oy-not">Renk koyulaştıkça değer yükselir. Her renk illerin beşte birini kapsar.</p>'; return; }
    var i = secili, fark = function (a, b) { var d = a - b; return (d >= 0 ? '+' : '−') + Math.abs(d).toFixed(1).replace('.', ','); };
    var yorum;
    if (i.bos >= 2.8) yorum = 'Boşanma hızı Türkiye ortalamasının belirgin biçimde üzerinde. Yüksek boşanma hızı yalnızca daha mutsuz evlilikler anlamına gelmeyebilir. Bir ilişkiden çıkmanın ne kadar mümkün olduğunu da gösterebilir. Kitabın 22. bölümünün sorduğu soru tam bu: Kalmak ne zaman gitmekten pahalıdır?';
    else if (i.bos <= 1.2) yorum = 'Boşanma hızı Türkiye ortalamasının çok altında. Bu, evliliklerin daha mutlu olduğu anlamına gelmeyebilir. Çıkışın maliyeti yüksek olduğunda da insanlar evli kalır. Kitabın 22. bölümünün sorusu: Kalmak ne zaman gitmekten pahalıdır?';
    else if (i.ev >= 7) yorum = 'Evlenme hızı yüksek. Genç nüfusun payı kaba hızı doğrudan etkiler, çünkü evlenme yaşındaki insanların oranı arttıkça bin kişiye düşen evlilik de artar. İlleri karşılaştırırken yaş yapısını akılda tutmak gerekir.';
    else if (i.ev <= 5) yorum = 'Evlenme hızı düşük. Kaba hız, il nüfusunun tamamına bölünerek hesaplanır. Bu yüzden yaşlı nüfusun payı yüksek ya da gençlerin göç ettiği illerde düşük çıkabilir.';
    else yorum = 'Değerler Türkiye ortalamasına yakın. Kaba hızlar nüfusun yaş yapısından etkilenir, bu yüzden küçük farkları yorumlarken dikkatli olmak gerekir.';
    k.innerHTML = '<p class="oy-adim">' + i.p + ' plaka · ' + sira(i) + '. sırada (' + GOS[gos].ad.toLowerCase() + ')</p><h3 class="hr-il-ad">' + i.il + '</h3>' +
      '<div class="hr-cubuklar">' +
      cubuk('Evlenme', i.ev, H.tr.ev, 8.5, GOS.ev.renk[3], fark(i.ev, H.tr.ev)) + cubuk('Boşanma', i.bos, H.tr.bos, 3.5, GOS.bos.renk[3], fark(i.bos, H.tr.bos)) +
      (GOS.tdh ? cocuk(i) : '') + (GOS.hane ? hane(i) : '') + '</div><p class="hr-oran">Her 100 evliliğe karşı <b>' + i.oran + '</b> boşanma <span>(Türkiye: ' + H.tr.oran + ')</span></p><p>' + yorum + '</p>' +
      '<div class="paylas"><a class="wa" data-k="wa" target="_blank" rel="noopener" href="#">WhatsApp</a><a data-k="x" target="_blank" rel="noopener" href="#">X</a><button data-k="indir">Görseli indir</button><button data-k="kopya">Bağlantıyı kopyala</button></div>';
    O.paylasBagla(k, { slug: 'harita', url: O.SITE + '/oyunlar/harita/?il=' + i.p, mesaj: 'Türkiye’nin aşk haritasında ' + i.il + ': bin kişide ' + i.ev.toFixed(1).replace('.', ',') + ' evlenme, ' + i.bos.toFixed(1).replace('.', ',') + ' boşanma' + (GOS.tdh ? ', kadın başına ' + i.tdh.toFixed(2).replace('.', ',') + ' çocuk' : '') + ' (TÜİK). Senin ilin?',
      kartAyar: { oyun: 'Türkiye’nin aşk haritası', ust: 'TÜİK 2025', baslik: i.il, alt: 'Bin kişide ' + i.ev.toFixed(1).replace('.', ',') + ' evlenme · ' + i.bos.toFixed(1).replace('.', ',') + ' boşanma', ciz: function (x, X, Y, W, HH) { kartCiz(x, X, Y, W, HH, i); } } });
  }
  function cocuk(i) {
    var d = i.tdh - H.tr.tdh, ikon = '';
    for (var k = 0; k < 5; k++) {
      var dol = Math.max(0, Math.min(1, i.tdh - k));
      ikon += '<svg viewBox="0 0 24 24" class="hr-cocuk"><defs><clipPath id="hc' + i.p + k + '"><rect width="' + (24 * dol) + '" height="24"/></clipPath></defs><g fill="none" stroke="#634892" stroke-width="1.6"><circle cx="12" cy="7" r="3.6"/><path d="M5.5 21c.6-5.4 3.2-8.2 6.5-8.2s5.9 2.8 6.5 8.2z"/></g><g clip-path="url(#hc' + i.p + k + ')" fill="#634892"><circle cx="12" cy="7" r="3.6"/><path d="M5.5 21c.6-5.4 3.2-8.2 6.5-8.2s5.9 2.8 6.5 8.2z"/></g></svg>';
    }
    return '<div class="hr-c hr-c-cocuk"><span>Çocuk</span><div class="hr-ikonlar">' + ikon + '</div><b>' + i.tdh.toFixed(2).replace('.', ',') + '</b><small>' + (d >= 0 ? '+' : '−') + Math.abs(d).toFixed(2).replace('.', ',') + '</small></div>';
  }
  function hane(i) {
    var d = i.hane - H.tr.hane, mx = 5;
    return '<div class="hr-c"><span>Hane</span><div class="hr-c-ic"><i style="width:' + (i.hane / mx * 100) + '%;background:#4e7b45"></i><u style="left:' + (H.tr.hane / mx * 100) + '%" title="Türkiye ' + H.tr.hane + '"></u></div><b>' + i.hane.toFixed(2).replace('.', ',') + '</b><small>' + (d >= 0 ? '+' : '−') + Math.abs(d).toFixed(2).replace('.', ',') + '</small></div>';
  }
  function cubuk(ad, v, tr, mx, renk, fk) {
    return '<div class="hr-c"><span>' + ad + '</span><div class="hr-c-ic"><i style="width:' + (v / mx * 100) + '%;background:' + renk + '"></i><u style="left:' + (tr / mx * 100) + '%" title="Türkiye ' + tr + '"></u></div><b>' + v.toFixed(1).replace('.', ',') + '‰</b><small>' + fk + '</small></div>';
  }
  function sec(i) {
    if (!i) return; secili = i;
    document.querySelectorAll('.hr-il.secili').forEach(function (p) { p.classList.remove('secili'); });
    i.el.classList.add('secili'); i.el.parentNode.appendChild(i.el);
    var v = document.getElementById('hrVurgu'); v.innerHTML = '<circle cx="' + i.cx + '" cy="' + i.cy + '" r="5" class="hr-nokta"/><circle cx="' + i.cx + '" cy="' + i.cy + '" r="5" class="hr-dalga"/>';
    document.getElementById('hrAra').value = i.il;
    try { history.replaceState(null, '', '?il=' + i.p); } catch (e) {}
    kart(); O.iz('harita-il', { il: i.il });
    if (window.innerWidth < 760) document.getElementById('hrKart').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
  function kartCiz(x, X, Y, W, HH, i) {
    // haritayı canvas'a çiz
    var vb = H.viewBox.split(' ').map(Number), sc = W / vb[2], oy = Y + (HH - vb[3] * sc) / 2 - 40, s = siniflar();
    H.iller.forEach(function (il) {
      var p = new Path2D(il.d); x.save(); x.translate(X, oy); x.scale(sc, sc);
      x.fillStyle = il === i ? R.bordo : renk(il, s); x.globalAlpha = il === i ? 1 : .55; x.fill(p);
      x.globalAlpha = 1; x.strokeStyle = '#fffaf2'; x.lineWidth = 1 / sc * 1.4; x.stroke(p); x.restore();
    });
    x.save(); x.translate(X, oy); x.scale(sc, sc); x.strokeStyle = R.murekkep; x.lineWidth = 3 / sc; x.stroke(new Path2D(i.d)); x.restore();
    var cy = oy + vb[3] * sc + 60;
    [['Evlenme', i.ev, H.tr.ev, 8.5, GOS.ev.renk[3]], ['Boşanma', i.bos, H.tr.bos, 3.5, GOS.bos.renk[3]]].forEach(function (c, k) {
      var y = cy + k * 70, bx = X + 200, bw = W - 360;
      x.fillStyle = R.murekkep; x.textAlign = 'left'; x.font = '500 32px Fraunces, Georgia, serif'; x.fillText(c[0], X, y + 28);
      x.fillStyle = '#ece3d6'; x.fillRect(bx, y + 4, bw, 32); x.fillStyle = c[4]; x.fillRect(bx, y + 4, bw * c[1] / c[3], 32);
      x.fillStyle = R.murekkep; x.fillRect(bx + bw * c[2] / c[3] - 2, y - 4, 4, 48);
      x.textAlign = 'right'; x.font = '600 34px Fraunces, Georgia, serif'; x.fillText(c[1].toFixed(1).replace('.', ',') + '‰', X + W, y + 32);
    });
    x.textAlign = 'left'; x.fillStyle = R.soluk; x.font = 'italic 400 26px "Crimson Pro", Georgia, serif'; x.fillText('çizgi: Türkiye ortalaması', X + 200, cy + 168);
  }

  document.querySelectorAll('.hr-sek button').forEach(function (b) {
    b.onclick = function () {
      gos = b.dataset.g;
      document.querySelectorAll('.hr-sek button').forEach(function (x) { var on = x === b; x.classList.toggle('secili', on); x.setAttribute('aria-selected', on); });
      boya(); O.iz('harita-gosterge', { g: gos });
    };
  });
  var ara = document.getElementById('hrAra');
  function bul() {
    var q = ara.value.trim().toLocaleLowerCase('tr'); if (!q) return;
    var i = H.iller.filter(function (x) { return x.il.toLocaleLowerCase('tr') === q; })[0] || H.iller.filter(function (x) { return x.il.toLocaleLowerCase('tr').indexOf(q) === 0; })[0];
    if (i) sec(i);
  }
  ara.addEventListener('change', bul);
  ara.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); bul(); } });
  document.getElementById('hrSon').outerHTML = '<div class="hr-son">' + O.abone() + '<p class="not">Kitapta: Bölüm 17 · Çocukların Ekonomisi, Bölüm 22 · Boşanmanın Ekonomisi ve Bölüm 29 · Modern Evlilik.</p></div>';
  boya();
  var q = new URLSearchParams(location.search).get('il');
  if (q) sec(H.iller.filter(function (i) { return i.p === +q; })[0]);
  O.iz('oyun-basladi', { oyun: 'harita' });
})();
