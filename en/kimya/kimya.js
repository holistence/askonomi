/* Love's Chemistry — interactive body map (English edition) */
(function () {
  'use strict';
  var KD = { guclu: 'Strong evidence', orta: 'Moderate evidence', sinirli: 'Limited evidence' };
  // x, y: coordinates on the 500×900 silhouette
  var B = [
    { id: 'odul', x: 250, y: 102, ad: 'Reward system', yer: 'Brain', kim: ['Dopamine'], evre: ['cekim', 'bag'],
      metin: 'Thinking about the person you love switches on the reward and wanting circuits deep in the brain. The main feeling here is not pleasure but wanting and motivation. The “I have to see them again” feeling comes from here. These circuits have been seen to stay active even in long marriages.',
      kanit: 'guclu', kaynak: 'Aron et al., 2005 · Acevedo et al., 2012' },
    { id: 'uyari', x: 222, y: 70, ad: 'Arousal', yer: 'Brain', kim: ['Noradrenaline'], evre: ['cekim'],
      metin: 'Energy rises and attention locks onto one person. Sleeplessness and loss of appetite are well-known signs of this phase. The role of noradrenaline is mostly inferred from the physiology of stress and arousal. Direct measurements specific to love are rare.',
      kanit: 'orta', kaynak: 'Fisher, 1998' },
    { id: 'yargi', x: 278, y: 70, ad: 'Judgement and obsession', yer: 'Brain', kim: ['Prefrontal areas', 'Serotonin?'], evre: ['cekim'],
      metin: 'Activity can drop in some areas linked to critical judgement of the loved one. This is part of the “I can’t see their flaws” feeling. The finding that links lovers’ inability to stop thinking about someone to low serotonin rests on a single study of just 20 people.',
      kanit: 'sinirli', kaynak: 'Bartels & Zeki, 2004 · Marazziti et al., 1999' },
    { id: 'kalp', x: 276, y: 290, ad: 'Heart', yer: 'Chest', kim: ['Adrenaline'], evre: ['cekim'],
      metin: 'The heart does not fall in love; it answers the brain. The sympathetic nervous system kicks in: your pulse races, your palms sweat, your face flushes. A sudden, intense emotional shock can even cause a temporary heart problem called “broken heart syndrome”.',
      kanit: 'guclu', kaynak: 'Wittstein et al., 2005' },
    { id: 'mide', x: 250, y: 398, ad: 'Butterflies in the stomach', yer: 'Belly', kim: ['Stress response'], evre: ['cekim'],
      metin: 'When the stress system kicks in, blood flow to digestion drops and gut movements change. That explains part of the fluttering in your stomach. The mechanism is well known, but there are almost no love studies that look at the “butterflies” directly.',
      kanit: 'orta', kaynak: 'General stress physiology' },
    { id: 'hormon', x: 250, y: 500, ad: 'Desire hormones', yer: 'Glands', kim: ['Testosterone', 'Oestrogen'], evre: ['arzu'],
      metin: 'Hormones linked to sexual desire. Testosterone is connected to desire in both women and men. Researchers treat desire as a system that can work separately from romantic attraction. That is why the two do not always point at the same person.',
      kanit: 'orta', kaynak: 'Fisher, 1998' },
    { id: 'dokunma', x: 399, y: 594, ad: 'Touch and attachment', yer: 'Skin, hands', kim: ['Oxytocin', 'Vasopressin'], evre: ['bag', 'arzu'],
      metin: 'Oxytocin is released during hugs, touch and closeness. It is a signal that supports trust and attachment, not a “love hormone” on its own. Nasal spray studies have not given consistent results. The strongest evidence for the role of vasopressin in attachment comes from studies of prairie voles.',
      kanit: 'orta', kaynak: 'Young & Wang, 2004 · Walum et al., 2016' }
  ];
  var EVRE_AD = { hepsi: 'All', arzu: 'Desire', cekim: 'Attraction', bag: 'Attachment' };
  var EVRE_METIN = {
    hepsi: 'Tap a point on the map, or choose a phase above.',
    arzu: 'Desire: wanting aimed at the body and closeness. Hormones lead.',
    cekim: 'Attraction: attention locked onto one person. Brain and body on alert.',
    bag: 'Attachment: trust and calm. The system of long relationships.'
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
      panel.innerHTML = '<span class="etiket">' + EVRE_AD[evre] + '</span><h2>' + (evre === 'hepsi' ? 'Seven stops' : say + (say === 1 ? ' stop' : ' stops')) + '</h2>' +
        '<p>' + EVRE_METIN[evre] + '</p><p class="kim-not">The heart, stomach and skin do not fall in love. They all answer signals from the brain.</p>';
      return;
    }
    var no = B.indexOf(b) + 1;
    panel.innerHTML = '<span class="etiket">' + no + ' · ' + b.yer + '</span><h2>' + b.ad + '</h2>' +
      '<div class="kim-kimyasal">' + b.kim.map(function (k) { return '<span>' + k + '</span>'; }).join('') + '</div>' +
      '<p>' + b.metin + '</p>' +
      '<div class="kim-alt"><b class="kd ' + b.kanit + '">' + KD[b.kanit] + '</b><span>' + b.kaynak + '</span></div>' +
      '<div class="kim-gez"><button id="kimOnce" aria-label="Previous stop">←</button><button id="kimSonra" aria-label="Next stop">Next stop →</button></div>';
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
