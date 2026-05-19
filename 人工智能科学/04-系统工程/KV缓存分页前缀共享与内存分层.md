---
title: KV Cache 分页、前缀共享与内存分层
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# KV Cache 分页、前缀共享与内存分层

## 页面关系

本页是 04 层推理与服务主题的**专题深化页**，聚焦 KV Cache 作为系统资源对象的组织方式——分页、前缀共享、内存分层。综合概述请转至：
- [Serving、KV Cache、推测解码与连续批处理](./serving-kv-cache-speculative-decoding-and-continuous-batching.md) — 综合概述

同主题其他专题页：
- [Serving 调度器、缓存布局与多租户推理](./serving-schedulers-cache-placement-and-multi-tenant-inference.md) — 侧重调度策略与多租户
- [推测解码、草稿模型与吞吐—时延权衡](./speculative-decoding-draft-models-and-throughput-latency-tradeoffs.md) — 侧重推测解码

## 1. 为什么这是核心工程问题

大模型推理成本中，KV Cache 往往是显存压力与吞吐约束的核心来源。随着上下文增长，多租户推理系统必须解决：

- Cache 怎么放；
- 哪些前缀可以共享；
- 显存不够时如何分页与分层；
- 怎样在吞吐与时延之间权衡。

## 2. KV Cache 的基本对象

在自注意力中，每个 token 会产生 key/value 表示并在后续解码中反复读取。上下文长度为 $L$、层数为 $N$ 时，缓存量随 $O(NL)$ 增长。

## 3. 分页（Paging）

分页思想是把 KV Cache 拆成固定大小块，而不是要求一段连续显存。这样可以：

- 降低碎片化；
- 提高动态批处理下的分配灵活性；
- 便于回收与复用。

## 4. 前缀共享

若多个请求拥有相同前缀，例如系统提示词或共同文档开头，则可共享前缀部分的 KV Cache。

优点：

- 节省显存；
- 降低重复计算；
- 提高多轮对话与模板化请求的吞吐。

风险：

- 前缀识别与命中策略复杂；
- cache 一致性与隔离问题；
- 多租户安全边界。

## 5. 内存分层

典型层级包括：

- GPU 高带宽显存（HBM）
- CPU 内存
- 更慢的二级存储或远程缓存

核心思想是“热数据留在近处，冷数据分层下沉”。

## 6. 系统级权衡

- 更激进的分页：分配灵活但调度开销上升；
- 更激进的前缀共享：节省计算但隔离和一致性更难；
- 更深的内存分层：显存压力下降但时延波动增大。

## 7. 与其他页面的关系

- `Serving、KV Cache、推测解码与连续批处理`
- `Serving 调度器、缓存布局与多租户推理`
- `Checkpointing、重计算与内存—计算权衡`

本页更聚焦 cache 作为“系统资源对象”的组织方式。
