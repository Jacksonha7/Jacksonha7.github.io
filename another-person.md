---
layout: page
title: Another Me
---

<style>
/* ── Page Base ───────────────────────────────────── */
.ap-wrap {
  max-width: 960px;
  margin: 0 auto;
  padding: 10px 20px 80px;
  font-family: "PT Serif", Georgia, serif;
  color: #1a1a1a;
}

/* ── Hero Banner ──────────────────────────────────── */
.ap-hero {
  text-align: center;
  padding: 48px 24px 40px;
  background: linear-gradient(135deg, #fdf6f0 0%, #f0f4ff 50%, #fdf0f8 100%);
  border-radius: 10px;
  margin-bottom: 48px;
  border: 1px solid #ebebeb;
}

.ap-hero-title {
  font-size: 2.2rem;
  font-weight: bold;
  margin: 0 0 12px;
  color: #111;
  font-family: "PT Sans Narrow", "PingFang SC", sans-serif;
}

.ap-hero-quote {
  font-size: 1.05rem;
  color: #666;
  font-style: italic;
  margin: 0;
  line-height: 1.7;
}

/* ── Section Headers ──────────────────────────────── */
.ap-section {
  margin-bottom: 56px;
}

.ap-sec-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.4rem;
  font-weight: bold;
  color: #111;
  font-family: "PT Sans Narrow", sans-serif;
  margin: 0 0 8px;
}

.ap-sec-icon {
  font-size: 1.5rem;
  line-height: 1;
}

.ap-sec-divider {
  height: 2px;
  background: linear-gradient(to right, #e05a5a, transparent);
  margin-bottom: 24px;
  border: none;
}

.ap-sec-divider.dance {
  background: linear-gradient(to right, #7c5cbf, transparent);
}

.ap-sec-divider.music {
  background: linear-gradient(to right, #2e86ab, transparent);
}

.ap-sec-desc {
  font-size: 0.92rem;
  color: #888;
  font-style: italic;
  margin: -14px 0 20px;
}

/* ── Art Gallery Grid ─────────────────────────────── */
.art-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 18px;
}

.art-card {
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #e0e0e0;
  background: #fff;
  box-shadow: 0 2px 10px rgba(0,0,0,0.07);
  transition: transform 0.2s, box-shadow 0.2s;
}

.art-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.art-img-wrap {
  width: 100%;
  height: 200px;
  background: #f0ece6;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.art-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.art-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  color: #bbb;
  font-size: 0.82rem;
  text-align: center;
  gap: 8px;
}

.art-placeholder i {
  font-size: 2rem;
  color: #d0c8be;
}

.art-info {
  padding: 12px 14px;
}

.art-info h4 {
  margin: 0 0 4px;
  font-size: 0.92rem;
  color: #333;
  font-family: "PT Sans Narrow", sans-serif;
}

.art-info p {
  margin: 0;
  font-size: 0.8rem;
  color: #999;
}

/* ── Dance Video Grid ─────────────────────────────── */
.dance-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 20px;
}

.dance-card {
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #e0e0e0;
  background: #fff;
  box-shadow: 0 2px 10px rgba(0,0,0,0.07);
  transition: transform 0.2s, box-shadow 0.2s;
}

.dance-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.dance-thumb {
  width: 100%;
  height: 160px;
  background: #1a1a2e;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.dance-thumb video,
.dance-thumb iframe {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.dance-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  color: #666;
  font-size: 0.82rem;
  text-align: center;
  gap: 8px;
  background: linear-gradient(135deg, #1a1a2e, #2d2b55);
}

.dance-placeholder i {
  font-size: 2.4rem;
  color: #9c88ff;
}

.dance-info {
  padding: 12px 14px;
}

.dance-info h4 {
  margin: 0 0 4px;
  font-size: 0.92rem;
  color: #333;
  font-family: "PT Sans Narrow", sans-serif;
}

.dance-info p {
  margin: 0;
  font-size: 0.8rem;
  color: #999;
}

/* ── Music List ───────────────────────────────────── */
.music-list {
  display: grid;
  gap: 14px;
}

.music-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 18px;
  background: #fff;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: border-color 0.2s, box-shadow 0.2s;
}

.music-item:hover {
  border-color: #2e86ab;
  box-shadow: 0 4px 16px rgba(46,134,171,0.1);
}

.music-cover {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #2e86ab, #1a4e6e);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
}

.music-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.music-cover i {
  font-size: 1.4rem;
  color: rgba(255,255,255,0.7);
}

.music-body {
  flex: 1;
  min-width: 0;
}

.music-title {
  font-size: 0.96rem;
  font-weight: bold;
  color: #222;
  margin: 0 0 4px;
  font-family: "PT Sans Narrow", sans-serif;
}

.music-meta {
  font-size: 0.82rem;
  color: #999;
  margin: 0;
}

.music-type {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  white-space: nowrap;
  font-family: "PT Sans Narrow", sans-serif;
  flex-shrink: 0;
}

.music-type.original  { background: #dbeafe; color: #1d4ed8; }
.music-type.cover     { background: #fce7f3; color: #be185d; }
.music-type.arrange   { background: #dcfce7; color: #15803d; }
.music-type.compose   { background: #fef3c7; color: #92400e; }

/* ── Coming Soon ──────────────────────────────────── */
.coming-soon {
  text-align: center;
  padding: 40px 20px;
  color: #aaa;
  font-size: 0.9rem;
  font-style: italic;
  border: 2px dashed #e0e0e0;
  border-radius: 8px;
}

.coming-soon i {
  display: block;
  font-size: 2rem;
  margin-bottom: 10px;
  opacity: 0.4;
}

/* ── Album Card ───────────────────────────────────── */
.album-card {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 22px 24px;
  background: linear-gradient(135deg, #0d1b2a 0%, #1b2a4a 50%, #1a2a3a 100%);
  border-radius: 12px;
  border: 1px solid rgba(46,134,171,0.3);
  text-decoration: none !important;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

.album-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(46,134,171,0.25);
  text-decoration: none !important;
}

.album-cover {
  width: 72px;
  height: 72px;
  background: linear-gradient(135deg, #2e86ab, #1a4e6e);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.album-cover i {
  font-size: 2rem;
  color: rgba(255,255,255,0.85);
  animation: vinyl-spin 8s linear infinite;
}

@keyframes vinyl-spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

.album-card:hover .album-cover i {
  animation-play-state: running;
}

.album-body {
  flex: 1;
  min-width: 0;
}

.album-title {
  font-size: 1.1rem;
  font-weight: bold;
  color: #fff;
  margin: 0 0 6px;
  font-family: "PT Sans Narrow", sans-serif;
}

.album-meta {
  font-size: 0.86rem;
  color: rgba(255,255,255,0.55);
  margin: 0;
  line-height: 1.5;
}

.album-arrow {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  color: #2e86ab;
  font-size: 0.76rem;
  font-weight: 700;
  font-family: "PT Sans Narrow", sans-serif;
  flex-shrink: 0;
}

.album-arrow i {
  font-size: 1.2rem;
}

/* ── Responsive ───────────────────────────────────── */
@media (max-width: 600px) {
  .art-grid, .dance-grid { grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); }
  .ap-hero-title { font-size: 1.7rem; }
  .album-card { flex-wrap: wrap; }
  .album-arrow { flex-direction: row; gap: 6px; }
}
</style>

<div class="ap-wrap">

  <!-- ══ Hero ══════════════════════════════════════ -->
  <div class="ap-hero">
    <h1 class="ap-hero-title">另一个人</h1>
    <p class="ap-hero-quote">
      在学术之外，我也是一个画画的人、跳舞的人、做音乐的人。<br>
      这里记录那些不写论文的时光。
    </p>
  </div>

  <!-- ══ 绘画作品 ══════════════════════════════════ -->
  <div class="ap-section">
    <div class="ap-sec-title">
      <span class="ap-sec-icon">🎨</span>
      绘画作品
    </div>
    <hr class="ap-sec-divider">
    <p class="ap-sec-desc">素描 · 水彩 · 数字绘画 · 插画</p>

    <div class="art-grid">

      <div class="art-card">
        <div class="art-img-wrap">
          <img src="/youhua/painting-1.jpg" alt="绘画作品 1" loading="lazy">
        </div>
        <div class="art-info"><h4>作品 01</h4><p>油画</p></div>
      </div>

      <div class="art-card">
        <div class="art-img-wrap">
          <img src="/youhua/painting-2.jpg" alt="绘画作品 2" loading="lazy">
        </div>
        <div class="art-info"><h4>作品 02</h4><p>油画</p></div>
      </div>

      <div class="art-card">
        <div class="art-img-wrap">
          <img src="/youhua/painting-3.jpg" alt="绘画作品 3" loading="lazy">
        </div>
        <div class="art-info"><h4>作品 03</h4><p>油画</p></div>
      </div>

      <div class="art-card">
        <div class="art-img-wrap">
          <img src="/youhua/painting-4.jpg" alt="绘画作品 4" loading="lazy">
        </div>
        <div class="art-info"><h4>作品 04</h4><p>油画</p></div>
      </div>

      <div class="art-card">
        <div class="art-img-wrap">
          <img src="/youhua/painting-5.jpg" alt="绘画作品 5" loading="lazy">
        </div>
        <div class="art-info"><h4>作品 05</h4><p>油画</p></div>
      </div>

      <div class="art-card">
        <div class="art-img-wrap">
          <img src="/youhua/painting-6.jpg" alt="绘画作品 6" loading="lazy">
        </div>
        <div class="art-info"><h4>作品 06</h4><p>油画</p></div>
      </div>

      <div class="art-card">
        <div class="art-img-wrap">
          <img src="/youhua/painting-7.jpg" alt="绘画作品 7" loading="lazy">
        </div>
        <div class="art-info"><h4>作品 07</h4><p>油画</p></div>
      </div>

      <div class="art-card">
        <div class="art-img-wrap">
          <img src="/youhua/painting-8.jpg" alt="绘画作品 8" loading="lazy">
        </div>
        <div class="art-info"><h4>作品 08</h4><p>油画</p></div>
      </div>

      <div class="art-card">
        <div class="art-img-wrap">
          <img src="/youhua/painting-9.jpg" alt="绘画作品 9" loading="lazy">
        </div>
        <div class="art-info"><h4>作品 09</h4><p>油画</p></div>
      </div>

    </div>
  </div>

  <!-- ══ 舞蹈视频 ══════════════════════════════════ -->
  <div class="ap-section">
    <div class="ap-sec-title">
      <span class="ap-sec-icon">💃</span>
      舞蹈视频
    </div>
    <hr class="ap-sec-divider dance">
    <p class="ap-sec-desc">街舞 · 现代舞 · 翻跳 · 创作</p>

    <div class="dance-grid">

      <div class="dance-card">
        <div class="dance-thumb">
          <iframe src="https://player.bilibili.com/player.html?bvid=BV1tv411J7p5&autoplay=0&danmaku=0"
                  scrolling="no" border="0" frameborder="no" framespacing="0"
                  allowfullscreen="true" style="width:100%;height:100%;"></iframe>
        </div>
        <div class="dance-info">
          <h4>在大学晚会上跳自己的编舞是一种什么样的体验？</h4>
          <p>原创编舞 · 晚会现场</p>
        </div>
      </div>

      <div class="dance-card">
        <div class="dance-thumb">
          <iframe src="https://player.bilibili.com/player.html?bvid=BV1X7411j7PW&autoplay=0&danmaku=0"
                  scrolling="no" border="0" frameborder="no" framespacing="0"
                  allowfullscreen="true" style="width:100%;height:100%;"></iframe>
        </div>
        <div class="dance-info">
          <h4>在学校里街演是一种什么样的感受？</h4>
          <p>街舞 · 校园街演</p>
        </div>
      </div>

    </div>
  </div>

  <!-- ══ 音乐作品 ══════════════════════════════════ -->
  <div class="ap-section">
    <div class="ap-sec-title">
      <span class="ap-sec-icon">🎵</span>
      音乐作品
    </div>
    <hr class="ap-sec-divider music">
    <p class="ap-sec-desc">原创 · 翻唱 · 编曲 · 器乐</p>

    <!-- 个人专辑卡片 -->
    <a class="album-card" href="https://h5.muse.top/album?id=64bf751358154cfa9979a5f87fc50b6e" target="_blank" rel="noopener">
      <div class="album-cover">
        <i class="fa-solid fa-record-vinyl"></i>
      </div>
      <div class="album-body">
        <p class="album-title">个人专辑</p>
        <p class="album-meta">收录我的原创与翻唱作品 · 在 Muse 平台收听</p>
      </div>
      <div class="album-arrow">
        <i class="fa-solid fa-arrow-up-right-from-square"></i>
        <span>前往收听</span>
      </div>
    </a>

  </div>

</div>
