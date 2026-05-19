---
title: Transformer 架构（Transformer）
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# Transformer 架构（Transformer）

## 页面关系

本页是 Transformer 的**入门级摘要页**，适合首次接触该架构的读者快速了解核心概念。详细的体系化讨论（包括 GPT 系列、MoE、检索增强、现代变体、长上下文等）请转至：

- [Transformer、GPT、MoE 与检索增强模型](./transformer-gpt-moe-and-retrieval-augmented-models.md) ← **主文件**
- [现代 Transformer 变体：线性注意力、长上下文与状态空间模型](./modern-transformer-variants-linear-attention-long-context-and-state-space-models.md)

## 定位

Transformer 是当前大模型时代最关键的通用架构之一。它用注意力机制替代传统序列模型中的递归主路径，使序列、图像、音频和多模态数据都可以在统一框架下处理。

## 一、基本思想

### 1. 自注意力

系统不再只依赖固定邻域或时间递归，而是动态决定“当前位置应关注哪些上下文”。

### 2. 表示与关系同时建模

Transformer 同时处理 token 自身表示与 token 之间关系，这是它在语言和多模态任务中成功的关键。

### 3. 并行计算友好

与 RNN 相比，Transformer 更利于大规模并行训练，因此特别适合 foundation model 时代的规模扩展。

## 二、关键组件

- embedding
- positional encoding
- multi-head attention
- feed-forward network
- residual connection
- normalization

## 三、为什么它重要

- 支撑大语言模型与多模态基础模型；
- 促成 in-context learning 与 test-time compute 扩展；
- 为检索增强、工具调用和 agentic system 提供统一表示底座。

## 联读

- [Transformer、GPT、MoE 与检索增强模型](./transformer-gpt-moe-and-retrieval-augmented-models.md)
- [大语言模型](./large-language-models.md)
- [现代 Transformer 变体：线性注意力、长上下文与状态空间模型](./modern-transformer-variants-linear-attention-long-context-and-state-space-models.md)
- [神经网络](./neural-networks.md)

## 参考文献

[1] Vaswani, A. et al. *Attention Is All You Need*. NeurIPS, 2017.
[2] Goodfellow, I., Bengio, Y., & Courville, A. *Deep Learning*. MIT Press, 2016.
