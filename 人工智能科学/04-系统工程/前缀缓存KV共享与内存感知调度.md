---
title: 前缀缓存、KV 共享与内存感知调度
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 前缀缓存、KV 共享与内存感知调度

## 合并说明

本页在 V32 中改为主题收束页，不再与 KV 缓存总论平行展开。主文件如下：

- [KV 缓存：分页、前缀共享与内存分层](./kv-cache-paging-prefix-sharing-and-memory-tiering.md)
- [服务化：KV 缓存、推测解码与连续批处理](./serving-kv-cache-speculative-decoding-and-continuous-batching.md)

本页保留的重点是提醒读者：
- 前缀缓存不是独立优化岛，而是 KV 缓存体系的一部分；
- KV 共享是否成立取决于请求相似性、缓存一致性和调度策略；
- 内存感知调度必须与批处理、租户隔离和时延目标共同设计。
