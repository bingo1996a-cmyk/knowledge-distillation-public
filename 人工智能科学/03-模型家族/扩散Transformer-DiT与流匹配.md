---
title: 扩散 Transformer（Diffusion Transformer, DiT）与流匹配（Flow Matching）
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 扩散 Transformer（Diffusion Transformer, DiT）与流匹配（Flow Matching）

## 基本思想
扩散 Transformer 的核心变化，是把传统扩散模型里偏卷积的去噪器，换成更容易扩展的大规模 Transformer 主干。流匹配进一步把生成过程看成连续时间上的分布搬运问题，因此更接近常微分方程与最优传输视角。

## 从 U-Net 到 DiT
- U-Net 更强调局部空间归纳偏置，DiT 更强调 token 化表示与统一主干。
- 图像、视频或潜变量一旦被切成 patch/token，就更容易复用 Transformer 基础设施。
- 代价是局部先验减弱，显存与注意力复杂度更高。

## 流匹配的理解
- 它学习的是速度场（velocity field），让简单分布连续演化为目标分布。
- 相比离散去噪链，它更强调连续时间生成、少步采样和路径解释。

## 工程关注点
- token 空间如何定义：像素、patch、VAE 潜变量还是视频 token。
- 条件如何注入，长视频和多模态输出如何控制服务成本。

## 与本库其他页面的关系
- [扩散模型与基于分数的生成](./diffusion-models-and-score-based-generation.md)
- [任意对任意多模态架构](./any-to-any-multimodal-architectures.md)
