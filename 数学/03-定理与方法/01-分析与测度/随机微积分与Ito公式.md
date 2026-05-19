# 随机微积分与 Itô 公式

## 作用

随机微积分（Stochastic Calculus）研究带有布朗运动噪声的连续时间随机系统。  
It\^o 公式（It\^o Formula）则是随机分析中的“链式法则”，是随机控制、连续时间滤波、金融数学和扩散过程分析的核心工具。

## 为什么普通微积分不够

对布朗运动 $W_t$ 而言，其轨道几乎处处不可导。  
因此表达式

$$
dW_t
$$

不能按普通导数那样理解。

随机微积分的关键在于：布朗运动虽然不可导，但具有稳定的二次变差（quadratic variation）：

$$
[W]_t=t
$$

这正是 It\^o 公式与普通链式法则不同的根源。

## Itô 过程

典型的连续时间状态过程写成

$$
dX_t=b(X_t,t)\,dt+\sigma(X_t,t)\,dW_t
$$

其中：

- $b$ 是漂移项（drift）
- $\sigma$ 是扩散项（diffusion）
- $W_t$ 是布朗运动（Brownian Motion）

## Itô 公式

若 $X_t$ 满足上式，且 $f(t,x)$ 足够光滑，则

$$
df(t,X_t)=\left(\partial_t f + b\,\partial_x f + \frac12\sigma^2\partial_{xx}f\right)dt + \sigma\,\partial_x f\, dW_t
$$

多维情形可写为

$$
df(t,X_t)=\left(\partial_t f + \nabla f^\top b + \frac12\operatorname{tr}(\sigma\sigma^\top \nabla^2 f)\right)dt + \nabla f^\top \sigma\, dW_t
$$

## 与普通链式法则的差异

普通链式法则里不会出现二阶项。  
It\^o 公式多出的

$$
\frac12\sigma^2\partial_{xx}f
$$

正是由布朗运动的二次变差产生的。

## 一个典型例子

若 $X_t=W_t$，取 $f(x)=x^2$，则由 It\^o 公式：

$$
d(W_t^2)=2W_t\,dW_t + dt
$$

积分后得

$$
W_t^2=t+2\int_0^t W_s\,dW_s
$$

这清楚展示了额外的 $dt$ 项。

## 为什么重要

### 1. 它是连续时间随机控制与滤波的基础

HJB 方程中的扩散项、连续时间 Kalman-Bucy 滤波、随机最优控制都依赖 It\^o 计算。

### 2. 它是随机微分方程理论的核心工具

很多稳定性、矩估计、变换公式与生成元（generator）分析都从 It\^o 公式出发。

### 3. 它把概率、微分方程与控制统一起来

随机系统不是简单“在 ODE 上加噪声”，而是需要全新的微分规则。

## 关键假设与前提检查

1. 过程是否确实可由 It\^o 过程建模
2. 函数 $f$ 是否满足所需光滑条件
3. 噪声是加性还是乘性，是否多维
4. 需要的是 It\^o 解释还是 Stratonovich 解释

## 最小例子

### 问题陈述
设 $X_t = W_t$ 为标准布朗运动，计算随机微分 $d(W_t^2)$ 并用 It\^o 公式验证。比较 It\^o 公式与经典微积分链式法则的差异。

### 数学表达
It\^o 公式（一维）：对 $f \in C^2$ 有 $df(X_t) = f'(X_t) dX_t + \frac12 f''(X_t) d[X]_t$。取 $f(x) = x^2$，$X_t = W_t$，$dW_t = 0 dt + 1 dW_t$，二次变差 $d[W]_t = dt$。

### 计算/推理步骤
1. $f'(x) = 2x$，$f''(x) = 2$。代入 It\^o 公式：
   $$
   d(W_t^2) = 2W_t\, dW_t + \frac12 \cdot 2\, dt = 2W_t\, dW_t + dt
   $$
2. 积分形式：$W_t^2 = 2\int_0^t W_s\, dW_s + t$。注意这里 $t$ 项来自二次变差。
3. 与经典微积分对比：若 $W_t$ 是确定性可微函数，$d(W_t^2) = 2W_t dW_t$。多出的 $dt$ 项完全由 Brownian 运动的非零二次变差（$d[W]_t = dt$）产生。
4. 验证期望：$\mathbb{E}[W_t^2] = t$，而 $\mathbb{E}[2\int_0^t W_s dW_s] = 0$（It\^o 积分的鞅性），故 $\mathbb{E}[W_t^2] = t$ 与 $t$ 项完全对应。

### 结果解读
本例展示了 It\^o 公式与经典链式法则的根本差异：**随机微积分中需要额外补偿项 $\frac12 f''(X_t) d[X]_t$**，这来源于 Brownian 运动二次变差不为零。$W_t^2$ 不是鞅（因为期望是 $t$），这正是 $dt$ 项的影响。这一机制对所有随机分析、金融建模和随机控制都是基础性的。

## 风险与约束

- It\^o 与 Stratonovich 积分不可混用
- 若忽略二次变差项，会得到错误推导
- 连续时间模型常依赖较强理想化假设
- 数值模拟 SDE 时，还需考虑 Euler-Maruyama 等离散化误差

## 在资源受限条件下的可行最优路径

1. 先学布朗运动与二次变差
2. 再学 It\^o 积分与 It\^o 公式
3. 再进入 SDE、HJB 与随机控制
4. 工程应用上先会用线性高斯与离散近似，再上更严格随机分析

## 与其他条目的关系

- 前置： [泊松过程与布朗运动](../01-分析与测度/Poisson过程与Brown运动.md)、[鞅与停时](../01-分析与测度/鞅与停时.md)
- 前序： [HJB 方程](../05-优化与控制/HJB方程.md)
- 后续： 随机控制、连续时间滤波、Fokker-Planck 方程

## 推荐教材与延伸阅读

- Øksendal, B. (2003). *Stochastic Differential Equations: An Introduction with Applications*, 6th ed. Springer. — 最经典的 SDE 入门教材，从布朗运动到 Itô 公式再到应用。
- Karatzas, I. & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer. — 更严格的处理，适合需要深厚理论准备的读者。
- Steele, J. M. (2001). *Stochastic Calculus and Financial Applications*. Springer. — 侧重金融应用，例子丰富且直觉性强。
