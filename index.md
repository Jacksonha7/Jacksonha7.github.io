---
layout: page
---

<style>
/* ===== 全局样式 ===== */
.page-container {
  font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
  max-width: 900px;
  margin: 0 auto;
  color: #2c3e50;
  padding: 0 20px 60px;
}

.section-title {
  position: relative;
  padding-bottom: 15px;
  margin: 45px 0 25px;
  font-weight: 600;
  letter-spacing: 0.5px;
  color: #2c3e50;
}

.section-title:after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 70px;
  height: 3px;
  background: linear-gradient(to right, #3498db, #9b59b6);
  border-radius: 3px;
}

/* ===== 关于部分 ===== */
.about-card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.07);
  padding: 35px 40px;
  margin-bottom: 40px;
}

.profile-header {
  display: flex;
  align-items: flex-start;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 20px;
}

.avatar-container {
  border-radius: 8px;
  overflow: hidden;
  width: 150px;
  height: 150px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  border: 3px solid white;
  background: #f8f9fa url('placeholder-avatar.jpg') center/cover; /* 替换为实际头像URL */
}

.profile-info {
  flex: 1;
  min-width: 300px;
}

.name {
  font-size: 2.1rem;
  font-weight: 700;
  margin: 0 0 5px;
  color: #2c3e50;
}

.name span {
  color: #7f8c8d;
  font-weight: 400;
  font-size: 1.6rem;
}

.position {
  font-size: 1.25rem;
  color: #3498db;
  margin-bottom: 12px;
  font-weight: 500;
}

.contact-info {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-top: 10px;
}

.contact-item {
  display: flex;
  align-items: center;
  font-size: 0.95rem;
}

.contact-item i {
  margin-right: 8px;
  color: #3498db;
}

.research-intro {
  line-height: 1.7;
  font-size: 1.08rem;
  color: #34495e;
  margin-bottom: 25px;
}

.research-highlight {
  background: linear-gradient(120deg, rgba(52, 152, 219, 0.1) 0%, transparent 100%);
  border-left: 3px solid #3498db;
  padding: 15px 20px;
  border-radius: 0 6px 6px 0;
  margin: 20px 0;
  font-weight: 500;
  color: #2c3e50;
}

/* ===== 教育部分 ===== */
.education-section {
  margin-top: 25px;
}

.education-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.05);
  overflow: hidden;
  margin-bottom: 25px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border-left: 4px solid #ecf0f1;
}

.education-card.featured {
  border-left: 4px solid #3498db;
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(52, 152, 219, 0.15);
}

.edu-header {
  display: flex;
  align-items: flex-start;
  padding: 22px 25px;
  border-bottom: 1px solid #f0f4f8;
  flex-wrap: wrap;
  gap: 15px;
}

.edu-time {
  background: #f8f9fa;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  color: #7f8c8d;
  min-width: 170px;
  text-align: center;
}

.edu-title-container {
  flex: 1;
  min-width: 250px;
}

.edu-school {
  margin: 0 0 5px;
  font-size: 1.35rem;
  font-weight: 600;
  color: #2c3e50;
}

.edu-degree {
  display: block;
  font-size: 1.05rem;
  color: #3498db;
  font-weight: 500;
}

.edu-tag {
  background: #e8f4fc;
  color: #3498db;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.edu-details {
  padding: 22px 25px;
  background: #f9fbfd;
}

.detail-group {
  display: flex;
  margin-bottom: 12px;
  align-items: baseline;
  gap: 10px;
  flex-wrap: wrap;
}

.detail-label {
  font-weight: 600;
  font-size: 0.95rem;
  color: #2c3e50;
  white-space: nowrap;
}

.detail-content {
  font-size: 1.05rem;
  color: #34495e;
  line-height: 1.5;
}

.highlight {
  color: #e74c3c;
  font-weight: 500;
}

/* ===== 研究兴趣 ===== */
.interests-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin: 30px 0;
}

.interest-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  padding: 25px;
  transition: transform 0.3s ease;
  position: relative;
  overflow: hidden;
}

.interest-card:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 5px;
  background: linear-gradient(to right, #3498db, #9b59b6);
}

.interest-card:hover {
  transform: translateY(-5px);
}

.interest-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 15px;
}

.interest-desc {
  font-size: 1rem;
  line-height: 1.7;
  color: #34495e;
}

/* ===== 出版物 ===== */
.publications-container {
  background: white;
  border-radius: 10px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.07);
  padding: 30px;
  margin: 30px 0;
}

.pub-item {
  padding: 18px 0;
  border-bottom: 1px dashed #eee;
}

.pub-item:last-child {
  border-bottom: none;
}

.pub-header {
  font-weight: 600;
  font-size: 1.05rem;
  color: #e74c3c;
  margin-bottom: 8px;
}

.pub-title {
  font-size: 1.15rem;
  font-style: italic;
  color: #2c3e50;
  margin-bottom: 6px;
  display: block;
}

.pub-authors {
  color: #7f8c8d;
  font-size: 0.95rem;
}

/* ===== 通知栏 ===== */
.notice-bar {
  background: linear-gradient(120deg, #ffefef 0%, #fff9f9 100%);
  border-left: 4px solid #c0392b;
  padding: 18px 25px;
  border-radius: 0 6px 6px 0;
  margin: 30px 0;
  color: #c0392b;
  font-weight: 500;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
}

.notice-bar i {
  font-size: 1.4rem;
  margin-right: 15px;
  flex-shrink: 0;
}

/* ===== 地图容器 ===== */
.map-container {
  background: white;
  border-radius: 10px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.07);
  padding: 25px;
  margin: 50px 0 30px;
  text-align: center;
}

.map-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 15px;
}

/* ===== 响应式设计 ===== */
@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
  }
  
  .avatar-container {
    margin: 0 auto;
  }
  
  .edu-header {
    flex-direction: column;
    gap: 12px;
  }
  
  .edu-time {
    align-self: flex-start;
  }
  
  .contact-info {
    flex-direction: column;
    gap: 10px;
  }
}

@media (max-width: 480px) {
  .about-card, .education-card, .publications-container {
    padding: 25px 20px;
  }
}
</style>

<div class="page-container">
  <!-- 关于部分 -->
  <h2 class="section-title">ABOUT ME</h2>
  
  <div class="about-card">
    <div class="profile-header">
      <div class="profile-info">
        <div class="name">Jianxiang He <span>何建翔</span></div>
        <div class="position">MPhil in Artificial Intelligence</div>
        <div class="research-highlight">
          Researching multimodal AI at HKUST(GZ) AI+ Lab/HKUST-GZ NLP Group, focusing on video understanding and efficiency optimization
        </div>
        
        <div class="contact-info">
          <div class="contact-item">
            <i class="fas fa-envelope"></i> jhe307@connect.hkust-gz.edu.cn
          </div>
          <div class="contact-item">
            <i class="fas fa-map-marker-alt"></i> Hong Kong University of Science and Technology (Guangzhou)
          </div>
        </div>
      </div>
    </div>
    
    <div class="research-intro">
      <p>I am a Master of Philosophy student at the Hong Kong University of Science and Technology (Guangzhou). My research is supervised by Professor <strong>Hui Xiong</strong> (Fellow of AAAS, IEEE, CAAI, and AAAI) and Assistant Professor <strong>Xuming Hu</strong>. I am affiliated with the <strong>AI+ Lab/HKUST-GZ NLP Group</strong>, specializing in multimodal large language models and reinforcement learning.</p>
      
      <p>My current research focuses on <strong>long video understanding</strong>, addressing the critical challenge of key frame selection in extended videos. By integrating key frame search algorithms with multimodal fusion techniques, I aim to enhance both efficiency and accuracy in long-video comprehension systems.</p>
      
      <p>I welcome collaborations with scholars working on related topics and enjoy exploring interdisciplinary applications of AI technologies.</p>
    </div>
    
    <div class="notice-bar">
      <i class="fas fa-bullhorn"></i>
      <div>I am actively seeking a PhD position for 2026 Fall admission. Please contact me if you have relevant information or opportunities!</div>
    </div>
  </div>
  
  <!-- 教育部分 -->
  <h2 class="section-title">EDUCATION</h2>
  
  <div class="education-section">
    <!-- 本科教育 -->
    <div class="education-card">
      <div class="edu-header">
        <span class="edu-time">Sept 2020 – June 2024</span>
        <div class="edu-title-container">
          <h3 class="edu-school">Shandong University</h3>
          <span class="edu-degree">Bachelor of Engineering in Automation</span>
        </div>
        <div class="edu-tag">Undergraduate</div>
      </div>

      <div class="edu-details">
        <div class="detail-group">
          <span class="detail-label">CORE COURSES:</span>
          <span class="detail-content">Natural Language Processing, Image Processing, Machine Learning</span>
        </div>
      </div>
    </div>

    <!-- 研究生教育 -->
    <div class="education-card featured">
      <div class="edu-header">
        <span class="edu-time">Sept 2024 – Present</span>
        <div class="edu-title-container">
          <h3 class="edu-school">Hong Kong University of Science and Technology (Guangzhou)</h3>
          <span class="edu-degree">Master of Philosophy in Artificial Intelligence</span>
        </div>
        <div class="edu-tag">Graduate</div>
      </div>

      <div class="edu-details">
        <div class="detail-group">
          <span class="detail-label">RESEARCH FOCUS:</span>
          <span class="detail-content">Multimodal Large Models, Natural Language Processing, Reinforcement Learning</span>
        </div>
        <div class="detail-group">
          <span class="detail-label">LAB:</span>
          <span class="detail-content">AI+ Lab/HKUST-GZ NLP Group</span>
        </div>
      </div>
    </div>
  </div>
  
  <!-- 研究兴趣 -->
  <h2 class="section-title">RESEARCH INTERESTS</h2>
  
  <div class="interests-section">
    <div class="interest-card">
      <h3 class="interest-title">Multi-modal LLM</h3>
      <div class="interest-desc">
        Exploring unified architectures that integrate visual, textual, and auditory information for more comprehensive AI systems that better understand the complex real world.
      </div>
    </div>
    
    <div class="interest-card">
      <h3 class="interest-title">Reinforcement Learning</h3>
      <div class="interest-desc">
        Developing adaptive learning algorithms for sequential decision-making processes, with applications in robotics, automation, and intelligent systems.
      </div>
    </div>
    
    <div class="interest-card">
      <h3 class="interest-title">Video Understanding</h3>
      <div class="interest-desc">
        Creating efficient algorithms for temporal modeling and key-frame selection in long-duration videos, enabling advanced content analysis and retrieval systems.
      </div>
    </div>
  </div>
  
  <!-- 出版物 -->
  <h2 class="section-title">NEWS</h2>
  
  <div class="publications-container">
    <div class="pub-item">
      <div class="pub-header">ACL 2025</div>
      <a href="https://arxiv.org/abs/2412.11936" class="pub-title">A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method & Challenges</a>
      <div class="pub-authors">Yibo Yan, Jiamin Su, <strong>Jianxiang He</strong>, et al.</div>
    </div>
    
    <div class="pub-item">
      <div class="pub-header">IEEE ROBIO 2022</div>
      <a href="https://ieeexplore.ieee.org/document/10012028" class="pub-title">The development of spiking neural network: A review</a>
      <div class="pub-authors"><strong>Jianxiang He</strong>, Yanzi Li, Yingtian Liu, et al.</div>
    </div>
  </div>
  
  <!-- 访客地图 -->
  <div class="map-container">
    <div class="map-title">VISITOR LOCATIONS</div>
    <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=Mf2edNvrXMP-LKR3oRo6m-y46Llurx-ccm_QSyDjnlE"></script>
  </div>
</div>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

---

<script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=Mf2edNvrXMP-LKR3oRo6m-y46Llurx-ccm_QSyDjnlE"></script>
<br>

