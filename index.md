---
layout: page
---

<style>
/* ── Reset & Base ─────────────────────────────────── */
.hp-wrap {
  max-width: 960px;
  margin: 0 auto;
  padding: 24px 20px 80px;
  font-family: "PT Serif", Georgia, serif;
  color: #1a1a1a;
}

/* ── Profile Block (top two-column) ──────────────── */
.profile-block {
  display: flex;
  gap: 40px;
  align-items: flex-start;
  margin-bottom: 48px;
  padding-bottom: 36px;
  border-bottom: 1px solid #e8e8e8;
}

.profile-photo-col {
  flex: 0 0 210px;
  text-align: center;
}

.profile-photo {
  width: 200px;
  height: 240px;
  object-fit: cover;
  border-radius: 6px;
  box-shadow: 0 4px 18px rgba(0,0,0,0.13);
  display: block;
  margin: 0 auto;
}

.profile-info-col {
  flex: 1;
  min-width: 0;
}

.profile-name-zh {
  font-size: 2rem;
  font-weight: bold;
  margin: 0 0 2px;
  color: #111;
  font-family: "PT Sans Narrow", "PingFang SC", "Heiti SC", sans-serif;
}

.profile-name-en {
  font-size: 1.15rem;
  color: #555;
  margin: 0 0 14px;
  font-family: "PT Sans Narrow", sans-serif;
}

.profile-title {
  font-size: 0.98rem;
  line-height: 1.7;
  color: #333;
  margin: 0 0 6px;
}

.profile-affil {
  font-size: 0.94rem;
  color: #555;
  line-height: 1.65;
  margin: 0 0 20px;
}

/* ── Social Links ─────────────────────────────────── */
.social-links {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
}

.social-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 5px 12px;
  border-radius: 4px;
  font-size: 0.82rem;
  font-weight: 600;
  text-decoration: none !important;
  transition: opacity 0.18s, transform 0.12s;
  white-space: nowrap;
  font-family: "PT Sans Narrow", sans-serif;
}

.social-btn:hover {
  opacity: 0.82;
  transform: translateY(-1px);
  text-decoration: none !important;
}

.social-btn.email    { background: #4a4a4a; color: #fff; }
.social-btn.github   { background: #24292e; color: #fff; }
.social-btn.scholar  { background: #4285f4; color: #fff; }
.social-btn.cv       { background: #0d9488; color: #fff; }
.social-btn.xhs      { background: #fe2c55; color: #fff; }
.social-btn.zhihu    { background: #0084ff; color: #fff; }
.social-btn.bili     { background: #fb7299; color: #fff; }

/* ── Section Headers ──────────────────────────────── */
.sec-title {
  font-size: 1.25rem;
  font-weight: bold;
  color: #111;
  border-bottom: 2px solid #0066cc;
  padding-bottom: 6px;
  margin: 36px 0 18px;
  font-family: "PT Sans Narrow", sans-serif;
  letter-spacing: 0.2px;
}

/* ── About ────────────────────────────────────────── */
.about-text {
  font-size: 0.97rem;
  line-height: 1.85;
  color: #333;
}

/* ── Scholar Widget ───────────────────────────────── */
.scholar-strip {
  display: flex;
  align-items: center;
  gap: 28px;
  flex-wrap: wrap;
  background: #f5f9ff;
  border: 1px solid #c7deff;
  border-radius: 8px;
  padding: 14px 20px;
  margin-top: 16px;
}
.scholar-stat { text-align: center; }
.scholar-stat-val  { font-size: 1.6rem; font-weight: 800; color: #0066cc; line-height: 1; }
.scholar-stat-lbl  { font-size: 0.75rem; color: #666; margin-top: 3px; font-weight: 600; }
.scholar-loading   { font-size: 0.88rem; color: #888; }

/* ── Education Timeline ───────────────────────────── */
.edu-list {
  display: grid;
  gap: 12px;
}

.edu-item {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  padding: 14px 16px;
  background: #fafafa;
  border-left: 3px solid #ccc;
  border-radius: 0 6px 6px 0;
}

.edu-item.current {
  border-left-color: #0066cc;
  background: #f5f9ff;
}

.edu-year {
  font-size: 0.8rem;
  color: #666;
  font-weight: 700;
  white-space: nowrap;
  min-width: 110px;
  padding-top: 2px;
  font-family: "PT Sans Narrow", sans-serif;
}

.edu-body {}

.edu-school {
  font-weight: bold;
  font-size: 0.97rem;
  color: #111;
  margin: 0 0 4px;
}

.edu-detail {
  font-size: 0.88rem;
  color: #555;
  line-height: 1.6;
  margin: 0;
}

/* ── Research Interests ───────────────────────────── */
.interest-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
}

.interest-card {
  padding: 14px 16px;
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.interest-card h4 {
  margin: 0 0 6px;
  font-size: 0.94rem;
  color: #0066cc;
  font-family: "PT Sans Narrow", sans-serif;
}

.interest-card p {
  margin: 0;
  font-size: 0.84rem;
  color: #555;
  line-height: 1.6;
}

/* ── News & Publications ──────────────────────────── */
.pub-list {
  display: grid;
  gap: 14px;
}

.pub-item {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  padding: 14px 16px;
  background: #fff;
  border: 1px solid #e8e8e8;
  border-radius: 6px;
}

.pub-badge {
  flex: 0 0 auto;
  font-size: 0.72rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 4px;
  white-space: nowrap;
  font-family: "PT Sans Narrow", sans-serif;
  letter-spacing: 0.3px;
  margin-top: 2px;
}

.pub-badge.conf  { background: #dbeafe; color: #1d4ed8; }
.pub-badge.jour  { background: #dcfce7; color: #15803d; }
.pub-badge.work  { background: #fef9c3; color: #92400e; }

.pub-body { flex: 1; min-width: 0; }

.pub-title {
  font-size: 0.95rem;
  font-weight: bold;
  color: #111;
  text-decoration: none;
  line-height: 1.5;
  display: block;
  margin-bottom: 4px;
}

.pub-title:hover { color: #0066cc; text-decoration: underline; }

.pub-authors {
  font-size: 0.84rem;
  color: #666;
  margin: 0;
  line-height: 1.5;
}

.pub-authors strong { color: #333; }

/* ── Map ──────────────────────────────────────────── */
.map-block {
  margin-top: 32px;
  text-align: center;
  background: #fff;
  border: 1px solid #e8e8e8;
  border-radius: 6px;
  padding: 18px;
}

.map-label {
  font-size: 0.88rem;
  color: #888;
  margin: 0 0 10px;
  font-weight: 600;
  font-family: "PT Sans Narrow", sans-serif;
  letter-spacing: 0.4px;
  text-transform: uppercase;
}

/* ── Responsive ───────────────────────────────────── */
@media (max-width: 660px) {
  .profile-block {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .profile-info-col { text-align: left; }
  .social-links { justify-content: center; }
  .edu-item { flex-direction: column; gap: 4px; }
  .edu-year { min-width: unset; }
}
</style>

<div class="hp-wrap">

  <!-- ══ Profile Block ══════════════════════════════ -->
  <div class="profile-block">
    <div class="profile-photo-col">
      <img class="profile-photo"
           src="https://picsum.photos/seed/nansha-scenery/400/480"
           alt="Profile placeholder — replace with your photo">
    </div>
    <div class="profile-info-col">
      <h1 class="profile-name-zh">何建翔</h1>
      <p class="profile-name-en">Jianxiang He &nbsp;/&nbsp; Jackson</p>
      <p class="profile-title">
        Incoming PhD Student · <strong>MBZUAI</strong><br>
        Advisor: Prof. <strong>Xiaojun Chang</strong> (常晓军)
      </p>
      <p class="profile-affil">
        MPhil in Artificial Intelligence · HKUST(GZ)<br>
        AI+ Lab &amp; NLP Group
      </p>

      <div class="social-links">
        <a class="social-btn email"   href="mailto:jhe307@connect.hkust-gz.edu.cn"><i class="fa fa-envelope"></i> Email</a>
        <a class="social-btn github"  href="https://github.com/Jacksonha7"          target="_blank" rel="noopener"><i class="fa-brands fa-github"></i> GitHub</a>
        <a class="social-btn scholar" href="https://scholar.google.com/citations?user=6ZJXY_EAAAAJ&hl=en" target="_blank" rel="noopener"><i class="fa-solid fa-graduation-cap"></i> Scholar</a>
        <a class="social-btn cv"      href="https://Jacksonha7.com/file/CV-Hejianxiang.pdf" target="_blank" rel="noopener"><i class="fa-solid fa-file-pdf"></i> CV</a>
        <a class="social-btn xhs"     href="{{ site.owner.xiaohongshu }}"           target="_blank" rel="noopener"><i class="fa-solid fa-book-open"></i> 小红书</a>
        <a class="social-btn zhihu"   href="{{ site.owner.zhihu }}"                 target="_blank" rel="noopener"><i class="fa-solid fa-circle-question"></i> 知乎</a>
        <a class="social-btn bili"    href="{{ site.owner.bilibili }}"              target="_blank" rel="noopener"><i class="fa-solid fa-play-circle"></i> Bilibili</a>
      </div>
    </div>
  </div>

  <!-- ══ About ══════════════════════════════════════ -->
  <div class="sec-title">About</div>
  <p class="about-text">
    I am a Master of Philosophy student at the Hong Kong University of Science and Technology (Guangzhou),
    advised by Professor <strong>Hui Xiong</strong> and Assistant Professor <strong>Xuming Hu</strong>.
    My current research focuses on long-video understanding, key-frame selection, and multimodal fusion.
  </p>
  <p class="about-text">
    I will join <strong>MBZUAI</strong> as a PhD student in Fall 2026, under the supervision of
    Prof. <strong>Xiaojun Chang</strong>, where I plan to work on Vision-Language-Action (VLA) models,
    embodied AI, and world models for robotics and embodied agents.
  </p>

  <!-- Google Scholar Stats -->
  <div class="scholar-strip">
    <span style="font-size:1.6rem;">📚</span>
    <div id="scholar-stats">
      <span class="scholar-loading">Loading citation stats…</span>
    </div>
    <a class="social-btn scholar" href="https://scholar.google.com/citations?user=6ZJXY_EAAAAJ&hl=en" target="_blank" rel="noopener" style="margin-left:auto;">
      <i class="fa-solid fa-graduation-cap"></i> Google Scholar ↗
    </a>
  </div>

  <!-- ══ Education ════════════════════════════════== -->
  <div class="sec-title">Education</div>
  <div class="edu-list">
    <div class="edu-item">
      <div class="edu-year">Sep 2020 – Jun 2024</div>
      <div class="edu-body">
        <p class="edu-school">Shandong University &nbsp;·&nbsp; 山东大学</p>
        <p class="edu-detail">B.E. in Automation &nbsp;·&nbsp; Core courses in NLP, image processing, and machine learning.</p>
      </div>
    </div>
    <div class="edu-item">
      <div class="edu-year">Sep 2024 – Jun 2026</div>
      <div class="edu-body">
        <p class="edu-school">HKUST(GZ) &nbsp;·&nbsp; 香港科技大学（广州）</p>
        <p class="edu-detail">MPhil in AI &nbsp;·&nbsp; Advisors: Prof. Hui Xiong &amp; Prof. Xuming Hu &nbsp;·&nbsp; Multimodal LLMs, long video understanding.</p>
      </div>
    </div>
    <div class="edu-item current">
      <div class="edu-year">Fall 2026 – Present</div>
      <div class="edu-body">
        <p class="edu-school">MBZUAI &nbsp;·&nbsp; 穆罕默德·本·扎耶德人工智能大学</p>
        <p class="edu-detail">PhD in AI &nbsp;·&nbsp; Advisor: Prof. Xiaojun Chang (常晓军) &nbsp;·&nbsp; VLA, Embodied AI, World Models.</p>
      </div>
    </div>
  </div>

  <!-- ══ Research Interests ═══════════════════════== -->
  <div class="sec-title">Research Interests</div>
  <div class="interest-grid">
    <div class="interest-card">
      <h4><i class="fa-solid fa-robot"></i> Vision-Language-Action</h4>
      <p>Unified models grounding language in visual perception and physical actions for robot learning.</p>
    </div>
    <div class="interest-card">
      <h4><i class="fa-solid fa-cube"></i> Embodied AI</h4>
      <p>Enabling agents to perceive, reason, and act in physical environments through sensorimotor integration.</p>
    </div>
    <div class="interest-card">
      <h4><i class="fa-solid fa-globe"></i> World Models</h4>
      <p>Internal representations of the world that allow agents to predict, plan, and generalize.</p>
    </div>
    <div class="interest-card">
      <h4><i class="fa-solid fa-brain"></i> Multimodal LLM</h4>
      <p>Long-video understanding and efficient key-frame selection via multimodal reasoning.</p>
    </div>
  </div>

  <!-- ══ Selected Publications ════════════════════== -->
  <div class="sec-title">Selected Publications</div>
  <div class="pub-list">

    <div class="pub-item">
      <span class="pub-badge conf">CVPR 2026</span>
      <div class="pub-body">
        <a class="pub-title" href="https://arxiv.org/abs/2508.06869" target="_blank" rel="noopener">
          VSI: Visual Subtitle Integration for Keyframe Selection to Enhance Long Video Understanding
        </a>
        <p class="pub-authors"><strong>Jianxiang He</strong>, Shaoguang Wang, Weiyu Guo, et al.</p>
      </div>
    </div>

    <div class="pub-item">
      <span class="pub-badge conf">NeurIPS 2025</span>
      <div class="pub-body">
        <a class="pub-title" href="https://arxiv.org/abs/2503.13139" target="_blank" rel="noopener">
          Logic-in-Frames: Dynamic Keyframe Search via Visual Semantic-Logical Verification for Long Video Understanding
        </a>
        <p class="pub-authors">Weiyu Guo, Ziyang Chen, Shaoguang Wang, <strong>Jianxiang He</strong>, et al.</p>
      </div>
    </div>

    <div class="pub-item">
      <span class="pub-badge conf">ACL 2025</span>
      <div class="pub-body">
        <a class="pub-title" href="https://arxiv.org/abs/2412.11936" target="_blank" rel="noopener">
          A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method &amp; Challenges
        </a>
        <p class="pub-authors">Yibo Yan, Jiamin Su, <strong>Jianxiang He</strong>, et al.</p>
      </div>
    </div>

    <div class="pub-item">
      <span class="pub-badge conf">IEEE ROBIO 2022</span>
      <div class="pub-body">
        <a class="pub-title" href="https://ieeexplore.ieee.org/document/10012028" target="_blank" rel="noopener">
          The development of spiking neural network: A review
        </a>
        <p class="pub-authors"><strong>Jianxiang He</strong>, Yanzi Li, Yingtian Liu, et al.</p>
      </div>
    </div>

  </div>

  <!-- ══ Visitor Map ═══════════════════════════════= -->
  <div class="map-block">
    <p class="map-label">Visitor Locations</p>
    <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=Mf2edNvrXMP-LKR3oRo6m-y46Llurx-ccm_QSyDjnlE"></script>
  </div>

</div>

<script>
(function () {
  var statsEl = document.getElementById("scholar-stats");
  fetch("/assets/data/scholar_stats.json?_=" + Date.now())
    .then(function (r) { return r.json(); })
    .then(function (d) {
      statsEl.innerHTML = [
        stat(d.citations, "Citations"),
        stat(d.h_index, "h-index"),
        stat(d.i10_index, "i10-index"),
      ].join("") + '<div class="scholar-stat" style="font-size:0.72rem;color:#94a3b8;align-self:flex-end">Updated ' + d.updated_at + '</div>';
    })
    .catch(function () {
      statsEl.innerHTML = '<span class="scholar-loading"><a href="https://scholar.google.com/citations?user=6ZJXY_EAAAAJ" target="_blank">View on Google Scholar ↗</a></span>';
    });

  function stat(v, l) {
    return '<div class="scholar-stat"><div class="scholar-stat-val">' + v + '</div><div class="scholar-stat-lbl">' + l + '</div></div>';
  }
})();
</script>
