# 测度与 $\sigma$-代数

## 定位

测度（Measure）与 $\sigma$-代数（Sigma-Algebra）是概率论现代形式化的底层语言。  
若没有这套语言，很多概率对象只能停留在"直觉随机性"的层面，难以严格定义条件期望、随机过程、极限定理与滤波。

## 为什么需要它

在有限集合上，给每个元素分配概率通常不困难。  
但当样本空间是连续的、无穷的、甚至是函数空间时，不能对"所有子集"都任意赋概率，否则会出现不可测集合之类的病态问题。

因此，需要先规定"哪些集合允许被赋值"，这就是 $\sigma$-代数的作用；再规定"如何给这些集合赋大小"，这就是测度的作用。

## $\sigma$-代数是什么

给定样本空间 $\Omega$，若集合族 $\mathcal{F}\subseteq 2^\Omega$ 满足：

1. $\Omega\in\mathcal{F}$
2. 若 $A\in\mathcal{F}$，则 $A^c\in\mathcal{F}$
3. 若 $A_1,A_2,\dots\in\mathcal{F}$，则 $\bigcup_{n=1}^{\infty}A_n\in\mathcal{F}$

则称 $\mathcal{F}$ 为 $\Omega$ 上的一个 $\sigma$-代数。

$$
\Omega\in\mathcal{F},\qquad A\in\mathcal{F}\Rightarrow A^c\in\mathcal{F},\qquad A_n\in\mathcal{F}\Rightarrow \bigcup_{n=1}^{\infty}A_n\in\mathcal{F}
$$

由补集与可列并封闭，还可推出对可列交也封闭。

## 测度是什么

在可测空间 $(\Omega,\mathcal{F})$ 上，函数 $\mu:\mathcal{F}\to[0,+\infty]$ 若满足：

1. $\mu(\varnothing)=0$
2. 对两两不交的可测集列 $A_1,A_2,\dots$，有可列可加性

$$
\mu\Bigl(\bigcup_{n=1}^{\infty}A_n\Bigr)=\sum_{n=1}^{\infty}\mu(A_n)
$$

则称 $\mu$ 为测度。

若进一步满足 $\mu(\Omega)=1$，则它就是概率测度（Probability Measure），常记作 $P$。

$$
P(\Omega)=1
$$

## 概率空间

概率论通常工作在三元组

$$
(\Omega,\mathcal{F},P)
$$

上：

- $\Omega$：样本空间（sample space）
- $\mathcal{F}$：可观测事件族
- $P$：这些事件上的概率赋值

## 可测函数与随机变量

随机变量并不是"随机变化的数"这一句直觉就够了。严格地说，随机变量 $X$ 是从样本空间到实数轴的可测函数：

$$
X:(\Omega,\mathcal{F})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))
$$

其中 $\mathcal{B}(\mathbb{R})$ 是实数轴上的 Borel $\sigma$-代数（Borel Sigma-Algebra）。

这意味着对任意 Borel 集 $B\subseteq\mathbb{R}$，原像 $X^{-1}(B)$ 都是可测事件，因而概率 $P(X\in B)$ 才有定义。

## 生成的 $\sigma$-代数

若一组集合族 $\mathcal{C}$ 给出局部观测结构，则可以定义由它生成的最小 $\sigma$-代数：

$$
\sigma(\mathcal{C})
$$

同理，随机变量 $X$ 生成的 $\sigma$-代数记作 $\sigma(X)$，它表示"由 $X$ 所包含的信息"。

这在条件期望、滤波和随机控制中极其关键。

## 与条件期望的关系

条件期望并不只是"给定某个条件后的平均值"，更严格地说，它是相对于某个子 $\sigma$-代数 $\mathcal{G}\subseteq\mathcal{F}$ 的投影对象：

$$
\mathbb{E}[X\mid \mathcal{G}]
$$

这个写法说明：条件的本质不是某个单独事件，而是一整套可用信息。

## 在控制、估计与强化学习中的意义

- 在滤波中，观测历史会生成一个信息流（filtration）
- 在部分可观测系统中，状态估计本质上是对条件分布的更新
- 在随机控制中，策略往往要求对当前信息集可适应（adapted）
- 在强化学习中，马尔可夫性、belief state 与部分可观测决策过程都涉及可测信息结构

## 最小例子

$\Omega=\{1,2,3,4,5,6\}$（掷骰子），$\mathcal{F}=2^\Omega$（所有子集构成 $\sigma$-代数）。对每个 $A\in\mathcal{F}$，$P(A)=|A|/6$ 是均匀概率测度。连续例子：$\Omega=[0,1]$ 上的 Borel $\sigma$-代数 $\mathcal{B}([0,1])$ 包含所有开区间的可列并交；Lebesgue 测度 $\mu$ 把区间长度推广为可测集上的测度，$\mu([a,b])=b-a$。

## 容易混淆的点

### 1. 不是所有子集都必须可测

概率论并不要求对 $2^\Omega$ 的全部子集都定义概率。  
连续样本空间上这样做往往会出问题。

### 2. $\sigma$-代数不是拓扑

二者都在刻画"结构"，但关注点不同：

- 拓扑关心连续性与开集
- $\sigma$-代数关心可测性与可列运算封闭

### 3. 测度不是长度的简单复制

Lebesgue 测度（Lebesgue Measure）是长度、面积、体积的抽象推广，但测度理论远比几何长度更一般。

## 与其他条目的关系

- 前置： [集合](./集合.md)、[函数](./函数.md)、[积分](./积分.md)
- 概率线： [随机变量](./随机变量.md)、[分布](./概率分布.md)、[条件期望](./条件期望.md)
- 后续：信息流、鞅（martingale）、随机积分、卡尔曼滤波、随机控制
- 分支层： [概率与统计](../01-分支/概率与统计.md)、[分析](../01-分支/分析.md)

## 推荐教材与延伸阅读

- Billingsley, *Probability and Measure*（概率测度论的标准参考，严格而全面）
- Durrett, *Probability: Theory and Examples*（从测度论出发的概率论教材，例子丰富）
- 严加安，《测度论讲义》（中文测度论经典，精炼紧凑）

## 风险提示

- 初学时不必立刻把全部测度论细节学完，但必须知道它是现代概率的正式语言
- 若跳过可测性概念，后续理解条件期望、随机过程和滤波时会频繁出现"形式会写、对象不清"的问题
