---
title: 人工智能历史时间线
layer: 08-thought-history-culture
tags:
  - ai-history
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-13
---
# 人工智能历史时间线

## 这页怎么用

时间线不是为了背年份，而是为了看清三类节点的先后关系：

1. **基础思想节点**：某个问题第一次被清楚提出；
2. **方法突破节点**：某个技术路线第一次显示出可扩展性；
3. **应用破圈节点**：某个系统第一次在学术圈外形成大范围影响。

同时追踪**人物命运**——技术史不只是论文列表，也是人的故事。

## 基本思想

很多"突然爆发"的成功，其实都经历了漫长伏笔。反向传播在 **1986 年**已系统化，但引爆深度学习要等 **2012 年**AlexNet——等了整整26年。强化学习在 **1980—1990 年代**已形成核心理论，但直到 **2016 年** AlphaGo 才成为公众事件。**自然语言处理走了三代人、三种范式、三堵墙，才走到今天的大语言模型。**

---

## 一、关键年份总表

### 前史（1943—1955）

| 年份 | 事件 | 人物 | 历史意义 |
|---|---|---|---|
| 1943 | 形式神经元模型 | McCulloch & Pitts | 把神经活动与逻辑计算联系起来 |
| 1948 | 控制论 | Wiener | 把反馈、控制、通信组织成统一视角 |
| 1949 | Weaver备忘录"Translation" | Warren Weaver | 首次提出翻译可视为解码密码——统计NLP的思想种子 |
| 1950 | "机器能思考吗？" | Turing（*Mind*） | 图灵测试：AI最持久的哲学问题 |
| 1954 | Georgetown-IBM俄英翻译演示 | Dostert | "3到5年，机器翻译就解决了"——第一个兑现不了的承诺 |
| 1956 | Dartmouth会议 | McCarthy等 | AI作为独立研究领域正式命名 |

### 符号主义与连接主义的第一次碰撞（1957—1969）

| 年份 | 事件 | 人物 | 历史意义 |
|---|---|---|---|
| 1957 | 感知机 | Rosenblatt | 早期连接主义原型——400个光电管做"眼睛"，机器自己学 |
| 1958 | 感知机公开展示 | Rosenblatt | 《纽约时报》头版："海军揭示电子计算机的胚胎" |
| 1959 | 猫视觉皮层感受野实验 | Hubel & Wiesel | 为CNN提供生物学灵感——每个神经元只管一小块 |
| 1965 | DENDRAL启动 | Stanford | 早期科学推理专家系统 |
| 1966 | ALPAC报告 | 美国政府 | 机器翻译"更慢更贵更差"——第一次NLP寒冬 |
| 1969 | *Perceptrons* 出版 | Minsky & Papert | XOR证伪单层感知机——一本书杀死了一个领域 |

### 专家系统的盛衰与连接主义的暗夜（1970—1985）

| 年份 | 事件 | 人物 | 历史意义 |
|---|---|---|---|
| 1970 | SHRDLU积木世界 | Winograd（MIT博士生） | 微世界策略——规则派的极致，能对话、能反问、能执行 |
| 1971 | Rosenblatt溺亡 | Rosenblatt（43岁） | "加一层就行"的答案随他沉入切萨皮克湾 |
| 1972 | MYCIN | Stanford（Shortliffe） | 感染诊断600条规则，准确率超住院医生 |
| 1973 | SHRDLU被chair击溃 | Winograd | 封闭世界假设破产——一个词干掉整个系统；Winograd从此离开AI |
| 1974 | 反向传播数学推导 | Werbos（哈佛博士论文） | 先于时代——被明斯基阴影覆盖，12年无人问津 |
| 1980 | XCON投产 | DEC | AI首次大规模进入企业配置 |
| 1980 | Neocognitron | 福岛邦彦 | 受猫脑启发的卷积架构原型（无监督学习） |
| 1982 | 日本第五代计算机计划 | 通产省 | 数十亿美元豪赌规则AI——十年后彻底失败 |
| 1984 | Cyc项目启动 | Lenat | 试图编码所有人类常识——40年至今未完成 |

### 反向传播与连接主义复活（1986—1997）

| 年份 | 事件 | 人物 | 历史意义 |
|---|---|---|---|
| 1986 | 反向传播系统化 | Rumelhart, Hinton, Williams（*Nature*） | 多层网络可训练性重建——死刑判决被推翻 |
| 1987—1993 | 第二次AI寒冬 | — | 专家系统产业崩塌；Lisp机器市场崩溃 |
| 1988 | "每开除一个语言学家准确率就上升" | Jelinek（IBM） | 统计NLP宣言——从规则到数据驱动的路线切换 |
| 1989 | 全连接网络的手写数字极限 | LeCun（Bell Labs） | 位置敏感、参数爆炸——CNN的驱动力 |
| 1992 | 第五代计算机计划结束 | 日本通产省 | 过度承诺经典案例：数十亿美元几乎零产出 |
| 1995 | SVM提出 | Cortes & Vapnik | 统计学习理论的优雅巅峰——神经网络的对立面 |
| 1997 | LSTM | Hochreiter & Schmidhuber | 长时依赖建模关键突破 |
| 1997 | Deep Blue战胜Kasparov | IBM | AI首次在全球媒体中形成强烈象征 |

### CNN的到来与寒冬的最后几年（1998—2005）

| 年份 | 事件 | 人物 | 历史意义 |
|---|---|---|---|
| 1998 | LeNet-5 | LeCun等 | CNN首次大规模部署——全美10%支票被它读取 |
| 1990s末 | CNN寒冬 | LeCun, Hinton, Bengio | 数据、算力、深度三瓶颈锁死——"在NIPS会场只坐着寥寥几人" |
| 2003 | 神经语言模型 | Bengio（蒙特利尔） | 词向量/词嵌入——打破One-hot孤岛，自监督学习的种子 |

### 深度学习复兴（2006—2012）

| 年份 | 事件 | 人物 | 历史意义 |
|---|---|---|---|
| 2006 | 逐层预训练/DBN | Hinton等 | 证明深层网络可以被训练——"深度学习"品牌创立 |
| 2006 | "加拿大黑手党"结盟 | Hinton, LeCun, Bengio | 三座城市一条战线 |
| 2006 | Google Translate上线 | Google | SMT最大规模部署——统计派巅峰 |
| 2009 | ImageNet | 李飞飞等 | 1400万张图片，167国标注工人——对抗整个学术评价体系 |

### 深度学习时代（2012—2017）

| 年份 | 事件 | 人物 | 历史意义 |
|---|---|---|---|
| **2012** | **AlexNet** | Krizhevsky, Sutskever, Hinton | **15.3% vs 26.2%——深度学习主流化分水岭** |
| 2013 | word2vec | Mikolov等（Google） | 词向量工业化 |
| 2013/2015 | DQN | Mnih等（DeepMind） | 深度强化学习首次大规模破圈 |
| 2014 | Seq2Seq + Attention | Sutskever等; Bahdanau等 | 神经机器翻译拐点 |
| 2014 | GAN | Goodfellow等 | 生成式学习进入新阶段 |
| **2015** | **ResNet（152层）** | 何恺明等（微软亚研） | **退化问题突破——ImageNet准确率首超人类；论文被引25万次** |
| 2016 | AlphaGo战胜李世石 | DeepMind | 规划、搜索、DL与RL融合的象征性胜利 |
| 2016 | Google Translate全面切换NMT | Google | 统计→神经路线切换完成 |

### Transformer时代（2017至今）

| 年份 | 事件 | 人物/来源 | 历史意义 |
|---|---|---|---|
| 2017 | Transformer | Vaswani等 | 序列建模骨架重置——Attention is all you need |
| 2018 | BERT | Devlin等 | 预训练语言模型成为NLP主线 |
| 2020 | GPT-3 | Brown等 | 规模化预训练与上下文学习破圈 |
| 2021 | AlphaFold2 | DeepMind | AI科学发现代表性胜利 |
| 2022 | Stable Diffusion开源 | Rombach等 | 文生图走向大众化 |
| 2022 | ChatGPT | OpenAI | 大模型首次在全球消费端形成平台级影响 |
| 2023 | GPT-4 | OpenAI | 多能力整合与通用助手叙事强化 |
| 2024 | AlphaFold3 | DeepMind | 多分子生物建模推进 |

---

## 二、三次最重要的"起—落—再起"

### 1. 早期AI的高涨与第一次降温（1956—1974）
1956年Dartmouth之后，研究共同体对通用智能抱有很高预期。Rosenblatt的感知机登上NYT头版。但到了1960年代末，感知、常识、语言和开放环境推理的困难暴露——Minsky用一本200页的书（*Perceptrons*, 1969）判处了连接主义死刑。1971年，Rosenblatt去世。1974年，Werbos写出反向传播的完整数学但无人问津。

### 2. 专家系统繁荣与第二次寒冬（1972—1993）
1970—1980年代，知识工程把AI带入企业与医疗——MYCIN、XCON成为明星。日本启动数十亿美元的第五代计算机计划。但波兰尼悖论在沉默中腐蚀一切——"我们知道的比我们能说出来的多。"规则永远写不完。Winograd的SHRDLU被chair一个词击溃。专家系统批量失败。第五代计算机计划在1992年悄然结束。AI这个词成了骗子的同义词。

### 3. 深度学习的缓慢复兴与突然爆发（1986—2012）
1986年反向传播没有立刻引爆革命。在1980—2000年间，做神经网络的人被主流学界视为炼金术士。Hinton、LeCun、Bengio——三个人，三座城市，守着同一个信念。2006年Hinton证明深层网络可以被训练，换了个品牌叫"深度学习"。2009年李飞飞赌上了学术生涯收集ImageNet。2012年，Krizhevsky用两块游戏显卡训练AlexNet，把第二名甩开11个百分点。**三张牌——深度、数据、算力——在同一天凑齐了。**

---

## 三、四代人的接力：NLP的特殊故事

NLP走过了一条三范式三堵墙的特殊路径：

| 代际 | 时间 | 代表人物 | 墙 | 遗产 |
|---|---|---|---|---|
| 第一代：规则派 | 1954—1973 | Dostert, Winograd | 规则写不完/封闭世界假设 | 知识表示、解释机制 |
| 第二代：统计派 | 1988—2010 | Jelinek, Brown | 维度诅咒——没见过的组合算不出 | 数据驱动、N-gram、SMT |
| 第三代：神经派 | 2003至今 | Bengio, Mikolov | 仍在前行——从词向量到Transformer | 分布式表示、自监督学习、预训练 |

图灵1950年问的那个问题——"机器能不能思考？"——经历了三代人接力的70年，到今天还没有被彻底回答。但每一代都推倒了前一代的墙。

---

## 四、那些没能看到答案的人

| 人物 | 生卒 | 关键贡献 | 结局 |
|---|---|---|---|
| Turing | 1912—1954 | 图灵测试、"机器能思考吗？" | 1954年服毒自杀，41岁。没看到第一次机器翻译演示 |
| Rosenblatt | 1928—1971 | 感知机——不靠规则从数据中学 | 1971年划船溺亡，43岁。带走了"加一层就行"的答案 |
| Werbos | 1947— | 1974年反向传播博士论文 | 论文被遗忘12年——辛顿后来读到时"五味杂陈" |
| Jelinek | 1932—2010 | 统计NLP革命、"每开除一个语言学家…" | 没活到看见维度诅咒被推倒的那一天 |

---

## 五、应用影响最大的节点

| 年份 | 应用节点 | 来源 | 为什么重要 |
|---|---|---|---|
| 1965 | DENDRAL | Stanford | AI首次在科学推理中显出实用价值 |
| 1972 | MYCIN | Stanford | 早期医疗决策支持代表 |
| 1980 | XCON | DEC | 企业级专家系统大规模部署 |
| 1997 | Deep Blue | IBM | AI首次以公共事件震动全球舆论 |
| 1998 | LeNet-5手写识别 | LeCun | 美国邮政/银行部署——全美10%支票被CNN读取 |
| 2011 | Siri | Apple | 语音助手进入消费终端 |
| 2012 | AlexNet | Krizhevsky等 | 深度学习进入主流——全世界AI实验室抢购GPU |
| 2016 | AlphaGo | DeepMind | AI从"会做事"变成"会赢"的象征 |
| 2016 | Google Translate NMT | Google | 全平台翻译质量跃升——统计→神经完成 |
| 2021 | AlphaFold2 | DeepMind | AI在生命科学中形成标志性学术与产业影响 |
| 2022 | ChatGPT | OpenAI | 大模型首次成为大众日常工具 |
| 2022—2024 | 文生图/文生视频 | Stability AI, OpenAI等 | 生成式AI进入创意生产与内容工业链 |

## 推荐联读

- [AI历史概览](./AI历史概览.md)
- [神经网络与 Transformer 历史谱系](./神经网络与Transformer的历史谱系.md)
- [专家系统、知识工程与AI寒冬](./专家系统知识工程与AI寒冬.md)
- [深度学习复兴的工程条件](./深度学习复兴的工程条件数据GPU与软件栈.md)
- [NLP发展史：三代范式与三堵墙](./自然语言处理发展史.md)
- [AI应用史：从实验室到大规模部署](./AI应用史从实验室到大规模部署.md)

## 参考文献
[1] TURING A M. Computing machinery and intelligence[J]. Mind, 1950.
[2] HUBEL D H, WIESEL T N. Receptive fields of single neurones in the cat's striate cortex[J]. The Journal of Physiology, 1959.
[3] MINSKY M, PAPERT S. Perceptrons[M]. MIT Press, 1969.
[4] WERBOS P. Beyond regression: new tools for prediction and analysis in the behavioral sciences[D]. Harvard, 1974.
[5] RUMELHART D E, HINTON G E, WILLIAMS R J. Learning representations by back-propagating errors[J]. Nature, 1986.
[6] LECUN Y, BOTTOU L, BENGIO Y, et al. Gradient-based learning applied to document recognition[J]. Proceedings of the IEEE, 1998.
[7] BENGIO Y, et al. A neural probabilistic language model[J]. Journal of Machine Learning Research, 2003.
[8] HINTON G E, OSINDERO S, TEH Y W. A fast learning algorithm for deep belief nets[J]. Neural Computation, 2006.
[9] DENG J, DONG W, SOCHER R, et al. ImageNet: a large-scale hierarchical image database[C]//CVPR. 2009.
[10] KRIZHEVSKY A, SUTSKEVER I, HINTON G E. ImageNet classification with deep convolutional neural networks[C]//NIPS. 2012.
[11] HE K, ZHANG X, REN S, et al. Deep residual learning for image recognition[C]//CVPR. 2016.
[12] SILVER D, HUANG A, MADDISON C J, et al. Mastering the game of Go with deep neural networks and tree search[J]. Nature, 2016.
[13] VASWANI A, et al. Attention is all you need[C]//NIPS. 2017.
[14] BROWN T B, et al. Language models are few-shot learners[C]//NeurIPS. 2020.
[15] JUMPER J, et al. Highly accurate protein structure prediction with AlphaFold[J]. Nature, 2021.
