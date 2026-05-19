---
title: Serving、KV Cache、推测解码与连续批处理
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# Serving、KV Cache、推测解码与连续批处理

## 页面关系

本页是 04 层推理与服务主题的**综合概述页**，同时覆盖四个核心机制的基础概念。同主题各页的分工如下：
- [Serving 调度器、缓存布局与多租户推理](./serving-schedulers-cache-placement-and-multi-tenant-inference.md) — **专题深化**：请求调度策略、KV cache 治理、多租户隔离
- [KV Cache 分页、前缀共享与内存分层](./kv-cache-paging-prefix-sharing-and-memory-tiering.md) — **专题深化**：KV Cache 作为系统资源对象的组织方式
- [推测解码、草稿模型与吞吐—时延权衡](./speculative-decoding-draft-models-and-throughput-latency-tradeoffs.md) — **专题深化**：推测解码的工程权衡与部署决策

建议阅读顺序：综合概述 → 按需选读专题页。

## 1. 这一页解决什么问题

大模型部署的关键瓶颈并不只在模型参数量，还在推理系统是否高效。真实服务中最常见的问题是：

- 首 token 延迟高；
- 吞吐不足；
- 上下文越长越慢；
- 多用户并发时显存与带宽压力激增。

这页聚焦四个核心机制：

1. serving 架构
2. KV cache
3. speculative decoding
4. continuous batching

## 2. KV cache 的基本思想

Transformer 在自回归生成中，每一步都需要访问此前 token 的键值对（key-value pairs）。若每次都从头重新计算，成本极高。

KV cache 的作用是：

- 把过去 token 的 key/value 缓存在显存中；
- 新 token 只需计算新增部分；
- 显著降低重复计算。

但 KV cache 也带来新问题：

- 上下文越长，占用越大；
- 多会话时显存迅速膨胀；
- cache 管理本身成为系统设计问题。

## 3. prefill 与 decode

推理通常分为两阶段：

- **prefill**：处理已有上下文，构建初始 KV cache；
- **decode**：逐 token 生成。

二者瓶颈不同：

- prefill 更吃算力；
- decode 更吃内存带宽与调度效率。

因此优化手段也不同。

## 4. speculative decoding

推测解码（speculative decoding）的基本思想是：

- 用一个更小、更快的草稿模型先提出若干 token；
- 用大模型并行验证这些 token；
- 若通过，则一次性接受多个 token。

这样可以减少“大模型逐 token 串行生成”的开销。

优势：

- 降低平均每 token 成本；
- 在高质量 draft model 下显著加速。

限制：

- 草稿模型与主模型差距过大时接受率低；
- 系统实现复杂；
- 不同任务收益差异很大。

## 5. continuous batching

传统 batching 往往等待一整批请求凑齐再统一处理。continuous batching 则让请求动态进入、动态离开 batch。

收益：

- 提升 GPU 利用率；
- 减少空转；
- 更适合长短请求混合场景。

难点：

- 调度复杂；
- cache 管理更难；
- 不同请求长度差异会造成碎片化问题。

## 6. 真实系统中的关键权衡

系统设计通常在以下维度折中：

- latency vs throughput
- 长上下文能力 vs 显存成本
- 多租户公平性 vs 单用户峰值性能
- 量化压缩 vs 精度下降
- 连续批处理收益 vs 调度复杂度

## 7. 与其他页面的关系

建议联动阅读：

- `tokenization-distillation-quantization-and-inference-optimization.md`
- `large-model-training-inference-alignment-and-evaluation-stack.md`
- `modern-transformer-variants-linear-attention-long-context-and-state-space-models.md`

## 参考文献

以下条目按 GB/T 7714—2025 数字顺序体例做最小化整理；因原文未提供完整元数据，缺失字段不补造。

[1] Leviathan, Y. et al. *Fast Inference from Transformers via Speculative Decoding*. ICML, 2023.
[2] Dao, T. et al. *FlashAttention*. NeurIPS, 2022.
[3] Kwon, W. et al. *Efficient Memory Management for Large Language Model Serving with PagedAttention*. SOSP, 2023.
