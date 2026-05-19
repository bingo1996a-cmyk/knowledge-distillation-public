# 曲率与 Gauss-Bonnet 定理

## 作用

Gauss-Bonnet 定理是微分几何中最优美的定理之一——它将曲面的局部几何量（Gauss 曲率 $K$）的积分与全局拓扑不变量（Euler 示性数 $\chi$）联系起来：$\int_M K dA = 2\pi\chi(M)$。这是"局部+局部+...= 全局拓扑"这一模式的范式，启发了 Atiyah-Singer 指标定理和 Chern-Weil 理论。

## 一、Gauss 曲率

### 定义

曲面上一点 $p$ 的 Gauss 曲率 $K(p)=\kappa_1\kappa_2$（两个主曲率的乘积）。主曲率是法截面曲线的最大和最小曲率。

- $K>0$（球面）：两个主方向同向弯曲——点状短程线局部汇聚
- $K<0$（鞍面）：两个主方向反向弯曲——短程线发散
- $K=0$（平面/柱面）：至少一个方向是直的

**Theorema Egregium（绝妙定理）**：Gauss 曲率 $K$ 仅依赖于度量张量 $g_{ij}$ 及其一阶和二阶导数——曲率是**内蕴**的（不依赖于曲面如何嵌入在三维空间中）。这意味着二维生物仅通过测地线和角度测量就可以"感知"他们世界的曲率，无需仰望三维。

### 最小例子：球面与伪球面

- 球面 $S^2(R)$：$K=1/R^2$（正定常）
- 伪球面（tractricoid）：$K=-1$（负定常）

球面三角形（三个大圆弧）内角和 $>180^\circ$。Gauss 曲率与"角盈"的关系：$\iint_T K dA = \alpha+\beta+\gamma-\pi$（Gauss 的局部 Gauss-Bonnet）。

## 二、Gauss-Bonnet 定理

### 全局形式

对于紧致无边可定向曲面 $M$：
$$
\int_M K dA = 2\pi\chi(M)
$$

其中 $\chi(M)=2-2g$（$g$ 为亏格）。

**拓扑含义**：左边是局部几何量 $K$ 的积分，右边是拓扑不变量——它只取决于曲面有多少个"洞"。

- 球面（$g=0$）：$\int K = 4\pi$ → 平均曲率 $=1/R^2$（$R$ 为半径）
- 环面（$g=1$）：$\int K = 0$ → 环面上曲率的正部与负部恰好抵消
- 双环面（$g=2$）：$\int K = -4\pi$

### 边界形式

若 $M$ 有边界 $\partial M$，需加测地曲率项：
$$
\int_M K dA + \int_{\partial M} k_g ds = 2\pi\chi(M)
$$

### 最小例子：环面的 Gauss-Bonnet 验证

环面可参数化使 $K(\theta,\phi)=\frac{\cos\theta}{R(R+r\cos\theta)}$。外圈 $\theta\in(0,\pi)$ 上 $K>0$（椭圆点），内圈 $\theta\in(\pi,2\pi)$ 上 $K<0$（双曲点）。积分 $\iint K dA = 2\pi\cdot0=0$——正负曲率精确抵消。

## 三、推广与影响

### Chern-Gauss-Bonnet 定理（Chern 1944）

将 Gauss-Bonnet 推广到任意偶数维紧致 Riemann 流形 $M^{2n}$：
$$
\int_M \operatorname{Pf}(\Omega) = (2\pi)^n\chi(M)
$$

其中 $\operatorname{Pf}$ 是 Pfaffian（曲率 2-形式的多项式）。这是微分几何的里程碑——将 Gauss 的曲面定理推广到任意维。

### Atiyah-Singer 指标定理

Gauss-Bonnet 是 Atiyah-Singer 定理的特例之一。更一般的指标定理将椭圆微分算子的解析指标与拓扑不变量联系——这是 20 世纪数学最深刻的成就之一。

## 四、三角形的角盈与角亏

### Gauss-Bonnet 的局部形式

对测地三角形 $T$：
$$
\iint_T K dA = \alpha+\beta+\gamma-\pi
$$

- 球面（$K>0$）：三角形内角和 $>\pi$（角盈）
- 平面（$K=0$）：内角和 $=\pi$
- 双曲面（$K<0$）：内角和 $<\pi$（角亏）

### 最小例子：球面上的等边三角形

球面 $S^2$ 上三个直角构成的三角形（各顶点在 $(1,0,0),(0,1,0),(0,0,1)$）。各角 $\pi/2$，内角和 $3\pi/2$。三角形面积占球面的 $1/8$（球面积的 $1/8=\pi R^2/2$）。$K=1/R^2$。$\iint K dA = (1/R^2)\cdot(\pi R^2/2) = \pi/2 = 3\pi/2-\pi$——验证。

## 推荐教材与延伸阅读

1. do Carmo, *Differential Geometry of Curves and Surfaces*（2nd ed., Dover）——第4章 Gauss-Bonnet 的经典推导。
2. Spivak, *A Comprehensive Introduction to Differential Geometry, Vol. III*（Publish or Perish）——Gauss-Bonnet 从局部到全局的完整论述。
3. Chern, "A Simple Intrinsic Proof of the Gauss-Bonnet Formula"（Annals 1944）——Chern 的原始论文。

## 与其他概念的关系

- 前置：[联络、曲率与测地线](./联络曲率与测地线.md)
- 前置：[曲线曲面与流形的微分几何](./曲线曲面与流形的微分几何.md)
- 延伸：Chern-Weil 理论、Atiyah-Singer 指标定理
