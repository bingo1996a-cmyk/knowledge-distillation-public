# Girsanov 定理、Doob 分解与局部鞅

## 作用

这一页连接三个经常一起出现但常被分散学习的主题：

- **Doob 分解（Doob Decomposition）**：把离散时间次鞅拆成"鞅部分 + 可预测漂移部分"
- **局部鞅（Local Martingale）**：解释为什么很多随机过程看起来像鞅，但只在停时截断后才真的是鞅
- **Girsanov 定理（Girsanov Theorem）**：解释在改变概率测度后，随机过程的漂移项怎样变化

它们共同支撑随机分析、金融数学、非线性滤波、风险敏感控制与连续时间决策。

## 一个最小框架

### 1. Doob 分解

离散时间可积次鞅 $X_n$ 常可写为

$$
X_n = M_n + A_n
$$

其中 $M_n$ 是鞅，$A_n$ 是可预测、递增过程。

### 2. 局部鞅

若存在停时序列 $\tau_k \uparrow \infty$，使得每个截断过程 $X^{\tau_k}$ 都是鞅，则称 $X$ 为局部鞅。

### 3. Girsanov 变换

对 Brownian Motion $W_t$，若漂移过程满足适当可积条件，则在新测度 $Q$ 下，

$$
\widetilde{W}_t = W_t - \int_0^t \theta_s\, ds
$$

成为 Brownian Motion。测度密度通常写作指数鞅形式

$$
\frac{dQ}{dP}\Big|_{\mathcal{F}_t}
=
\exp\!\left(
\int_0^t \theta_s\, dW_s
-
\frac12\int_0^t \|\theta_s\|^2 ds
\right)
$$

## 为什么重要

### 1. 它解释"随机过程的漂移来自哪里"

Doob 分解把"系统性漂移"和"真正不可预测扰动"分开。

### 2. 它解释"为什么换一个概率视角，动力学会变"

Girsanov 不是魔法，而是把漂移吸收到测度中。

### 3. 它是风险评估与连续时间控制的桥

风险中性定价、重要性采样、风险敏感控制与部分滤波推导中都会遇到测度变换。

## 风险与误区

- 局部鞅不一定是真鞅，期望性质可能失效
- Girsanov 需要可积条件，常见的是 Novikov 条件；条件不满足时，指数局部鞅未必给出合法测度
- Doob 分解在离散和连续时间表述不同，不能直接混用

## 最小例子

### 问题陈述
设标量扩散过程
$$
dX_t = \mu\, dt + \sigma\, dW_t,
\quad X_0 = 0
$$
其中 $W_t$ 是 $(\Omega,\mathcal{F},P)$ 下的标准 Brownian Motion。我们希望找到一个新概率测度 $Q$，使得在新测度下该过程不再有漂移（成为一个鞅）。

### 数学表达
取 $\theta = \mu/\sigma$（常数），定义
$$
\frac{dQ}{dP}\Big|_{\mathcal{F}_T}
= \exp\!\left(
\int_0^T \theta\, dW_s - \frac12 \int_0^T \theta^2 ds
\right)
= \exp\!\left(
\theta W_T - \frac12 \theta^2 T
\right)
$$
这是一个指数鞅（满足 Novikov 条件），因此 $Q$ 是合法概率测度。

### 计算/推理步骤
1. 由 Girsanov 定理，在 $Q$ 下
   $$
   \widetilde{W}_t = W_t - \theta t
   $$
   是标准 Brownian Motion。
2. 将原过程用 $\widetilde{W}_t$ 重写：
   $$
   dX_t = \mu\, dt + \sigma\, (d\widetilde{W}_t + \theta\, dt)
        = (\mu + \sigma\theta)\, dt + \sigma\, d\widetilde{W}_t
   $$
3. 代入 $\theta = \mu/\sigma$ 得 $\mu + \sigma\theta = 0$，于是
   $$
   dX_t = \sigma\, d\widetilde{W}_t
   $$
   在 $Q$ 下 $X_t$ 是无漂移的扩散过程（鞅）。

### 结果解读
Girsanov 定理的核心洞见是：**漂移不是过程的固有属性，而是依赖于我们选择的概率视角**。本例说明，通过适当的测度变换，一个带漂移的 Brownian 运动在新的概率测度下可以变成无漂移的鞅。这正是金融中风险中性定价的理论基础——在风险中性测度下，所有资产的折现价格都是鞅。

## 在资源受限条件下的可行最优路径

1. 先掌握 [Radon–Nikodym、弱收敛与测度变换](../01-分析与测度/Radon-Nikodym弱收敛与测度变换.md)
2. 再回看 [鞅与停时](../01-分析与测度/鞅与停时.md)
3. 然后进入 [随机微积分与 Itô 公式](../01-分析与测度/随机微积分与Ito公式.md)
4. 最后再读 Girsanov、局部鞅与测度变换在控制或金融中的应用

## 与其他条目的关系

- 前置： [测度概率基础](../01-分析与测度/测度论概率基础.md)
- 前置： [鞅与停时](../01-分析与测度/鞅与停时.md)
- 前置： [随机微积分与 Itô 公式](../01-分析与测度/随机微积分与Ito公式.md)
- 相关： [风险敏感控制与微分博弈](../05-优化与控制/风险敏感控制与微分博弈.md)
- 相关： [Kalman-Bucy 滤波与非线性滤波](../06-数值与计算/Kalman-Bucy与非线性滤波.md)
- 路径： [测度概率与随机分析路线](../../05-学习路径/测度概率与随机分析.md)

## 推荐教材与延伸阅读

1. Karatzas, I. & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus* (2nd ed.). Springer. — 第 3 章 Girsanov 定理，第 1 章 Doob 分解与局部鞅
2. Revuz, D. & Yor, M. (1999). *Continuous Martingales and Brownian Motion* (3rd ed.). Springer. — 测度变换与局部鞅理论的深入标准参考
3. Steele, J. M. (2001). *Stochastic Calculus and Financial Applications*. Springer. — Girsanov 定理在金融中直观应用的优秀入门
