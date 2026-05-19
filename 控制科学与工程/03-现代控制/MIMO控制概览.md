# MIMO 控制概览 (Overview of MIMO Control)

## 定位

从 SISO 到 MIMO 的跃迁不只是维度的增加——耦合、方向性和交互是 MIMO 控制的核心新问题。在 MIMO 系统中，每个输入可能影响多个输出，每个输出可能受多个输入影响，这使得单变量设计方法（如 SISO 根轨迹、Bode 图）不再直接适用。

MIMO 控制需要全新的分析工具和设计理念来理解和处理系统内部的交互关系。

## 核心问题

**问题一：如何处理输入-输出之间的耦合？**

MIMO 系统的耦合意味着调整一个参考值会同时干扰其他回路。如何量化耦合的强弱？解耦是否必要和有益？

**问题二：如何分析多变量系统的增益方向性？**

SISO 系统只有一个增益值（Bode 幅值）。MIMO 系统的增益是方向相关的——在不同输入方向上，系统表现出不同的放大倍数。如何全面描述这种方向性？

## 基本模型

### 多变量传递函数

MIMO 系统的传递函数矩阵 $G(s) \in \mathbb{C}^{p \times m}$：

$$
y(s) = G(s) u(s), \quad G(s) = C(sI - A)^{-1}B + D
$$

其中 $p$ 为输出维数，$m$ 为输入维数。

### 相对增益阵列 (RGA)

RGA（Relative Gain Array）是 MIMO 耦合分析最常用的工具。定义：

$$
\Lambda(G) = G \times (G^{-1})^T \quad \text{（逐元素相乘）}
$$

RGA 元素 $\lambda_{ij}$ 表示第 $j$ 个输入对第 $i$ 个输出的影响程度（考虑其他回路开环 vs 闭环）：
- $\lambda_{ij} \approx 1$：耦合弱，可独立控制；
- $\lambda_{ij} \approx 0$：该通道对该输入不敏感；
- $\lambda_{ij} > 1$：回路间存在增益放大；
- $\lambda_{ij} < 0$：回路交互反相，可能导致失稳。

### 奇异值分解 (SVD)

对频率响应矩阵 $G(j\omega)$ 做 SVD：

$$
G(j\omega) = U(\omega) \Sigma(\omega) V^H(\omega)
$$

其中 $\Sigma(\omega) = \text{diag}(\sigma_1(\omega), \ldots, \sigma_k(\omega))$ 为奇异值，$\sigma_{\max}(\omega)$ 和 $\sigma_{\min}(\omega)$ 分别表示该频率下的最大和最小增益方向。

### 条件数

条件数 $\kappa(G) = \sigma_{\max} / \sigma_{\min}$ 是 MIMO 系统方向敏感性的度量：
- $\kappa \approx 1$：系统各方向增益均匀（良态, well-conditioned）
- $\kappa \gg 1$：系统在某些方向上增益极弱（病态, ill-conditioned）

## 解耦控制方法

| 方法 | 描述 | 适用场景 |
|:---|:---|:---|
| 静态解耦 | $K = G^{-1}(0)K_{diag}$ 低频解耦 | 低频主导的过程 |
| 动态解耦 | $K(s) = G^{-1}(s)K_{diag}(s)$ 全频段解耦 | 精确解耦要求高 |
| 前置补偿器 | 在控制器前串联解耦矩阵 | 简化多变量设计 |
| 分散式控制 | 忽略耦合，独立设计 SISO 回路 | 弱耦合系统 |

## 关键概念

### MIMO 的零点和极点

- **传输零点（Transmission Zeros）**：使 $G(s)$ 降秩的 $s$ 值。MIMO 零点可以阻止特定方向信号的传输，且不一定是解耦零点。
- **解耦零点（Decoupling Zeros）**：源于不可控或不可观模态，分为输入解耦零点和输出解耦零点。
- **McMillan 阶数**：最小实现的阶数，等于系统极点的个数（计入重数）。

MIMO 零点对控制系统有重要影响：右半平面零点限制可实现带宽、限制可达到的性能。

### 结构奇异值 mu (Structured Singular Value)

$\mu$ 分析是 MIMO 鲁棒性分析的核心工具。结构化奇异值 $\mu_{\Delta}(M)$ 衡量在结构化不确定性 $\Delta$ 下系统保持稳定的最小扰动规模：

$$
\mu_{\Delta}(M) = \frac{1}{\min\{\bar{\sigma}(\Delta) : \det(I - M\Delta) = 0, \Delta \in \boldsymbol{\Delta}\}}
$$

$\mu < 1$ 保证系统对所有考虑的结构化不确定性具有鲁棒稳定性。

## 工程判断

### 什么时候需要解耦

- 强耦合系统（RGA 元素偏离 1 较大）：通常需要解耦或全 MIMO 设计；
- 弱耦合系统（RGA 近似为单位阵）：分散式 PID 控制已足够；
- 大 RGA 元素提示系统对模型误差敏感——即使解耦后鲁棒性仍需验证。

### 工程实用方法

- **顺序调环法（Sequential Loop Closing）**：先调最慢的回路，然后依次闭合其他回路；
- **独立调环法（Decentralized Control）**：忽略耦合各自调参，然后用 RGA 分析交互频率降级接受；
- 工业过程控制中：分散式 PID 结合 RGA 分析是最常见的选择。

### MIMO PID 调参

- 使用 BLT（Biggest Log-Modulus Tuning）方法在多变量系统中调整 PID 参数；
- 在 Nyquist 阵列上画 Gershgorin 带分析回路交互；
- 最终 PID 参数需在非线性仿真中验证。

## 常见误区

### "MIMO 系统可以简化为多个独立的 SISO 环路"
忽略耦合交互可能导致失稳。需通过 RGA 或其他耦合分析确认耦合强度。

### "全解耦总是好的"
解耦可能牺牲性能并引入额外动态。动态解耦可能产生非最小相位特性或极高的控制器阶数。

### "SISO 的频域工具可以无修改地用于 MIMO"
Bode 图和 Nyquist 判据推广到 MIMO 时需要特征轨迹（characteristic loci）方法，不再是简单的 SISO 图形。

## 回链

- [线性系统理论路线图](./线性系统理论路线图.md)
- [分布式与分散式控制](../04-最优鲁棒自适应控制/分布式与分散式控制.md)
- [状态反馈与极点配置](./状态反馈与极点配置.md)
- [Bode 图](../02-经典控制/Bode图.md)
