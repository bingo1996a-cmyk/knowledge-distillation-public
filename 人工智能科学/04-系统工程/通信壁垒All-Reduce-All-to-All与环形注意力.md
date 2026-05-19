---
title: 通信墙：All-Reduce、All-to-All 与 Ring Attention
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 通信墙：All-Reduce、All-to-All 与 Ring Attention

## 基本思想

并行训练和大规模推理并不会因为设备增多就自动线性加速。常见情况是：计算可以并行，但通信跟不上，最终形成“通信墙”。理解通信墙，就是理解哪些数据必须交换、交换频率如何、交换发生在什么拓扑上、是否存在可以减少交换的算法重写。

## 三类典型通信

### 1. All-Reduce

用于梯度聚合、参数同步等场景。所有设备都贡献一部分结果，再让每个设备都拿到聚合结果。数据并行最典型的瓶颈常在这里。

### 2. All-to-All

用于专家并行（Mixture of Experts, MoE）等场景。每个设备都要把一部分 token 或激活发送给其他设备。它对网络负载更不规则，更容易形成热点和不均衡。

### 3. Ring Attention

是一类为长上下文或分块注意力而设计的分布式注意力计算思路。它试图把注意力计算按设备间环形流动展开，从而缓解一次性全量交换压力。

## 为什么它们重要

训练速度可粗略看成：

$$
T_{\text{step}} \approx T_{\text{compute}} + T_{\text{communication}} + T_{\text{overhead}}.
$$

当模型很大或并行规模很高时，$T_{\text{communication}}$ 往往先成为主项。此时继续堆设备，收益会迅速下降。

## 工程关注点

- 算子与通信能否重叠；
- 梯度、激活和路由张量是否能压缩；
- 分片方式是否贴合拓扑；
- 通信是否被长尾节点拖慢；
- 推理服务中连续批处理（continuous batching）是否放大缓存交换开销。

## 常见误区

- 把理论并行度直接等同于实际加速比；
- 只优化算子内核，不优化通信调度；
- 忽视 All-to-All 在 MoE 系统中的主导成本；
- 在高延迟网络上生搬硬套长上下文并行方案。

## 联读

- [集群网络、NVLink、InfiniBand 与拓扑设计](./cluster-networking-nvlink-infiniband-and-topology-design.md)
- [服务化：KV 缓存、推测解码与连续批处理](./serving-kv-cache-speculative-decoding-and-continuous-batching.md)
