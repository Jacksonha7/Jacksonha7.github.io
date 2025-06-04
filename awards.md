---
layout: page
permalink: /awards/index.html
title: Awards
---

<style>
/* 全局样式 */
.page-content {
  font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
  max-width: 800px;
  margin: 0 auto;
  color: #2c3e50;
  padding: 0 20px;
}

/* 标题样式 */
.page-title {
  text-align: center;
  font-weight: 600;
  margin: 40px 0 30px;
  position: relative;
  color: #2c3e50;
}

.page-title:after {
  content: '';
  display: block;
  width: 80px;
  height: 3px;
  background: #3498db;
  margin: 15px auto 0;
}

/* 分区样式 */
.section-container {
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  padding: 30px;
  margin-bottom: 40px;
}

.section-header {
  display: flex;
  align-items: center;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}

.section-header h2 {
  margin: 0;
  font-weight: 600;
  color: #3498db;
  font-size: 1.6rem;
}

.section-header i {
  margin-right: 12px;
  color: #e67e22;
}

/* 奖项样式 */
.category-container {
  margin-bottom: 30px;
}

.category-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.category-header h3 {
  margin: 0;
  font-size: 1.3rem;
  font-weight: 500;
  color: #2c3e50;
  background: linear-gradient(to right, transparent 0%, #f8f9fa 50%, transparent 100%);
  padding: 5px 0 5px 15px;
  width: 100%;
}

.award-list {
  list-style: none;
  padding-left: 0;
}

.award-item {
  margin-bottom: 20px;
  padding-left: 40px;
  position: relative;
}

.award-item:before {
  content: '★';
  position: absolute;
  left: 0;
  top: 2px;
  color: #e67e22;
  font-size: 18px;
}

.award-time {
  display: inline-block;
  background: #e8f4fc;
  padding: 3px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 500;
  color: #3498db;
  margin-right: 10px;
}

.award-title {
  font-size: 1.1rem;
  font-weight: 500;
  margin-bottom: 5px;
}

.award-description {
  display: block;
  color: #7f8c8d;
  font-size: 0.95rem;
  line-height: 1.5;
  margin-top: 5px;
}

/* 科研项目样式 */
.project-item {
  border-left: 3px solid #3498db;
  padding-left: 25px;
  margin-bottom: 35px;
  position: relative;
}

.project-header {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-bottom: 8px;
}

.project-title {
  font-size: 1.25rem;
  font-weight: 500;
  color: #2c3e50;
  margin: 0;
}

.project-subtitle {
  font-size: 0.95rem;
  color: #7f8c8d;
  font-weight: 400;
  font-style: italic;
}

.project-time {
  background: #f8f9fa;
  padding: 3px 12px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  color: #7f8c8d;
  min-width: 170px;
  text-align: center;
  align-self: flex-start;
}

.project-advisor {
  display: flex;
  align-items: center;
  color: #3498db;
  font-size: 0.95rem;
  margin: 10px 0 15px;
}

.project-advisor i {
  margin-right: 8px;
}

.project-list {
  list-style: none;
  padding-left: 20px;
}

.project-list li {
  margin-bottom: 10px;
  position: relative;
  padding-left: 25px;
  line-height: 1.6;
}

.project-list li:before {
  content: '—';
  position: absolute;
  left: 0;
  color: #3498db;
}

.project-list strong {
  color: #e74c3c;
}

.project-badge {
  display: inline-block;
  background: #e8f4fc;
  color: #3498db;
  padding: 5px 12px;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-right: 8px;
  margin-top: 15px;
}

@media (max-width: 768px) {
  .project-header {
    flex-direction: column;
    gap: 10px;
  }
  
  .project-time {
    align-self: flex-start;
  }
}
</style>

<div class="page-content">
  <h1 class="page-title">AWARDS & RESEARCH</h1>

  <!-- 奖项部分 -->
  <div class="section-container">
    <div class="section-header">
      <i class="fas fa-trophy"></i>
      <h2>AWARDS</h2>
    </div>

    <div class="category-container">
      <div class="category-header">
        <h3>COMPETITIONS</h3>
      </div>
      <ul class="award-list">
        <li class="award-item">
          <span class="award-time">2021</span>
          <div class="award-title">Provincial First Prize of the National College Students' Mathematical Modeling Competition (National Competition)</div>
        </li>
      </ul>
    </div>

    <div class="category-container">
      <div class="category-header">
        <h3>SCHOLARSHIPS</h3>
      </div>
      <ul class="award-list">
        <li class="award-item">
          <span class="award-time">2022-2023</span>
          <div class="award-title">New Scenery Special Scholarship of Shandong University</div>
          <span class="award-description">One of the university's highest honors and scholarships</span>
        </li>
      </ul>
    </div>

    <div class="category-container">
      <div class="category-header">
        <h3>HONORS</h3>
      </div>
      <ul class="award-list">
        <li class="award-item">
          <span class="award-time">2021-2022</span>
          <div class="award-title">Excellent Individual of Innovation and Entrepreneurship of Shandong University</div>
          <span class="award-description">Annual award rate &lt; 5%</span>
        </li>
      </ul>
    </div>
  </div>

  <!-- 科研经历部分 -->
  <div class="section-container">
    <div class="section-header">
      <i class="fas fa-flask"></i>
      <h2>EARLY RESEARCH EXPERIENCE</h2>
    </div>

    <!-- 牛津导师制项目 -->
    <div class="project-item">
      <div class="project-header">
        <div>
          <h3 class="project-title">Oxford Online Tutorial Project</h3>
          <span class="project-subtitle">Mentored Research</span>
        </div>
        <span class="project-time">Sep 2021 - Dec 2021</span>
      </div>
      
      <div class="project-advisor">
        <i class="fas fa-chalkboard-teacher"></i>
        <span>Supervisor: Prof. David Clifton, Computer Vision Group</span>
      </div>
      
      <ul class="project-list">
        <li>Developed real-time gaze tracking system using <strong>OpenCV</strong> and MediaPipe, achieving 85% accuracy on MIT Eye Dataset</li>
        <li>Built multi-modal data synchronization pipeline for aligning eye tracking videos with EEG signals</li>
        <li>Implemented image preprocessing workflow including ROI detection and perspective correction</li>
        <li>Visualized attention heatmaps through Gaussian kernel density estimation</li>
      </ul>
      
      <div>
        <span class="project-badge">Real-time Processing</span>
        <span class="project-badge">Human-Computer Interaction</span>
      </div>
    </div>

    <!-- STEM跨学科项目 -->
    <div class="project-item">
      <div class="project-header">
        <div>
          <h3 class="project-title">Oxford STEM Summer School</h3>
          <span class="project-subtitle">Interdisciplinary Program</span>
        </div>
        <span class="project-time">Dec 2021 - Dec 2022</span>
      </div>
      
      <ul class="project-list">
        <li>Collaborated with materials science researchers on microstructure image analysis using <strong>Scikit-image</strong></li>
        <li>Designed CNN-based classifier for defect detection in SEM images (F1-score 78.5%)</li>
        <li>Participated in cross-domain workshops with Oxford Robotics Institute on sensor fusion techniques</li>
        <li>Presented technical report on applications of homography transformation in drone navigation</li>
      </ul>
      
      <div>
        <span class="project-badge">Cross-domain Collaboration</span>
        <span class="project-badge">Image Analysis</span>
      </div>
    </div>
  </div>
</div>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">