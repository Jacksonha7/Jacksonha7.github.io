---
layout: page
permalink: /awards/index.html
title: Awards
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

        /* ===== 卡片样式 ===== */
        .content-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.07);
            padding: 35px 40px;
            margin-bottom: 40px;
        }

        /* ===== 奖项部分 ===== */
        .category-container {
            margin-bottom: 30px;
        }

        .category-header {
            position: relative;
            padding-bottom: 12px;
            margin-bottom: 20px;
        }

        .category-header h3 {
            font-size: 1.35rem;
            font-weight: 600;
            color: #2c3e50;
            margin: 0;
        }

        .category-header:after {
            content: '';
            position: absolute;
            left: 0;
            bottom: 0;
            width: 50px;
            height: 2px;
            background: linear-gradient(to right, #3498db, #9b59b6);
            border-radius: 2px;
        }

        .award-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .award-item {
            padding: 15px 0;
            border-bottom: 1px solid #f0f4f8;
            display: flex;
            gap: 15px;
        }

        .award-item:last-child {
            border-bottom: none;
        }

        .award-time {
            background: #f8f9fa;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            color: #7f8c8d;
            min-width: 100px;
            text-align: center;
            height: fit-content;
        }

        .award-content {
            flex: 1;
        }

        .award-title {
            font-size: 1.1rem;
            font-weight: 500;
            color: #2c3e50;
            margin: 0 0 8px;
        }

        .award-description {
            font-size: 0.95rem;
            color: #7f8c8d;
            line-height: 1.5;
        }

        /* ===== 科研经历部分 ===== */
        .project-item {
            background: white;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            overflow: hidden;
            margin-bottom: 25px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-left: 4px solid #ecf0f1;
        }

        .project-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(52, 152, 219, 0.15);
        }

        .project-header {
            display: flex;
            align-items: flex-start;
            padding: 22px 25px;
            border-bottom: 1px solid #f0f4f8;
            flex-wrap: wrap;
            gap: 15px;
        }

        .project-time {
            background: #f8f9fa;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            color: #7f8c8d;
            min-width: 170px;
            text-align: center;
        }

        .project-title-container {
            flex: 1;
            min-width: 250px;
        }

        .project-title {
            margin: 0 0 5px;
            font-size: 1.35rem;
            font-weight: 600;
            color: #2c3e50;
        }

        .project-subtitle {
            display: block;
            font-size: 1.05rem;
            color: #3498db;
            font-weight: 500;
        }

        .project-tag {
            background: #e8f4fc;
            color: #3498db;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.5px;
        }

        .project-details {
            padding: 22px 25px;
            background: #f9fbfd;
        }

        .project-advisor {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            font-size: 0.95rem;
            color: #7f8c8d;
        }

        .project-advisor i {
            margin-right: 10px;
            color: #3498db;
        }

        .project-list {
            padding: 0;
            margin: 0 0 20px;
            list-style: none;
        }

        .project-list li {
            position: relative;
            padding-left: 25px;
            margin-bottom: 12px;
            line-height: 1.7;
            color: #34495e;
        }

        .project-list li:before {
            content: '•';
            position: absolute;
            left: 0;
            color: #3498db;
            font-weight: bold;
        }

        .project-badge {
            display: inline-block;
            background: #e8f4fc;
            color: #3498db;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            margin-right: 10px;
            margin-bottom: 5px;
        }

        /* ===== 响应式设计 ===== */
        @media (max-width: 768px) {
            .award-item {
                flex-direction: column;
            }
            
            .award-time {
                align-self: flex-start;
            }
            
            .project-header {
                flex-direction: column;
                gap: 12px;
            }
            
            .project-time {
                align-self: flex-start;
            }
        }

        @media (max-width: 480px) {
            .content-card, .project-item {
                padding: 25px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="page-container">
        <!-- 主标题 -->
        <h2 class="section-title">AWARDS & RESEARCH</h2>
        
        <!-- 奖项部分 -->
        <div class="content-card">
            <div class="category-container">
                <div class="category-header">
                    <h3>COMPETITIONS</h3>
                </div>
                <ul class="award-list">
                    <li class="award-item">
                        <span class="award-time">2021</span>
                        <div class="award-content">
                            <div class="award-title">Provincial First Prize of the National College Students' Mathematical Modeling Competition (National Competition)</div>
                        </div>
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
                        <div class="award-content">
                            <div class="award-title">New Scenery Special Scholarship of Shandong University</div>
                            <div class="award-description">One of the university's highest honors and scholarships</div>
                        </div>
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
                        <div class="award-content">
                            <div class="award-title">Excellent Individual of Innovation and Entrepreneurship of Shandong University</div>
                            <div class="award-description">Annual award rate &lt; 5%</div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
        
        <!-- 科研经历部分 -->
        <h2 class="section-title">RESEARCH EXPERIENCE</h2>
        
        <!-- 牛津导师制项目 -->
        <div class="project-item">
            <div class="project-header">
                <span class="project-time">Sep 2021 - Dec 2021</span>
                <div class="project-title-container">
                    <h3 class="project-title">Oxford Online Tutorial Project</h3>
                    <span class="project-subtitle">Mentored Research</span>
                </div>
                <div class="project-tag">Computer Vision</div>
            </div>
            
            <div class="project-details">
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
        </div>
        
        <!-- STEM跨学科项目 -->
        <div class="project-item">
            <div class="project-header">
                <span class="project-time">Dec 2021 - Dec 2022</span>
                <div class="project-title-container">
                    <h3 class="project-title">Oxford STEM Summer School</h3>
                    <span class="project-subtitle">Interdisciplinary Program</span>
                </div>
                <div class="project-tag">Materials Science</div>
            </div>
            
            <div class="project-details">
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
</body>
</html>