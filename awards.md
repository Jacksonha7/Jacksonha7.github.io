---
layout: page-clean
permalink: /awards/index.html
title: Awards
---

<style>
/* ── Award list ──────────────────────────────── */
.award-section { margin-bottom: 56px; }

.award-section-title {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #bbb;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 0;
}

.award-row {
  display: flex;
  gap: 24px;
  align-items: flex-start;
  padding: 22px 0;
  border-bottom: 1px solid #f6f6f6;
  margin-left: -12px;
  padding-left: 12px;
  border-radius: 6px;
  transition: background 0.18s;
}
.award-row:last-child { border-bottom: none; }
.award-row:hover { background: #fafafa; }

.award-year {
  font-size: 0.72rem;
  font-weight: 700;
  color: #ccc;
  white-space: nowrap;
  min-width: 72px;
  padding-top: 3px;
  letter-spacing: 0.04em;
  font-variant-numeric: tabular-nums;
}

.award-body { flex: 1; min-width: 0; }

.award-name {
  font-size: 0.93rem;
  font-weight: 600;
  color: #111;
  letter-spacing: -0.01em;
  line-height: 1.5;
  margin-bottom: 3px;
}

.award-desc {
  font-size: 0.8rem;
  color: #aaa;
  line-height: 1.6;
}

/* ── Research experience ─────────────────────── */
.res-section { margin-bottom: 56px; }

.res-row {
  padding: 28px 0;
  border-bottom: 1px solid #f6f6f6;
  margin-left: -12px;
  padding-left: 12px;
  border-radius: 6px;
  transition: background 0.18s;
}
.res-row:last-child { border-bottom: none; }
.res-row:hover { background: #fafafa; }

.res-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
  margin-bottom: 14px;
}

.res-title {
  font-size: 0.96rem;
  font-weight: 600;
  color: #111;
  letter-spacing: -0.01em;
  line-height: 1.4;
}
.res-sub {
  font-size: 0.8rem;
  color: #aaa;
  margin-top: 3px;
}

.res-meta {
  text-align: right;
  flex-shrink: 0;
}
.res-period {
  font-size: 0.72rem;
  font-weight: 700;
  color: #ccc;
  letter-spacing: 0.04em;
  white-space: nowrap;
}
.res-tag {
  display: inline-block;
  margin-top: 5px;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 4px;
  background: #f0f0f0;
  color: #888;
}

.res-advisor {
  font-size: 0.8rem;
  color: #aaa;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.res-advisor i { font-size: 0.72rem; }

.res-list {
  list-style: none;
  padding: 0;
  margin: 0 0 14px;
  display: flex;
  flex-direction: column;
  gap: 7px;
}
.res-list li {
  font-size: 0.82rem;
  color: #777;
  line-height: 1.65;
  padding-left: 16px;
  position: relative;
}
.res-list li::before {
  content: '·';
  position: absolute;
  left: 4px;
  color: #ccc;
  font-weight: 700;
}

.res-tags { display: flex; gap: 8px; flex-wrap: wrap; }
.res-pill {
  font-size: 0.68rem;
  font-weight: 600;
  color: #999;
  background: #f5f5f5;
  padding: 3px 10px;
  border-radius: 999px;
  letter-spacing: 0.02em;
}

@media (max-width: 600px) {
  .res-header { flex-direction: column; gap: 6px; }
  .res-meta { text-align: left; }
}
</style>

<!-- Awards -->
<div class="award-section reveal">
  <p class="award-section-title">Competitions</p>
  <div class="award-row">
    <span class="award-year">2021</span>
    <div class="award-body">
      <p class="award-name">Provincial First Prize · National College Students' Mathematical Modeling Competition</p>
    </div>
  </div>
</div>

<div class="award-section reveal">
  <p class="award-section-title">Scholarships</p>
  <div class="award-row">
    <span class="award-year">2022–23</span>
    <div class="award-body">
      <p class="award-name">New Scenery Special Scholarship &nbsp;·&nbsp; Shandong University</p>
      <p class="award-desc">One of the university's highest honors and scholarships</p>
    </div>
  </div>
</div>

<div class="award-section reveal">
  <p class="award-section-title">Honors</p>
  <div class="award-row">
    <span class="award-year">2021–22</span>
    <div class="award-body">
      <p class="award-name">Excellent Individual of Innovation and Entrepreneurship &nbsp;·&nbsp; Shandong University</p>
      <p class="award-desc">Annual award rate &lt; 5%</p>
    </div>
  </div>
</div>

<!-- Research Experience -->
<div class="res-section reveal">
  <p class="award-section-title">Research Experience</p>

  <div class="res-row">
    <div class="res-header">
      <div>
        <p class="res-title">Oxford Online Tutorial Project</p>
        <p class="res-sub">Mentored Research &nbsp;·&nbsp; Computer Vision Group</p>
      </div>
      <div class="res-meta">
        <p class="res-period">Sep – Dec 2021</p>
        <span class="res-tag">Computer Vision</span>
      </div>
    </div>
    <p class="res-advisor"><i class="fa-solid fa-circle-user"></i> Supervisor: Prof. David Clifton</p>
    <ul class="res-list">
      <li>Developed real-time gaze tracking system using <strong>OpenCV</strong> and MediaPipe, achieving 85% accuracy on MIT Eye Dataset</li>
      <li>Built multi-modal data synchronization pipeline for aligning eye tracking videos with EEG signals</li>
      <li>Implemented image preprocessing workflow including ROI detection and perspective correction</li>
      <li>Visualized attention heatmaps via Gaussian kernel density estimation</li>
    </ul>
    <div class="res-tags">
      <span class="res-pill">Real-time Processing</span>
      <span class="res-pill">Human-Computer Interaction</span>
    </div>
  </div>

  <div class="res-row">
    <div class="res-header">
      <div>
        <p class="res-title">Oxford STEM Summer School</p>
        <p class="res-sub">Interdisciplinary Program &nbsp;·&nbsp; Oxford Robotics Institute</p>
      </div>
      <div class="res-meta">
        <p class="res-period">Dec 2021 – Dec 2022</p>
        <span class="res-tag">Materials Science</span>
      </div>
    </div>
    <ul class="res-list">
      <li>Collaborated with materials science researchers on microstructure image analysis using <strong>Scikit-image</strong></li>
      <li>Designed CNN-based classifier for defect detection in SEM images (F1-score 78.5%)</li>
      <li>Participated in cross-domain workshops on sensor fusion techniques</li>
      <li>Presented technical report on homography transformation in drone navigation</li>
    </ul>
    <div class="res-tags">
      <span class="res-pill">Cross-domain Collaboration</span>
      <span class="res-pill">Image Analysis</span>
    </div>
  </div>
</div>
