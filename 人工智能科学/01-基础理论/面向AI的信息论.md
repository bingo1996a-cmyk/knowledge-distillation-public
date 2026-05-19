---
title: 人工智能中的信息论
layer: 01-foundations
tags:
  - ai-theory
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能中的信息论

## 定位

信息论为人工智能提供了关于不确定性、编码、压缩、预测和表征的统一语言。很多看似分散的对象——交叉熵损失、语言建模、最小描述长度、自监督学习、信息瓶颈——都可以在信息论框架下被重新理解。

## 一、三个基本问题

1. 信息量如何度量；
2. 数据如何被压缩、传输与恢复；
3. 学习系统如何在保留有用信息的同时丢弃冗余信息。

## 二、核心量

### 1. 熵

离散随机变量 \(X\) 的熵定义为：

$$
H(X)=-\sum_x p(x)\log p(x)
$$

它刻画平均不确定性。

### 2. 条件熵

$$
H(Y\mid X)= -\sum_{x,y} p(x,y)\log p(y\mid x)
$$

它反映在知道 \(X\) 后，\(Y\) 还剩多少不确定性。

### 3. 互信息

$$
I(X;Y)=H(X)-H(X\mid Y)
$$

互信息衡量两个变量共享多少信息，是理解表征质量、跨模态对齐与检索增强的重要工具。

### 4. KL 散度与交叉熵

KL 散度：

$$
D_{\mathrm{KL}}(p\|q)=\sum_x p(x)\log\frac{p(x)}{q(x)}
$$

交叉熵：

$$
H(p,q)=H(p)+D_{\mathrm{KL}}(p\|q)
$$

这解释了为什么最大似然训练等价于最小化交叉熵。

## 三、信息论如何进入 AI

### 1. 监督学习与语言建模

分类中的交叉熵损失、本质上是在逼近真实标签分布与模型分布之间的距离。语言模型的 next-token prediction 也可以理解为压缩与预测的统一。

### 2. 表征学习

好表征既要保留对任务有用的信息，又要丢弃噪声与无关因素。信息瓶颈（information bottleneck）正是这一思想的经典表达。

### 3. 检索、通信与多智能体系统

在多智能体通信中，带宽有限、消息冗余和信息增益都是信息论问题；在 RAG 中，文档选择可以被视为最大化与目标输出相关的互信息。

## 四、基本思想层面的三条线

### 1. 预测就是压缩

如果一个模型能高效预测数据，它往往也能高效压缩数据。最小描述长度（MDL）把模型选择解释为“选择最短的可解释编码”。

### 2. 学习就是保留有效信息

学习不是保留一切，而是形成任务相关压缩。这个观点对自监督学习、对比学习和表征去噪非常关键。

### 3. 通信与推理都受信息预算约束

token、上下文窗口、带宽、实验采样次数，本质上都可以看成信息预算。

## 五、常见误区

- 把互信息当作“越大越好”的单指标；
- 忽略估计互信息在高维空间中的困难；
- 只把信息论当作损失函数背景，不把它当作表征与系统设计的语言。

## 联读

- [表征学习、自监督学习与迁移](./representation-learning-self-supervision-and-transfer.md)
- [自监督学习：对比学习、掩码建模与迁移接口](../03-model-families/self-supervised-learning-contrastive-learning-and-masked-modeling.md)
- [大语言模型：预训练、尺度扩展、后训练与测试时计算](../03-model-families/large-language-model-pretraining-scaling-post-training-and-test-time-compute.md)

## 参考文献

1. Thomas M. Cover, Joy A. Thomas. Elements of Information Theory. 2nd ed. Wiley-Interscience, 2006.
2. Shannon C E. A mathematical theory of communication. The Bell System Technical Journal, 1948, 27(3): 379–423.
3. MacKay D J C. Information Theory, Inference, and Learning Algorithms. Cambridge University Press, 2003.
