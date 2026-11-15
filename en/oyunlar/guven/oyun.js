/* Trust game — repeated trust game (based on the design of Berg, Dickhaut and McCabe, 1995) */
(function () {
  'use strict';
  var O = window.OYUN, R = O.R, NS = 'http://www.w3.org/2000/svg';
  var TUR = 10, BUTCE = 10;
  var kok = document.getElementById('oyun');
  var STRATEJI = {
    karsilikli: { ad: 'Reciprocal', aciklama: 'They answered your trust with trust. When you gave more, they gave back more generously; when you cut back, so did they.' },
    comert: { ad: 'Generous', aciklama: 'Every round they sent you back more than half of the tripled amount. However much you invested, you always came out ahead.' },
    firsatci: { ad: 'Opportunist', aciklama: 'They acted trustworthy for six rounds, then kept one of your big investments in a single go. After that they tried to win your trust back.' },
    temkinli: { ad: 'Cautious', aciklama: 'They gave back little at first. As you kept on trusting, they slowly opened up.' }
  };
  var s;
  function yeni() {
    var r = Math.random(), st = r < .4 ? 'firsatci' : r < .65 ? 'karsilikli' : r < .85 ? 'temkinli' : 'comert';
    s = { tur: 1, st: st, G: 50, gecmis: [], secim: 5, ihanet: 0, oran: .3, mesgul: false };
  }
  function geriVer(y) {
    var k = 3 * y, t = s.tur, onceki = s.gecmis.length ? s.gecmis[s.gecmis.length - 1].y : 5, f;
    if (y === 0) return 0;
    if (s.st === 'comert') f = .55;
    else if (s.st === 'karsilikli') f = y >= onceki - 1 ? .36 + .2 * (y / 10) : .22;
    else if (s.st === 'temkinli') { f = s.oran; if (y >= 5) s.oran = Math.min(.55, s.oran + .05); }
    else { // opportunist
      if (!s.ihanet && t >= 7 && y >= 4) { s.ihanet = t; return 0; }
      f = s.ihanet ? (y >= 5 ? .5 : .62) : .48;
    }
    return Math.max(0, Math.min(k, Math.round(k * f)));
  }
  // trust capital: builds slowly when returned, melts fast after betrayal
  function gHesap(G, y, r) {
    if (y === 0) G -= 2;
    else if (r >= y) G += 1.5 + y * .25 + Math.min(2, (r - y) * .15);
    else if (r === 0) G -= 22 + y * 2.2;
    else G -= 6 + (y - r) * 2.5;
    return Math.max(0, Math.min(100, Math.round(G)));
  }
  function guncelleG(y, r) { s.G = gHesap(s.G, y, r); }

  // ---------- scene ----------
  function figur(x, renk, ad) {
    return '<g><circle cx="' + x + '" cy="92" r="30" fill="none" stroke="' + renk + '" stroke-width="5"/>' +
      '<path d="M' + (x - 54) + ' 196q54-84 108 0" fill="none" stroke="' + renk + '" stroke-width="5" stroke-linecap="round"/>' +
      '<text x="' + x + '" y="232" text-anchor="middle" class="gv-ad" fill="' + renk + '">' + ad + '</text></g>';
  }
  function ciz() {
    kok.innerHTML =
      '<div class="gv-ust"><div><p class="oy-adim" id="gvTur"></p><div class="gv-tl" id="gvTl"></div></div>' +
      '<div class="gv-g"><small>Trust capital</small><div class="gv-g-cubuk"><i id="gvGi"></i></div><b id="gvGb"></b></div></div>' +
      '<svg id="gvSahne" class="gv-sahne" viewBox="0 0 800 300" role="img" aria-label="You on the left, your partner on the right. In the middle your investment triples.">' +
      '<defs><radialGradient id="gvIs"><stop offset="0" stop-color="#C99A2E" stop-opacity=".35"/><stop offset="1" stop-color="#C99A2E" stop-opacity="0"/></radialGradient></defs>' +
      figur(130, R.bordo, 'You') + figur(670, R.petrol, 'Partner') +
      '<circle id="gvIsik" cx="400" cy="120" r="96" fill="url(#gvIs)" opacity="0"/>' +
      '<circle cx="400" cy="120" r="46" fill="#fffaf2" stroke="#C99A2E" stroke-width="3" stroke-dasharray="4 7"/>' +
      '<text x="400" y="133" text-anchor="middle" class="gv-kat">×3</text>' +
      '<path d="M190 120H340M460 120H610" stroke="#d8ccbb" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/>' +
      '<g id="gvJ"></g><text id="gvMesaj" x="400" y="286" text-anchor="middle" class="gv-mesaj"></text></svg>' +
      '<div id="gvKontrol"></div>';
    turHazirla();
  }
  function jetonDiz(n) {
    var g = document.getElementById('gvJ'); g.innerHTML = '';
    for (var i = 0; i < BUTCE; i++) {
      var c = document.createElementNS(NS, 'circle');
      c.setAttribute('cx', 62 + (i % 5) * 34); c.setAttribute('cy', 252 + Math.floor(i / 5) * 0); c.setAttribute('r', 13);
      c.setAttribute('cy', i < 5 ? 248 : 278);
      c.setAttribute('class', 'gv-jeton' + (i < n ? ' secili' : ''));
      c.dataset.i = i; g.appendChild(c);
    }
  }
  function turHazirla() {
    s.mesgul = false;
    document.getElementById('gvTur').textContent = 'Round ' + s.tur + ' / ' + TUR;
    zamanCizgisi(); gGoster();
    document.getElementById('gvMesaj').textContent = '';
    jetonDiz(s.secim);
    var k = document.getElementById('gvKontrol');
    k.innerHTML = '<p class="oy-buyuk" style="margin:14px 0 6px">How many coins will you trust your partner with this round?</p>' +
      '<p class="oy-not" style="margin:0 0 12px">You have ' + BUTCE + ' coins. Every coin you hand over reaches your partner tripled. They decide for themselves how much of it to send back.</p>' +
      '<div class="gv-secim" role="radiogroup" aria-label="Amount to invest">' +
      Array.apply(null, Array(BUTCE + 1)).map(function (_, i) { return '<button role="radio" aria-checked="' + (i === s.secim) + '" data-n="' + i + '"' + (i === s.secim ? ' class="secili"' : '') + '>' + i + '</button>'; }).join('') + '</div>' +
      '<div class="oy-dugmeler"><button class="oy-btn" id="gvYatir">Trust them with ' + s.secim + (s.secim === 1 ? ' coin' : ' coins') + '</button></div>';
    k.querySelectorAll('.gv-secim button').forEach(function (b) {
      b.onclick = function () {
        s.secim = +b.dataset.n;
        k.querySelectorAll('.gv-secim button').forEach(function (x) { var on = x === b; x.classList.toggle('secili', on); x.setAttribute('aria-checked', on); });
        document.getElementById('gvYatir').textContent = 'Trust them with ' + s.secim + (s.secim === 1 ? ' coin' : ' coins');
        jetonDiz(s.secim);
      };
    });
    document.getElementById('gvYatir').onclick = oyna;
    if (s.tur === 1) O.iz('oyun-basladi', { oyun: 'guven' });
  }
  function zamanCizgisi() {
    var h = '';
    for (var t = 1; t <= TUR; t++) {
      var g = s.gecmis[t - 1], cls = 'gv-hucre';
      if (g) cls += g.y === 0 ? ' bos' : g.r >= g.y ? ' iyi' : g.r === 0 ? ' kotu' : ' zarar';
      else if (t === s.tur) cls += ' simdi';
      h += '<span class="' + cls + '" title="' + (g ? 'Round ' + t + ': you gave ' + g.y + ', got back ' + g.r : 'Round ' + t) + '"></span>';
    }
    document.getElementById('gvTl').innerHTML = h;
  }
  function gGoster() {
    var i = document.getElementById('gvGi'); i.style.width = s.G + '%';
    i.style.background = s.G >= 60 ? R.altin : s.G >= 35 ? '#b88a3a' : R.bordo;
    document.getElementById('gvGb').textContent = s.G;
  }

  // animation helpers
  function uc(el, from, to, sure, gecikme) {
    return el.animate([{ transform: 'translate(' + from[0] + 'px,' + from[1] + 'px)' }, { transform: 'translate(' + to[0] + 'px,' + to[1] + 'px)' }],
      { duration: sure, delay: gecikme || 0, easing: 'cubic-bezier(.5,0,.2,1)', fill: 'forwards' }).finished;
  }
  var hareketAz = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function bekle(ms) { return new Promise(function (r) { setTimeout(r, hareketAz ? 0 : ms); }); }
  function yeniJeton(x, y, r, cls) {
    var c = document.createElementNS(NS, 'circle'); c.setAttribute('cx', 0); c.setAttribute('cy', 0); c.setAttribute('r', r); c.setAttribute('class', 'gv-jeton ' + cls);
    c.style.transform = 'translate(' + x + 'px,' + y + 'px)'; document.getElementById('gvJ').appendChild(c); return c;
  }

  function oyna() {
    if (s.mesgul) return; s.mesgul = true;
    var y = s.secim, r = geriVer(y);
    document.getElementById('gvKontrol').querySelectorAll('button').forEach(function (b) { b.disabled = true; });
    var sure = hareketAz ? 1 : 520, g = document.getElementById('gvJ'), msg = document.getElementById('gvMesaj');
    var secili = Array.prototype.slice.call(g.querySelectorAll('.gv-jeton.secili'));
    // move the selected coins from their places to the middle
    var adimlar = secili.map(function (c, i) {
      var x0 = +c.getAttribute('cx'), y0 = +c.getAttribute('cy');
      c.setAttribute('cx', 0); c.setAttribute('cy', 0); c.style.transform = 'translate(' + x0 + 'px,' + y0 + 'px)';
      return uc(c, [x0, y0], [400 + (i % 5 - 2) * 6, 120 - Math.floor(i / 5) * 6], sure, i * 40);
    });
    msg.textContent = y ? y + (y === 1 ? ' coin is on its way' : ' coins are on their way') : 'You trusted them with nothing this round';
    Promise.all(adimlar).then(function () { return bekle(150); }).then(function () {
      secili.forEach(function (c) { c.remove(); });
      if (!y) return;
      var isik = document.getElementById('gvIsik');
      isik.animate([{ opacity: 0 }, { opacity: 1 }, { opacity: 0 }], { duration: hareketAz ? 1 : 700 });
      msg.textContent = y + (y === 1 ? ' coin' : ' coins') + ' ×3 = ' + 3 * y;
      var kat = [];
      for (var i = 0; i < 3 * y; i++) kat.push(yeniJeton(400 + (Math.random() - .5) * 60, 120 + (Math.random() - .5) * 60, 7, 'kucuk'));
      return bekle(550).then(function () {
        return Promise.all(kat.map(function (c, i) {
          var m = c.style.transform.match(/translate\(([-\d.]+)px,\s*([-\d.]+)px\)/);
          return uc(c, [+m[1], +m[2]], [612 + (i % 10) * 13, 250 + Math.floor(i / 10) * 13], sure, i * 15);
        }));
      }).then(function () { return bekle(350); }).then(function () {
        msg.textContent = 'Your partner is thinking…';
        return bekle(650);
      }).then(function () {
        var don = kat.slice(0, r), kal = kat.slice(r);
        kal.forEach(function (c) { c.animate([{ opacity: 1 }, { opacity: .25 }], { duration: 300, fill: 'forwards' }); });
        msg.textContent = r ? 'Your partner sent back ' + r + (r === 1 ? ' coin' : ' coins') : 'Your partner sent nothing back';
        return Promise.all(don.map(function (c, i) {
          var m = c.style.transform.match(/translate\(([-\d.]+)px,\s*([-\d.]+)px\)/);
          c.classList.add('donen');
          return uc(c, [+m[1], +m[2]], [222 + (i % 10) * 13, 250 + Math.floor(i / 10) * 13], sure, i * 25);
        }));
      });
    }).then(function () {
      var kazanc = BUTCE - y + r;
      s.gecmis.push({ y: y, r: r, k: kazanc, p: 3 * y - r });
      var onceG = s.G; guncelleG(y, r); gGoster(); zamanCizgisi();
      var fark = s.G - onceG;
      var yorum = !y ? 'You took no risk. You lost nothing, but no shared value was created either.' :
        r === 0 ? 'Betrayal. Trust capital melted by ' + (-fark) + ' points in a single round.' :
        r < y ? 'Less came back than you gave. Trust capital fell by ' + (-fark) + ' points.' :
        'More came back than you gave. Trust capital rose by only ' + fark + (fark === 1 ? ' point' : ' points') + '. Building it up is slow.';
      var k = document.getElementById('gvKontrol');
      k.innerHTML = '<div class="gv-ozet"><div><small>You trusted</small><b class="sen-r">' + y + '</b></div><div><small>Tripled</small><b class="alt-r">' + 3 * y + '</b></div><div><small>Came back</small><b class="o-r">' + r + '</b></div><div><small>Your round gain</small><b>' + kazanc + '</b></div></div>' +
        '<p class="gv-yorum' + (fark < 0 ? ' dusus' : '') + '">' + yorum + '</p>' +
        '<div class="oy-dugmeler"><button class="oy-btn" id="gvSonraki">' + (s.tur < TUR ? 'On to round ' + (s.tur + 1) : 'See the result') + '</button></div>';
      var b = document.getElementById('gvSonraki'); b.focus({ preventScroll: true });
      b.onclick = function () { if (s.tur < TUR) { s.tur++; turHazirla(); } else sonuc(); };
    });
  }

  // ---------- result ----------
  function stil() {
    var g = s.gecmis, ort = g.reduce(function (a, x) { return a + x.y; }, 0) / g.length;
    var ki = -1; g.forEach(function (x, i) { if (ki < 0 && x.y > 0 && (x.r === 0 || x.y - x.r >= 3)) ki = i; });
    if (ki > -1 && ki < g.length - 1) {
      var sonra = g.slice(ki + 1), sOrt = sonra.reduce(function (a, x) { return a + x.y; }, 0) / sonra.length;
      var son = sonra[sonra.length - 1].y;
      if (sOrt <= 2) return 'affetmeyen';
      if (sonra[0].y < g[ki].y && son >= 5) return 'affeden';
    }
    if (ort >= 7) return 'comert';
    if (ort <= 3) return 'temkinli';
    return 'karsilikli';
  }
  var STIL = {
    affeden: ['The forgiving strategist', 'When your trust was shaken you pulled back, but you did not close the door. As your partner acted trustworthy again, you invested again. In repeated games, “hurt but forgiving” strategies like this do well in the long run. The book’s warning applies here too: one big betrayal can change how you read the whole past. Repair is possible, but the saving starts again from scratch.'],
    affetmeyen: ['The door-closer', 'Once burned, you stopped investing and never came back. You protected yourself, and that is an understandable reaction. But here is the economics of the game: when nobody trusts, there is no value to triple at all. When trust capital hits zero, you lose more than the loss itself; you lose all future shared gains too.'],
    comert: ['The generous investor', 'Every round you handed over most of your budget. This is the strategy that grows shared value the most, because every coin you trust triples. It is also the riskiest. With a partner who returns the favour, generosity turns into capital; with an opportunist, it turns into a loss. That is how trust capital works: both sides have to invest for it to grow.'],
    temkinli: ['The cautious accountant', 'You kept the risk small and never lost big in any round. The price: when you trust little, there is little value to triple. Trust capital only grows by trusting. Caution protects you, but it also slows down how fast shared value grows in a relationship.'],
    karsilikli: ['The reciprocal player', 'Whatever your partner did, you adjusted to it. When they were generous you gave more; when they held back, you held back. In repeated games, this kind of reciprocity is one of the strongest strategies. It is also the logic of trust capital: each side watches the other’s past behaviour and invests in the future accordingly.']
  };
  function grafikCiz(x, X, Y, W, H) {
    var g = s.gecmis, bw = W / TUR, mx = 30;
    x.strokeStyle = '#d8ccbb'; x.lineWidth = 2; x.beginPath(); x.moveTo(X, Y + H); x.lineTo(X + W, Y + H); x.stroke();
    g.forEach(function (t, i) {
      var cx = X + i * bw + bw * .18, w = bw * .3;
      x.fillStyle = R.bordo; var h1 = t.y / mx * H; x.fillRect(cx, Y + H - h1, w, h1);
      x.fillStyle = R.petrol; var h2 = t.r / mx * H; x.fillRect(cx + w + 4, Y + H - h2, w, h2);
    });
    // trust capital line
    var G = 50, nok = [[X, Y + H - G / 100 * H]];
    var kopya = s.G; // recalculate
    var s0 = { G: 50 };
    g.forEach(function (t, i) {
      s0.G = gHesap(s0.G, t.y, t.r);
      nok.push([X + (i + 1) * bw, Y + H - s0.G / 100 * H]);
    });
    x.strokeStyle = R.altin; x.lineWidth = 7; x.lineJoin = 'round'; x.beginPath();
    nok.forEach(function (p, i) { if (i) x.lineTo(p[0], p[1]); else x.moveTo(p[0], p[1]); }); x.stroke();
    x.fillStyle = R.altin; nok.forEach(function (p) { x.beginPath(); x.arc(p[0], p[1], 8, 0, 7); x.fill(); });
    return kopya;
  }
  function sonuc() {
    var g = s.gecmis, sen = g.reduce(function (a, x) { return a + x.k; }, 0), o = g.reduce(function (a, x) { return a + x.p; }, 0);
    var stl = stil(), S = STIL[stl], st = STRATEJI[s.st];
    O.iz('oyun-bitti', { oyun: 'guven', sonuc: S[0], partner: st.ad });
    var gecG = [50], G0 = 50;
    g.forEach(function (t) { G0 = gHesap(G0, t.y, t.r); gecG.push(G0); });
    var bw = 64, H = 200, W = bw * TUR;
    var svg = '<svg class="gv-grafik" viewBox="0 0 ' + (W + 60) + ' ' + (H + 60) + '" role="img" aria-label="Round by round: what you trusted, what came back, and trust capital">' +
      [0, 10, 20, 30].map(function (v) { var yy = 20 + H - v / 30 * H; return '<line x1="40" x2="' + (W + 40) + '" y1="' + yy + '" y2="' + yy + '" stroke="#ece3d6"/><text x="32" y="' + (yy + 5) + '" text-anchor="end" class="gv-eks">' + v + '</text>'; }).join('') +
      g.map(function (t, i) {
        var x0 = 40 + i * bw + 12, h1 = t.y / 30 * H, h2 = t.r / 30 * H;
        return '<rect x="' + x0 + '" y="' + (20 + H - h1) + '" width="18" height="' + h1 + '" fill="' + R.bordo + '"/><rect x="' + (x0 + 21) + '" y="' + (20 + H - h2) + '" width="18" height="' + h2 + '" fill="' + R.petrol + '"/>' +
          '<text x="' + (x0 + 20) + '" y="' + (H + 44) + '" text-anchor="middle" class="gv-eks">' + (i + 1) + '</text>';
      }).join('') +
      '<polyline points="' + gecG.map(function (v, i) { return (40 + i * bw) + ',' + (20 + H - v / 100 * H); }).join(' ') + '" fill="none" stroke="' + R.altin + '" stroke-width="4" stroke-linejoin="round"/>' +
      gecG.map(function (v, i) { return '<circle cx="' + (40 + i * bw) + '" cy="' + (20 + H - v / 100 * H) + '" r="5" fill="' + R.altin + '"/>'; }).join('') + '</svg>';
    kok.innerHTML = '<div class="oy-sonuc"><p class="oy-adim">Ten rounds done</p><h2>' + S[0] + '</h2>' +
      '<div class="oy-olcu"><div><small>Your gain</small><b class="sen-r">' + sen + '</b><span>coins</span></div><div><small>Your partner’s gain</small><b class="o-r">' + o + '</b><span>coins</span></div>' +
      '<div><small>Shared value</small><b class="alt-r">' + (sen + o) + '</b><span>max 300</span></div><div><small>Trust capital</small><b>' + s.G + '</b><span>started at 50</span></div></div>' +
      svg + '<p class="gv-lejant"><i style="background:' + R.bordo + '"></i>you trusted <i style="background:' + R.petrol + '"></i>came back <i class="cizgi" style="background:' + R.altin + '"></i>trust capital (0–100)</p>' +
      '<p>' + S[1] + '</p>' +
      '<div class="gv-partner"><small>Your partner’s strategy</small><b class="o-r">' + st.ad + '</b><p>' + st.aciklama + (s.ihanet ? ' The betrayal came in round ' + s.ihanet + '.' : '') + '</p></div>' +
      '<p class="not">In the book: Chapter 24 · Trust Capital. The game is based on the classic trust game of experimental economics (Berg, Dickhaut and McCabe, 1995).</p>' +
      O.paylasHTML() + O.abone() +
      '<div class="oy-dugmeler"><button class="oy-btn ikincil" id="gvYeniden">Play with a new partner</button></div></div>';
    O.paylasBagla(kok, { slug: 'guven', mesaj: 'My strategy in the Aşkonomi trust game: “' + S[0] + '”. Shared value: ' + (sen + o) + '/300. What’s yours?',
      kartAyar: { oyun: 'The trust game', baslik: S[0], alt: 'Shared value ' + (sen + o) + ' / 300 · my partner: ' + st.ad, ciz: function (x, X, Y, W, H) { grafikCiz(x, X + 20, Y + 20, W - 40, H - 60); } } });
    document.getElementById('gvYeniden').onclick = function () { yeni(); ciz(); window.scrollTo({ top: 0, behavior: 'smooth' }); };
    kok.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  yeni(); ciz();
})();
