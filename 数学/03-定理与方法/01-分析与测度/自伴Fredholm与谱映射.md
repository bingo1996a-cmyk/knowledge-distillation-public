# 自伴算子、Fredholm 理论与谱映射

## 作用

这页是对 [谱理论与紧算子](../01-分析与测度/谱理论与紧算子.md) 的继续深化，重点补三类在分析、PDE、控制与量子系统里反复出现的桥梁对象：

- 自伴算子（Self-Adjoint Operator）
- Fredholm 算子与 Fredholm 理论（Fredholm Theory）
- 谱映射定理（Spectral Mapping Theorem）

## 自伴算子

在 Hilbert 空间中，若算子 $T$ 满足

$$
\langle Tx,y\rangle=\langle x,Ty\rangle
$$

则称 $T$ 为自伴算子。

它的重要性在于：自伴结构通常对应能量、守恒、稳定模态与正交分解。有限维实对称矩阵是它的最直接原型。

## Fredholm 算子

若有界线性算子 $T$ 满足：

- $\ker T$ 维数有限
- $\operatorname{coker} T$ 维数有限
- $\operatorname{Ran}(T)$ 闭

则称其为 Fredholm 算子。其指标定义为

$$
\operatorname{ind}(T)=\dim(\ker T)-\dim(\operatorname{coker} T)
$$

这使“方程是否可解、解是否唯一、差多少维自由度”可以被精确审计。

## 谱映射定理

若 $A$ 生成半群 $e^{tA}$，则一个典型形式为

$$
\sigma(e^{tA})\setminus\{0\}=e^{t\sigma(A)}
$$

它把“生成元的谱位置”与“演化系统的增长/衰减行为”直接接了起来。

## 为什么重要

- 自伴算子提供最稳的谱分解与模态分析框架
- Fredholm 理论把 PDE、积分方程与边值问题的可解性结构化
- 谱映射定理把算子谱与动力系统稳定性连接起来
- 在控制、信号、量子、振动与演化方程中，很多“稳定 / 不稳定”判断最终都回到这里

## 推荐教材与延伸阅读

1. Reed & Simon，*Methods of Modern Mathematical Physics I: Functional Analysis (Academic Press)*——泛函分析标准参考，自伴算子与谱定理的完整论述
2. Kato，*Perturbation Theory for Linear Operators (Springer Classics)*——算子扰动与Fredholm理论的权威著作

## 风险与误区

- 无穷维下“像有限维那样对角化”往往并不成立
- 谱信息重要，但只看谱位置不一定足以给出完整瞬态行为
- Fredholm 指数稳定，不代表数值离散后条件数就一定良好
- 自伴问题较稳，但非正规算子（non-normal operator）可产生很强瞬态放大

## 最小例子

### 问题陈述
在 $L^2[0,1]$ 上考虑积分算子 $(Kf)(x) = \int_0^1 k(x,y) f(y)\,dy$，其中核函数 $k(x,y) = \min(x,y)$。验证 $K$ 是自伴紧算子，求其特征值和特征函数的显式形式。

### 数学表达
算子 $K$ 满足 $Kf = \lambda f$ 等价于积分方程 $\int_0^1 \min(x,y) f(y)\,dy = \lambda f(x)$。

### 计算/推理步骤
1. 自伴性：$k(x,y)=\min(x,y)=\min(y,x)=k(y,x)$，故 $K$ 是对称核，算子自伴。
2. 紧性：$\int_0^1\int_0^1 |k(x,y)|^2 dx dy = \int_0^1\int_0^1 \min(x,y)^2 dx dy < \infty$，故 $K$ 是 Hilbert-Schmidt 算子，必为紧算子。
3. 特征问题：将积分方程两次微分。令 $g(x) = \int_0^1 \min(x,y) f(y)\,dy = \int_0^x y f(y)\,dy + x\int_x^1 f(y)\,dy$。求导得 $g'(x) = x f(x) + \int_x^1 f(y)\,dy - x f(x) = \int_x^1 f(y)\,dy$，再求导得 $g''(x) = -f(x)$。代入 $g = \lambda f$ 得 $-\lambda f''(x) = f(x)$，即 $f''(x) + \frac{1}{\lambda} f(x) = 0$。
4. 边条件：$g(0)=0$ 只给出平凡条件；$g'(1) = 0$ 得 $f'(1) = 0$。解得 $\lambda_n = \frac{4}{(2n-1)^2\pi^2}$，$f_n(x) = \sqrt{2}\sin\left(\frac{(2n-1)\pi x}{2}\right)$。

### 结果解读
本例展示了自伴紧算子的标准分析路线：对称核 $\to$ Hilbert-Schmidt 紧性 $\to$ 可数实谱 $\to$ 显式特征函数。$\min(x,y)$ 核恰好对应协方差核（Brownian bridge 的协方差），这使其在随机过程与统计学习中非常基本。

## 在资源受限条件下的可行最优路径

1. [Banach 空间与 Hilbert 空间](../../02-核心概念/Banach空间与Hilbert空间.md)
2. [泛函分析：Banach、Hilbert 与算子](../01-分析与测度/泛函分析Banach-Hilbert与算子.md)
3. [谱理论与紧算子](../01-分析与测度/谱理论与紧算子.md)
4. 本页
5. [算子半群与演化方程](../01-分析与测度/算子半群与演化方程.md)、[PDE 正则性、分布解与有限元](../01-分析与测度/PDE正则性分布与有限元.md)

## 与其他条目的关系

- 前置： [紧算子与谱](../../02-核心概念/紧算子与谱.md)
- 相关： [算子半群与演化方程](../01-分析与测度/算子半群与演化方程.md)
- 相关： [随机系统与演化方程中的数学](../../04-应用/随机系统与演化方程中的数学.md)
