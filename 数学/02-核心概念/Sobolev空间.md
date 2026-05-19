# Sobolev 空间

## 概念

Sobolev 空间（Sobolev Space）用于描述“函数本身以及其弱导数都具有一定可积性”的函数类。它是把“可微”从经典点值意义放宽到积分意义后的自然空间。

典型记号为

$$
W^{k,p}(\Omega)=\{u\in L^p(\Omega): D^\alpha u\in L^p(\Omega),\ |\alpha|\le k\}
$$

其中 $D^\alpha$ 表示弱导数，$k$ 是可微阶数，$p$ 描述可积性。

## 为什么重要

- 经典导数不存在时，弱导数仍可能存在
- 变分法、有限元、PDE 弱解通常以 Sobolev 空间为舞台
- 正则性、嵌入定理、边界条件与数值离散都依赖它

## 关键点

- $H^k(\Omega)$ 常表示 $W^{k,2}(\Omega)$
- 弱导数不是“近似导数”，而是通过积分分部定义的广义导数
- Sobolev 空间既服务纯分析，也服务工程数值法

## 最小例子

**问题**：函数 \(f(x)=|x|\) 在区间 \((-1,1)\) 上是否属于 \(H^1(-1,1)\)？它的弱导数是什么？

**解**：\(f\in L^2(-1,1)\)。考虑测试函数 \(\varphi\in C_c^\infty(-1,1)\)，分部积分得 \(\int_{-1}^1 |x|\varphi'(x)dx = -\int_{-1}^1 \operatorname{sgn}(x)\varphi(x)dx\)，其中 \(\operatorname{sgn}(x)\) 当 \(x>0\) 为 1、\(x<0\) 为 -1。因此弱导数为 \(v(x)=\operatorname{sgn}(x)\in L^2\)，故 \(f\in H^1(-1,1)\)。经典导数在 \(x=0\) 处不存在，但弱导数存在——这就是 Sobolev 空间的关键意义。

## 相关条目

- [Banach 空间与 Hilbert 空间](./Banach空间与Hilbert空间.md)
- [PDE、弱解与变分方法](../03-定理与方法/01-分析与测度/PDE弱解与变分方法.md)
- [Sobolev 空间与弱导数](../03-定理与方法/01-分析与测度/Sobolev空间与弱导数.md)
