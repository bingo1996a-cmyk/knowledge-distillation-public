---
title: 机器学习、深度学习、强化学习与大模型的算法覆盖图
layer: 90-appendices
tags:
  - evaluation
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 机器学习、深度学习、强化学习与大模型的算法覆盖图

## 1. 这页解决什么问题

用户在算法清单中已经列出大量关键方法，但若要形成系统知识库，仍需补一张“覆盖图”，说明哪些栏目已覆盖、哪些栏目的名字虽未提出但实际不可缺。

## 2. 你原始清单之外，最应该加入的栏目

### 2.1 统计学习与经典机器学习

- SVM
- kNN
- 决策树 / 随机森林 / GBDT / XGBoost
- Gaussian Process
- HMM / CRF / 图模型
- EM 算法
- 异常检测与密度估计
- 排序学习与因果学习

### 2.2 深度学习基础机制

- backpropagation
- 参数初始化
- normalization
- residual connection
- attention
- optimizer family
- learning rate scheduler
- regularization / calibration / uncertainty

### 2.3 生成模型

- VAE
- diffusion model
- normalizing flow
- autoregressive model
- energy-based model

### 2.4 强化学习

- bandit
- Monte Carlo
- eligibility traces / TD(\lambda)
- expected SARSA
- distributional RL
- hierarchical RL
- imitation learning
- inverse RL
- POMDP
- RLHF / RLAIF / process supervision

### 2.5 大模型技术

- tokenization
- MoE
- retrieval-augmented generation
- tool use / computer use
- verifier / search / deliberate inference
- quantization / distillation / serving
- agent runtime governance

## 3. 当前知识库中已补入的核心覆盖

- 统计决策理论、风险最小化与贝叶斯学习；
- 深度学习中的损失、激活、反向传播与优化；
- DP / TD / SARSA / Q-learning / DQN / actor-critic / PPO 系列；
- classical ML、deep network family、generative model family；
- 大模型训练—推理—对齐—评测全栈。

## 4. 建议使用方式

把这页当成索引页，不当成正文页。若继续扩库，优先补尚未单列但已经被识别为“必需栏目”的条目。
