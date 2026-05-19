---
title: 人工智能历史注释阅读单
layer: 90-appendices
tags:
  - evaluation
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能历史注释阅读单

## 用途

这份阅读单不是简单列书单，而是帮助你用“史料—教材—回顾”三层材料搭建人工智能史的阅读框架。  
建议的使用原则是：

1. 先读少量一手材料，建立历史现场感；
2. 再读教材与综述，建立概念框架；
3. 最后回到专题论文和系统案例，形成自己的判断。

## 一、起点：问题是怎样被提出的

### [1] Turing, 1950
**材料**：TURING A M. *Computing machinery and intelligence*  
**为什么先读**：它不是今天技术最直接的工程来源，却是“机器智能”问题最有代表性的早期表达之一。读它，是为了明白 AI 起初并不是一个单纯的建模问题，而是哲学、语言和可计算性问题的交叉。

### [2] Wiener, 1948
**材料**：WIENER N. *Cybernetics*  
**为什么读**：理解反馈、控制、通信、目标维持这些思想如何进入智能讨论。对控制科学背景读者尤其重要。

## 二、早期 AI 与符号主义

### [3] Dartmouth proposal, 1955
**材料**：MCCARTHY J, MINSKY M L, ROCHESTER N, et al. *A proposal for the Dartmouth summer research project on artificial intelligence*  
**为什么读**：这份文档让你看到“人工智能”一词是如何被组织成研究议程的。

### [4] Newell & Simon 相关文献
**为什么读**：理解问题求解、搜索、启发式和符号操作为何构成了早期 AI 的中心。

## 三、连接主义的起伏

### [5] Rosenblatt, 1958
**材料**：ROSENBLATT F. *The perceptron*  
**为什么读**：感知机不是今天最强的模型，但它是“可学习网络”路线第一次大规模进入公众视野的代表。

### [6] Rumelhart, Hinton, Williams, 1986
**材料**：*Learning representations by back-propagating errors*  
**为什么读**：这是现代神经网络训练史中的关键节点，很多后续路线都要从这里往下接。

## 四、专家系统与寒冬

### [7] Shortliffe, 1976
**材料**：SHORTLIFFE E H. *Computer-based medical consultations: MYCIN*  
**为什么读**：理解专家系统为什么能成功，也理解它的部署边界和组织代价。

### [8] McDermott, 1982
**材料**：MCDERMOTT J. *R1 (XCON) at age 12*  
**为什么读**：这是企业级 AI 应用史必须读的一篇案例材料。

## 五、统计学习与概率转向

### [9] Pearl, 1988
**材料**：PEARL J. *Probabilistic reasoning in intelligent systems*  
**为什么读**：理解不确定性、结构化推理与贝叶斯网络如何进入 AI 主线。

### [10] Hastie, Tibshirani, Friedman, 2001
**材料**：*The elements of statistical learning*  
**为什么读**：帮助把统计学习的核心语言系统化。

## 六、深度学习复兴与大模型前史

### [11] Krizhevsky, Sutskever, Hinton, 2012
**材料**：ImageNet 论文  
**为什么读**：理解深度学习为什么在 2012 年形成公开转折点。

### [12] Vaswani et al., 2017
**材料**：*Attention is all you need*  
**为什么读**：理解 Transformer 如何成为后来基础模型的主骨架。

### [13] Brown et al., 2020
**材料**：GPT-3 论文  
**为什么读**：理解规模化预训练与上下文学习叙事为何迅速升温。

## 七、强化学习历史线

### [14] Sutton & Barto
**材料**：*Reinforcement Learning: An Introduction*  
**为什么读**：这本书对理解动态规划、TD 学习、Q-learning、策略梯度和现代 RL 之间的连续性很重要。

## 推荐阅读顺序

### 顺序 A：按时间读
Turing → Wiener → Dartmouth → Rosenblatt → MYCIN/XCON → Pearl → Backprop → AlexNet → Transformer → GPT-3

### 顺序 B：按问题读
- 智能是什么：Turing, Wiener  
- 智能怎样表示：符号主义与知识工程  
- 智能怎样学习：Perceptron, Backprop, Deep Learning  
- 智能怎样面对不确定性：Pearl, ESL  
- 智能怎样行动：RL, AlphaGo  
- 智能怎样成为基础设施：Transformer, GPT-3, ChatGPT

## 参考文献（示例）
[1] TURING A M. Computing machinery and intelligence[J]. Mind, 1950.  
[2] WIENER N. Cybernetics: or control and communication in the animal and the machine[M]. 1948.  
[3] MCCARTHY J, MINSKY M L, ROCHESTER N, et al. A proposal for the Dartmouth summer research project on artificial intelligence[R]. 1955.  
[4] RUMELHART D E, HINTON G E, WILLIAMS R J. Learning representations by back-propagating errors[J]. Nature, 1986.  
[5] PEARL J. Probabilistic reasoning in intelligent systems[M]. 1988.  
[6] VASWANI A, SHAZEER N, PARMAR N, et al. Attention is all you need[C]//NIPS. 2017.
