#!/usr/bin/env python3
"""Generates the ZIBTR PRO redesign pages. Run: python3 _build.py"""
import os, html
OUT = os.path.dirname(os.path.abspath(__file__))
PDF = "https://www.zibtrpro.si/modules/uploader/uploads/catalogue/files_catalogue/"
E = html.escape

ARR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
ARL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 12H5M11 6l-6 6 6 6"/></svg>'
CHEV = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M2 4l4 4 4-4"/></svg>'

def mask(text):
    return "".join(f'<span class="mask"><span>{line}</span></span>' for line in text.split("|"))

# ---------------------------------------------------------------- data
PROGRAMS = [
    dict(slug="rezilno-orodje", name="Rezilno orodje", img="assets/cats/High_Feed_1.png",
         subs=[("Rezkanje", "#rezkanje"), ("Rezkanje navojev", "#navoji"), ("Vrtanje", "#vrtanje")]),
    dict(slug="vpenjalni-sistemi", name="Vpenjalni sistemi", img="assets/cats/SMW_AUTOBLOK_OML_prime_i_5_axis.png",
         subs=[("Stružne glave", "#struzne-glave"), ("Primeži", "#primezi"), ("Magnetna vpenjala", "#magnetna"), ("Čeljusti za stružne glave", "#celjusti")]),
    dict(slug="merilno-orodje", name="Merilno orodje", img="assets/cats/Nehrg.png",
         subs=[("Pomična merila", "#pomicna-merila"), ("TESA Technology", "#znamke"), ("Schut", "#znamke")]),
]

FEATURED = [
    ("Svedri TEZD 3D / 5D / 8D", "Vrtanje", "assets/cats/Nszhjf.png", False, "rezilno-orodje.html#vrtanje"),
    ("Pomično merilo TESA-CAL IP67", "Merilno orodje", "assets/cats/Tesa_Cal.png", True, "merilno-orodje.html"),
    ("Rezkarji Hifeed Integ", "Rezkanje", "assets/cats/Hifeed_Integ.png", False, "rezilno-orodje.html#rezkanje"),
    ("Rezila TEZ", "Vrtanje", "assets/cats/Navsfd.png", False, "rezilno-orodje.html#vrtanje"),
    ("Rezkarji Tip 918", "Rezkanje", "assets/cats/tip_918.jpg", True, "rezilno-orodje.html#rezkanje"),
    ("Magnetne mize PSP", "Magnetna vpenjala", "assets/cats/New_Project_199_.png", False, "vpenjalni-sistemi.html#magnetna"),
    ("Primež IMG", "Primeži", "assets/cats/Negsfdhn.png", False, "vpenjalni-sistemi.html#primezi"),
    ("Primež GENIUS za 5-osno obdelavo", "Primeži", "assets/cats/New_gsfdr.png", True, "vpenjalni-sistemi.html#primezi"),
    ("Pomično merilo TWIN-CAL IP67", "Merilno orodje", "assets/cats/Twin_Cal.png", True, "merilno-orodje.html"),
    ("Stružna glava AND", "Stružne glave", "assets/cats/New_Project_210_.png", False, "vpenjalni-sistemi.html#struzne-glave"),
    ("Stružna glava BHD", "Stružne glave", "assets/cats/New_Project_209_.png", False, "vpenjalni-sistemi.html#struzne-glave"),
    ("Svedri XCS 2D", "Vrtanje", "assets/cats/New_Prsfgnxyoject.png", False, "rezilno-orodje.html#vrtanje"),
]

CATALOGUES = [  # title, brand, cover, pdf
    ("HEXAFEED", "PALBIT", "PALBIT_HEXAFEED", "PALBIT_HEXAFEED.pdf"),
    ("GripLock novosti 10-2026", "KEMMER", "KEMMER_GripLock_novosti_10_2026", "KEMMER_GripLock_novosti_10_2026.pdf"),
    ("High Feed QM MXG-07", "DIJET", "DIJET_QM_GII", "DIJET_QM_GII_07.pdf"),
    ("Novosti 2026", "CPT", "CPT_Novosti_2026", "CPT_Novosti_2026.pdf"),
    ("Robotska prijemala", "SMW-AUTOBLOK", "SMW_Robotska_prijemala_2026", "SMW_Robotska_prijemala_2026.pdf"),
    ("Die & Mold", "HPMT", "HPMT_DM70X", "HPMT_DM70X.pdf"),
    ("VARIA Next", "EWS", "EWS_VARIA_Next", "EWS_VARIA_Next.pdf"),
    ("CST Skip Tooth", "CPT", "CPT_Navojni_rezkarji_CST", "CPT_Navojni_rezkarji_CST.pdf"),
    ("HEXAPLUS", "PALBIT", "PALBIT_HEXAPLUS_49490_49590", "PALBIT_HEXAPLUS_49490_49590.pdf"),
    ("CBN struženje", "PALBIT", "PALBIT_PCBN_for_Turning", "PALBIT_PCBN_Turning.pdf"),
    ("W-PRO LINE", "PALBIT", "PALBIT_W_PRO", "PALBIT_W_PRO.pdf"),
    ("Navojni rezkarji CM Line", "CPT", "CPT_Navojni_rezkarji_CM_Line", "CPT_Navojni_rezkarji_CM_Line.pdf"),
    ("VARIA Nastavki", "EWS", "EWS_VARIA_Adapter", "EWS_VARIA_Adapter.pdf"),
    ("VARIA VX Quick change", "EWS", "EWS_VARIA_VX_1", "EWS_VARIA_VX_Quick_change.pdf"),
    ("VARIA VXT Turning", "EWS", "EWS_VARIA_VXT_Turning", "EWS_VARIA_VXT_Turning.pdf"),
    ("Anti-vibracijska držala", "EWS", "EWS_Boring_Bars", "EWS_Boring_Bars.pdf"),
    ("Ready Safe and Go", "EWS", "EWS_VARIA_VX", "EWS_VARIA_VX.pdf"),
    ("Enostavno čiščenje", "EWS", "EWS_Prodigy", "EWS_Prodigy.pdf"),
    ("Avtomatizacija", "SMW-AUTOBLOK", "page1_1_1", "SMW_AUTOBLOK_AUTOMATION_2024.pdf"),
    ("GripLock novosti 01-2026", "KEMMER", "KEMMER_Novosti_GripLock_2026", "KEMMER_Novosti_GripLock_2026.pdf"),
]

BRANDS = [  # name, logo, photo
    ("SMW-AUTOBLOK", "smw_autoblok.png", "SMW_Autoblok_vpenjalni_steber.png"),
    ("CPT", "CPT_Logo.png", "cpt___slika2.png"),
    ("TESA", "tesa.png", "tesa___slika_za_internet1.png"),
    ("EWS", "ews.png", "ews_3x_0_0.jpg"),
    ("DIJET", "822.png", "dijet_predstavitvena_slika.jpg"),
    ("HPMT", "HPMT.png", "hpmt_slika_rezkarji.png"),
    ("Palbit", None, "palbit.png"),
    ("Kemmer", "kemmer.png", "Grip_Lock.png"),
    ("OML", "oml.png", "oml___primezi_img_0.png"),
    ("Botek", "botek.png", "botek_slika.png"),
    ("iLiX", "ilix.png", "ilix___naslovnica1_0.png"),
    ("BASS", "bass_tools.png", "BASS.png"),
    ("Mario Pinto", "MARIO_PINTO_logo.png", "mario_pinto_slika.jpg"),
    ("NT Tool", "nt_tool.png", "nt_slika_cts_2.jpg"),
    ("SIMTEK", "simtek.png", "simtek_pregledna2.jpg"),
    ("BRISC", "brisc_logo_update.png", "brisc.png"),
    ("Conzella", "conzella.png", "conzella_slika_1_0.png"),
    ("Pinzbohr", "images.png", "pinzbohr_slika_1_0.png"),
    ("Rineck", "rineck.png", "rineck_slika.png"),
    ("Schut", "schut.png", "schut___slika_za_internet2.png"),
    ("Tapmatic", "tapmatic.png", "tapmatic_1_0.jpg"),
    ("ThurMetall", "ThurMetall.png", "Thurmetall_TM.png"),
    ("EROGLU", "EROGLU_logo_111114444444_removebg_preview.png", None),
    ("OMG", "346.png", None),
]

APPS = ["Tool Advisor", "Testna poročila odrezilnih ploščic", "Poiščite pravo orodje za izdelavo navoja",
        "Namestitev in nastavitev TA kotnih glav", "Čeljusti za vsako stružno glavo", "Gnana orodja"]

# ---------------------------------------------------------------- partials
def head(title, desc):
    return f"""<!doctype html>
<html lang="sl" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="noindex">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preload" href="assets/fonts/Aeonik-Medium.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
"""

def nav(active=""):
    def a(href, label, key):
        cls = ' class="is-active"' if key == active else ""
        return f'<a href="{href}"{cls}>{label}</a>'
    mega_cols = ""
    for p in PROGRAMS:
        subs = "".join(f'<li><a href="{p["slug"]}.html{h}">{E(n)}</a></li>' for n, h in p["subs"])
        mega_cols += f"""<div class="mega__col"><a class="mega__head" href="{p['slug']}.html"><div class="mega__img"><img src="{p['img']}" alt=""></div><h3>{p['name']}</h3></a><ul>{subs}</ul></div>"""
    mob_subs = "".join(f'<a href="{p["slug"]}.html">{p["name"]}</a>' for p in PROGRAMS)
    return f"""<div class="loader" aria-hidden="true"><div class="loader__in"><img src="assets/img/logo.png" alt=""><div class="loader__line"></div></div></div>
<header class="nav">
  <a class="nav__logo" href="index.html" aria-label="ZIBTR PRO domov"><img src="assets/img/logo.png" alt="ZIBTR PRO" width="220" height="37"></a>
  <nav class="nav__links" aria-label="Glavna navigacija">
    <button type="button" data-mega aria-expanded="false" class="{'is-active' if active=='program' else ''}">Prodajni program {CHEV}</button>
    {a('proizvajalci.html','Proizvajalci','proizvajalci')}
    {a('o-nas.html','O nas','o-nas')}
    {a('index.html#aplikacije','Aplikacije','apps')}
    {a('kontakt.html','Kontakt','kontakt')}
  </nav>
  <div class="nav__right">
    <a class="tel" href="tel:+38618962280">01 896 22 80</a>
    <a class="shop" href="https://www.zibtrpro.si/e-trgovina">E-trgovina</a>
    <a class="btn btn--ink" href="kontakt.html#b2b">Prijava B2B</a>
    <button class="burger" type="button" aria-label="Meni" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>
<div class="mega" role="region" aria-label="Prodajni program">
  {mega_cols}
  <a class="mega__promo" href="vpenjalni-sistemi.html#struzne-glave">
    <div><h3>CENTCO 4</h3><p>Ena glava za vse obdelovance in aplikacije.</p></div>
    <img src="assets/hero/CENTCO4_2.png" alt="">
    <span class="link">Odkrijte {ARR}</span>
  </a>
</div>
<div class="mega-veil"></div>
<div class="mmenu">
  <nav>
    <a href="index.html">Domov</a>
    <div class="sub">{mob_subs}</div>
    <a href="proizvajalci.html">Proizvajalci</a>
    <a href="o-nas.html">O nas</a>
    <a href="kontakt.html">Kontakt</a>
  </nav>
  <div class="mmenu__foot">
    <a href="tel:+38618962280">01 896 22 80</a>
    <a href="mailto:info@zibtrpro.si">info@zibtrpro.si</a>
    <a class="btn btn--ink" href="kontakt.html#b2b" style="justify-self:start">Prijava B2B</a>
  </div>
</div>
<main>
"""

def b2b():
    return f"""<section class="b2b" id="b2b">
  <h2 data-split>{mask('Postanite naš|poslovni partner.')}</h2>
  <div class="rv">
    <p>Spletna trgovina B2B je namenjena poslovnim partnerjem podjetja ZIBTR PRO za enostaven nakup izdelkov in pregled naročil. Registrirajte se in pridobite dostop do cen in statusa naročil.</p>
    <div class="btns">
      <a class="btn btn--white" href="https://www.zibtrpro.si/?mod=user&amp;c=user&amp;action=new_registration&amp;lang=sl">Registracija {ARR}</a>
      <a class="btn btn--ghost" href="https://www.zibtrpro.si/">Prijava B2B</a>
    </div>
  </div>
</section>
"""

def foot():
    prog = "".join(f'<li><a href="{p["slug"]}.html">{p["name"]}</a></li>' for p in PROGRAMS)
    return f"""</main>
<footer class="foot">
  <div class="foot__big">
    <a href="mailto:info@zibtrpro.si">info@zibtrpro.si</a>
    <a href="tel:+38618962280">01 896 22 80</a>
  </div>
  <div class="foot__cols">
    <div>
      <a class="foot__logo" href="index.html"><img src="assets/img/logo.png" alt="ZIBTR PRO"></a>
      <p class="foot__addr">ZIBTR PRO d.o.o.<br>Zgornji Hotič 25b<br>1270 Litija, Slovenija</p>
    </div>
    <div><h4>Prodajni program</h4><ul>{prog}<li><a href="index.html#novo">Novo v ponudbi</a></li></ul></div>
    <div><h4>Podjetje</h4><ul><li><a href="o-nas.html">O nas</a></li><li><a href="proizvajalci.html">Proizvajalci</a></li><li><a href="index.html#aplikacije">Aplikacije</a></li><li><a href="kontakt.html">Kontakt</a></li><li><a href="https://si.linkedin.com/in/zibtrpro">LinkedIn</a></li></ul></div>
    <div><h4>Nakupovanje</h4><ul><li><a href="https://www.zibtrpro.si/e-trgovina">Spletna trgovina</a></li><li><a href="https://www.zibtrpro.si/dostava">Dostava</a></li><li><a href="https://www.zibtrpro.si/pogoji-poslovanja">Splošni pogoji poslovanja</a></li><li><a href="https://www.zibtrpro.si/politika-zasebnosti">Politika zasebnosti</a></li><li><a href="https://www.zibtrpro.si/okoljska-odgovornost">Okoljska odgovornost</a></li></ul></div>
  </div>
  <div class="foot__legal"><span>© 2023–2026 ZIBTR PRO d.o.o. Vse pravice pridržane.</span><span>Rezilno, merilno in vpenjalno orodje za CNC obdelavo</span></div>
</footer>
<script src="assets/js/gsap.min.js"></script>
<script src="assets/js/ScrollTrigger.min.js"></script>
<script src="assets/js/lenis.min.js"></script>
<script src="assets/js/site.js"></script>
</body>
</html>
"""

def card(name, cat, img, sale, href):
    tag = '<span class="tag">Akcija</span>' if sale else ""
    return f"""<a class="card" href="{href}">{tag}<div class="card__img"><img src="{img}" alt="{E(name)}" loading="lazy"></div><span class="card__cat">{E(cat)}</span><h3>{E(name)}</h3><div class="card__foot"><span>Podrobneje</span>{ARR}</div></a>"""

def text_card(name, big, href, note=""):
    n = f'<span class="card__cat">{E(note)}</span>' if note else ""
    return f"""<a class="card card--text" href="{href}"><span class="card__big">{E(big)}</span><div>{n}<h3>{E(name)}</h3></div></a>"""

def cover(t, brand, img, pdf, more=False):
    cls = " is-more" if more else ""
    return f"""<a class="cover{cls}" href="{PDF}{pdf}" target="_blank" rel="noopener"><div class="cover__img"><img src="assets/cat/{img}.jpg" alt="{E(t)}" loading="lazy"></div><h4>{E(t)}</h4><span>{E(brand)}</span></a>"""

def brand_tile(name, logo, photo):
    inner = f'<img class="brand__logo" src="assets/logos/{logo}" alt="{E(name)}" loading="lazy">' if logo else f'<span class="brand__name">{E(name)}</span>'
    if photo:
        inner += f'<img class="brand__photo" src="assets/logos/{photo}" alt="" loading="lazy"><span class="brand__lbl">{E(name)}</span>'
    return f'<div class="brand">{inner}</div>'

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)

# ---------------------------------------------------------------- home
HERO = [
    ("Centco 4", "assets/hero/CENTCO4_2.png", "Ena glava za vse obdelovance in aplikacije.", "vpenjalni-sistemi.html#struzne-glave"),
    ("Tip-K", "assets/hero/type_k_removebg_preview.png", "Revolucija struženja navojev se nadaljuje. Novi TIP-K.", "rezilno-orodje.html#navoji"),
    ("HiFeed", "assets/hero/hifeed_removebg_preview.png", "PALBIT HiFeed. Ko hitrost postane standard.", "rezilno-orodje.html#rezkanje"),
    ("IMG", "assets/hero/img_removebg_preview_1_.png", "Primeži IMG. Domišljija ne pozna meja.", "vpenjalni-sistemi.html#primezi"),
    ("TDM", "assets/hero/tdm_removebg_preview_1_.png", "Sledi rdeči črti. TDM Zero Point.", "vpenjalni-sistemi.html#primezi"),
]

def home():
    words = "".join(f'<div class="hero__word" aria-hidden="true">{w}</div>' for w, *_ in HERO)
    prods = "".join(f'<div class="hero__prod"><img class="hero__float" src="{img}" alt="{E(w)}" style="animation-delay:-{i*1.3}s"></div>' for i, (w, img, *_rest) in enumerate(HERO))
    caps = "".join(f'<div class="hero__cap"{"" if i==0 else " hidden"}><p>{E(c)}</p><a class="link" href="{h}">Preberite več {ARR}</a></div>' for i, (w, img, c, h) in enumerate(HERO))
    tabs = "".join(f'<button class="hero__tab{" is-on" if i==0 else ""}" type="button"><i></i>{E(w)}</button>' for i, (w, *_r) in enumerate(HERO))

    statement_txt = "Od leta 1992 svetujemo, tehnično podpiramo in optimiziramo procese CNC obdelave kovin. Za avtomobilsko industrijo, orodjarstvo in strojegradnjo."
    st_words = " ".join(f'<span class="w">{E(w)}</span>' for w in statement_txt.split())

    progs = ""
    for p in PROGRAMS:
        subs = "".join(f'<li><a href="{p["slug"]}.html{h}">{E(n)}</a></li>' for n, h in p["subs"])
        progs += f"""<div class="prog"><h3><a class="prog__main" href="{p['slug']}.html">{p['name'].replace(' ', '<br>')}</a></h3><div class="prog__img"><img src="{p['img']}" alt="" loading="lazy"></div><div class="prog__foot"><ul>{subs}</ul><span class="arrow">{ARR}</span></div></div>"""

    cards = "".join(card(*f) for f in FEATURED)
    covers = "".join(cover(*c, more=i >= 8) for i, c in enumerate(CATALOGUES))
    wall = "".join(brand_tile(*b) for b in BRANDS)
    apps = "".join(f'<a class="app" href="https://www.zibtrpro.si/aplikacije"><span>0{i+1}</span><h3>{E(a)}</h3><span class="arrow">{ARR}</span></a>' for i, a in enumerate(APPS))

    body = f"""<section class="hero">
  <div class="hero__words">{words}</div>
  <div class="hero__stage">{prods}</div>
  <p class="hero__top">Oprema za CNC stroje in delavnice<br>Litija, Slovenija</p>
  <div class="hero__bottom">
    <h1>{mask('Rezilno, merilno in|vpenjalno orodje za CNC|struženje in rezkanje.')}</h1>
    <div class="hero__side">{caps}<div class="hero__tabs">{tabs}</div></div>
  </div>
</section>

<section class="statement"><p>{st_words}</p></section>
<div class="stats" data-stagger>
  <div class="stat"><b>1992</b><p>Ustanovitev podjetja ZIBTR</p></div>
  <div class="stat"><b data-count="2018" data-from="1992">2018</b><p>Nova lokacija in novo ime ZIBTR PRO</p></div>
  <div class="stat"><b data-count="{len(BRANDS)}">{len(BRANDS)}<sup>+</sup></b><p>Zaupanja vrednih evropskih in svetovnih proizvajalcev</p></div>
  <div class="stat"><b data-count="4">4</b><p>Področja: rezilno, vpenjalno in merilno orodje ter avtomatizacija</p></div>
</div>

<section id="program">
  <div class="sec-head"><h2 class="d2" data-split>{mask('Prodajni program')}</h2><p class="lead rv">Vse za CNC struženje in rezkanje na enem mestu. Od rezkarja do primeža in pomičnega merila.</p></div>
  <div class="programs">{progs}</div>
</section>

<section class="story">
  <div class="story__pin">
    <div class="story__glow"></div>
    <div class="story__intro">
      <h2>Ena glava za vse obdelovance.</h2>
      <p>Štiričeljustna vpenjalna glava SMW-AUTOBLOK CENTCO 4 s samocentrirnim in kompenzacijskim vpenjanjem 2+2.</p>
      <a class="btn btn--red" href="{PDF}smw_vpenjalna_glava_centco_4_prednosti.pdf" target="_blank" rel="noopener">Prednosti CENTCO 4 {ARR}</a>
    </div>
    <div class="story__prod"><div class="story__ring"></div><img src="assets/hero/CENTCO4_2.png" alt="SMW-AUTOBLOK CENTCO 4"></div>
    <div class="story__facts">
      <div class="fact is-on"><b>2+2</b><p>Samocentrirno vpenjanje v dveh oseh. Sila se vzpostavi šele, ko se obdelovanca dotaknejo vse štiri čeljusti.</p></div>
      <div class="fact"><b>4 mm<small>na čeljust</small></b><p>Kompenzacijski hod, npr. pri Ø 260, pokrije velike tolerance surovih kosov.</p></div>
      <div class="fact"><b>210–400</b><p>Hidravlične izvedbe. Ročne izvedbe od 600 do 1400.</p></div>
      <div class="fact"><b>1 set</b><p>Standardne čeljusti za kvadratne, okrogle, nepravilne in tankostenske obdelovance.</p></div>
    </div>
    <div class="story__bar"><i></i></div>
  </div>
</section>

<section class="rail-sec" data-rail>
  <div class="sec-head"><h2 class="d2" data-split>{mask('Priporočeni izdelki')}</h2><div class="rail-ctrl"><button type="button" data-prev aria-label="Nazaj">{ARL}</button><button type="button" data-next aria-label="Naprej">{ARR}</button></div></div>
  <div class="rail">{cards}</div>
</section>

<section class="cats" id="novo">
  <div class="cats__side">
    <h2 class="d2" data-split>{mask('Novo v|ponudbi')}</h2>
    <p class="lead">Najnovejši katalogi in novosti naših proizvajalcev. Kliknite naslovnico in prenesite PDF.</p>
    <button class="btn btn--ink" type="button" data-more="#catgrid" data-label="Vsi katalogi ({len(CATALOGUES)})"><span>Vsi katalogi ({len(CATALOGUES)})</span> {ARR}</button>
  </div>
  <div class="cats__grid" id="catgrid">{covers}</div>
</section>

<section class="partners">
  <div class="sec-head"><h2 class="d2" data-split>{mask('Proizvajalci, ki|jim zaupamo')}</h2><a class="link rv" href="proizvajalci.html">Vsi proizvajalci {ARR}</a></div>
  <div class="wall" data-stagger>{wall}</div>
</section>

<section class="apps" id="aplikacije">
  <div class="sec-head" style="padding:0"><h2 class="d2" data-split>{mask('Aplikacije')}</h2><p class="lead rv">Orodja, testi in navodila, s katerimi hitreje izberete in nastavite pravo orodje.</p></div>
  <div class="apps__list">{apps}</div>
</section>
"""
    write("index.html", head("ZIBTR PRO | Rezilno, merilno in vpenjalno orodje za CNC", "Rezilno, merilno ter vpenjalno orodje za CNC struženje in rezkanje. ZIBTR PRO, Litija.") + nav() + body + b2b() + foot())

# ---------------------------------------------------------------- category pages
def group(id_, title, lead, inner):
    return f"""<section class="group" id="{id_}"><div class="group__head"><h2 class="d2" data-split>{mask(title)}</h2><p class="lead rv">{lead}</p></div>{inner}</section>"""

def catpage(slug, title, lead, img, jumps, groups, cats, crumbs_name):
    j = "".join(f'<a href="#{i}">{E(n)}</a>' for n, i in jumps)
    covers = "".join(cover(*c) for c in cats)
    catsec = f"""<section class="group"><div class="group__head"><h2 class="d2" data-split>{mask('Katalogi')}</h2><p class="lead rv">Prenesite aktualne kataloge in novosti v PDF obliki.</p></div><div class="cats__grid" style="padding:0 var(--pad);grid-template-columns:repeat(auto-fill,minmax(200px,1fr))" data-stagger>{covers}</div></section>""" if cats else ""
    body = f"""<section class="phero">
  <div class="crumbs"><a href="index.html">Domov</a> / Prodajni program</div>
  <div><h1>{mask(title)}</h1><p class="lead">{lead}</p><div class="jump">{j}</div></div>
  <div class="phero__img"><img src="{img}" alt="" data-par></div>
</section>
{''.join(groups)}
{catsec}
<div style="height:clamp(110px,12vw,200px)"></div>
"""
    write(f"{slug}.html", head(f"{title.replace('|',' ')} | ZIBTR PRO", lead) + nav("program") + body + b2b() + foot())

def grid(items):
    return f'<div class="grid" data-stagger>{"".join(items)}</div>'

def rezilno():
    thread_rows = [
        ("Navojni rezkarji MT", "", ["ISO", "UN", "G (55°)", "NPT"]),
        ("Navojni rezkarji MTB", "", ["ISO", "UN", "G (55°)", "Whitworth", "NPT"]),
        ("Navojni rezkarji MTZ", "", ["ISO", "UN", "G (55°)", "Whitworth", "NPT"]),
        ("Navojni rezkarji MTSH", "Za kaljene materiale do 62 HRc", ["ISO", "G (55°)"]),
    ]
    def mrow(n, s, chips):
        small = "<small>" + E(s) + "</small>" if s else ""
        ch = "".join('<a href="#navoji">' + E(c) + "</a>" for c in chips)
        return f'<div class="mrow"><h3>{E(n)}{small}</h3><div class="chips">{ch}</div></div>'
    rows = "".join(mrow(*r) for r in thread_rows)
    groups = [
        group("rezkanje", "Rezkanje", "Trdokovinski rezkarji, rezkalne glave in držala ter podaljški za rezkalne glave z navojem.", grid([
            card("Trdokovinski rezkarji", "Rezkanje", "assets/cats/Rezkarji_HM.png", False, "#rezkanje"),
            card("Rezkarji Tip 918", "Trdokovinski rezkarji", "assets/cats/tip_918.jpg", True, "#rezkanje"),
            card("Rezkarji Hifeed Integ", "Trdokovinski rezkarji", "assets/cats/Hifeed_Integ.png", False, "#rezkanje"),
            card("Rezkalne glave in držala", "Rezkanje", "assets/cats/High_Feed_1.png", False, "#rezkanje"),
            text_card("Podaljšek MSN", "MSN", "#rezkanje", "Podaljški za rezkalne glave z navojem"),
            text_card("Podaljšek MSN-S", "MSN-S", "#rezkanje", "Podaljški za rezkalne glave z navojem"),
        ])),
        group("navoji", "Rezkanje|navojev", "Navojni rezkarji za vse standardne navoje, tudi za kaljene materiale do 62 HRc.", f'<div class="matrix rv">{rows}</div>'),
        group("vrtanje", "Vrtanje", "Svedri MAXPRO, XCS in TEZD na izmenljive konice, MULTICUT za vrtanje in struženje ter BOTEK topovski svedri.", grid([
            card("Svedri TEZD 3D / 5D / 8D", "Na izmenljive konice", "assets/cats/Nszhjf.png", False, "#vrtanje"),
            card("Rezila TEZ", "Na izmenljive konice", "assets/cats/Navsfd.png", False, "#vrtanje"),
            card("Svedri XCS 2D", "Svedri XCS", "assets/cats/New_Prsfgnxyoject.png", False, "#vrtanje"),
            card("BOTEK Topovski svedri 110", "Topovsko vrtanje", "assets/logos/botek_slika.png", False, "#vrtanje"),
            text_card("Svedri MAXPRO", "MAX", "#vrtanje", "High Performance Line"),
            text_card("Svedri XCS 3D / 4D / 5D", "XCS", "#vrtanje", "Rezila SOKX / XKOX"),
            text_card("MULTICUT", "MC", "#vrtanje", "Za vrtanje in struženje. Držala XMS, rezila XCMT"),
            card("Vrtanje", "Pregled programa", "assets/cats/Drilling.png", False, "#vrtanje"),
        ])),
    ]
    cats = [c for c in CATALOGUES if c[1] in ("PALBIT", "CPT", "DIJET", "HPMT")]
    catpage("rezilno-orodje", "Rezilno|orodje", "Rezkanje, rezkanje navojev in vrtanje. Trdokovinski rezkarji, navojni rezkarji in svedri vodilnih evropskih in svetovnih proizvajalcev.",
            "assets/cats/5.png", [("Rezkanje", "rezkanje"), ("Rezkanje navojev", "navoji"), ("Vrtanje", "vrtanje")], groups, cats, "Rezilno orodje")

def vpenjalni():
    groups = [
        group("struzne-glave", "Stružne|glave", "Stružne glave AND in BHD, prirobnice ter vpenjalni trni. Za vsak obdelovanec prava vpenjalna rešitev.", grid([
            card("Stružna glava AND", "Stružne glave", "assets/cats/New_Project_210_.png", False, "#struzne-glave"),
            card("Stružna glava BHD", "Stružne glave", "assets/cats/New_Project_209_.png", False, "#struzne-glave"),
            card("Vpenjalni trni", "Stružne glave", "assets/cats/New_Project_161_.png", False, "#struzne-glave"),
            text_card("Prirobnice", "Ø", "#struzne-glave", "Stružne glave"),
        ])),
        group("primezi", "Primeži", "Primeži IMG, primež GENIUS za 5-osno obdelavo in sistemi ničelne točke TDM Zero Point.", grid([
            card("Primež IMG", "Primeži", "assets/cats/Negsfdhn.png", False, "#primezi"),
            card("Primež GENIUS za 5-osno obdelavo", "Primeži", "assets/cats/New_gsfdr.png", True, "#primezi"),
            card("TDM Zero Point", "Sistemi ničelne točke", "assets/hero/tdm_removebg_preview_1_.png", False, "#primezi"),
            card("Primeži IMG", "Domišljija ne pozna meja", "assets/hero/img_removebg_preview_1_.png", False, "#primezi"),
        ])),
        group("magnetna", "Magnetna|vpenjala", "Elektro-permanentne magnetne mize BRISC-AA in BRISC-BB z visoko toleranco izdelave, magnetne mize PSP in kontrolne enote.", grid([
            card("Magnetne mize AA / BB", "Elektro-permanentne", "assets/cats/BRISC_MAGNETNE_MIZE_AA.png", False, "#magnetna"),
            card("Magnetne mize PSP", "Magnetna vpenjala", "assets/cats/New_Project_199_.png", False, "#magnetna"),
            card("Magnetna vpenjala", "Pregled programa", "assets/cats/New_Project_160_.png", False, "#magnetna"),
            text_card("Kontrolne enote CUA / CUD", "CU", "#magnetna", "Magnetna vpenjala"),
        ])),
        group("celjusti", "Čeljusti", "Mehke čeljusti za stružne glave v metričnih in colskih izvedbah.", grid([
            card("Mehke čeljusti", "Čeljusti za stružne glave", "assets/cats/New_Project_158_.png", False, "#celjusti"),
            text_card("Metrične mehke čeljusti AWB-M", "M", "#celjusti", "Čeljusti za stružne glave"),
            text_card("Colske mehke čeljusti AWB-D", "″", "#celjusti", "Čeljusti za stružne glave"),
            card("Čeljusti za vsako stružno glavo", "Aplikacije", "assets/logos/BH_D_1.png", False, "index.html#aplikacije"),
        ])),
    ]
    cats = [c for c in CATALOGUES if c[1] in ("SMW-AUTOBLOK", "EWS", "KEMMER")]
    catpage("vpenjalni-sistemi", "Vpenjalni|sistemi", "Stružne glave, primeži, magnetna vpenjala in čeljusti. Zanesljivo vpenjanje za struženje, rezkanje in 5-osno obdelavo.",
            "assets/cats/SMW_AUTOBLOK_OML_prime_i_5_axis.png", [("Stružne glave", "struzne-glave"), ("Primeži", "primezi"), ("Magnetna vpenjala", "magnetna"), ("Čeljusti", "celjusti")], groups, cats, "Vpenjalni sistemi")

def merilno():
    brands = f"""<div class="brands-strip" data-stagger>
      <div class="bcard"><div class="bcard__txt"><img src="assets/logos/tesa.png" alt="TESA Technology"><p class="lead">Ročna merila, višinomeri in merilni instrumenti švicarske natančnosti.</p></div><div class="bcard__ph"><img src="assets/logos/tesa___slika_za_internet1.png" alt=""></div></div>
      <div class="bcard"><div class="bcard__txt"><img src="assets/logos/schut.png" alt="Schut"><p class="lead">Merilna oprema za delavnico in merilnico.</p></div><div class="bcard__ph"><img src="assets/logos/schut___slika_za_internet2.png" alt=""></div></div>
    </div>"""
    groups = [
        group("pomicna-merila", "Pomična|merila", "Digitalna pomična merila TESA-CAL in TWIN-CAL z zaščito IP67 za zanesljivo merjenje tudi v zahtevnem delavniškem okolju.", grid([
            card("Pomično merilo TESA-CAL IP67", "Pomična merila", "assets/cats/Tesa_Cal.png", True, "#pomicna-merila"),
            card("Pomično merilo TWIN-CAL IP67", "Pomična merila", "assets/cats/Twin_Cal.png", True, "#pomicna-merila"),
            card("Pomična merila", "Pregled programa", "assets/cats/Nehrg.png", False, "#pomicna-merila"),
            text_card("Zaščita IP67", "IP67", "#pomicna-merila", "Odporno na prah in vodo"),
        ])),
        group("znamke", "Znamke", "Merilno orodje proizvajalcev, s katerimi sodelujemo že vrsto let.", brands),
    ]
    catpage("merilno-orodje", "Merilno|orodje", "Pomična merila in merilna oprema za natančno kontrolo v proizvodnji in merilnici.",
            "assets/cats/Nehrg.png", [("Pomična merila", "pomicna-merila"), ("Znamke", "znamke")], groups, [], "Merilno orodje")

def proizvajalci():
    wall = "".join(brand_tile(*b) for b in BRANDS)
    body = f"""<section class="phero" style="min-height:0">
  <div class="crumbs"><a href="index.html">Domov</a> / Proizvajalci</div>
  <div><h1>{mask('Proizvajalci')}</h1><p class="lead">Sodelujemo izključno z zaupanja vrednimi evropskimi in svetovnimi proizvajalci z dolgoletno tradicijo, ki so specializirani za posamezna strokovna področja.</p></div>
  <div></div>
</section>
<section style="padding:6px 0 clamp(110px,12vw,200px)"><div class="mwall" data-stagger>{wall}</div></section>
"""
    write("proizvajalci.html", head("Proizvajalci | ZIBTR PRO", "Proizvajalci rezilnega, vpenjalnega in merilnega orodja.") + nav("proizvajalci") + body + b2b() + foot())

def onas():
    areas = [("Rezilno orodje", "assets/cats/High_Feed_1.png"), ("Vpenjalno orodje", "assets/cats/New_Project_163_.png"),
             ("Avtomatizacija", "assets/logos/SMW_Autoblok_vpenjalni_steber.png"), ("Merilno orodje", "assets/cats/Tesa_Cal.png")]
    ar = "".join(f'<div class="area"><b>0{i+1}</b><img src="{img}" alt="" loading="lazy"><h3>{n}</h3></div>' for i, (n, img) in enumerate(areas))
    body = f"""<section class="phero">
  <div class="crumbs"><a href="index.html">Domov</a> / O nas</div>
  <div><h1>{mask('Od leta|1992.')}</h1><p class="lead">Svetovanje, tehnična podpora in optimizacija procesov na področju CNC obdelave kovin, vpenjalnih sistemov in meroslovja.</p></div>
  <div class="phero__img"><img src="assets/img/gallery3.png" alt="" data-par></div>
</section>
<section class="about-text">
  <h2 class="d3" data-split>{mask('ZIBTR PRO d.o.o.')}</h2>
  <div class="rv">
    <p class="lead">Podjetje ZIBTR d.o.o. je bilo ustanovljeno leta 1992. Ukvarjamo se s svetovanjem, tehnično podporo in optimizacijo procesov na področju CNC obdelave kovin, vpenjalnih sistemov, meroslovja ter reševanjem individualnih zahtev strank v avtomobilski industriji, orodjarstvu in strojegradnji.</p>
    <p class="lead">Sodelujemo izključno z zaupanja vrednimi evropskimi in svetovnimi proizvajalci z dolgoletno tradicijo, ki so specializirani za posamezna strokovna področja. Z visoko stopnjo strokovnosti in hitro odzivnostjo zagotavljamo kakovostne in učinkovite tehnične rešitve, prilagojene specifičnim potrebam naših kupcev.</p>
  </div>
</section>
<section class="areas" data-stagger>{ar}</section>
<section class="timeline" data-stagger>
  <div class="tl"><b>1992</b><p>Ustanovitev podjetja ZIBTR d.o.o.</p></div>
  <div class="tl"><b>2018</b><p>Ob selitvi na novo lokacijo se preimenujemo v ZIBTR PRO d.o.o. Novo poglavje v razvoju in še večja osredotočenost na kakovost, inovacije in dolgoročna partnerstva.</p></div>
  <div class="tl"><b class="red">Danes</b><p>Več kot {len(BRANDS)} proizvajalcev, spletna trgovina B2B in tehnična podpora od izbire orodja do optimizacije procesa.</p></div>
</section>
<section class="gallery" data-stagger>
  <figure><img src="assets/img/SIMTEK_TOOL.png" alt="" loading="lazy"></figure>
  <figure><img src="assets/img/gallery1.png" alt="" loading="lazy"></figure>
  <figure><img src="assets/img/gallery02.png" alt="" loading="lazy"></figure>
  <figure><img src="assets/img/gallery3.png" alt="" loading="lazy"></figure>
  <figure><img src="assets/cats/5.png" alt="" loading="lazy"></figure>
</section>
"""
    write("o-nas.html", head("O nas | ZIBTR PRO", "ZIBTR PRO d.o.o., od leta 1992.") + nav("o-nas") + body + b2b() + foot())

def kontakt():
    body = f"""<section class="contact">
  <div>
    <h1>{mask('Kontakt')}</h1>
    <p class="lead">Kontaktirajte nas in odgovorili vam bomo v najkrajšem možnem času.</p>
    <div class="cinfo">
      <div><span>Telefon</span><a href="tel:+38618962280">01 896 22 80</a></div>
      <div><span>E-pošta</span><a href="mailto:info@zibtrpro.si">info@zibtrpro.si</a></div>
      <div><span>Naslov</span><p>ZIBTR PRO d.o.o.<br>Zgornji Hotič 25b, 1270 Litija</p></div>
      <div><span>Spremljajte nas</span><a href="https://si.linkedin.com/in/zibtrpro">LinkedIn</a></div>
    </div>
  </div>
  <form class="form" novalidate>
    <h2>Kontaktni obrazec</h2>
    <div class="field"><label for="f-name">Ime in priimek *</label><input id="f-name" name="name" required autocomplete="name"><span class="msg">Vpišite ime in priimek.</span></div>
    <div class="field"><label for="f-co">Podjetje</label><input id="f-co" name="company" autocomplete="organization"></div>
    <div class="field"><label for="f-mail">Vaša e-pošta *</label><input id="f-mail" type="email" name="email" required autocomplete="email"><span class="msg">Vpišite veljaven e-poštni naslov.</span></div>
    <div class="field"><label for="f-tel">Vaša telefonska številka *</label><input id="f-tel" type="tel" name="phone" required autocomplete="tel"><span class="msg">Vpišite telefonsko številko.</span></div>
    <div class="field full"><label for="f-msg">Sporočilo</label><textarea id="f-msg" name="message" placeholder="Vsebina sporočila..."></textarea></div>
    <label class="check"><input type="checkbox" required><span>Strinjam se, da ZIBTR PRO d.o.o. hrani osebne podatke na obrazcu za notranjo uporabo in komunikacijo z mano za namene predložene zahteve. Izbris podatkov lahko zahtevam po e-pošti info@zibtrpro.si.</span></label>
    <div class="form__send"><small>Polja, označena z *, so obvezna.</small><button class="btn btn--red" type="submit">Pošlji sporočilo {ARR}</button></div>
    <div class="form__ok"><h3>Hvala, sporočilo je poslano.</h3><p class="lead">Odgovorili vam bomo v najkrajšem možnem času.</p></div>
  </form>
</section>
<div class="map"><iframe title="Zemljevid ZIBTR PRO" loading="lazy" src="https://maps.google.com/maps?q=Zgornji%20Hoti%C4%8D%2025b%2C%201270%20Litija&amp;z=14&amp;output=embed"></iframe></div>
"""
    write("kontakt.html", head("Kontakt | ZIBTR PRO", "Kontakt ZIBTR PRO d.o.o., Zgornji Hotič 25b, Litija.") + nav("kontakt") + body + b2b() + foot())

if __name__ == "__main__":
    home(); rezilno(); vpenjalni(); merilno(); proizvajalci(); onas(); kontakt()
