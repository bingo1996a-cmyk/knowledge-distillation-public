---
title: 人工智能中的图论
layer: 01-foundations
tags:
  - ai-theory
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能中的图论

## 定位

图论为 AI 提供“对象—关系—结构”的表达语言。当问题不再只是独立样本分类，而是涉及实体关系、拓扑、约束传播、通信与依赖结构时，图论几乎不可避免。

## 一、为什么图重要

很多真实系统天然是图结构：

- 社交网络与知识图谱；
- 分子与材料结构；
- 道路、通信、供电、航天网络；
- 多智能体协同中的交互拓扑；
- 程序调用图与任务图。

## 二、基本对象

- 节点（vertex）：实体、状态、任务或对象；
- 边（edge）：关系、依赖、通信、相互作用；
- 邻接矩阵与拉普拉斯矩阵：图计算的代数基础；
- 子图、路径、连通分量、团、中心性：结构分析的常用概念。

## 三、AI 中最常见的三种用法

### 1. 结构表示

把世界表示成图，而不是平铺的表格或 token 序列。这是知识图谱、场景图、程序图的重要基础。

### 2. 关系推理

在图上做消息传递、邻域聚合、路径搜索与约束传播。图神经网络和神经符号系统都建立在这里。

### 3. 系统工程建模

任务图、工作流 DAG、planner-critic 图、agent communication graph 都是系统工程层的图模型。

## 四、基本思想

### 1. 图不是“多一维数据”，而是关系归纳偏置

一旦对象之间的关系本身携带信息，忽略拓扑就会丢掉问题结构。

### 2. 局部交互可以累积成全局行为

图上的消息传递体现了“局部规则—全局结构”的基本思想，这对多智能体协同、扩散过程和故障传播都很重要。

### 3. 图结构同时带来表达力与计算难度

图搜索、图匹配、子图同构等问题很快就会进入组合爆炸区域，因此图论既是表示理论，也是复杂性理论入口。

## 五、工程接口

- [图神经网络](../03-model-families/graph-neural-networks.md)
- [知识图谱与神经符号系统](../03-model-families/knowledge-graphs-and-neural-symbolic-systems.md)
- [scientific knowledge base、图记忆与可验证 agent 推理](../04-systems-engineering/scientific-knowledge-bases-graph-memory-and-verifiable-agent-reasoning.md)
- [多智能体系统](../04-systems-engineering/multi-agent-systems.md)
