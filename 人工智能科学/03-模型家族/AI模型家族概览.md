---
title: 人工智能模型体系概览
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能模型体系概览

## 1. 组织原则

模型体系层不只是列出模型名称，而是回答三个问题：

1. 这个模型家族要解决什么结构问题；
2. 它与邻近模型有什么连续关系；
3. 它在训练、推理与部署时的主要瓶颈是什么。

## 2. 推荐主线

### 2.1 经典统计学习

- [经典学习算法：回归、分类、聚类、降维与贝叶斯学习](./classical-learning-algorithms-regression-classification-clustering-dimensionality-reduction-and-bayesian-learning.md)
- [经典统计学习模型：SVM、树模型、集成学习、高斯过程与进化方法](./classical-statistical-learning-models-svm-trees-ensembles-gaussian-processes-and-evolutionary-methods.md)

### 2.2 深度网络家族

- [深度网络家族：MLP、CNN、RNN、LSTM、GRU、AlexNet、VGG、ResNet 与 NAS](./deep-network-families-mlp-cnn-rnn-lstm-gru-alexnet-vgg-resnet-and-nas.md)
- [神经网络结构原理：MLP、CNN、RNN、LSTM、GRU 与残差学习](./neural-architecture-principles-mlp-cnn-rnn-lstm-gru-and-residual-learning.md)

### 2.3 强化学习算法谱系

- [强化学习算法谱系：DP、MC、TD、SARSA、Q-learning、DQN、actor-critic 与 PPO](./reinforcement-learning-algorithm-family-dp-mc-td-sarsa-q-learning-dqn-actor-critic-and-ppo.md)
- [值函数强化学习：DP、TD、SARSA、Q-learning、DQN 与 Double DQN](./value-based-reinforcement-learning-dp-td-sarsa-q-learning-dqn-and-double-dqn.md)
- [策略梯度、Actor-Critic、TRPO、PPO 与优势估计](./policy-gradient-actor-critic-trpo-ppo-and-advantage-estimation.md)
- [连续控制：DDPG、TD3、SAC 与离策略 Actor-Critic](./continuous-control-ddpg-td3-sac-and-off-policy-actor-critic.md)

### 2.4 现代大模型与结构模型

- [大语言模型（Large Language Models, LLMs）](./large-language-models.md)
- [Transformer、GPT、混合专家（MoE）与检索增强模型](./transformer-gpt-moe-and-retrieval-augmented-models.md)
- [图神经网络](./graph-neural-networks.md)
- [世界模型](./world-models.md)

## 联读

- [Transformer](./transformers.md)
- [大语言模型](./large-language-models.md)
- [生成式模型总览](./generative-model-families-gans-vaes-diffusion-and-autoregressive-models.md)
- [经典学习算法](./classical-learning-algorithms-regression-classification-clustering-dimensionality-reduction-and-bayesian-learning.md)

## 参考文献

[1] Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson, 2020.
[2] Goodfellow, I., Bengio, Y., & Courville, A. *Deep Learning*. MIT Press, 2016.
