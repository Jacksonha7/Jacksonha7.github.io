---
layout: home
---

<style>
/* ══════════════════════════════════════════════════
   HERO SECTION
══════════════════════════════════════════════════ */
.hero {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

/* Background image layer */
.hero-bg {
  position: absolute;
  inset: 0;
  background:
    url('/youhua/background.png')
    center / cover no-repeat;
  transform: scale(1.04);
  transition: transform 8s ease;
}
.hero-bg.loaded { transform: scale(1); }

/* Dark gradient overlay */
.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    160deg,
    rgba(4, 8, 20, 0.72) 0%,
    rgba(4, 8, 20, 0.62) 45%,
    rgba(4, 8, 20, 0.80) 100%
  );
}

/* Centered content */
.hero-cnt {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 100px 24px 80px;
  max-width: 720px;
  animation: heroFadeIn 1.1s ease both;
}

@keyframes heroFadeIn {
  from { opacity: 0; transform: translateY(28px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Avatar */
.hero-avatar {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid rgba(255,255,255,0.22);
  box-shadow: 0 8px 40px rgba(0,0,0,0.4);
  margin-bottom: 22px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

/* Name */
.hero-name {
  font-size: clamp(1.9rem, 4vw, 2.8rem);
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.3px;
  line-height: 1.2;
  margin-bottom: 10px;
  text-shadow: 0 2px 16px rgba(0,0,0,0.3);
}

/* Subtitle */
.hero-sub {
  font-size: clamp(0.9rem, 1.8vw, 1.05rem);
  color: rgba(255,255,255,0.78);
  line-height: 1.75;
  margin-bottom: 22px;
  font-weight: 400;
}
.hero-sub strong { color: rgba(255,255,255,0.95); font-weight: 600; }

/* Research badges */
.hero-badges {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
  margin-bottom: 28px;
}
.hero-badge {
  padding: 5px 13px;
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(255,255,255,0.20);
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 600;
  color: rgba(255,255,255,0.85);
  letter-spacing: 0.3px;
  backdrop-filter: blur(6px);
}

/* Social buttons */
.hero-social {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
}
.hero-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 0.80rem;
  font-weight: 700;
  text-decoration: none !important;
  transition: transform 0.18s, opacity 0.18s, box-shadow 0.18s;
  letter-spacing: 0.3px;
  white-space: nowrap;
  backdrop-filter: blur(8px);
}
.hero-btn:hover {
  transform: translateY(-2px);
  opacity: 0.9;
  box-shadow: 0 6px 20px rgba(0,0,0,0.25);
  text-decoration: none !important;
}
.hero-btn.email   { background: rgba(80,80,90,0.75);  color: #fff; border: 1px solid rgba(255,255,255,0.15); }
.hero-btn.github  { background: rgba(30,30,35,0.80);  color: #fff; border: 1px solid rgba(255,255,255,0.15); }
.hero-btn.scholar { background: rgba(30,80,200,0.75); color: #fff; border: 1px solid rgba(100,160,255,0.25); }
.hero-btn.cv      { background: rgba(10,130,120,0.75);color: #fff; border: 1px solid rgba(80,220,200,0.2); }
.hero-btn.xhs     { background: rgba(200,30,60,0.75); color: #fff; border: 1px solid rgba(255,80,100,0.2); }
.hero-btn.zhihu   { background: rgba(0,100,220,0.75); color: #fff; border: 1px solid rgba(80,180,255,0.2); }
.hero-btn.bili    { background: rgba(220,60,130,0.70);color: #fff; border: 1px solid rgba(255,120,180,0.2); }

/* Scroll hint */
.hero-scroll {
  position: absolute;
  bottom: 28px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 2;
  color: rgba(255,255,255,0.45);
  font-size: 1.1rem;
  animation: bounceDown 2s ease-in-out infinite;
  cursor: pointer;
}
@keyframes bounceDown {
  0%,100% { transform: translateX(-50%) translateY(0); }
  50%     { transform: translateX(-50%) translateY(8px); }
}

/* ══════════════════════════════════════════════════
   CONTENT SECTIONS
══════════════════════════════════════════════════ */
.hp {
  max-width: 860px;
  margin: 0 auto;
  padding: 0 28px 80px;
}

/* Section title */
.sec {
  font-size: 1.2rem;
  font-weight: 700;
  color: #111;
  margin: 56px 0 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #e8e8e8;
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: "Inter", "PT Sans Narrow", sans-serif;
  letter-spacing: 0.2px;
}
.sec::before {
  content: '';
  display: inline-block;
  width: 4px; height: 18px;
  background: linear-gradient(180deg, #0055cc, #7c3aed);
  border-radius: 3px;
  flex-shrink: 0;
}

/* Override global p+p rule from main.css (margin-top:-1.5em causes overlap) */
.hp p { text-indent: 0 !important; }
.hp p + p { margin-top: 0 !important; }

/* About */
.about-p {
  font-size: 0.97rem;
  line-height: 1.88;
  color: #333;
  margin-bottom: 14px;
}

/* Scholar strip */
.scholar-strip {
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
  background: #f5f9ff;
  border: 1px solid #c7deff;
  border-radius: 10px;
  padding: 16px 22px;
  margin-top: 20px;
}
.sc-stat { text-align: center; }
.sc-val  { font-size: 1.65rem; font-weight: 800; color: #0055cc; line-height: 1; }
.sc-lbl  { font-size: 0.74rem; color: #667; margin-top: 3px; font-weight: 600; letter-spacing: 0.3px; text-transform: uppercase; }
.sc-loading { font-size: 0.88rem; color: #888; }
.sc-link {
  margin-left: auto;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: #0055cc;
  color: #fff;
  border-radius: 7px;
  font-size: 0.82rem;
  font-weight: 700;
  text-decoration: none;
  transition: opacity 0.2s, transform 0.2s;
  white-space: nowrap;
}
.sc-link:hover { opacity: 0.85; transform: translateY(-1px); color: #fff; text-decoration: none; }

/* Education */
.edu-list { display: grid; gap: 12px; }
.edu-item {
  display: flex;
  gap: 18px;
  align-items: flex-start;
  padding: 16px 18px;
  background: #fafafa;
  border-left: 3px solid #ddd;
  border-radius: 0 8px 8px 0;
  transition: border-color 0.2s, background 0.2s;
}
.edu-item.current { border-left-color: #0055cc; background: #f5f9ff; }
.edu-item:hover   { border-left-color: #0055cc; background: #f8faff; }
.edu-year {
  font-size: 0.78rem;
  font-weight: 700;
  color: #888;
  white-space: nowrap;
  min-width: 118px;
  padding-top: 3px;
  letter-spacing: 0.2px;
}
.edu-body {
  flex: 1;
  min-width: 0;
}
/* Override main.css p+p rule (margin-top:-1.5em causes overlap) */
.edu-body p { margin: 0; text-indent: 0 !important; }
.edu-body p + p { margin-top: 0 !important; }
.edu-school {
  font-weight: 700;
  font-size: 0.96rem;
  color: #111;
  margin-bottom: 5px;
}
.edu-detail {
  font-size: 0.86rem;
  color: #666;
  line-height: 1.65;
}

/* Research grid */
.research-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
  gap: 14px;
}
.research-card {
  padding: 16px 18px;
  background: #fff;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.04);
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
}
.research-card:hover {
  border-color: #0055cc;
  box-shadow: 0 6px 22px rgba(0,85,204,0.1);
  transform: translateY(-2px);
}
.research-card h4 {
  font-size: 0.88rem;
  font-weight: 700;
  color: #0055cc;
  margin-bottom: 6px;
  font-family: "Inter", sans-serif;
}
.research-card p {
  font-size: 0.82rem;
  color: #666;
  line-height: 1.6;
}

/* Publications */
.pub-list { display: grid; gap: 14px; }
.pub-item {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  padding: 16px 18px;
  background: #fff;
  border: 1px solid #ebebeb;
  border-radius: 8px;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.pub-item:hover {
  border-color: #0055cc;
  box-shadow: 0 4px 18px rgba(0,85,204,0.08);
}
.pub-badge {
  flex-shrink: 0;
  font-size: 0.7rem;
  font-weight: 800;
  padding: 3px 9px;
  border-radius: 5px;
  white-space: nowrap;
  margin-top: 2px;
  letter-spacing: 0.3px;
  font-family: "Inter", sans-serif;
}
.pub-badge.conf { background: #dbeafe; color: #1d4ed8; }
.pub-badge.work { background: #fef3c7; color: #92400e; }
.pub-title {
  font-size: 0.94rem;
  font-weight: 700;
  color: #111;
  text-decoration: none;
  line-height: 1.5;
  display: block;
  margin-bottom: 5px;
  transition: color 0.2s;
}
.pub-title:hover { color: #0055cc; }
.pub-authors {
  font-size: 0.82rem;
  color: #777;
  line-height: 1.5;
}
.pub-authors strong { color: #333; }

/* Map */
.map-block {
  margin-top: 40px;
  text-align: center;
  background: #fafafa;
  border: 1px solid #ebebeb;
  border-radius: 10px;
  padding: 22px;
}
.map-lbl {
  font-size: 0.78rem;
  font-weight: 700;
  color: #bbb;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  margin-bottom: 12px;
}

/* ══ Responsive ══════════════════════════════════ */
@media (max-width: 600px) {
  .hero-cnt { padding: 90px 20px 70px; }
  .hero-avatar { width: 105px; height: 105px; }
  .edu-item { flex-direction: column; gap: 4px; }
  .edu-year { min-width: unset; }
  .research-grid { grid-template-columns: 1fr 1fr; }
  .hp { padding: 0 18px 60px; }
}
</style>

<!-- ══════════════════════════════════════════════
     HERO
══════════════════════════════════════════════ -->
<section class="hero" id="top">
  <div class="hero-bg" id="hero-bg"></div>
  <div class="hero-overlay"></div>

  <div class="hero-cnt">
    <img class="hero-avatar"
         src="/youhua/me.jpg"
         alt="Jianxiang He">

    <h1 class="hero-name">何建翔 &nbsp;·&nbsp; Jianxiang He</h1>

    <p class="hero-sub">
      Incoming PhD Student &nbsp;·&nbsp; <strong>MBZUAI</strong><br>
      Advisor: Prof. <strong>Xiaojun Chang</strong> (常晓军)<br>
      MPhil in AI · HKUST(GZ)
    </p>

    <div class="hero-badges">
      <span class="hero-badge">Vision-Language-Action</span>
      <span class="hero-badge">Embodied AI</span>
      <span class="hero-badge">World Models</span>
      <span class="hero-badge">Multimodal LLM</span>
    </div>

    <div class="hero-social">
      <a class="hero-btn email"   href="mailto:jhe307@connect.hkust-gz.edu.cn"><i class="fa fa-envelope"></i>Email</a>
      <a class="hero-btn github"  href="https://github.com/Jacksonha7" target="_blank" rel="noopener"><i class="fa-brands fa-github"></i>GitHub</a>
      <a class="hero-btn scholar" href="https://scholar.google.com/citations?user=6ZJXY_EAAAAJ&hl=en" target="_blank" rel="noopener"><i class="fa-solid fa-graduation-cap"></i>Scholar</a>
      <a class="hero-btn cv"      href="https://Jacksonha7.com/file/CV-Hejianxiang.pdf" target="_blank" rel="noopener"><i class="fa-solid fa-file-pdf"></i>CV</a>
      <a class="hero-btn xhs"     href="{{ site.owner.xiaohongshu }}" target="_blank" rel="noopener"><i class="fa-solid fa-book-open"></i>小红书</a>
      <a class="hero-btn zhihu"   href="{{ site.owner.zhihu }}"       target="_blank" rel="noopener"><i class="fa-solid fa-circle-question"></i>知乎</a>
      <a class="hero-btn bili"    href="{{ site.owner.bilibili }}"    target="_blank" rel="noopener"><i class="fa-solid fa-play-circle"></i>Bilibili</a>
    </div>
  </div>

  <div class="hero-scroll" onclick="document.getElementById('about').scrollIntoView({behavior:'smooth'})">
    <i class="fa-solid fa-angle-down"></i>
  </div>
</section>

<!-- ══════════════════════════════════════════════
     CONTENT
══════════════════════════════════════════════ -->
<div class="hp" id="about">

  <!-- About -->
  <h2 class="sec reveal">About</h2>
  <div class="reveal">
    <p class="about-p">
      I am a Master of Philosophy student at the Hong Kong University of Science and Technology (Guangzhou),
      advised by Professor <strong>Hui Xiong</strong> and Assistant Professor <strong>Xuming Hu</strong>.
      My current research focuses on long-video understanding, key-frame selection, and multimodal fusion.
    </p>
    <p class="about-p">
      I will join <strong>MBZUAI</strong> as a PhD student in Fall 2026, under the supervision of
      Prof. <strong>Xiaojun Chang</strong>, where I plan to work on
      Vision-Language-Action (VLA) models, embodied AI, and world models.
    </p>
  </div>

  <!-- Scholar Widget -->
  <div class="scholar-strip reveal">
    <span style="font-size:1.5rem;flex-shrink:0;">📚</span>
    <div id="scholar-stats"><span class="sc-loading">Loading citation stats…</span></div>
    <a class="sc-link" href="https://scholar.google.com/citations?user=6ZJXY_EAAAAJ&hl=en" target="_blank" rel="noopener">
      <i class="fa-solid fa-graduation-cap"></i> Google Scholar ↗
    </a>
  </div>

  <!-- Education -->
  <h2 class="sec reveal">Education</h2>
  <div class="edu-list">
    <div class="edu-item reveal">
      <div class="edu-year">Sep 2020 – Jun 2024</div>
      <div class="edu-body">
        <p class="edu-school">Shandong University &nbsp;·&nbsp; 山东大学</p>
        <p class="edu-detail">B.E. in Automation &nbsp;·&nbsp; NLP, image processing, machine learning</p>
      </div>
    </div>
    <div class="edu-item reveal">
      <div class="edu-year">Sep 2024 – Jun 2026</div>
      <div class="edu-body">
        <p class="edu-school">HKUST(GZ) &nbsp;·&nbsp; 香港科技大学（广州）</p>
        <p class="edu-detail">MPhil in AI &nbsp;·&nbsp; Advisors: Prof. Hui Xiong &amp; Prof. Xuming Hu &nbsp;·&nbsp; Multimodal LLMs, long video</p>
      </div>
    </div>
    <div class="edu-item current reveal">
      <div class="edu-year">Fall 2026 – Present</div>
      <div class="edu-body">
        <p class="edu-school">MBZUAI &nbsp;·&nbsp; 穆罕默德·本·扎耶德人工智能大学</p>
        <p class="edu-detail">PhD in AI &nbsp;·&nbsp; Advisor: Prof. Xiaojun Chang &nbsp;·&nbsp; VLA · Embodied AI · World Models</p>
      </div>
    </div>
  </div>

  <!-- Research Interests -->
  <h2 class="sec reveal">Research Interests</h2>
  <div class="research-grid">
    <div class="research-card reveal">
      <h4><i class="fa-solid fa-robot"></i>&nbsp; VLA Models</h4>
      <p>Unified models grounding language in visual perception and physical actions for robot learning.</p>
    </div>
    <div class="research-card reveal">
      <h4><i class="fa-solid fa-cube"></i>&nbsp; Embodied AI</h4>
      <p>Enabling agents to perceive, reason, and act in physical environments through sensorimotor integration.</p>
    </div>
    <div class="research-card reveal">
      <h4><i class="fa-solid fa-globe"></i>&nbsp; World Models</h4>
      <p>Internal representations allowing agents to predict, plan, and generalize across scenarios.</p>
    </div>
    <div class="research-card reveal">
      <h4><i class="fa-solid fa-brain"></i>&nbsp; Multimodal LLM</h4>
      <p>Long-video understanding and efficient key-frame selection via multimodal reasoning.</p>
    </div>
  </div>

  <!-- Publications -->
  <h2 class="sec reveal">Selected Publications</h2>
  <div class="pub-list">

    <div class="pub-item reveal">
      <span class="pub-badge conf">CVPR 2026</span>
      <div>
        <a class="pub-title" href="https://arxiv.org/abs/2508.06869" target="_blank" rel="noopener">
          VSI: Visual Subtitle Integration for Keyframe Selection to Enhance Long Video Understanding
        </a>
        <p class="pub-authors"><strong>Jianxiang He</strong>, Shaoguang Wang, Weiyu Guo, et al.</p>
      </div>
    </div>

    <div class="pub-item reveal">
      <span class="pub-badge conf">NeurIPS 2025</span>
      <div>
        <a class="pub-title" href="https://arxiv.org/abs/2503.13139" target="_blank" rel="noopener">
          Logic-in-Frames: Dynamic Keyframe Search via Visual Semantic-Logical Verification for Long Video Understanding
        </a>
        <p class="pub-authors">Weiyu Guo, Ziyang Chen, Shaoguang Wang, <strong>Jianxiang He</strong>, et al.</p>
      </div>
    </div>

    <div class="pub-item reveal">
      <span class="pub-badge conf">ACL 2025</span>
      <div>
        <a class="pub-title" href="https://arxiv.org/abs/2412.11936" target="_blank" rel="noopener">
          A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method &amp; Challenges
        </a>
        <p class="pub-authors">Yibo Yan, Jiamin Su, <strong>Jianxiang He</strong>, et al.</p>
      </div>
    </div>

    <div class="pub-item reveal">
      <span class="pub-badge conf">IEEE ROBIO 2022</span>
      <div>
        <a class="pub-title" href="https://ieeexplore.ieee.org/document/10012028" target="_blank" rel="noopener">
          The Development of Spiking Neural Network: A Review
        </a>
        <p class="pub-authors"><strong>Jianxiang He</strong>, Yanzi Li, Yingtian Liu, et al.</p>
      </div>
    </div>

  </div>

  <!-- Visitor Map -->
  <div class="map-block reveal">
    <p class="map-lbl">Visitor Locations</p>
    <script type="text/javascript" id="clstr_globe"
      src="//clustrmaps.com/globe.js?d=Mf2edNvrXMP-LKR3oRo6m-y46Llurx-ccm_QSyDjnlE"></script>
  </div>

</div>

<script>
/* Scholar stats */
(function () {
  var el = document.getElementById('scholar-stats');
  fetch('/assets/data/scholar_stats.json?_=' + Date.now())
    .then(function (r) { return r.json(); })
    .then(function (d) {
      el.innerHTML =
        stat(d.citations, 'Citations') +
        stat(d.h_index, 'h-index') +
        stat(d.i10_index, 'i10-index') +
        '<div class="sc-stat" style="font-size:0.7rem;color:#aaa;align-self:flex-end">Updated ' + d.updated_at + '</div>';
    })
    .catch(function () {
      el.innerHTML = '<span class="sc-loading"><a href="https://scholar.google.com/citations?user=6ZJXY_EAAAAJ" target="_blank" style="color:#0055cc">View on Google Scholar ↗</a></span>';
    });
  function stat(v, l) {
    return '<div class="sc-stat"><div class="sc-val">' + v + '</div><div class="sc-lbl">' + l + '</div></div>';
  }
})();

/* Hero bg slow zoom after load */
window.addEventListener('load', function () {
  var bg = document.getElementById('hero-bg');
  if (bg) bg.classList.add('loaded');
});
</script>
