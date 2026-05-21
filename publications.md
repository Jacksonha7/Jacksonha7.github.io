---
layout: page-clean
permalink: /publications/index.html
title: Publications
---

<style>
/* ── Pub section ─────────────────────────────── */
.pub-section { margin-bottom: 56px; }

.pub-section-title {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #bbb;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 0;
}

/* ── Pub row ─────────────────────────────────── */
.pub-row {
  display: grid;
  grid-template-columns: 76px 1fr;
  gap: 0 24px;
  padding: 26px 0;
  border-bottom: 1px solid #f6f6f6;
  transition: background 0.18s;
  margin-left: -12px;
  padding-left: 12px;
  border-radius: 6px;
}
.pub-row:last-child { border-bottom: none; }
.pub-row:hover { background: #fafafa; }

/* Badge column */
.pub-badge-col { padding-top: 4px; }
.pb {
  display: inline-block;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 4px 8px;
  border-radius: 4px;
  white-space: nowrap;
  line-height: 1.4;
}
.pb-green  { background: #ecfdf5; color: #059669; }
.pb-orange { background: #fff7ed; color: #c2410c; }
.pb-blue   { background: #eff6ff; color: #1d4ed8; }
.pb-gray   { background: #f5f5f5; color: #888; }

/* Content column */
.pub-title {
  font-size: 0.94rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: 1.55;
  margin-bottom: 6px;
}
.pub-title a {
  color: #111;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0;
  transition: color 0.2s, gap 0.2s;
}
.pub-title a::after {
  content: '→';
  font-size: 0.8rem;
  opacity: 0;
  transform: translateX(-5px);
  transition: opacity 0.2s, transform 0.2s;
  display: inline-block;
  line-height: 1;
}
.pub-title a:hover { color: #0055cc; gap: 5px; }
.pub-title a:hover::after { opacity: 1; transform: translateX(0); }

.pub-authors {
  font-size: 0.8rem;
  color: #aaa;
  line-height: 1.65;
  margin-bottom: 4px;
}
.pub-authors strong { color: #555; font-weight: 600; }

.pub-venue {
  font-size: 0.78rem;
  color: #ccc;
  font-style: italic;
  margin-bottom: 10px;
}

.pub-links { display: flex; gap: 18px; }
.pub-link {
  font-size: 0.76rem;
  font-weight: 600;
  color: #ccc;
  text-decoration: none;
  letter-spacing: 0.02em;
  transition: color 0.18s;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.pub-link:hover { color: #111; }
.pub-link i { font-size: 0.72rem; }

/* ── Highlight note ──────────────────────────── */
.pub-note {
  font-size: 0.82rem;
  color: #bbb;
  line-height: 1.7;
  margin-bottom: 24px;
  padding-left: 14px;
  border-left: 2px solid #eee;
}
</style>

<!-- Accepted -->
<div class="pub-section reveal">
  <p class="pub-section-title">Conference Papers — Accepted</p>

  <div class="pub-row">
    <div class="pub-badge-col"><span class="pb pb-green">Accepted</span></div>
    <div>
      <p class="pub-title">
        <a href="https://arxiv.org/abs/2508.06869" target="_blank" rel="noopener">
          VSI: Visual Subtitle Integration for Keyframe Selection to Enhance Long Video Understanding
        </a>
      </p>
      <p class="pub-authors"><strong>Jianxiang He</strong>, Shaoguang Wang, Weiyu Guo, Meisheng Hong, Jungang Li, Yijie Xu, Ziyang Chen, Hui Xiong</p>
      <p class="pub-venue">CVPR 2026 Findings &nbsp;·&nbsp; IEEE/CVF Conference on Computer Vision and Pattern Recognition</p>
      <div class="pub-links">
        <a class="pub-link" href="https://arxiv.org/abs/2508.06869" target="_blank" rel="noopener"><i class="fa-solid fa-file-lines"></i> arXiv</a>
        <a class="pub-link" href="#"><i class="fa-brands fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div class="pub-row">
    <div class="pub-badge-col"><span class="pb pb-green">Accepted</span></div>
    <div>
      <p class="pub-title">
        <a href="https://arxiv.org/abs/2503.13139" target="_blank" rel="noopener">
          Logic-in-Frames: Dynamic Keyframe Search via Visual Semantic-Logical Verification for Long Video Understanding
        </a>
      </p>
      <p class="pub-authors">Weiyu Guo, Ziyang Chen, Shaoguang Wang, <strong>Jianxiang He</strong>, Yijie Xu, Jinhui Ye, Ying Sun, Hui Xiong</p>
      <p class="pub-venue">NeurIPS 2025 &nbsp;·&nbsp; 38th Conference on Neural Information Processing Systems</p>
      <div class="pub-links">
        <a class="pub-link" href="https://arxiv.org/abs/2503.13139" target="_blank" rel="noopener"><i class="fa-solid fa-file-lines"></i> arXiv</a>
        <a class="pub-link" href="#"><i class="fa-brands fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div class="pub-row">
    <div class="pub-badge-col"><span class="pb pb-green">Published</span></div>
    <div>
      <p class="pub-title">
        <a href="https://arxiv.org/abs/2412.11936" target="_blank" rel="noopener">
          A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method &amp; Challenges
        </a>
      </p>
      <p class="pub-authors">Yibo Yan, Jiamin Su, <strong>Jianxiang He</strong>, Fangteng Fu, Xu Zheng, Yuanhuiyi Lyu, Kun Wang, Shen Wang, Qingsong Wen, Xuming Hu</p>
      <p class="pub-venue">ACL 2025 &nbsp;·&nbsp; 63rd Annual Meeting of the Association for Computational Linguistics</p>
      <div class="pub-links">
        <a class="pub-link" href="https://arxiv.org/abs/2412.11936" target="_blank" rel="noopener"><i class="fa-solid fa-file-lines"></i> PDF</a>
        <a class="pub-link" href="#"><i class="fa-brands fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div class="pub-row">
    <div class="pub-badge-col"><span class="pb pb-green">Published</span></div>
    <div>
      <p class="pub-title">
        <a href="https://ieeexplore.ieee.org/abstract/document/10012028/" target="_blank" rel="noopener">
          The Development of Spiking Neural Network: A Review
        </a>
      </p>
      <p class="pub-authors"><strong>Jianxiang He</strong>, Yanzi Li, Yingtian Liu, Jiyang Chen, Chaoqun Wang, Rui Song, Yibin Li</p>
      <p class="pub-venue">IEEE ROBIO 2022 &nbsp;·&nbsp; International Conference on Robotics and Biomimetics</p>
      <div class="pub-links">
        <a class="pub-link" href="https://ieeexplore.ieee.org/abstract/document/10012028/" target="_blank" rel="noopener"><i class="fa-solid fa-file-lines"></i> PDF</a>
      </div>
    </div>
  </div>
</div>

<!-- Under Review -->
<div class="pub-section reveal">
  <p class="pub-section-title">Preprints &amp; Under Review</p>

  <div class="pub-row">
    <div class="pub-badge-col"><span class="pb pb-orange">Review</span></div>
    <div>
      <p class="pub-title">
        <a href="https://openreview.net/pdf?id=y5X44PzafF" target="_blank" rel="noopener">
          Distribution Preference Optimization: A Fine-grained Perspective for LLM Unlearning
        </a>
      </p>
      <p class="pub-authors">Kai Qin, Jiaqi Wu, <strong>Jianxiang He</strong>, Haoyuan Sun, Yifei Zhao, Bin Liang, Yongzhe Chang, Tiantian Zhang, Houde Liu</p>
      <p class="pub-venue">Under Review</p>
      <div class="pub-links">
        <a class="pub-link" href="https://openreview.net/pdf?id=y5X44PzafF" target="_blank" rel="noopener"><i class="fa-solid fa-file-lines"></i> PDF</a>
      </div>
    </div>
  </div>

  <div class="pub-row">
    <div class="pub-badge-col"><span class="pb pb-gray">Preprint</span></div>
    <div>
      <p class="pub-title">
        <a href="https://arxiv.org/abs/2502.16861" target="_blank" rel="noopener">
          A Survey of fMRI to Image Reconstruction
        </a>
      </p>
      <p class="pub-authors">Weiyu Guo, Guoying Sun, <strong>Jianxiang He</strong>, Tong Shao, Shaoguang Wang, Ziyang Chen, Meisheng Hong, Ying Sun, Hui Xiong</p>
      <p class="pub-venue">arXiv preprint</p>
      <div class="pub-links">
        <a class="pub-link" href="https://arxiv.org/abs/2502.16861" target="_blank" rel="noopener"><i class="fa-solid fa-file-lines"></i> PDF</a>
      </div>
    </div>
  </div>
</div>
