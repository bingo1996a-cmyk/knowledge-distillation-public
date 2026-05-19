# Lie 代数的分类与表示

## 作用

Lie 代数（Lie Algebra）是 Lie 群的"线性化"——群在单位元处的切空间带上 Lie 括号。Lie 代数的分类（特别是半单 Lie 代数的 Cartan-Killing 分类）是 20 世纪数学的伟大成就之一，在对称性分析、粒子物理（标准模型的规范群）和可积系统中起核心作用。

## Lie 代数的基本结构

Lie 代数 $\mathfrak{g}$ 是带有双线性反对称括号 $[\cdot,\cdot]$ 的向量空间，满足 Jacobi 恒等式：

$$
[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0
$$

**典型案例**：
- $\mathfrak{so}(3)$：三维旋转 Lie 代数，$[X_i,X_j]=\epsilon_{ijk}X_k$，对应角动量对易关系
- $\mathfrak{sl}(2,\mathbb{C})$：迹为零的 $2\times2$ 矩阵，基 $H,X,Y$ 满足 $[H,X]=2X,[H,Y]=-2Y,[X,Y]=H$

### 半单性

Lie 代数 $\mathfrak{g}$ 是**半单**的 ⟺ 它不含非平凡 Abel 理想 ⟺ Killing 型 $\kappa(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ 非退化。

## Cartan-Killing 分类

半单复 Lie 代数由 Dynkin 图完全分类：

| 系列 | Dynkin 图 | 维数 | 对应 |
|------|----------|------|------|
| $A_n$ | $n$ 个节点连成线 | $n(n+2)$ | $\mathfrak{sl}(n+1,\mathbb{C})$ |
| $B_n$ | 最后两端为双箭头 | $n(2n+1)$ | $\mathfrak{so}(2n+1,\mathbb{C})$ |
| $C_n$ | 最后两端为反向双箭头 | $n(2n+1)$ | $\mathfrak{sp}(2n,\mathbb{C})$ |
| $D_n$ | 最后节点分叉 | $n(2n-1)$ | $\mathfrak{so}(2n,\mathbb{C})$ |
| $G_2,F_4,E_{6,7,8}$ | — | — | 例外 Lie 代数 |

**根系统**：半单 Lie 代数的结构完全由根 $\alpha$（Cartan 子代数上的线性泛函）和根系决定。Weyl 群作用于根系，提供对称性的群论解释。

## 表示论要点

有限维不可约表示由最高权 $\lambda$ 唯一决定。$\mathfrak{sl}(2,\mathbb{C})$ 是最简单的例子——不可约表示由最高权 $m$（非负整数）标记，维数为 $m+1$。

## 最小例子

### 例 1：$\mathfrak{sl}(2,\mathbb{C})$ 的不可约表示

基 $H,X,Y$ 满足 $[H,X]=2X,[H,Y]=-2Y,[X,Y]=H$。最高权 $m$ 的不可约表示 $V_m$：
- 基 $\{v_0,v_1,\dots,v_m\}$
- $H v_k = (m-2k)v_k$
- $X v_k = (m-k+1)v_{k-1}$（$X v_0=0$）
- $Y v_k = (k+1)v_{k+1}$（$Y v_m=0$）

验证 $[X,Y]v_k = XYv_k - YXv_k = \cdots = H v_k$。$\mathfrak{sl}(2)$ 的表示是所有更高秩 Lie 代数表示理论的基本构件。

### 例 2：$\mathfrak{so}(3)$ 与角动量

$\mathfrak{so}(3)$ 是 $A_1$ 型（$\cong \mathfrak{sl}(2,\mathbb{C})$ 的紧实形）。不可约表示由角动量量子数 $\ell=0,\frac12,1,\frac32,\dots$ 标记，维数 $2\ell+1$。球谐函数 $Y_{\ell m}(\theta,\phi)$ 正是 SO(3) 的不可约表示的基函数。

## 与其他概念的关系

- 前置： [Lie 群与 Lie 代数](../../02-核心概念/Lie群与Lie代数.md)
- 前置： [Lie 群、Lie 代数与几何控制](./Lie群Lie代数与几何控制.md)
- 延伸：Kac-Moody 代数（无穷维推广）、量子群、共形场论
- 应用： [物理中的数学](../../04-应用/物理中的数学.md)

## 推荐教材与延伸阅读

1. Humphreys, *Introduction to Lie Algebras and Representation Theory*（Springer GTM 9）——Lie 代数分类的标准入门教材。
2. Fulton & Harris, *Representation Theory: A First Course*（Springer GTM 129）——表示论的绝佳入门，$\mathfrak{sl}(2)$ 的论述极为详尽。
3. Hall, *Lie Groups, Lie Algebras, and Representations*（2nd ed., Springer GTM 222）——Lie 群到 Lie 代数的完整桥梁。

## 待补充

- 实 Lie 代数的分类
- 例外 Lie 代数的构造
- Verma 模与最高权表示的一般理论
