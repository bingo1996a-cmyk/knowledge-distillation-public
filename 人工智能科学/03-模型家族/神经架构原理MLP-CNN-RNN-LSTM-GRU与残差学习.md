---
title: 神经网络结构原理：多层感知机、卷积神经网络、循环神经网络、长短期记忆网络、门控循环单元与残差学习
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 神经网络结构原理：多层感知机、卷积神经网络、循环神经网络、长短期记忆网络、门控循环单元与残差学习

## 1. 一个统一视角

这些网络结构看似不同，实则都在回答同一个问题：**怎样把任务先验和优化需求编码进函数类中**。

结构设计至少决定：

- 参数如何共享；
- 信息如何局部传播或全局传播；
- 记忆如何存储；
- 梯度如何传递；
- 深层网络怎样保持可训练性。

## 2. MLP：通用逼近与局限

MLP 的基本形式为：

$$
f(x)=W_L\sigma(\cdots\sigma(W_1x+b_1)\cdots)+b_L.
$$

它的理论价值在于通用逼近能力；其局限在于缺少对输入结构的先验。

## 3. CNN：卷积为何不是普通线性层

卷积不是简单矩阵乘法的替代写法，而是把空间局部性和平移等变性编码进网络。它相当于在参数层面约束可学习函数族，从而在样本有限时更容易泛化。

## 4. RNN：递归状态的本质

RNN 把序列历史压缩成状态 $h_t$。本质上，这是在学习一个状态空间模型的神经近似：

$$
h_t = \phi(h_{t-1},x_t),\qquad y_t = \psi(h_t).
$$

## 5. LSTM / GRU：门控为何重要

门控机制不是技巧堆叠，而是对信用分配问题的结构响应：

- 选择性写入；
- 选择性遗忘；
- 选择性读取。

这使得长依赖不必完全通过未受控的递归链传播。

## 6. 残差学习：更深网络为何更容易优化

残差连接的意义在于把一个难学的映射 $H(x)$ 改写为：

$$
H(x)=F(x)+x.
$$

若理想映射接近恒等映射，则学习残差 $F(x)$ 更容易。更深层的意义是：它为梯度提供了稳定的旁路。

## 7. 结构原理与现代模型的延伸关系

- Transformer 继承了残差、归一化与层级堆叠；
- GNN 继承了局部消息传播与共享参数思想；
- 大模型训练中的优化稳定性仍然受这些结构原理影响。

## 联读

- [深度网络家族：MLP、CNN、RNN、LSTM、GRU、AlexNet、VGG、ResNet 与 NAS](./deep-network-families-mlp-cnn-rnn-lstm-gru-alexnet-vgg-resnet-and-nas.md)
- [反向传播、损失函数、激活函数与梯度下降](../01-foundations/backpropagation-loss-functions-activation-functions-and-gradient-descent.md)
- [深度学习训练动力学、曲率、初始化与隐式偏差](../04-systems-engineering/deep-learning-training-dynamics-curvature-initialization-and-implicit-bias.md)

## 参考文献

[1] LeCun, Y., Bengio, Y., & Hinton, G. *Deep Learning*. Nature, 2015.
[2] He, K. et al. *Deep Residual Learning for Image Recognition*. CVPR, 2016.
[3] Hochreiter, S. & Schmidhuber, J. *Long Short-Term Memory*. Neural Computation, 1997.
