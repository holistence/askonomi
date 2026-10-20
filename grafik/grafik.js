/* Aşkının Grafiği — değer–zaman eğrisi, piyasa yorumu, paylaşım kartı */
(function () {
  'use strict';
  var SITE = 'https://askonomi.com';
  var DONEM = ['Başlangıç', 'İlk aylar', 'İlk yıl', 'Orta dönem', 'Yakın geçmiş', 'Bugün'];
  var KISA = ['Başta', 'Aylar', '1. yıl', 'Orta', 'Yakın', 'Bugün'];
  var BOLUM = { '06': 'Sinyaller', '24': 'Güven Sermayesi', '25': 'İlişkiye Yatırım', '28': 'Beklenti Enflasyonu' };
  var SONUC = {
    yukselis: ['Uzun vadeli yükseliş', 'Grafiğin sabırlı bir yatırımcının hayali. Değer zamanla artmış, sert düşüşler yaşanmamış. İktisatta bu tür birikime sermaye denir. İlişkide de güven, ortak alışkanlıklar ve paylaşılan geçmiş birikerek değer üretir. Riski şu: Yükselen grafikler kendiliğinden yükselmeye devam etmez. Bakım ister, yeni deneyim ister.', '25'],
    balon: ['Balon ve düzeltme', 'Başlangıç parlak, sonrası daha sakin. Piyasalarda buna köpük ve ardından gelen düzeltme denir. Aşkın ilk evresi beklentileri şişirir ve beyin o dönemde tarafsız bir rapor sunmaz. Düzeltme kötü haber olmak zorunda değil. Çoğu zaman beklentiler gerçek değere iner. Asıl soru şu: Bugünkü değer, şişkin beklentiyle değil gerçekle karşılaştırıldığında nasıl?', '28'],
    toparlanma: ['V tipi toparlanma', 'Bir kriz yaşamışsınız ve ilişki geri dönmüş. İktisatçılar buna V tipi toparlanma der. Krizden sonra toparlanan ilişkilerde genellikle bir şey yeniden inşa edilir: Güven. Güven sermayesi yavaş birikir, hızlı erir. Ama onarılabildiğinde krizden önceki hâlinden daha sağlam bir zemin kurabilir.', '24'],
    yatay: ['Yatay seyir', 'Grafiğin sakin. Büyük iniş yok, büyük çıkış da yok. Piyasalarda yatay seyir istikrar demektir ama durgunluk riski de taşır. Uzun ilişkilerde rutin güven verir, aynı zamanda heyecanı söndürebilir. Birlikte yaşanan yeni ve uyarıcı deneyimlerin bazı çiftlerde ilişki kalitesini desteklediği biliniyor. Bazen küçük bir yenilik yatırımı grafiği oynatır.', '25'],
    oynak: ['Yüksek oynaklık', 'Grafiğin iniş çıkışlarla dolu. Finans dilinde buna yüksek oynaklık denir ve oynaklık belirsizlik demektir. İlişkide sık dalgalanma, tarafların birbirine verdiği sinyallerin tutarsız olduğunu gösterebilir. Ortalama değer iyi olsa bile belirsizliğin kendisi yorucudur. Tutarlılık, bir ilişkideki en güçlü sinyallerden biridir.', '06'],
    dusus: ['Düşüş trendi', 'Grafik bir süredir aşağıyı gösteriyor. İktisadın bu noktadaki uyarısı açık: Geçmişte verilenler geri gelmez, onlar batık maliyettir. Karar geçmişe değil, önümüzdeki döneme bakılarak verilir. Bu, ilişkinin bitmesi gerektiği anlamına gelmez. Düşüşün nedeni konuşulabilir ve onarılabilir olabilir. Ama “bunca yıl verdim” cümlesi tek başına kalma nedeni değildir.', '25'],
    karma: ['Karma seyir', 'Grafiğin tek bir hikâyeye sığmıyor. İnişler, çıkışlar ve sakin dönemler bir arada. Gerçek ilişkilerin çoğu böyledir. Tek tek noktalardan çok son dönemin yönü önemlidir. Bir piyasa analisti olsaydın soracağın soru şu olurdu: Son yükselişi ya da düşüşü ne başlattı ve hâlâ sürüyor mu?', '']
  };
  var BASLANGIC = [5, 7, 6, 5, 6, 7];
  var v = BASLANGIC.slice(), paylasilan = false, aktif = -1, hesaplandi = false;

  // paylaşılan bağlantı: ?d=476567 (her hane değer-1)
  var q = new URLSearchParams(location.search).get('d');
  if (q && /^[0-9]{6}$/.test(q)) { v = q.split('').map(function (c) { return +c + 1; }); paylasilan = true; }

  function $(s) { return document.querySelector(s); }
  function iz(n, d) { try { if (window.umami) umami.track(n, d); } catch (e) {} }
  var svg = $('#grSvg'); if (!svg) return;
  var X0 = 70, X1 = 610, Y0 = 60, Y1 = 360;
  function px(i) { return X0 + 20 + i * (X1 - X0 - 40) / 5; }
  function py(val) { return Y1 - (val / 10) * (Y1 - Y0); }

  function ciz() {
    var h = '';
    for (var k = 2; k <= 10; k += 2) h += '<line class="gr-izgara" x1="' + X0 + '" x2="' + X1 + '" y1="' + py(k) + '" y2="' + py(k) + '"/><text class="gr-sayi" x="' + (X0 - 10) + '" y="' + (py(k) + 5) + '" text-anchor="end">' + k + '</text>';
    h += '<line class="gr-eksen" x1="' + X0 + '" y1="' + (Y0 - 18) + '" x2="' + X0 + '" y2="' + Y1 + '"/><line class="gr-eksen" x1="' + X0 + '" y1="' + Y1 + '" x2="' + X1 + '" y2="' + Y1 + '"/>';
    h += '<text class="gr-etk" x="' + (X0 + 10) + '" y="' + (Y0 - 4) + '">değer</text><text class="gr-etk" x="' + X1 + '" y="' + (Y1 + 58) + '" text-anchor="end">zaman</text>';
    KISA.forEach(function (d, i) { h += '<text class="gr-donem" x="' + px(i) + '" y="' + (Y1 + 30) + '" text-anchor="middle"><title>' + DONEM[i] + '</title>' + d + '</text>'; });
    h += '<polyline class="gr-cizgi" points="' + v.map(function (y, i) { return px(i) + ',' + py(y); }).join(' ') + '"/>';
    v.forEach(function (y, i) {
      h += '<g class="gr-nokta' + (i === aktif ? ' aktif' : '') + '" data-i="' + i + '" tabindex="0" role="slider" aria-label="' + DONEM[i] + '" aria-valuemin="1" aria-valuemax="10" aria-valuenow="' + y + '">' +
        '<circle class="tut" cx="' + px(i) + '" cy="' + py(y) + '" r="32"/><circle class="gor" cx="' + px(i) + '" cy="' + py(y) + '" r="12"/>' +
        '<text class="gr-deger" x="' + px(i) + '" y="' + (py(y) - 22) + '" text-anchor="middle">' + y + '</text></g>';
    });
    svg.innerHTML = h;
    svg.querySelectorAll('.gr-nokta').forEach(function (n) {
      var i = +n.dataset.i;
      n.addEventListener('pointerdown', function (e) { e.preventDefault(); aktif = i; surukle(e); svg.setPointerCapture(e.pointerId); });
      n.addEventListener('keydown', function (e) {
        var d = { ArrowUp: 1, ArrowRight: 0, ArrowDown: -1, ArrowLeft: 0 }[e.key];
        if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') { e.preventDefault(); var j = Math.max(0, Math.min(5, i + (e.key === 'ArrowRight' ? 1 : -1))); aktif = j; ciz(); odakla(j); return; }
        if (d) { e.preventDefault(); v[i] = Math.max(1, Math.min(10, v[i] + d)); aktif = i; degisti(); odakla(i); }
      });
      n.addEventListener('focus', function () { if (aktif !== i) { aktif = i; n.classList.add('aktif'); } });
    });
  }
  function odakla(i) { var n = svg.querySelector('.gr-nokta[data-i="' + i + '"]'); if (n) n.focus(); }
  function surukle(e) {
    if (aktif < 0) return;
    var r = svg.getBoundingClientRect(), y = (e.clientY - r.top) * (430 / r.height);
    var val = Math.round((Y1 - y) / (Y1 - Y0) * 10);
    val = Math.max(1, Math.min(10, val));
    if (val !== v[aktif]) { v[aktif] = val; degisti(); }
  }
  svg.addEventListener('pointermove', function (e) { if (e.buttons && aktif > -1) surukle(e); });
  svg.addEventListener('pointerup', function () { aktif = -1; ciz(); });
  function degisti() { paylasilan = false; ust(); ciz(); if (hesaplandi) hesapla(false); }

  // ---- analiz ----
  function analiz(a) {
    var n = a.length, xm = (n - 1) / 2, ym = a.reduce(function (s, x) { return s + x; }, 0) / n, sxy = 0, sxx = 0;
    a.forEach(function (y, i) { sxy += (i - xm) * (y - ym); sxx += (i - xm) * (i - xm); });
    var egim = sxy / sxx, fark = [];
    for (var i = 1; i < n; i++) fark.push(a[i] - a[i - 1]);
    var fm = fark.reduce(function (s, x) { return s + x; }, 0) / fark.length;
    var oyn = Math.sqrt(fark.reduce(function (s, x) { return s + (x - fm) * (x - fm); }, 0) / fark.length);
    var tepe = a[0], dd = 0, ddDip = 0;
    a.forEach(function (y, i) { if (y > tepe) tepe = y; if (tepe - y > dd) { dd = tepe - y; ddDip = i; } });
    var imax = a.indexOf(Math.max.apply(null, a)), imin = a.lastIndexOf(Math.min.apply(null, a));
    var tur;
    if (dd >= 3 && ddDip >= 1 && ddDip <= 4 && a[5] >= a[ddDip] + 3) tur = 'toparlanma';
    else if (imax <= 2 && a[imax] - a[5] >= 3) tur = 'balon';
    else if (egim <= -0.4) tur = 'dusus';
    else if (oyn >= 2.2) tur = 'oynak';
    else if (egim >= 0.4) tur = 'yukselis';
    else if (Math.max.apply(null, a) - Math.min.apply(null, a) <= 3) tur = 'yatay';
    else tur = 'karma';
    return { tur: tur, egim: egim, oyn: oyn, dd: dd, son: a[5] - a[4], imin: imin };
  }
  function sayi(x, isaret) { var s = (Math.round(x * 10) / 10).toFixed(1).replace('.', ','); return (isaret && x > 0 ? '+' : '') + s; }
  function kod() { return v.map(function (x) { return x - 1; }).join(''); }

  function ust() {
    $('#grUst').innerHTML = paylasilan ? '<span class="davet">Arkadaşının grafiği. Noktaları değiştirerek kendi grafiğini çizebilirsin.</span>' : '';
  }

  function hesapla(kaydir) {
    hesaplandi = true;
    var a = analiz(v), s = SONUC[a.tur], url = SITE + '/grafik/?d=' + kod();
    var msg = 'Aşkonomi’ye göre aşkımın grafiği: “' + s[0] + '”. Seninki nasıl?';
    var son = a.son > 0 ? '↑ ' + sayi(a.son, true) : (a.son < 0 ? '↓ ' + sayi(a.son) : '→ 0');
    $('#grSonuc').innerHTML = '<div class="kart sonuc gr-sonuc"><span class="bolumno">' + (paylasilan ? 'Arkadaşının piyasa yorumu' : 'Piyasa yorumun') + '</span><h2>' + s[0] + '</h2>' +
      '<div class="gr-olcu"><div><small>Trend</small><b>' + sayi(a.egim, true) + '</b><span>puan / dönem</span></div><div><small>Oynaklık</small><b>' + sayi(a.oyn) + '</b><span>dönemler arası</span></div>' +
      '<div><small>En büyük düşüş</small><b>' + a.dd + '</b><span>puan</span></div><div><small>Son dönem</small><b>' + son + '</b><span>puan</span></div></div>' +
      '<p>' + s[1] + '</p>' + (s[2] ? '<p class="not">İlgili bölüm: ' + parseInt(s[2], 10) + ' · ' + BOLUM[s[2]] + '</p>' : '') +
      '<div class="paylas"><button id="grIndir">Görseli indir</button>' + (navigator.canShare ? '<button id="grPaylas">Görseli paylaş</button>' : '') +
      '<a class="wa" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent(msg + ' ' + url + '&utm_source=whatsapp') + '">WhatsApp</a>' +
      '<a target="_blank" rel="noopener" href="https://x.com/intent/tweet?via=askonomikitap&text=' + encodeURIComponent(msg + ' ' + url + '&utm_source=x') + '">X</a>' +
      '<button id="grKopya">Bağlantıyı kopyala</button></div>' +
      '<p class="not">Grafiğin hiçbir sunucuya kaydedilmez. Paylaşım bağlantısı yalnızca altı sayıyı taşır.</p>' +
      '<div class="abone-kutu"><p>Kalbin kararlarının iktisadı, kitabın tamamında. Çıktığında ilk duymak için:</p><a class="btn abone-git" href="/#takip">E-posta listesine katıl</a></div></div>';
    $('#grIndir').onclick = function () { kart(function (b) { var a2 = document.createElement('a'); a2.href = URL.createObjectURL(b); a2.download = 'askonomi-grafigim.png'; a2.click(); }); iz('grafik-indir', { sonuc: s[0] }); };
    var pb = $('#grPaylas');
    if (pb) pb.onclick = function () {
      kart(function (b) {
        var f = new File([b], 'askonomi-grafigim.png', { type: 'image/png' });
        if (navigator.canShare({ files: [f] })) navigator.share({ files: [f], text: msg + ' ' + url }).catch(function () {});
        else { var a2 = document.createElement('a'); a2.href = URL.createObjectURL(b); a2.download = 'askonomi-grafigim.png'; a2.click(); }
      });
      iz('grafik-paylas', { sonuc: s[0] });
    };
    $('#grKopya').onclick = function (e) { try { navigator.clipboard.writeText(url); e.target.textContent = 'Kopyalandı'; } catch (x) { prompt('Bağlantı:', url); } };
    if (kaydir !== false) { $('#grSonuc').scrollIntoView({ behavior: 'smooth', block: 'start' }); iz('grafik-bitti', { sonuc: s[0], kod: kod() }); }
  }

  // ---- paylaşım kartı (1080×1350, kapak dilinde) ----
  function kart(cb) {
    var c = document.createElement('canvas'); c.width = 1080; c.height = 1350;
    var x = c.getContext('2d'), a = analiz(v), s = SONUC[a.tur];
    var Z = '#F2EBE0', M = '#262028', S = '#6b6070', BO = '#B3263A', CI = '#d8ccbb';
    (document.fonts ? document.fonts.ready : Promise.resolve()).then(function () {
      x.fillStyle = Z; x.fillRect(0, 0, 1080, 1350);
      x.strokeStyle = CI; x.lineWidth = 3; x.strokeRect(36, 36, 1008, 1278);
      x.fillStyle = M; x.textAlign = 'center';
      x.font = '600 30px Fraunces, Georgia, serif'; x.fillText('A Ş K O N O M İ', 540, 128);
      x.font = 'italic 400 64px Fraunces, Georgia, serif'; x.fillStyle = BO; x.fillText('Aşkımın grafiği', 540, 230);
      // grafik
      var gx0 = 150, gx1 = 960, gy0 = 320, gy1 = 900;
      x.strokeStyle = 'rgba(38,32,40,.08)'; x.lineWidth = 2;
      for (var k = 2; k <= 10; k += 2) { var yy = gy1 - k / 10 * (gy1 - gy0); x.beginPath(); x.moveTo(gx0, yy); x.lineTo(gx1, yy); x.stroke(); }
      x.strokeStyle = '#b9ad9c'; x.lineWidth = 3; x.beginPath(); x.moveTo(gx0, gy0 - 30); x.lineTo(gx0, gy1); x.lineTo(gx1, gy1); x.stroke();
      x.font = 'italic 400 34px "Crimson Pro", Georgia, serif'; x.fillStyle = S; x.textAlign = 'left'; x.fillText('değer', gx0 + 18, gy0 - 30);
      x.textAlign = 'right'; x.fillText('zaman', gx1, gy1 + 60);
      var P = v.map(function (y, i) { return [gx0 + 40 + i * (gx1 - gx0 - 80) / 5, gy1 - y / 10 * (gy1 - gy0)]; });
      x.strokeStyle = BO; x.lineWidth = 9; x.lineJoin = 'round'; x.lineCap = 'round'; x.beginPath();
      P.forEach(function (p, i) { if (i) x.lineTo(p[0], p[1]); else x.moveTo(p[0], p[1]); }); x.stroke();
      // en yüksek noktada küçük kalp
      var im = v.indexOf(Math.max.apply(null, v)), hp = P[im];
      x.save(); x.translate(hp[0], hp[1] - 46); x.scale(1.6, 1.6); x.fillStyle = BO; x.beginPath();
      x.moveTo(0, 8); x.bezierCurveTo(-14, -2, -12, -14, -5, -14); x.bezierCurveTo(-2, -14, 0, -12, 0, -9); x.bezierCurveTo(0, -12, 2, -14, 5, -14); x.bezierCurveTo(12, -14, 14, -2, 0, 8); x.fill(); x.restore();
      x.fillStyle = BO; P.forEach(function (p) { x.beginPath(); x.arc(p[0], p[1], 11, 0, 7); x.fill(); });
      // sonuç
      x.textAlign = 'center'; x.fillStyle = S; x.font = 'italic 400 36px "Crimson Pro", Georgia, serif'; x.fillText('Piyasa yorumu', 540, 1040);
      x.fillStyle = M; x.font = '600 76px Fraunces, Georgia, serif'; x.fillText(s[0], 540, 1124);
      x.fillStyle = BO; x.font = '500 36px Fraunces, Georgia, serif'; x.fillText('Seninki nasıl?  askonomi.com/grafik', 540, 1250);
      c.toBlob(cb, 'image/png');
    });
  }

  $('#grHesap').onclick = function () { hesapla(true); };
  $('#grSifirla').onclick = function () { v = BASLANGIC.slice(); paylasilan = false; hesaplandi = false; $('#grSonuc').innerHTML = ''; ust(); ciz(); };
  ust(); ciz();
  if (paylasilan) hesapla(false);
})();
