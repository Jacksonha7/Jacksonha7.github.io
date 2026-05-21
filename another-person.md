---
layout: page-clean
title: Another Me
permalink: /another-person/index.html
---

<style>
/* ── Section header ──────────────────────────── */
.ap-section { margin-bottom: 64px; }

.ap-sec-head {
  display: flex;
  align-items: baseline;
  gap: 14px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 28px;
}
.ap-sec-title {
  font-size: 1rem;
  font-weight: 600;
  color: #111;
  letter-spacing: -0.02em;
}
.ap-sec-sub {
  font-size: 0.75rem;
  color: #ccc;
  font-weight: 400;
  letter-spacing: 0.01em;
}

/* ── Painting grid ───────────────────────────── */
.art-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}
.art-card {
  position: relative;
  border-radius: 6px;
  overflow: hidden;
  background: #f5f5f5;
  aspect-ratio: 1 / 1;
  cursor: pointer;
}
.art-card img {
  width: 100%; height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.4s ease, filter 0.3s ease;
}
.art-card:hover img {
  transform: scale(1.04);
  filter: brightness(0.88);
}
.art-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  padding: 14px;
  opacity: 0;
  transition: opacity 0.25s ease;
  background: linear-gradient(to top, rgba(0,0,0,0.45) 0%, transparent 60%);
}
.art-card:hover .art-overlay { opacity: 1; }
.art-label {
  font-size: 0.72rem;
  font-weight: 600;
  color: rgba(255,255,255,0.85);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

/* ── Dance grid ──────────────────────────────── */
.dance-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}
.dance-card {
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #f0f0f0;
  background: #fff;
  transition: box-shadow 0.2s, border-color 0.2s;
}
.dance-card:hover {
  border-color: #e0e0e0;
  box-shadow: 0 8px 32px rgba(0,0,0,0.08);
}
.dance-frame {
  width: 100%;
  height: 180px;
  background: #111;
  display: block;
}
.dance-frame iframe {
  width: 100%; height: 100%;
  border: none;
}
.dance-info {
  padding: 16px 18px;
}
.dance-title {
  font-size: 0.86rem;
  font-weight: 600;
  color: #111;
  letter-spacing: -0.01em;
  line-height: 1.5;
  margin-bottom: 4px;
}
.dance-meta {
  font-size: 0.75rem;
  color: #bbb;
  letter-spacing: 0.02em;
}

/* ── Music ───────────────────────────────────── */
.album-link {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 24px 26px;
  border: 1px solid #f0f0f0;
  border-radius: 10px;
  text-decoration: none;
  transition: border-color 0.2s, box-shadow 0.2s;
  background: #fff;
}
.album-link:hover {
  border-color: #ddd;
  box-shadow: 0 8px 32px rgba(0,0,0,0.07);
  text-decoration: none;
}
.album-icon {
  width: 56px; height: 56px;
  border-radius: 8px;
  background: #111;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.album-icon i {
  font-size: 1.4rem;
  color: rgba(255,255,255,0.75);
}
.album-body { flex: 1; min-width: 0; }
.album-title {
  font-size: 0.93rem;
  font-weight: 600;
  color: #111;
  letter-spacing: -0.01em;
  margin-bottom: 4px;
}
.album-desc {
  font-size: 0.78rem;
  color: #bbb;
  line-height: 1.6;
}
.album-arrow {
  font-size: 0.8rem;
  color: #ccc;
  flex-shrink: 0;
  transition: color 0.2s, transform 0.2s;
}
.album-link:hover .album-arrow {
  color: #111;
  transform: translateX(3px);
}

/* ── Responsive ──────────────────────────────── */
@media (max-width: 600px) {
  .art-grid { grid-template-columns: repeat(3, 1fr); gap: 6px; }
  .dance-grid { grid-template-columns: 1fr; }
}
</style>

<!-- ── Painting ── -->
<div class="ap-section reveal">
  <div class="ap-sec-head">
    <span class="ap-sec-title">Paintings</span>
    <span class="ap-sec-sub">Oil &nbsp;·&nbsp; 9 works</span>
  </div>

  <div class="art-grid">
    <div class="art-card">
      <img src="/youhua/painting-1.jpg" alt="Painting 01" loading="lazy">
      <div class="art-overlay"><span class="art-label">01</span></div>
    </div>
    <div class="art-card">
      <img src="/youhua/painting-2.jpg" alt="Painting 02" loading="lazy">
      <div class="art-overlay"><span class="art-label">02</span></div>
    </div>
    <div class="art-card">
      <img src="/youhua/painting-3.jpg" alt="Painting 03" loading="lazy">
      <div class="art-overlay"><span class="art-label">03</span></div>
    </div>
    <div class="art-card">
      <img src="/youhua/painting-4.jpg" alt="Painting 04" loading="lazy">
      <div class="art-overlay"><span class="art-label">04</span></div>
    </div>
    <div class="art-card">
      <img src="/youhua/painting-5.jpg" alt="Painting 05" loading="lazy">
      <div class="art-overlay"><span class="art-label">05</span></div>
    </div>
    <div class="art-card">
      <img src="/youhua/painting-6.jpg" alt="Painting 06" loading="lazy">
      <div class="art-overlay"><span class="art-label">06</span></div>
    </div>
    <div class="art-card">
      <img src="/youhua/painting-7.jpg" alt="Painting 07" loading="lazy">
      <div class="art-overlay"><span class="art-label">07</span></div>
    </div>
    <div class="art-card">
      <img src="/youhua/painting-8.jpg" alt="Painting 08" loading="lazy">
      <div class="art-overlay"><span class="art-label">08</span></div>
    </div>
    <div class="art-card">
      <img src="/youhua/painting-9.jpg" alt="Painting 09" loading="lazy">
      <div class="art-overlay"><span class="art-label">09</span></div>
    </div>
  </div>
</div>

<!-- ── Dance ── -->
<div class="ap-section reveal">
  <div class="ap-sec-head">
    <span class="ap-sec-title">Dance</span>
    <span class="ap-sec-sub">Choreography &nbsp;·&nbsp; Street performance</span>
  </div>

  <div class="dance-grid">
    <div class="dance-card">
      <div class="dance-frame">
        <iframe src="https://player.bilibili.com/player.html?bvid=BV1tv411J7p5&autoplay=0&danmaku=0"
                scrolling="no" frameborder="0" allowfullscreen="true"></iframe>
      </div>
      <div class="dance-info">
        <p class="dance-title">在大学晚会上跳自己的编舞是一种什么样的体验？</p>
        <p class="dance-meta">Original choreography &nbsp;·&nbsp; University gala</p>
      </div>
    </div>

    <div class="dance-card">
      <div class="dance-frame">
        <iframe src="https://player.bilibili.com/player.html?bvid=BV1X7411j7PW&autoplay=0&danmaku=0"
                scrolling="no" frameborder="0" allowfullscreen="true"></iframe>
      </div>
      <div class="dance-info">
        <p class="dance-title">在学校里街演是一种什么样的感受？</p>
        <p class="dance-meta">Street dance &nbsp;·&nbsp; Campus performance</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Music ── -->
<div class="ap-section reveal">
  <div class="ap-sec-head">
    <span class="ap-sec-title">Music</span>
    <span class="ap-sec-sub">Original &nbsp;·&nbsp; Arrangement &nbsp;·&nbsp; Vocal</span>
  </div>

  <a class="album-link" href="https://h5.muse.top/album?id=64bf751358154cfa9979a5f87fc50b6e" target="_blank" rel="noopener">
    <div class="album-icon">
      <i class="fa-solid fa-record-vinyl"></i>
    </div>
    <div class="album-body">
      <p class="album-title">个人专辑 &nbsp;·&nbsp; Personal Album</p>
      <p class="album-desc">原创与翻唱作品合集 &nbsp;·&nbsp; Listen on Muse</p>
    </div>
    <span class="album-arrow">→</span>
  </a>
</div>
