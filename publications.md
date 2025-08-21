---
layout: page
permalink: /publications/index.html
title: Publications
---


<style>
        /* ===== 全局样式 ===== */
        body {
            margin: 0;
            padding: 0;
            background-color: #f5f7fa;
            font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
            color: #2c3e50;
        }

        .page-container {
            max-width: 900px;
            margin: 0 auto;
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

        .pub-header {
            position: relative;
            padding-bottom: 12px;
            margin-bottom: 20px;
        }

        .pub-header h2 {
            font-size: 1.5rem;
            font-weight: 600;
            color: #2c3e50;
            margin: 0;
        }

        .pub-header:after {
            content: '';
            position: absolute;
            left: 0;
            bottom: 0;
            width: 50px;
            height: 2px;
            background: linear-gradient(to right, #3498db, #9b59b6);
            border-radius: 2px;
        }

        /* ===== 出版物项目 ===== */
        .pub-item {
            padding: 22px 0;
            border-bottom: 1px dashed #eee;
            position: relative;
        }

        .pub-item:last-child {
            border-bottom: none;
        }

        .pub-item:before {
            content: '';
            position: absolute;
            left: -15px;
            top: 28px;
            width: 8px;
            height: 8px;
            background: #3498db;
            border-radius: 50%;
        }

        .pub-title {
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 10px;
            line-height: 1.4;
        }

        .pub-title a {
            color: #2c3e50;
            text-decoration: none;
            transition: color 0.3s;
        }

        .pub-title a:hover {
            color: #3498db;
            text-decoration: underline;
        }

        .pub-authors {
            color: #7f8c8d;
            font-size: 0.95rem;
            margin-bottom: 8px;
            line-height: 1.5;
        }

        .pub-venue {
            font-size: 0.95rem;
            color: #34495e;
            margin-bottom: 5px;
            font-style: italic;
        }

        .pub-status {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            margin-top: 10px;
        }

        .status-submitted {
            background-color: #e8f4fc;
            color: #3498db;
        }

        .status-review {
            background-color: #fff8e1;
            color: #ff9800;
        }

        .status-published {
            background-color: #e8f5e9;
            color: #4caf50;
        }

        .pub-tag {
            display: inline-block;
            background: #f0f4f8;
            color: #2c3e50;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            margin-right: 10px;
            margin-top: 10px;
        }

        .pub-links {
            margin-top: 12px;
        }

        .pub-link {
            display: inline-flex;
            align-items: center;
            margin-right: 20px;
            text-decoration: none;
            font-size: 0.9rem;
            color: #3498db;
            transition: color 0.3s;
        }

        .pub-link:hover {
            color: #2980b9;
        }

        .pub-link i {
            margin-right: 6px;
            font-size: 0.9rem;
        }

        /* ===== 特殊高亮 ===== */
        .author-highlight {
            font-weight: 600;
            color: #3498db;
        }

        .highlight-box {
            background: linear-gradient(120deg, rgba(52, 152, 219, 0.1) 0%, transparent 100%);
            border-left: 3px solid #3498db;
            padding: 15px 20px;
            border-radius: 0 6px 6px 0;
            margin: 20px 0;
            font-weight: 500;
            color: #2c3e50;
            font-size: 1.05rem;
        }

        /* ===== 响应式设计 ===== */
        @media (max-width: 768px) {
            .content-card {
                padding: 25px;
            }
            
            .section-title {
                margin: 35px 0 20px;
            }
            
            .pub-header h2 {
                font-size: 1.35rem;
            }
            
            .pub-title {
                font-size: 1.05rem;
            }
        }

        @media (max-width: 480px) {
            .content-card {
                padding: 20px;
            }
            
            .section-title:after {
                width: 50px;
            }
            
            .pub-links {
                display: flex;
                flex-wrap: wrap;
            }
            
            .pub-link {
                margin-right: 15px;
                margin-bottom: 8px;
            }
        }
    </style>
<body>
    <div class="page-container">
        <!-- 主标题 -->
        <h2 class="section-title">PUBLICATIONS</h2>
        
        <!-- 工作论文部分 -->
        <div class="content-card">
            <div class="pub-header">
                <h2>Working Paper</h2>
            </div>
            
            <div class="highlight-box">
                Recent works submitted to top-tier conferences in AI and multimodal research.
            </div>
            
            <!-- 论文1 -->
            <div class="pub-item">
                <h3 class="pub-title">
                    <a href="https://arxiv.org/pdf/2508.06869">VSI: Visual Subtitle Integration for Keyframe Selection to enhance Long Video Understanding</a>
                </h3>
                <div class="pub-authors">
                    <span class="author-highlight">Jianxiang He</span>, Shaoguang Wang, Weiyu Guo, Meisheng Hong, Jungang Li, Yijie Xu, Ziyang Chen, Hui Xiong
                </div>
                <div class="pub-venue">Submitted to AAAI 2026</div>
                <div class="pub-status status-submitted">Submitted</div>
                <div class="pub-tag">Video Understanding</div>
                <div class="pub-tag">Keyframe Selection</div>
                <div class="pub-links">
                    <a href="#" class="pub-link">
                        <i class="fas fa-file-pdf"></i> PDF
                    </a>
                    <a href="#" class="pub-link">
                        <i class="fas fa-code"></i> Code
                    </a>
                </div>
            </div>
            
            <!-- 论文2 -->
            <div class="pub-item">
                <h3 class="pub-title">
                    <a href="https://arxiv.org/pdf/2508.03337">Less is More: Token-Efficient Video-QA via Adaptive Frame-Pruning and Semantic Graph Integration</a>
                </h3>
                <div class="pub-authors">
                    Shaoguang Wang, <span class="author-highlight">Shaoguang Wang, Jianxiang He, Yijie Xu, Ziyang Chen, Weiyu Guo, Hui Xiong
                </div>
                <div class="pub-venue">Submitted to AAAI 2026</div>
                <div class="pub-status status-submitted">Submitted</div>
                <div class="pub-tag">Video Summarization</div>
                <div class="pub-tag">Efficiency Optimization</div>
                <div class="pub-links">
                    <a href="#" class="pub-link">
                        <i class="fas fa-file-pdf"></i> PDF
                    </a>
                    <a href="#" class="pub-link">
                        <i class="fas fa-code"></i> Code
                    </a>
                </div>
            </div>
        </div>
        
        <!-- 会议论文部分 -->
        <div class="content-card">
            <div class="pub-header">
                <h2>Conference Paper</h2>
            </div>
            
            <div class="highlight-box">
                Published and under review papers in top AI conferences and journals.
            </div>
            
            <!-- 论文1 -->
            <div class="pub-item">
                <h3 class="pub-title">
                    <a href="https://openreview.net/pdf?id=y5X44PzafF">Distribution Preference Optimization: A Fine-grained Perspective for LLM Unlearning</a>
                </h3>
                <div class="pub-authors">
                    Kai Qin, Jiaqi Wu, <span class="author-highlight">Jianxiang He</span>, Haoyuan Sun, Yifei Zhao, Bin Liang, Yongzhe Chang, Tiantian Zhang, Houde Liu
                </div>
                <div class="pub-venue">Under Review</div>
                <div class="pub-status status-review">Under Review</div>
                <div class="pub-tag">LLM Unlearning</div>
                <div class="pub-tag">Fine-grained Control</div>
                <div class="pub-links">
                    <a href="https://openreview.net/pdf?id=y5X44PzafF" class="pub-link">
                        <i class="fas fa-file-pdf"></i> PDF
                    </a>
                    <a href="#" class="pub-link">
                        <i class="fas fa-code"></i> Code
                    </a>
                </div>
            </div>
            
            <!-- 论文2 -->
            <div class="pub-item">
                <h3 class="pub-title">
                    <a href="https://arxiv.org/abs/2503.13139">Logic-in-Frames: Dynamic Keyframe Search via Visual Semantic-Logical Verification for Long Video Understanding</a>
                </h3>
                <div class="pub-authors">
                    Weiyu Guo, Ziyang Chen, Shaoguang Wang, <span class="author-highlight">Jianxiang He</span>, Yijie Xu, Jinhui Ye, Ying Sun, Hui Xiong
                </div>
                <div class="pub-venue">arXiv preprint</div>
                <div class="pub-tag">Long Video Analysis</div>
                <div class="pub-tag">Multimodal Fusion</div>
                <div class="pub-links">
                    <a href="https://arxiv.org/abs/2503.13139" class="pub-link">
                        <i class="fas fa-file-pdf"></i> PDF
                    </a>
                    <a href="#" class="pub-link">
                        <i class="fas fa-code"></i> Code
                    </a>
                </div>
            </div>
            
            <!-- 论文3 -->
            <div class="pub-item">
                <h3 class="pub-title">
                    <a href="https://arxiv.org/abs/2412.11936">A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method & Challenges</a>
                </h3>
                <div class="pub-authors">
                    Yibo Yan, Jiamin Su, <span class="author-highlight">Jianxiang He</span>, Fangteng Fu, Xu Zheng, Yuanhuiyi Lyu, Kun Wang, Shen Wang, Qingsong Wen, Xuming Hu
                </div>
                <div class="pub-venue">The 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025)</div>
                <div class="pub-status status-published">Published</div>
                <div class="pub-tag">Survey Paper</div>
                <div class="pub-tag">Mathematical Reasoning</div>
                <div class="pub-links">
                    <a href="https://arxiv.org/abs/2412.11936" class="pub-link">
                        <i class="fas fa-file-pdf"></i> PDF
                    </a>
                    <a href="#" class="pub-link">
                        <i class="fas fa-code"></i> Code
                    </a>
                </div>
            </div>
            
            <!-- 论文4 -->
            <div class="pub-item">
                <h3 class="pub-title">
                    <a href="https://arxiv.org/abs/2502.16861">A Survey of fMRI to Image Reconstruction</a>
                </h3>
                <div class="pub-authors">
                    Weiyu Guo, Guoying Sun, <span class="author-highlight">JianXiang He</span>, Tong Shao, Shaoguang Wang, Ziyang Chen, Meisheng Hong, Ying Sun, Hui Xiong~
                </div>
                <div class="pub-venue">arXiv preprint</div>
                <div class="pub-tag">Survey Paper</div>
                <div class="pub-tag">fMRI Reconstruction</div>
                <div class="pub-links">
                    <a href="https://arxiv.org/abs/2502.16861" class="pub-link">
                        <i class="fas fa-file-pdf"></i> PDF
                    </a>
                    <a href="#" class="pub-link">
                        <i class="fas fa-code"></i> Code
                    </a>
                </div>
            </div>
            
            <!-- 论文5 -->
            <div class="pub-item">
                <h3 class="pub-title">
                    <a href="https://ieeexplore.ieee.org/abstract/document/10012028/">The development of spiking neural network: A review</a>
                </h3>
                <div class="pub-authors">
                    <span class="author-highlight">Jianxiang He</span>, Yanzi Li, Yingtian Liu, Jiyang Chen, Chaoqun Wang, Rui Song, Yibin Li~
                </div>
                <div class="pub-venue">2022 IEEE International Conference on Robotics and Biomimetics (ROBIO 2022)</div>
                <div class="pub-status status-published">Published</div>
                <div class="pub-tag">Review Paper</div>
                <div class="pub-tag">Spiking Neural Networks</div>
                <div class="pub-links">
                    <a href="https://ieeexplore.ieee.org/abstract/document/10012028/" class="pub-link">
                        <i class="fas fa-file-pdf"></i> PDF
                    </a>
                    <a href="#" class="pub-link">
                        <i class="fas fa-code"></i> Code
                    </a>
                </div>
            </div>
        </div>
    </div>
</body>

<!-- ## Working Paper

- [Beyond Visual Semantics: Dynamic Keyframe Search via Multimodal Syntactic Alignmen]<br>**Jianxiang He**, Shaoguang Wang, Jungang Li, Meisheng Hong<br>Submitted to **AAAI 2025**.<br>
- [Visual-Clustering: Efficient Keyframe Reduction and Semantic Graph Construction for Enhanced Video Understanding]<br>Shaoguang Wang, **Jianxiang He**, Jungang Li, Meisheng Hong<br>Submitted to **AAAI 2025**.<br>

---

## Conference Paper

- [Distribution Preference Optimization: A Fine-grained Perspective for LLM Unlearning](https://openreview.net/pdf?id=y5X44PzafF)<br>Kai Qin, Jiaqi Wu, **Jianxiang He**, Haoyuan Sun, Yifei Zhao, Bin Liang, Yongzhe Chang, Tiantian Zhang, Houde Liu<br>Under Review<br>

- [Logic-in-Frames: Dynamic Keyframe Search via Visual Semantic-Logical Verification for Long Video Understanding](https://arxiv.org/abs/2503.13139)<br>Weiyu Guo, Ziyang Chen, Shaoguang Wang, **Jianxiang He**, Yijie Xu, Jinhui Ye, Ying Sun, Hui Xiong<br>arXiv<br>

- [A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method & Challenges](https://arxiv.org/abs/2412.11936)<br>Yibo Yan, Jiamin Su, **Jianxiang He**, Fangteng Fu, Xu Zheng, Yuanhuiyi Lyu, Kun Wang, Shen Wang, Qingsong Wen, Xuming Hu<br>The 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025)<br>

- [A Survey of fMRI to Image Reconstruction](https://arxiv.org/abs/2502.16861)<br>Weiyu Guo, Guoying Sun, **JianXiang He**, Tong Shao, Shaoguang Wang, Ziyang Chen, Meisheng Hong, Ying Sun, Hui Xiong**~**<br>arXiv<br>

- [The development of spiking neural network: A review](https://ieeexplore.ieee.org/abstract/document/10012028/)<br>**Jianxiang He**, Yanzi Li, Yingtian Liu, Jiyang Chen, Chaoqun Wang, Rui Song, Yibin Li**~**<br>2022 IEEE International Conference on Robotics and Biomimetics (ROBIO 2022)<br> -->



<br>


---

<br>