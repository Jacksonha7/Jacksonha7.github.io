---
layout: page
---

<style>
:root {
  --primary: #2563eb;
  --secondary: #7c3aed;
  --text-main: #0f172a;
  --text-muted: #475569;
  --card-bg: rgba(255, 255, 255, 0.92);
  --border-soft: rgba(37, 99, 235, 0.14);
}

.page-container {
  max-width: 980px;
  margin: 0 auto;
  padding: 0 20px 60px;
  color: var(--text-main);
  font-family: "Inter", "Segoe UI", "Helvetica Neue", sans-serif;
}

.hero {
  margin-top: 12px;
  padding: 34px;
  border-radius: 22px;
  background:
    radial-gradient(1200px 300px at -10% 0%, rgba(37, 99, 235, 0.14), transparent 70%),
    radial-gradient(1000px 400px at 110% 100%, rgba(124, 58, 237, 0.14), transparent 72%),
    #f8fbff;
  border: 1px solid var(--border-soft);
  box-shadow: 0 16px 35px rgba(15, 23, 42, 0.08);
}

.hero-headline {
  font-size: clamp(1.8rem, 2.8vw, 2.5rem);
  margin: 0;
  letter-spacing: 0.2px;
}

.hero-subline {
  margin: 12px 0 0;
  color: var(--text-muted);
  font-size: 1.05rem;
  line-height: 1.75;
}

.badge-row {
  margin-top: 18px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.badge {
  background: white;
  color: #1e3a8a;
  border: 1px solid #bfdbfe;
  border-radius: 999px;
  padding: 6px 12px;
  font-size: 0.84rem;
  font-weight: 600;
}

.section-title {
  margin: 42px 0 18px;
  font-size: 1.5rem;
  position: relative;
  padding-left: 14px;
}

.section-title::before {
  content: "";
  position: absolute;
  left: 0;
  top: 5px;
  bottom: 5px;
  width: 4px;
  border-radius: 99px;
  background: linear-gradient(180deg, var(--primary), var(--secondary));
}

.grid-2 {
  display: grid;
  gap: 18px;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

.card {
  background: var(--card-bg);
  border: 1px solid rgba(15, 23, 42, 0.08);
  border-radius: 16px;
  padding: 20px 22px;
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
  backdrop-filter: blur(4px);
}

.card h3 {
  margin: 0 0 10px;
  font-size: 1.18rem;
}

.card p {
  margin: 0;
  line-height: 1.7;
  color: var(--text-muted);
}

.timeline {
  display: grid;
  gap: 14px;
}

.timeline-item {
  position: relative;
  padding: 18px 20px 16px 22px;
  border-left: 3px solid #c7d2fe;
  border-radius: 0 14px 14px 0;
  background: #fff;
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05);
}

.timeline-item.current {
  border-left-color: var(--primary);
}

.timeline-time {
  font-size: 0.84rem;
  color: #475569;
  font-weight: 700;
  margin-bottom: 8px;
}

.timeline-title {
  margin: 0;
  font-size: 1.08rem;
}

.timeline-meta {
  margin: 6px 0 0;
  color: var(--text-muted);
  line-height: 1.6;
}

.news-list {
  display: grid;
  gap: 12px;
}

.news-item {
  background: #fff;
  border: 1px solid rgba(148, 163, 184, 0.25);
  border-radius: 12px;
  padding: 14px 16px;
}

.news-item .tag {
  display: inline-block;
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.3px;
  color: #0c4a6e;
  background: #e0f2fe;
  padding: 4px 8px;
  border-radius: 8px;
  margin-bottom: 8px;
}

.news-title {
  display: block;
  font-weight: 700;
  line-height: 1.5;
  margin-bottom: 6px;
}

.news-authors {
  margin: 0;
  color: var(--text-muted);
  font-size: 0.94rem;
}

/* Scholar Stats Widget */
.scholar-widget {
  margin-top: 18px;
  border-radius: 16px;
  border: 1px solid rgba(37, 99, 235, 0.18);
  padding: 20px 24px;
  background: linear-gradient(135deg, #f0f7ff, #f8f5ff);
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
}

.scholar-widget-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.scholar-stats {
  display: flex;
  gap: 28px;
  flex-wrap: wrap;
}

.scholar-stat {
  text-align: center;
}

.scholar-stat-value {
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--primary);
  line-height: 1;
}

.scholar-stat-label {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 4px;
  font-weight: 600;
  letter-spacing: 0.3px;
}

.scholar-link {
  margin-left: auto;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--primary);
  color: white;
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 10px;
  font-size: 0.88rem;
  font-weight: 600;
  transition: opacity 0.2s;
}

.scholar-link:hover {
  opacity: 0.85;
  color: white;
  text-decoration: none;
}

.scholar-loading {
  color: var(--text-muted);
  font-size: 0.9rem;
}

.map-container {
  margin-top: 26px;
  border-radius: 16px;
  border: 1px solid rgba(15, 23, 42, 0.08);
  padding: 18px;
  text-align: center;
  background: #fff;
}

.map-title {
  margin: 0 0 12px;
  font-weight: 700;
  font-size: 1rem;
  color: #334155;
  letter-spacing: 0.3px;
}

.contact-grid {
  display: grid;
  gap: 10px;
  margin-top: 16px;
}

.contact-line {
  color: #334155;
  margin: 0;
}

@media (max-width: 640px) {
  .hero {
    padding: 24px;
  }

  .card,
  .timeline-item {
    padding: 16px;
  }

  .scholar-widget {
    flex-direction: column;
    align-items: flex-start;
  }

  .scholar-link {
    margin-left: 0;
  }
}
</style>

<div class="page-container">
  <section class="hero">
    <h1 class="hero-headline">Jianxiang He / 何建翔</h1>
    <p class="hero-subline">
      Incoming PhD student at <strong>MBZUAI</strong>, advised by Prof. <strong>Xiaojun Chang</strong> (常晓军).
      MPhil in Artificial Intelligence at HKUST(GZ). Research focuses on Vision-Language-Action models,
      embodied AI, world models, and multimodal large language models.
    </p>
    <div class="badge-row">
      <span class="badge">Vision-Language-Action</span>
      <span class="badge">Embodied AI</span>
      <span class="badge">World Models</span>
      <span class="badge">Multimodal LLM</span>
      <span class="badge">Video Understanding</span>
    </div>
    <div class="contact-grid">
      <p class="contact-line"><strong>Email:</strong> jhe307@connect.hkust-gz.edu.cn</p>
      <p class="contact-line"><strong>Affiliation:</strong> AI+ Lab / HKUST-GZ NLP Group → MBZUAI (Fall 2026)</p>
    </div>
  </section>

  <h2 class="section-title">About</h2>
  <div class="card">
    <p>
      I am a Master of Philosophy student at the Hong Kong University of Science and Technology (Guangzhou),
      advised by Professor <strong>Hui Xiong</strong> and Assistant Professor <strong>Xuming Hu</strong>.
      My current research focuses on long-video understanding, key-frame selection, and multimodal fusion.
      I will join <strong>MBZUAI</strong> as a PhD student in Fall 2026, under the supervision of
      Prof. <strong>Xiaojun Chang</strong>, where I plan to work on Vision-Language-Action (VLA) models,
      embodied AI, and world models.
    </p>
  </div>

  <!-- Google Scholar Citation Stats -->
  <div class="scholar-widget">
    <span class="scholar-widget-icon">📚</span>
    <div class="scholar-stats" id="scholar-stats">
      <span class="scholar-loading">Loading citation stats…</span>
    </div>
    <a class="scholar-link" href="https://scholar.google.com/citations?user=6ZJXY_EAAAAJ&hl=en" target="_blank" rel="noopener">
      Google Scholar ↗
    </a>
  </div>

  <h2 class="section-title">Education</h2>
  <div class="timeline">
    <div class="timeline-item">
      <div class="timeline-time">Sept 2020 – June 2024</div>
      <h3 class="timeline-title">Shandong University</h3>
      <p class="timeline-meta">B.E. in Automation · Core courses in NLP, image processing, and machine learning.</p>
    </div>
    <div class="timeline-item">
      <div class="timeline-time">Sept 2024 – June 2026</div>
      <h3 class="timeline-title">Hong Kong University of Science and Technology (Guangzhou)</h3>
      <p class="timeline-meta">MPhil in AI · Advisors: Prof. Hui Xiong &amp; Prof. Xuming Hu · Focused on Multimodal LLMs, long video understanding.</p>
    </div>
    <div class="timeline-item current">
      <div class="timeline-time">Fall 2026 – Present</div>
      <h3 class="timeline-title">Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)</h3>
      <p class="timeline-meta">PhD in AI · Advisor: Prof. Xiaojun Chang (常晓军) · Research focus: VLA, Embodied AI, World Models.</p>
    </div>
  </div>

  <h2 class="section-title">Research Interests</h2>
  <div class="grid-2">
    <article class="card">
      <h3>Vision-Language-Action (VLA)</h3>
      <p>Developing unified models that ground language instructions in visual perception and physical actions for robot learning.</p>
    </article>
    <article class="card">
      <h3>Embodied AI</h3>
      <p>Enabling agents to perceive, reason, and act in physical environments through sensorimotor integration and interactive learning.</p>
    </article>
    <article class="card">
      <h3>World Models</h3>
      <p>Building internal representations of the world that allow agents to predict, plan, and generalize across diverse scenarios.</p>
    </article>
    <article class="card">
      <h3>Multimodal LLM</h3>
      <p>Advancing long-video understanding and efficient key-frame selection via multimodal reasoning and semantic alignment.</p>
    </article>
  </div>

  <h2 class="section-title">News & Publications</h2>
  <div class="news-list">
    <article class="news-item">
      <span class="tag">CVPR 2026 Findings</span>
      <a class="news-title" href="https://arxiv.org/abs/2508.06869">VSI: Visual Subtitle Integration for Keyframe Selection to Enhance Long Video Understanding</a>
      <p class="news-authors"><strong>Jianxiang He</strong>, Shaoguang Wang, Weiyu Guo, et al.</p>
    </article>
    <article class="news-item">
      <span class="tag">NeurIPS 2025</span>
      <a class="news-title" href="https://arxiv.org/abs/2503.13139">Logic-in-Frames: Dynamic Keyframe Search via Visual Semantic-Logical Verification for Long Video Understanding</a>
      <p class="news-authors">Weiyu Guo, Ziyang Chen, Shaoguang Wang, <strong>Jianxiang He</strong>, et al.</p>
    </article>
    <article class="news-item">
      <span class="tag">ACL 2025</span>
      <a class="news-title" href="https://arxiv.org/abs/2412.11936">A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method &amp; Challenges</a>
      <p class="news-authors">Yibo Yan, Jiamin Su, <strong>Jianxiang He</strong>, et al.</p>
    </article>
    <article class="news-item">
      <span class="tag">IEEE ROBIO 2022</span>
      <a class="news-title" href="https://ieeexplore.ieee.org/document/10012028">The development of spiking neural network: A review</a>
      <p class="news-authors"><strong>Jianxiang He</strong>, Yanzi Li, Yingtian Liu, et al.</p>
    </article>
  </div>

  <div class="map-container">
    <p class="map-title">Visitor Locations</p>
    <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=Mf2edNvrXMP-LKR3oRo6m-y46Llurx-ccm_QSyDjnlE"></script>
  </div>
</div>

<script>
(function () {
  var authorId = "2347022035";
  var statsEl = document.getElementById("scholar-stats");

  fetch("https://api.semanticscholar.org/graph/v1/author/" + authorId + "?fields=citationCount,hIndex,paperCount")
    .then(function (r) { return r.json(); })
    .then(function (data) {
      statsEl.innerHTML = [
        stat(data.citationCount, "Citations"),
        stat(data.hIndex, "h-index"),
        stat(data.paperCount, "Papers"),
      ].join("");
    })
    .catch(function () {
      statsEl.innerHTML = '<span class="scholar-loading"><a href="https://scholar.google.com/citations?user=6ZJXY_EAAAAJ" target="_blank">View on Google Scholar ↗</a></span>';
    });

  function stat(value, label) {
    return '<div class="scholar-stat"><div class="scholar-stat-value">' + value + '</div><div class="scholar-stat-label">' + label + '</div></div>';
  }
})();
</script>
