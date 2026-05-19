# Banach 空间与 Hilbert 空间

## 它们是什么

Banach 空间（Banach Space）是带范数且完备的线性空间。Hilbert 空间（Hilbert Space）是内积诱导范数下完备的线性空间。

## 形式定义

设线性空间 $X$ 带范数 $\|\cdot\|$。若任意 Cauchy 列在该范数下收敛于 $X$ 内元素，则 $X$ 是 Banach 空间。

若存在内积 $\langle \cdot,\cdot\rangle$，并由

$$
\|x\|=\sqrt{\langle x,x\rangle}
$$

诱导范数，且空间完备，则它是 Hilbert 空间。

## 为什么重要

- Banach 空间适合研究一般函数空间与算子
- Hilbert 空间保留正交投影、最小二乘与谱分解等强结构
- 现代 PDE、量子力学、核方法、控制与反问题都离不开它们

## 最小例子

$\mathbb{R}^n$ 带欧氏范数 $\|x\|_2=\sqrt{x_1^2+\cdots+x_n^2}$ 是 Hilbert 空间（内积诱导范数且完备）。$\mathbb{R}^n$ 带 $p$-范数 $\|x\|_p=(|x_1|^p+\cdots+|x_n|^p)^{1/p}$（$p\neq 2$）是 Banach 空间但非 Hilbert——因为平行四边形法则 $\|x+y\|^2+\|x-y\|^2=2(\|x\|^2+\|y\|^2)$ 对 $p\neq2$ 不成立。函数空间 $L^2[0,1]$ 也是 Hilbert 空间，内积 $\langle f,g\rangle=\int_0^1 f(t)g(t)dt$。

## 推荐教材与延伸阅读

- Kreyszig, *Introductory Functional Analysis with Applications*（泛函分析入门的标准教材）
- Conway, *A Course in Functional Analysis*（Hilbert 空间部分尤为精炼）
- 张恭庆等，《泛函分析讲义》（中文经典，理论与应用兼顾）

## 与哪些内容相关

- [泛函分析](../01-分支/泛函分析.md)
- [内积](./内积.md)
- [范数与正定性](./范数与正定性.md)
- [泛函分析：Banach、Hilbert 与算子](../03-定理与方法/01-分析与测度/泛函分析Banach-Hilbert与算子.md)
