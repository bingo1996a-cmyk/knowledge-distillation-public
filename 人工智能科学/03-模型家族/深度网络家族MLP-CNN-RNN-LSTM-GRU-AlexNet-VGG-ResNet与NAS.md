---
title: 深度网络家族：多层感知机、卷积神经网络、循环神经网络、长短期记忆网络、门控循环单元、AlexNet、VGG、ResNet 与神经架构搜索
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 深度网络家族：多层感知机、卷积神经网络、循环神经网络、长短期记忆网络、门控循环单元、AlexNet、VGG、ResNet 与神经架构搜索

## 1. 统一问题：不同数据结构需要不同归纳偏置

这些网络并不是一串彼此无关的缩写，而是在回答同一个问题：**当数据具有向量结构、网格结构、时间结构或层级组合结构时，神经网络应该嵌入什么归纳偏置（inductive bias）**。

- 多层感知机（Multilayer Perceptron, MLP）：一般函数逼近；
- 卷积神经网络（Convolutional Neural Network, CNN）：局部性、平移等变与层级特征；
- 循环神经网络（Recurrent Neural Network, RNN）：序列依赖与递归状态；
- 长短期记忆网络（Long Short-Term Memory, LSTM）/门控循环单元（Gated Recurrent Unit, GRU）：门控记忆；
- AlexNet / VGG / ResNet：深层视觉网络的关键里程碑；
- 神经架构搜索（Neural Architecture Search, NAS）：自动化结构设计。

## 2. MLP：最通用的前馈非线性逼近器

MLP 的层更新可写为：

$$
h^{(l+1)} = \sigma(W^{(l)}h^{(l)}+b^{(l)}).
$$

它的意义在于：

- 用层级组合逼近复杂函数；
- 作为大量更复杂网络的构件；
- 在表格数据、小型表示学习任务中仍很重要。

局限：

- 对图像和序列缺少结构偏置；
- 参数量随输入维数增长快；
- 泛化更依赖正则化与数据结构假设。

## 3. CNN：局部连接、参数共享与层级视觉表示

卷积操作：

$$
y_{i,j} = \sum_{u,v} K_{u,v}x_{i+u,j+v}.
$$

CNN 的关键不是“做了卷积”本身，而是把三个偏置硬编码进网络：

1. **局部感受野**；
2. **参数共享**；
3. **层级特征组合**。

这解释了为什么 CNN 在图像、语音频谱、遥感和医学影像中长期有效。

## 4. RNN、LSTM、GRU：为什么序列需要状态

RNN 用递归状态压缩历史：

$$
h_t = \phi(W_h h_{t-1}+W_x x_t+b).
$$

问题在于：梯度在长链上容易消失或爆炸。LSTM 和 GRU 通过门控改善这个问题。其根本思想是：**不是所有历史都该等权传递，记忆需要可控读写。**

## 5. AlexNet、VGG、ResNet 的结构意义

### 5.1 AlexNet

AlexNet 的历史意义不只是赢了 ImageNet，而是证明了：

- 大规模数据；
- GPU 训练；
- 深卷积网络；
- ReLU 与 dropout

可以共同改变视觉模型路线。

### 5.2 VGG

VGG 的贡献在于结构简洁：用小卷积核重复堆叠，展示了“深而规则”的设计价值。

### 5.3 ResNet

ResNet 用残差块：

$$
y = F(x)+x.
$$

它的根本意义在于为深层网络提供更短的梯度传播路径，显著缓解优化困难。

## 6. 神经架构搜索（NAS）

NAS 的核心思想是把网络设计也交给优化过程。常见思路有：

- 强化学习搜索；
- 进化搜索；
- 可微架构搜索。

NAS 的意义不只是“自动调结构”，还在于揭示结构空间、计算预算与任务性能之间的系统性折中。

## 7. 各模型之间的联系与区别

- MLP 是最一般的前馈逼近器；
- CNN 是在 MLP 基础上加入空间归纳偏置；
- RNN/LSTM/GRU 是在 MLP 基础上加入递归状态；
- ResNet 主要解决深层优化问题；
- NAS 则把“结构选择”上升为搜索或优化问题。

## 8. 训练与应用要点

需要同时关注：

- 初始化；
- 激活函数；
- 归一化；
- 残差连接；
- 数据增强；
- 学习率调度；
- 计算预算与部署约束。

## 联读

- [神经网络架构原理：MLP、CNN、RNN、LSTM、GRU 与残差学习](./neural-architecture-principles-mlp-cnn-rnn-lstm-gru-and-residual-learning.md)
- [神经网络](./neural-networks.md)
- [Transformer](./transformers.md)
- [深度学习训练动力学、曲率、初始化与隐式偏差](../04-systems-engineering/deep-learning-training-dynamics-curvature-initialization-and-implicit-bias.md)

## 参考文献

[1] LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. *Gradient-Based Learning Applied to Document Recognition*. Proceedings of the IEEE, 1998.
[2] Krizhevsky, A., Sutskever, I., & Hinton, G. *ImageNet Classification with Deep Convolutional Neural Networks*. NeurIPS, 2012.
[3] Simonyan, K., & Zisserman, A. *Very Deep Convolutional Networks for Large-Scale Image Recognition*. ICLR, 2015.
[4] He, K. et al. *Deep Residual Learning for Image Recognition*. CVPR, 2016.
