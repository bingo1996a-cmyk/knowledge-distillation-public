---
title: 生成式模型总览：GAN、VAE、扩散模型与自回归模型
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 生成式模型总览：GAN、VAE、扩散模型与自回归模型

## 基本思想
生成式模型都在做同一件事：学习数据分布，然后从中采样出新样本。差异主要体现在如何表示分布、如何训练、如何采样。这一页给出总论，不承担各子方向细节展开。

## 四条主线
- 生成对抗网络（GAN）依赖生成器与判别器博弈，图像锐利，但训练不稳定。
- 变分自编码器（VAE）强调潜变量建模，概率解释清楚，潜空间友好。
- 扩散模型通过逐步加噪与去噪进行生成，训练稳定、质量高、条件控制强。
- 自回归模型按 token 顺序生成，适合统一文本、图像 token 和音频 token 序列建模。

## 选择标准
- 重视训练稳定性和条件生成时，扩散模型常更合适。
- 重视潜空间编辑与压缩表示时，VAE 更常见。
- 重视统一序列接口与多模态 token 生成时，自回归模型更自然。

## 联读

- [扩散模型与基于分数的生成](./diffusion-models-and-score-based-generation.md)
- [语音—语言与流式音频基础模型](./speech-language-and-streaming-audio-foundation-models.md)
- [扩散 Transformer（DiT）与流匹配](./diffusion-transformers-dit-and-flow-matching.md)

## 参考文献

[1] Goodfellow, I. et al. *Generative Adversarial Nets*. NeurIPS, 2014.
[2] Kingma, D. P. & Welling, M. *Auto-Encoding Variational Bayes*. ICLR, 2014.
[3] Ho, J., Jain, A., & Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS, 2020.
