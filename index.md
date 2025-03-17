---
layout: page
---

# About Me

<!-- <img src="https://caihanlin.com/caihanlin.jpg" class="floatpic"> -->

Here is **Jianxiang He (Jackson, 何建翔)**.<br>
<div class="education-section">
    <h2>Education</h2>

    <!-- 本科教育 -->
    <div class="education-item">
        <div class="bordered-container"> <!-- 新增边框容器 -->
            <div class="two-col-entry">
                <div class="time-range">Sept 2020 – June 2024</div>
                <div class="details">
                    <strong>Shandong University</strong>, Undergraduate, Automation
                </div>
            </div>
        </div>
        
        <div class="one-col-entry">
            <ul class="highlights">
                <li><strong>Coursework:</strong> Natural Language Processing, Image Processing, Machine Learning</li>
            </ul>
        </div>
    </div>

    <!-- 研究生教育 -->
    <div class="education-item">
        <div class="bordered-container"> <!-- 新增边框容器 -->
            <div class="two-col-entry">
                <div class="time-range">Sept 2024 – now</div>
                <div class="details">
                    <strong>Hong Kong University of Science and Technology (GZ)</strong>, MPhil, AI Thrust
                </div>
            </div>
        </div>
        
        <div class="one-col-entry">
            <ul class="highlights">
                <li><strong>Areas of Interest:</strong> Multimodal Large Models, Natural Language Processing, Reinforcement Learning</li>
            </ul>
        </div>
    </div>
</div>

<style>
.bordered-container {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 10px;
    background: #f9f9f9;
}

.education-section {
    margin-bottom: 30px;
}

.two-col-entry {
    display: flex;
}

.time-range {
    width: 20%;
    font-weight: 500;
    color: #666;
}

.details {
    width: 80%;
    color: #333;
}

.one-col-entry {
    margin-bottom: 20px;
}

.highlights {
    margin: 8px 0;
    padding-left: 25px;
}

.highlights li {
    margin-bottom: 6px;
}
</style>

**<font color="#990000">I am actively seeking a PhD position for 2026 Fall admission. If you have any information, please contact me. Thank you!</font>**

---

## Current Research Interests

- Vision and Language Large Model
- Reinforcement Learning

<!-- My current research focuses on practical problems that artificial intelligence faces in real life. My interests are on the Machine Learning and its applications in Industrial IoT. In a word, advanced technologies like ML and IoT positively influence the life of everybody.  I wish to devote my talent to this meaningful cause and bring well-being to society. -->

---

## News and Updates
<div class="publications">
  <!-- <h2>Publications</h2> -->
  <ul class="timeline">
    <!-- 已发表论文 -->
    <li>
      <strong>IEEE ROBIO 2022</strong>
      <div class="pub-item">
        <a href="#"><em>The development of spiking neural network: A review</em></a>
        <div class="authors"><u>Jianxiang He</u>, Yanzi Li, Yingtian Liu, et al.</div>
        <!-- <p>系统综述了脉冲神经网络（SNN）的四大核心模块（神经元模型、编码方法、网络架构与学习算法），对比了Hodgkin-Huxley、LIF等模型的生物解释性与计算效率...</p> -->
      </div>
    </li>

    <!-- 在审论文统一模板 -->
    <li>
      <strong>Under Review · ACL 2025</strong>
      <div class="pub-item">
        <a href="#"><em>A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model</em></a>
        <div class="authors">Yibo Yan, Jiaming Su, <u>Jianxiang He</u>, et al.</div>
        <!-- <p>系统整合了200+项研究，提出涵盖问题求解、定理证明与错误诊断的多任务评估体系...</p> -->
      </div>
    </li>

    <li>
      <strong>Under Review · IJCAI 2025</strong>
      <div class="pub-item">
        <a href="#"><em>A Survey of fMRI to Image Reconstruction</em></a>
        <div class="authors">Weiyu Guo, Guoying Sun, <u>Jianxiang He</u>, et al.</div>
        <!-- <p>首次提出并系统梳理了fMRI到图像重建（fMRI2Image）领域的完整方法论框架...</p> -->
      </div>
    </li>

    <li>
      <strong>Under Review · ICCV 2025</strong>
      <div class="pub-item">
        <a href="#"><em>Logic-in-Frames: Dynamic keyframe search through visual semantic-logic verification for long video understanding</em></a>
        <div class="authors">Weiyu Guo, Ziyang Chen, Shaoguang Wang, <u>Jianxiang He</u>, et al.</div>
        <!-- <p>提出VSLS视觉语义逻辑搜索框架，首次在长视频理解中引入四类语义逻辑关系...</p> -->
      </div>
    </li>
  </ul>
</div>
---

## Early experiences
<div class="cv-experience">
  <h2>Computer Vision Research</h2>
  
  <div class="project">
    <div class="project-header">
      <h3>Oxford Visual Intelligence Lab</h3>
      <span class="time">Sep 2021 - Dec 2021</span>
    </div>
    <ul class="tech-list">
      <li>Developed multi-camera 3D human pose estimation pipeline using PyTorch with <strong>87% PCK accuracy</strong></li>
      <li>Designed temporal alignment framework for RGB-D video streams using <em>OpenCV</em> and <em>FFmpeg</em></li>
      <li>Implemented attention-guided visual saliency prediction combining CNN and LSTM architectures</li>
      <li>Created synthetic training data pipeline with <strong>Blender</strong> for occlusion-robust object detection</li>
    </ul>
    <div class="achievement">
      <span class="badge">Innovation</span>
      <span class="badge">Real-time System</span>
      <span class="badge">Multi-modal Fusion</span>
    </div>
  </div>

  <div class="project">
    <div class="project-header">
      <h3>Oxford Autonomous Systems Initiative</h3>
      <span class="time">Dec 2021 - Dec 2022</span>
    </div>
    <ul class="tech-list">
      <li>Built vision transformer (ViT) model for traffic flow prediction from surveillance camera feeds (<em>79.2% mAP</em>)</li>
      <li>Pioneered neural radiance fields (NeRF) implementation for urban scene reconstruction from drone footage</li>
      <li>Optimized YOLOv7 deployment on edge devices using TensorRT with <strong>23ms inference latency</strong></li>
      <li>Developed GAN-based framework for synthetic adverse weather condition generation (<em>FID score 18.7</em>)</li>
    </ul>
    <div class="achievement">
      <span class="badge">3D Reconstruction</span>
      <span class="badge">Edge AI</span>
      <span class="badge">Synthetic Data</span>
    </div>
  </div>
</div>

<br>

