# 解析延拓与 Riemann zeta 函数

## 作用

解析延拓（Analytic Continuation）是复分析中最深刻的概念之一——它允许一个原本只在较小区域定义的解析函数被"延拓"到更大的区域，且延拓方式是唯一的。Riemann zeta 函数 $\zeta(s)$ 是其最著名的例子：最初只在 $\operatorname{Re}s>1$ 上由 Dirichlet 级数定义，但可解析延拓到除 $s=1$ 外的整个复平面，从而揭示素数与复分析之间最深层的联系。

## 解析延拓的基本原理

若 $f$ 在区域 $D$ 上解析，$g$ 在区域 $D'$（$D\cap D'\neq\emptyset$）上解析，且 $f=g$ 在 $D\cap D'$ 上成立，则 $g$ 是 $f$ 到 $D'$ 的**直接解析延拓**。

**唯一性定理**：若 $f$ 和 $g$ 在某区域上解析，且在具有聚点的点集上相等，则 $f\equiv g$。

这意味着一旦在"一小片"上确定了函数值，它在整个连通区域上的值就唯一确定了。

## Riemann zeta 函数

### Dirichlet 级数定义（$\operatorname{Re}s>1$）

$$
\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \prod_{p\text{ prime}}\frac{1}{1-p^{-s}}
$$

其中 Euler 乘积将 zeta 函数与所有素数连接起来。

### 函数方程

$\zeta(s)$ 满足：

$$
\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right)\Gamma(1-s)\zeta(1-s)
$$

这个对称性（$s\leftrightarrow 1-s$）是 Riemann 假设——所有非平凡零点位于 $\operatorname{Re}s=1/2$ 上的核心动机。

### Riemann 假设

Riemann zeta 函数的所有非平凡零点都具有实部 $1/2$。这是数学中最重要的未解决问题之一，与素数分布的精确估计直接相关。

## 最小例子

### 例 1：几何级数的解析延拓

$f(z)=\sum_{n=0}^\infty z^n$ 在 $|z|<1$ 上收敛，和函数为 $\frac{1}{1-z}$。而 $\frac{1}{1-z}$ 在 $\mathbb{C}\setminus\{1\}$ 上解析，它是该级数到整个复平面（除 $z=1$）的自然延拓。

关键点：原级数仅在单位圆盘内收敛，但和函数却可以定义在更大的区域上。

### 例 2：$\zeta(2)$ 的计算（Basel 问题）

Euler 证明了 $\zeta(2)=\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$。这是解析数论的起点——素数分布通过 Euler 乘积与 zeta 值相关联，zeta 的特殊值又回到 $\pi$。

### 例 3：Gamma 函数的解析延拓

$\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}dt$ 最初只对 $\operatorname{Re}z>0$ 定义。利用函数方程 $\Gamma(z+1)=z\Gamma(z)$，可延拓到除 $z=0,-1,-2,\dots$ 外的整个复平面。

## 与其他概念的关系

- 前置： [复分析与 Cauchy 理论](./复分析与Cauchy理论.md)、[留数定理](./留数定理及其应用.md)
- 延伸：Dirichlet L-函数、模形式、Langlands 纲领
- 交叉： [二次互反律与素数分布](../02-代数与数论/二次互反律与素数分布.md)

## 推荐教材与延伸阅读

1. Stein & Shakarchi, *Complex Analysis*（Princeton Lectures in Analysis II）——第6-7章对解析延拓和zeta函数有极清晰的论述。
2. Edwards, *Riemann's Zeta Function*（Dover）——Riemann原始论文的详尽解读。
3. Titchmarsh, *The Theory of the Riemann Zeta-Function*（2nd ed., Oxford）——zeta函数的经典专著。
