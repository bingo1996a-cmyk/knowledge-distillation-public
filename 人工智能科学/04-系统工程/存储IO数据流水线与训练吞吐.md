---
title: 存储、I/O、数据管线与训练吞吐
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 存储、I/O、数据管线与训练吞吐

## 基本思想
训练吞吐不只取决于模型算得多快，还取决于数据能否稳定、连续地送到设备上。许多系统在 GPU 利用率不高时，根因不是模型结构，而是数据预处理、解码、缓存、网络文件系统或对象存储成为瓶颈。

## 训练吞吐链路
- 数据读取 -> 解码/预处理 -> 批处理组装 -> 传输到设备 -> 前向/反向计算。
- 链路中任意一环过慢，都会导致设备空转。

## 常见瓶颈
- 小文件过多导致元数据访问开销大。
- 远程存储带宽不足或抖动大。
- CPU 预处理、压缩解码或数据增强跟不上 GPU 速度。

## 工程关注点
- 分层缓存、数据分片、预取和异步加载。
- 对象存储、并行文件系统和本地 NVMe 的角色分工。

## 与本库其他页面的关系
- [跨数据中心训练、故障域与检查点策略](./cross-datacenter-training-fault-domains-and-checkpoint-strategy.md)
