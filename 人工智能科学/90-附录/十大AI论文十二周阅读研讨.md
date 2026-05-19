---
title: “人工智能最具影响力的 10 篇论文”十二周研讨课（12-Week Reading Seminar）
layer: 90-appendices
tags:
  - evaluation
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# “人工智能最具影响力的 10 篇论文”十二周研讨课（12-Week Reading Seminar）

## 课程定位

这份研讨课不是按年代机械排列，而是按“问题怎样层层推进”来组织。目标是让读者在 12 周里建立一条最小但闭环的人工智能学术史主线：

- 神经元与网络形式化；
- 可训练表示；
- 深度视觉；
- 深度强化学习与搜索；
- 生成模型；
- Transformer 与预训练大模型。

## 使用方式

每周建议完成三件事：

1. 精读 1 篇主论文；
2. 对照 1–2 篇辅助材料；
3. 输出 1 页问题导向笔记。

## Week 1：McCulloch–Pitts

- 主论文：*A Logical Calculus of the Ideas Immanent in Nervous Activity*  
- 问题：什么是“神经元的形式化版本”？  
- 输出：把逻辑门、阈值单元、网络计算能力写成图示。

## Week 2：Perceptron

- 主论文：Rosenblatt, *The Perceptron*  
- 问题：为什么“可学习”是质变而不只是延续？  
- 输出：写出感知机更新规则与线性可分条件。

## Week 3：Backpropagation

- 主论文：Rumelhart, Hinton, Williams, *Learning Representations by Back-Propagating Errors*  
- 问题：链式法则怎样变成可训练深网络的核心？  
- 输出：手推两层网络的反向传播。

## Week 4：AlexNet

- 主论文：Krizhevsky et al., *ImageNet Classification with Deep Convolutional Neural Networks*  
- 问题：为什么 2012 是深度学习成为主流的转折点？  
- 输出：总结卷积、ReLU、GPU 训练、数据规模的协同效应。

## Week 5：DQN

- 主论文：Mnih et al., *Playing Atari with Deep Reinforcement Learning*  
- 问题：为什么 value-based RL 与深网络结合会成功？  
- 输出：解释 replay buffer 与 target network 的必要性。

## Week 6：GAN

- 主论文：Goodfellow et al., *Generative Adversarial Nets*  
- 问题：对抗训练为什么能做生成建模？  
- 输出：写出极小极大目标与常见不稳定性。

## Week 7：AlphaGo

- 主论文：Silver et al., *Mastering the Game of Go with Deep Neural Networks and Tree Search*  
- 问题：深度网络、强化学习与搜索如何被系统化组合？  
- 输出：拆出 policy network、value network、MCTS 之间的角色分工。

## Week 8：Transformer

- 主论文：Vaswani et al., *Attention Is All You Need*  
- 问题：为什么“注意力”替代“循环”会带来范式变化？  
- 输出：手写 scaled dot-product attention 计算图。

## Week 9：BERT

- 主论文：Devlin et al., *BERT*  
- 问题：预训练—微调为什么成为 NLP 主流工作流？  
- 输出：比较 masked language model 与自回归训练。

## Week 10：GPT-3

- 主论文：Brown et al., *Language Models are Few-Shot Learners*  
- 问题：规模化为什么会改变能力分布？  
- 输出：总结 few-shot、in-context learning 与 scale 的关系。

## Week 11：交叉主题复盘

- 比较三条路线：
  - 表示学习路线；
  - 决策与搜索路线；
  - 预训练大模型路线。

## Week 12：读后重构

- 任务：把 10 篇论文重新组织成你自己的研究图谱。  
- 建议输出：`问题—方法—理论—工程—影响` 五列表。

## 建议联读

- `ten-most-influential-ai-papers.md`
- `reading-map-for-the-ten-most-influential-ai-papers.md`
- `reference-textbooks.md`
