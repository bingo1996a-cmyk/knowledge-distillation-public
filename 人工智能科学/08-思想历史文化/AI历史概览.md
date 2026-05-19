---
title: 人工智能史总览
layer: 08-thought-history-culture
tags:
  - ai-history
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能史总览

## 这页解决什么问题

这页不是把历史材料简单排成时间顺序，而是帮助读者先抓住一个判断：人工智能（Artificial Intelligence, AI）从来不是单线增长的学科。它的历史由三股力量反复拉扯而成：

1. **思想路线的竞争**：逻辑与符号、概率与统计、神经网络与表示学习、行动与决策；
2. **工程条件的成熟**：数据、算力、软件栈、硬件体系、互联网平台；
3. **应用牵引的变化**：从实验室演示到企业流程，再到大规模消费级产品和基础设施服务。

## 基本思想

读人工智能史，最容易犯的错误是把今天的技术优势投射回过去，以为历史早就注定会走到深度学习或大模型。事实并非如此。  
这段历史更像一条多次改道的河流：有时是符号主义（Symbolicism）声势最盛，有时是专家系统（Expert System）几乎完成产业化部署；有时连接主义（Connectionism）看起来已经被判死刑，却又在数据、图形处理器（Graphics Processing Unit, GPU）和软件栈成熟后突然卷土重来；而在深度学习高歌猛进之后，概率建模、知识表示、工具调用、验证器和系统工程又重新被召回前台。

因此，本页把历史分为六个阶段来读。

## 一、思想源头：计算、逻辑、控制与反馈（1940 年代—1950 年代前半）

- **1943 年**，McCulloch 与 Pitts 在论文 *A Logical Calculus of the Ideas Immanent in Nervous Activity* 中提出形式神经元模型。这不是今天神经网络的直接工程原型，但它第一次把“神经活动—逻辑计算”联系在一起。
- **1948 年**，Wiener 的 *Cybernetics* 把反馈、控制、通信和生物—机器类比组织成一套宏大框架。此时“智能”还没有被狭义地理解为模式识别，它更接近“能在反馈回路中维持目标行为的系统”。
- **1950 年**，Turing 在 *Computing Machinery and Intelligence* 中提出后来被称为图灵测试（Turing Test）的思想实验，把“机器能否思考”从纯哲学争论推进到可操作的判据讨论。

这一阶段最重要的不是算法性能，而是问题被怎样提出：智能究竟是推理、学习、控制，还是模仿人的外在行为？

## 二、学科命名与早期乐观：Dartmouth 之后（1956 年—1960 年代）

- **1956 年**，McCarthy、Minsky、Rochester、Shannon 等人发起 Dartmouth Summer Research Project on Artificial Intelligence。人工智能作为独立研究议题被正式命名。
- **1957 年**，Rosenblatt 提出感知机（Perceptron），连接主义第一次以可训练模型的形态进入公众视野。
- **1958—1961 年**，LISP、General Problem Solver（GPS）等成果强化了早期 AI 的一条主线：通过符号表示、搜索和启发式推理来解决问题。

这个阶段充满了乐观。原因并不难理解：研究者第一次看到机器在下棋、定理证明、简单问题求解上表现出“像智能”的行为，于是很多人自然推测，通用智能也许并不遥远。

## 三、第一次收缩：能力边界暴露与早期寒意（1960 年代末—1970 年代）

- **1966 年**，美国 ALPAC 报告否定了当时机器翻译（Machine Translation）项目的实际成效，资金迅速收紧。
- **1969 年**，Minsky 与 Papert 的 *Perceptrons* 系统指出单层感知机的表示局限，连接主义遭受重创。
- 这一时期，许多系统只能在“玩具世界”中表现良好，一旦进入开放环境，知识不全、组合爆炸、感知脆弱、推理不可扩展等问题就暴露出来。

于是，第一次教训出现了：**会演示，不等于会落地；会在狭小闭环里成功，不等于可以在开放世界里扩展。**

## 四、专家系统的繁荣与第二次收缩（1970 年代中后期—1980 年代末）

- **1965—1972 年**，DENDRAL 与 MYCIN 让知识工程（Knowledge Engineering）路线取得突破。它们说明：在高价值、规则清晰、专家知识可显式编码的领域，AI 可以非常有用。
- **1980 年左右**，DEC 的 XCON 成为专家系统商业成功的代表案例，AI 开始真正进入企业流程。
- 但繁荣背后藏着新的脆弱性：知识获取难、维护成本高、规则库膨胀、迁移性差、对不确定性处理不足。

到 **1987—1993 年** 左右，专家系统泡沫破裂，第二次 AI winter（人工智能寒冬）到来。  
这不是“AI 完全无用”，而是“当时那套主流工程路线在规模、成本和可维护性上撞墙了”。

## 五、统计学习与连接主义复兴（1990 年代—2010 年代前半）

- **1988 年**，Pearl 的 *Probabilistic Reasoning in Intelligent Systems* 标志概率图模型（Probabilistic Graphical Models, PGM）系统化成形。
- **1995 年**，支持向量机（Support Vector Machine, SVM）等统计学习方法推动“泛化误差、模型选择、正则化、核方法”成为中心议题。
- **1986 年** 的反向传播（Backpropagation）在理论上已重新打开神经网络之门，但真正的大规模突破仍需等待工程条件成熟。
- **2006 年**，Hinton 等人的深层信念网络（Deep Belief Network, DBN）工作让“深层表示学习”重新变成热点。
- **2012 年**，AlexNet 在 ImageNet 上的突破成为深度学习复兴的公开转折点。

这时，历史终于发生一次真正的急转弯：神经网络不再只是学术边缘路线，而开始改写主流方法栈。

## 六、Transformer、基础模型与智能体阶段（2017 年至今）

- **2017 年**，Vaswani 等人在 *Attention Is All You Need* 中提出 Transformer，序列建模和大规模预训练出现新的统一骨架。
- **2018 年**，BERT 把双向预训练推向自然语言处理（Natural Language Processing, NLP）主线。
- **2020 年**，GPT-3 让“规模化预训练 + 上下文学习（In-Context Learning, ICL）”形成新的范式信号。
- **2022 年**，ChatGPT 把大模型从研究与开发者工具推进到全球大众产品层。
- **2022—2024 年**，扩散模型（Diffusion Models）、多模态模型、代码模型、科学智能体（Scientific Agents）、工具使用（Tool Use）与检索增强生成（Retrieval-Augmented Generation, RAG）不断扩张，AI 从“给出答案”逐步走向“调动外部世界”。

这一阶段最关键的变化是：**模型不再只是静态函数近似器，而成为系统中的中心调度器、接口理解器与行动规划器。**

## 如何把这段历史读明白

建议把人工智能史至少分成三条线同时看：

1. **模型线**：从感知机、反向传播、卷积网络、循环网络、Transformer 到基础模型；
2. **方法线**：从搜索与符号推理，到概率建模、统计学习、强化学习、表示学习、工具增强；
3. **应用线**：从 DENDRAL、MYCIN、XCON、Deep Blue、AlphaGo，到 AlphaFold、ChatGPT 及现代 agent 系统。

只有把三条线放在一起，才能解释为什么某些成果在发表时影响有限，却在若干年后突然成为主流。

## 推荐联读
1. [人工智能历史时间线](./AI历史时间线.md)
2. [人工智能历史中的范式转移](./AI范式的历史变迁.md)
3. [人工智能应用史：从实验室原型到大规模部署](./AI应用史从实验室到大规模部署.md)

## 参考文献
[1] MCCULLOCH W S, PITTS W. A logical calculus of the ideas immanent in nervous activity[J]. The Bulletin of Mathematical Biophysics, 1943.  
[2] WIENER N. Cybernetics: or Control and Communication in the Animal and the Machine[M]. Paris: Hermann & Cie; Cambridge, Mass.: MIT Press, 1948.  
[3] TURING A M. Computing machinery and intelligence[J]. Mind, 1950.  
[4] MCCARTHY J, MINSKY M L, ROCHESTER N, et al. A proposal for the Dartmouth summer research project on artificial intelligence[R]. 1955.  
[5] VASWANI A, SHAZEER N, PARMAR N, et al. Attention is all you need[C]//Advances in Neural Information Processing Systems. 2017.  
[6] BROWN T, MANN B, RYDER N, et al. Language models are few-shot learners[C]//Advances in Neural Information Processing Systems. 2020.
