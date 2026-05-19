---
title: 模型体系入口页（V37）
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 模型体系入口页（V37）

## 定位

本目录按"模型家族与算法谱系"组织，而不是按年份或公司组织。覆盖生成模型、语言模型、强化学习、世界模型、经典机器学习等主要模型家族。

## 推荐入口

### 总览
- [人工智能模型体系概览](./overview-of-ai-model-families.md)
- [生成式模型总览：GAN、VAE、Diffusion 与自回归](./generative-model-families-gans-vaes-diffusion-and-autoregressive-models.md)

### 生成式与多模态主线
- [扩散模型与 score-based 生成](./diffusion-models-and-score-based-generation.md)
- [扩散 Transformer、DiT 与流匹配](./diffusion-transformers-dit-and-flow-matching.md)
- [视频生成、世界模型与物理一致性](./video-generation-world-models-and-physics-consistency.md)
- [3D 生成、重建与神经渲染](./3d-generation-reconstruction-and-neural-rendering.md)
- [任意对任意多模态架构](./any-to-any-multimodal-architectures.md)
- [语音—语言与流式音频基础模型](./speech-language-and-streaming-audio-foundation-models.md)

### 语言模型与大模型
- [Transformer、GPT、MoE 与检索增强模型](./transformer-gpt-moe-and-retrieval-augmented-models.md)
- [现代 Transformer 变体：线性注意力、长上下文与状态空间模型](./modern-transformer-variants-linear-attention-long-context-and-state-space-models.md)
- [推理型语言模型、验证器、搜索与自适应计算](./reasoning-language-models-verifiers-search-and-adaptive-compute.md)

### 强化学习与序列决策
- [值函数强化学习：DP、TD、SARSA、Q-learning、DQN 与 Double DQN](./value-based-reinforcement-learning-dp-td-sarsa-q-learning-dqn-and-double-dqn.md)
- [策略梯度、Actor-Critic、TRPO、PPO 与优势估计](./policy-gradient-actor-critic-trpo-ppo-and-advantage-estimation.md)
- [连续控制：DDPG、TD3、SAC 与离策略 Actor-Critic](./continuous-control-ddpg-td3-sac-and-off-policy-actor-critic.md)
- [风险敏感、CVaR、熵正则化与鲁棒强化学习](./risk-sensitive-cvar-entropy-regularized-and-robust-rl.md)

### 世界模型与具身方向
- [世界模型](./world-models.md)
- [交互式智能体与持续世界建模](./interactive-agents-and-continual-world-modeling.md)
- [视觉—语言—动作模型（Vision-Language-Action, VLA）](./vision-language-action-models.md)

### 经典机器学习
- [神经网络结构原理](./neural-architecture-principles-mlp-cnn-rnn-lstm-gru-and-residual-learning.md)
- [经典统计学习模型：SVM、树模型、集成、高斯过程与进化方法](./classical-statistical-learning-models-svm-trees-ensembles-gaussian-processes-and-evolutionary-methods.md)
- [图神经网络](./graph-neural-networks.md)
- [机器学习模型族：核方法、树模型、集成学习与神经模型](./machine-learning-models-kernel-methods-tree-ensembles-and-neural-models.md)

## V37 说明
- V37.1 完成了重定向页清理：统一了 4 个旧版重定向页的格式，修复了 2 组循环引用（OPE 互指和离策略修正互指），均已指向相关内容页。
- V36 对 03 层进行了全库去重检查，识别出部分 RL 算法文件的重叠（已在 V36.6 微调）。

## 联读
- [人工智能模型家族总览](./overview-of-ai-model-families.md)
- [范式入口页](../02-paradigms/README.md)
- [系统工程入口页](../04-systems-engineering/README.md)

## 参考文献
[1] Goodfellow, I., Bengio, Y., & Courville, A. *Deep Learning*. MIT Press, 2016.
[2] Bishop, C. M. *Pattern Recognition and Machine Learning*. Springer, 2006.
