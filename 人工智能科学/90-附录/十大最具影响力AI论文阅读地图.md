---
title: “人工智能最具影响力的 10 篇论文”阅读地图
layer: 90-appendices
tags:
  - evaluation
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# “人工智能最具影响力的 10 篇论文”阅读地图

## 1. 目的

`ten-most-influential-ai-papers.md` 给出的是名单；本页给出的是**怎么读**。重点不是把论文逐字读完，而是建立一条从历史主干到现代系统的阅读路径。

## 2. 第一阶段：建立“可学习模型”的起点

1. McCulloch–Pitts (1943)
2. Perceptron (1958)
3. Backprop (1986)

### 应配套阅读的正文页

- `01-foundations/backpropagation-loss-functions-activation-functions-and-gradient-descent.md`
- `03-model-families/neural-architecture-principles-mlp-cnn-rnn-lstm-gru-and-residual-learning.md`

## 3. 第二阶段：深度学习主流化

4. AlexNet (2012)
5. GAN (2014)

### 应配套阅读的正文页

- `03-model-families/deep-network-families-mlp-cnn-rnn-lstm-gru-alexnet-vgg-resnet-and-nas.md`
- `03-model-families/generative-model-families-gans-vaes-diffusion-and-autoregressive-models.md`

## 4. 第三阶段：深度强化学习与搜索结合

6. DQN (2013/2015)
7. AlphaGo (2016)

### 应配套阅读的正文页

- `03-model-families/value-based-reinforcement-learning-dp-td-sarsa-q-learning-dqn-and-double-dqn.md`
- `03-model-families/policy-gradient-actor-critic-trpo-ppo-and-advantage-estimation.md`
- `03-model-families/model-based-rl-world-models-and-planning.md`

## 5. 第四阶段：Transformer 与大模型时代

8. Attention Is All You Need (2017)
9. BERT (2019)
10. GPT-3 (2020)

### 应配套阅读的正文页

- `03-model-families/transformer-gpt-moe-and-retrieval-augmented-models.md`
- `03-model-families/modern-transformer-variants-linear-attention-long-context-and-state-space-models.md`
- `03-model-families/tokenization-distillation-quantization-and-inference-optimization.md`
- `04-systems-engineering/large-model-training-inference-alignment-and-evaluation-stack.md`

## 6. 两种读法

### 6.1 历史主干读法

按论文年份顺序读，理解范式变迁。

### 6.2 主题映射读法

- 神经网络起源：McCulloch–Pitts → Perceptron → Backprop
- 深度视觉：AlexNet → ResNet
- 生成建模：GAN → VAE → Diffusion
- 决策与强化学习：DQN → AlphaGo → PPO / SAC
- 大模型：Transformer → BERT → GPT-3 → MoE / RAG / Agent

## 7. 建议输出物

读完这 10 篇后，建议至少形成三份输出：

1. 一份 2–3 页的发展脉络总结；
2. 一张“论文—模型—系统—应用”映射表；
3. 一份自己版本的“前十论文”替代表。
