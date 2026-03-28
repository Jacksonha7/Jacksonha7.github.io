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

.notice-bar {
  margin-top: 18px;
  border-radius: 12px;
  padding: 14px 16px;
  border: 1px solid rgba(234, 88, 12, 0.28);
  background: linear-gradient(120deg, #fff7ed, #fff);
  color: #9a3412;
  font-weight: 600;
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
}
</style>

<div class="page-container">
  <section class="hero">
    <h1 class="hero-headline">Jianxiang He / 何建翔</h1>
    <p class="hero-subline">
      MPhil in Artificial Intelligence at HKUST(GZ), currently working on multimodal large language models,
      long video understanding, and efficient key-frame selection.
    </p>
    <div class="badge-row">
      <span class="badge">Multimodal LLM</span>
      <span class="badge">Video Understanding</span>
      <span class="badge">Reinforcement Learning</span>
      <span class="badge">NLP</span>
    </div>
    <div class="contact-grid">
      <p class="contact-line"><strong>Email:</strong> jhe307@connect.hkust-gz.edu.cn</p>
      <p class="contact-line"><strong>Affiliation:</strong> AI+ Lab / HKUST-GZ NLP Group</p>
    </div>
    <div class="notice-bar">
      I am actively seeking a PhD position for Fall 2026. Feel free to reach out for collaboration or opportunities.
    </div>
  </section>

  <h2 class="section-title">About</h2>
  <div class="card">
    <p>
      I am a Master of Philosophy student at the Hong Kong University of Science and Technology (Guangzhou),
      advised by Professor <strong>Hui Xiong</strong> and Assistant Professor <strong>Xuming Hu</strong>.
      My current research focuses on long-video understanding, where I explore key-frame selection and multimodal
      fusion strategies to improve both efficiency and reasoning quality.
    </p>
  </div>

  <h2 class="section-title">Education</h2>
  <div class="timeline">
    <div class="timeline-item">
      <div class="timeline-time">Sept 2020 – June 2024</div>
      <h3 class="timeline-title">Shandong University</h3>
      <p class="timeline-meta">B.E. in Automation · Core courses in NLP, image processing, and machine learning.</p>
    </div>
    <div class="timeline-item current">
      <div class="timeline-time">Sept 2024 – Present</div>
      <h3 class="timeline-title">Hong Kong University of Science and Technology (Guangzhou)</h3>
      <p class="timeline-meta">MPhil in AI · Focused on Multimodal LLMs, NLP, and reinforcement learning.</p>
    </div>
  </div>

  <h2 class="section-title">Research Interests</h2>
  <div class="grid-2">
    <article class="card">
      <h3>Multimodal LLM</h3>
      <p>Building unified systems that align language, vision, and audio for robust real-world understanding.</p>
    </article>
    <article class="card">
      <h3>Reinforcement Learning</h3>
      <p>Designing adaptive optimization strategies for sequential decision-making and efficient policy learning.</p>
    </article>
    <article class="card">
      <h3>Video Understanding</h3>
      <p>Studying temporal reasoning and sparse key-frame retrieval in long videos for scalable model inference.</p>
    </article>
    <article class="card">
      <h3>Applied NLP</h3>
      <p>Exploring efficient and reliable language technologies for research, education, and productivity tools.</p>
    </article>
  </div>

  <h2 class="section-title">News & Publications</h2>
  <div class="news-list">
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
