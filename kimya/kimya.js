/* Aşkın Kimyası — etkileşimli beden haritası */
(function () {
  'use strict';
  var KD = { guclu: 'Güçlü kanıt', orta: 'Orta düzey kanıt', sinirli: 'Sınırlı kanıt' };
  // x, y: 500×900 silüet koordinatları
  var B = [
    { id: 'odul', x: 250, y: 102, ad: 'Ödül sistemi', yer: 'Beyin', kim: ['Dopamin'], evre: ['cekim', 'bag'],
      metin: 'Sevilen kişiyi düşünmek, beynin derinindeki ödül ve istek devrelerini harekete geçirir. Buradaki asıl duygu haz değil, istek ve motivasyondur. “Yine görmeliyim” hissi buradan gelir. Uzun evliliklerde bile bu devrelerin etkin kalabildiği görüldü.',
      kanit: 'guclu', kaynak: 'Aron vd., 2005 · Acevedo vd., 2012' },
    { id: 'uyari', x: 222, y: 70, ad: 'Uyarılma', yer: 'Beyin', kim: ['Noradrenalin'], evre: ['cekim'],
      metin: 'Enerji artar, dikkat tek bir kişiye kilitlenir. Uykusuzluk ve iştahsızlık bu evrenin bilinen işaretleridir. Noradrenalinin rolü büyük ölçüde stres ve uyarılma fizyolojisinden çıkarılır. Aşka özgü doğrudan ölçümler azdır.',
      kanit: 'orta', kaynak: 'Fisher, 1998' },
    { id: 'yargi', x: 278, y: 70, ad: 'Yargı ve takıntı', yer: 'Beyin', kim: ['Prefrontal bölgeler', 'Serotonin?'], evre: ['cekim'],
      metin: 'Sevilen kişiye yönelik eleştirel yargıyla ilişkili bazı bölgelerde etkinlik azalabilir. “Kusurlarını görmüyorum” hissinin bir parçası budur. Âşıkların onu aklından çıkaramamasını düşük serotoninle ilişkilendiren bulgu ise yalnızca 20 kişilik bir çalışmaya dayanır.',
      kanit: 'sinirli', kaynak: 'Bartels ve Zeki, 2004 · Marazziti vd., 1999' },
    { id: 'kalp', x: 276, y: 290, ad: 'Kalp', yer: 'Göğüs', kim: ['Adrenalin'], evre: ['cekim'],
      metin: 'Kalp âşık olmaz, beyne cevap verir. Sempatik sinir sistemi devreye girer: Nabız hızlanır, avuçlar terler, yüz kızarır. Ani ve yoğun bir duygusal şok ise “kırık kalp sendromu” denen geçici bir kalp sorununa bile yol açabilir.',
      kanit: 'guclu', kaynak: 'Wittstein vd., 2005' },
    { id: 'mide', x: 250, y: 398, ad: 'Midede kelebekler', yer: 'Karın', kim: ['Stres tepkisi'], evre: ['cekim'],
      metin: 'Stres sistemi devreye girdiğinde sindirime giden kan akışı azalır, bağırsak hareketleri değişir. Midedeki kıpırtının bir kısmı bundandır. Mekanizma iyi bilinir ama “kelebekleri” doğrudan inceleyen aşk çalışması neredeyse yoktur.',
      kanit: 'orta', kaynak: 'Genel stres fizyolojisi' },
    { id: 'hormon', x: 250, y: 500, ad: 'Arzu hormonları', yer: 'Hormon bezleri', kim: ['Testosteron', 'Östrojen'], evre: ['arzu'],
      metin: 'Cinsel arzuyla ilişkili hormonlar. Testosteron hem kadınlarda hem erkeklerde arzuyla bağlantılıdır. Araştırmacılar arzuyu romantik çekimden ayrı işleyebilen bir sistem olarak ele alır. Bu yüzden ikisi her zaman aynı kişiye yönelmez.',
      kanit: 'orta', kaynak: 'Fisher, 1998' },
    { id: 'dokunma', x: 399, y: 594, ad: 'Dokunma ve bağ', yer: 'Deri, eller', kim: ['Oksitosin', 'Vazopresin'], evre: ['bag', 'arzu'],
      metin: 'Sarılma, dokunma ve yakınlık sırasında oksitosin salınır. Güveni ve bağlanmayı destekleyen bir sinyaldir, tek başına “aşk hormonu” değildir. Burun spreyi çalışmaları tutarlı sonuç vermedi. Vazopresinin bağlanmadaki rolüne dair en güçlü kanıt çayır faresi çalışmalarından gelir.',
      kanit: 'orta', kaynak: 'Young ve Wang, 2004 · Walum vd., 2016' }
  ];
  var EVRE_AD = { hepsi: 'Hepsi', arzu: 'Arzu', cekim: 'Çekim', bag: 'Bağ' };
  var EVRE_METIN = {
    hepsi: 'Haritada bir noktaya dokun ya da yukarıdan bir evre seç.',
    arzu: 'Arzu: Bedene ve yakınlığa yönelen istek. Hormonlar baskındır.',
    cekim: 'Çekim: Tek bir kişiye kilitlenen dikkat. Beyin ve beden alarmda.',
    bag: 'Bağ: Güven ve sakinlik. Uzun ilişkinin sistemi.'
  };
  var SVGNS = 'http://www.w3.org/2000/svg';
  var g = document.getElementById('kimNoktalar'), panel = document.getElementById('kimPanel'), liste = document.getElementById('kimListe');
  if (!g || !panel) return;
  var evre = 'hepsi', secili = null;

  function iz(n, d) { try { if (window.umami) umami.track(n, d); } catch (e) {} }

  B.forEach(function (b, i) {
    var n = document.createElementNS(SVGNS, 'g');
    n.setAttribute('class', 'kim-nokta'); n.setAttribute('tabindex', '0'); n.setAttribute('role', 'button');
    n.setAttribute('aria-label', b.ad + ', ' + b.yer); n.dataset.id = b.id;
    n.innerHTML = '<circle class="isik" cx="' + b.x + '" cy="' + b.y + '" r="44" fill="url(#kimIsik)"/>' +
      '<circle class="tut" cx="' + b.x + '" cy="' + b.y + '" r="24"/>' +
      '<circle class="halka" cx="' + b.x + '" cy="' + b.y + '" r="17"/>' +
      '<circle class="ic" cx="' + b.x + '" cy="' + b.y + '" r="12.5"/>' +
      '<text x="' + b.x + '" y="' + (b.y + 4.5) + '" text-anchor="middle">' + (i + 1) + '</text>';
    n.addEventListener('click', function () { sec(b.id); gorunur(); });
    n.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sec(b.id); } });
    g.appendChild(n);
    var c = document.createElement('button');
    c.className = 'kim-cip'; c.dataset.id = b.id; c.setAttribute('role', 'listitem');
    c.innerHTML = '<span>' + (i + 1) + '</span>' + b.ad;
    c.onclick = function () { sec(b.id); gorunur(); };
    liste.appendChild(c);
  });

  function gorunur() { if (window.innerWidth < 760) panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }
  function aktif(b) { return evre === 'hepsi' || b.evre.indexOf(evre) > -1; }
  function guncelle() {
    B.forEach(function (b) {
      var on = aktif(b), s = secili === b.id;
      document.querySelectorAll('[data-id="' + b.id + '"]').forEach(function (el) {
        el.classList.toggle('sonuk', !on); el.classList.toggle('secili', s);
      });
    });
  }
  function panelCiz() {
    var b = null; B.forEach(function (x) { if (x.id === secili) b = x; });
    if (!b) {
      var say = B.filter(aktif).length;
      panel.innerHTML = '<span class="etiket">' + EVRE_AD[evre] + '</span><h2>' + (evre === 'hepsi' ? 'Yedi durak' : say + ' durak') + '</h2>' +
        '<p>' + EVRE_METIN[evre] + '</p><p class="kim-not">Kalp, mide ve deri âşık olmaz. Hepsi beyinden gelen sinyallere cevap verir.</p>';
      return;
    }
    var no = B.indexOf(b) + 1;
    panel.innerHTML = '<span class="etiket">' + no + ' · ' + b.yer + '</span><h2>' + b.ad + '</h2>' +
      '<div class="kim-kimyasal">' + b.kim.map(function (k) { return '<span>' + k + '</span>'; }).join('') + '</div>' +
      '<p>' + b.metin + '</p>' +
      '<div class="kim-alt"><b class="kd ' + b.kanit + '">' + KD[b.kanit] + '</b><span>' + b.kaynak + '</span></div>' +
      '<div class="kim-gez"><button id="kimOnce" aria-label="Önceki durak">←</button><button id="kimSonra" aria-label="Sonraki durak">Sonraki durak →</button></div>';
    var aktifler = B.filter(aktif), j = aktifler.indexOf(b);
    if (j < 0) { aktifler = B; j = B.indexOf(b); }
    document.getElementById('kimOnce').onclick = function () { sec(aktifler[(j - 1 + aktifler.length) % aktifler.length].id); };
    document.getElementById('kimSonra').onclick = function () { sec(aktifler[(j + 1) % aktifler.length].id); };
  }
  function sec(id) { secili = id; guncelle(); panelCiz(); iz('kimya-durak', { durak: id, evre: evre }); }
  document.querySelectorAll('.kim-evre button').forEach(function (bt) {
    bt.onclick = function () {
      evre = bt.dataset.evre;
      document.querySelectorAll('.kim-evre button').forEach(function (x) { x.classList.toggle('secili', x === bt); });
      if (secili) { var b = B.filter(function (x) { return x.id === secili; })[0]; if (!aktif(b)) secili = null; }
      guncelle(); panelCiz(); iz('kimya-evre', { evre: evre });
    };
  });
  guncelle(); panelCiz();
})();
