---
title: 人工智能历史中的范式转移
layer: 08-thought-history-culture
tags:
  - ai-history
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能历史中的范式转移

## 这页解决什么问题

“范式转移”不是指某种算法突然出现，而是指研究者开始用另一种方式理解“什么叫智能、怎样构造智能、怎样评价智能”。这页专门解释人工智能史上几次真正改变游戏规则的转向。

## 基本思想

人工智能史上最剧烈的冲突，通常不是“谁的准确率高 1%”，而是下面这些更深的分歧：

- 智能主要是**符号操作**还是**统计学习**？
- 系统应靠**显式知识**还是**隐式表征**？
- 成功的关键在于**算法思想**还是**工程条件**？
- 模型是要**做判断**，还是要**做行动系统中的一个环节**？

当这些问题的答案变化时，范式才会变。

## 一、从逻辑—搜索到知识工程

### 转向前的主流
1950—1960 年代，早期 AI 主要围绕符号表示、定理证明、问题求解和启发式搜索展开。代表性来源包括 Newell 与 Simon 的问题求解研究、McCarthy 的逻辑表达体系，以及 GPS 这类系统。

### 转向发生的原因
研究者发现，单纯的搜索在复杂现实问题中很快遭遇组合爆炸。于是问题变成：能否把专家经验显式编码进系统，使系统不只是“盲搜”，而是“带知识地推理”。

### 结果
由此进入知识工程与专家系统阶段。DENDRAL、MYCIN、XCON 的成功说明：在规则相对稳定、价值足够高的狭窄领域，显式知识可以很有效。

## 二、从显式规则到不确定性建模

专家系统的成功并没有解决两个深层难题：

1. 世界并不总能被清楚写成规则；
2. 现实任务通常充满缺失信息和噪声。

于是到了 1980—1990 年代，概率图模型、贝叶斯网络（Bayesian Networks）和统计学习开始改写主线。Pearl 的工作代表了一次关键转向：AI 不再只问“能否推导”，而是开始问“在不确定条件下怎样合理推断”。

## 三、从手工特征到表示学习

统计学习时期的很多成功依赖特征工程（Feature Engineering）。这条路线有效，但代价是系统高度依赖人工设计。  
连接主义重新上升后，深度学习给出的新答案是：**让系统自己学表征，而不是把表征大部分预先写好。**

这条转向的早期伏笔在 1986 年反向传播，公开转折点则是 2012 年 AlexNet。  
从那之后，视觉、语音、自然语言处理（Natural Language Processing, NLP）开始被“端到端表示学习”重组。

## 四、从单任务模型到预训练基础模型

2010 年代中后期，另一场范式转移发生了：  
模型不再主要面向单个任务训练，而是先在大规模语料上进行预训练（Pretraining），再通过微调、提示（Prompting）或上下文学习适配具体任务。

- **2017 年** Transformer 提供统一的序列建模骨架；
- **2018 年** BERT 显示预训练语言模型的强大迁移性；
- **2020 年** GPT-3 强化了“规模化 + 上下文学习”叙事；
- **2022 年** ChatGPT 则让这一范式真正进入全球公共空间。

## 五、从静态模型到系统中的行动体

最近一轮转向不只是“大模型更大”，而是模型开始嵌入完整系统流程：

- 调用工具；
- 访问外部知识；
- 在界面中执行动作；
- 形成长期记忆；
- 接受审核、权限和日志约束。

这意味着 AI 的中心问题再次变化：  
不再只是“模型会不会预测”，而是“模型如何在真实系统中被约束、放大、验证和协同”。

## 六、范式转移为什么总伴随误判

人工智能史里常见两类误判：

### 误判 A：把局部成功误看成通用胜利
早期符号系统、专家系统、深度学习、大模型都经历过这种阶段。某一路线在一组任务上领先后，人们往往过快把它看成普适终局。

### 误判 B：把暂时失利误看成路线死亡
连接主义在 1969 年后长期受挫，但并未真正消失；概率方法在深度学习崛起后也没有被消灭，反而在不确定性、因果、校准和结构化建模中持续发挥作用。

## 推荐联读
- [控制论、符号主义、连接主义与统计转向](./控制论符号主义连接主义与统计转向.md)
- [专家系统、知识工程与人工智能寒冬](./专家系统知识工程与AI寒冬.md)
- [概率图模型与统计学习转向](./概率图模型与统计转向.md)
- [人工智能应用史：从实验室原型到大规模部署](./AI应用史从实验室到大规模部署.md)

## 参考文献
[1] NEWELL A, SHAW J C, SIMON H A. Report on a general problem-solving program[R]. 1959.  
[2] PEARL J. Probabilistic reasoning in intelligent systems[M]. San Francisco: Morgan Kaufmann, 1988.  
[3] KRIZHEVSKY A, SUTSKEVER I, HINTON G E. ImageNet classification with deep convolutional neural networks[C]//Advances in Neural Information Processing Systems. 2012.  
[4] DEVLIN J, CHANG M W, LEE K, et al. BERT: pre-training of deep bidirectional transformers for language understanding[C]//NAACL-HLT. 2019.  
[5] BROWN T, MANN B, RYDER N, et al. Language models are few-shot learners[C]//Advances in Neural Information Processing Systems. 2020.
