# Kalman-Bucy 与非线性滤波

## 作用

Kalman-Bucy 滤波处理连续时间线性高斯系统，非线性滤波则研究在非线性、非高斯和连续观测条件下如何递推估计隐藏状态。

## 一个连续时间线性模型

常见模型写为

$$
dx_t = A x_t\,dt + G\,dW_t,\qquad
dy_t = C x_t\,dt + D\,dV_t
$$

Kalman-Bucy 滤波是该类模型下连续时间最优线性最小方差估计的重要基准。

## 为什么重要

### 1. 它把离散 Kalman 思想推广到连续时间观测

### 2. 它为随机控制、导航、金融和连续时间系统辨识提供基础

### 3. 它是理解 EKF、UKF 和一般非线性滤波的标准参考系

## 最小例子

### 例 1：标量 Kalman-Bucy 滤波

设一维系统 $dx = -\theta x\,dt + dW_t$，观测 $dy = x\,dt + dV_t$，其中 $W,V$ 独立布朗运动。

- **问题陈述**：写出 Kalman-Bucy 滤波的 Riccati 方程并求稳态协方差。
- **数学表达**：$d\hat x = -\theta \hat x\,dt + P(dy - \hat x\,dt)$，$\dot P = -2\theta P - P^2 + 1$。
- **计算/推理步骤**：稳态时 $\dot P=0$，$P^2 + 2\theta P - 1=0$，得 $P = -\theta + \sqrt{\theta^2+1}$（取正根）。$\theta=1$ 时 $P = -1 + \sqrt{2} \approx 0.414$。增益为常数 $P=0.414$。
- **结果解读**：Kalman-Bucy 滤波的 Riccati 方程决定了稳态估计精度。观测噪声和过程噪声之间的比值驱动稳态方差。

### 例 2：EKF 的单步——标量非线性

- **问题陈述**：系统 $x_{k+1} = \sin(x_k) + w_k$，$y_k = x_k^2 + v_k$，在 $x=1$ 附近做 EKF 更新。
- **数学表达**：线性化 $F_k = \cos(1) \approx 0.54$，$H_k = 2 \times 1 = 2$。
- **计算/推理步骤**：预测 $\hat x_{k|k-1} = \sin(1)\approx 0.84$，$P_{k|k-1} = 0.54^2 P_{k-1} + Q$。增益 $K = P_{k|k-1} \times 2 / (4P_{k|k-1}+R)$。更新 $\hat x_{k|k} = 0.84 + K(y_k - 0.84^2)$。
- **结果解读**：EKF 在每个滤波步对非线性系统做局部线性化，然后应用标准 Kalman 公式，代价是线性化误差在小样本或强非线性下可能显著。

## 风险与约束

- 连续时间理想模型与离散采样实现之间存在差距
- 非线性滤波一般没有 Kalman 那样的封闭递推形式
- 数值离散化和噪声假设错误会显著破坏估计质量

## 在资源受限条件下的可行最优路径

1. 先掌握 [卡尔曼滤波](../06-数值与计算/Kalman滤波.md)
2. 再掌握 [随机微积分与 Itô 公式](../01-分析与测度/随机微积分与Ito公式.md)
3. 然后进入 Kalman-Bucy、EKF、UKF 和粒子滤波的比较

## 推荐教材与延伸阅读

1. Trefethen & Bau，*Numerical Linear Algebra (SIAM)*——数值线性代数的最佳入门
2. Golub & Van Loan，*Matrix Computations (4th ed., Johns Hopkins)*——矩阵计算的权威百科全书
3. Dellaert & Kaess，*Factor Graphs for Robot Perception (Found. Trends Robot. 2017)*——因子图与SLAM的现代视角

## 与其他条目的关系

- 前置： [状态空间模型](../../02-核心概念/状态空间模型.md)、[随机过程](../../02-核心概念/随机过程.md)
- 相关： [卡尔曼滤波](../06-数值与计算/Kalman滤波.md)、[粒子滤波与序贯 Monte Carlo](../06-数值与计算/粒子滤波与序贯MonteCarlo.md)
- 应用： [滤波与估计中的数学](../../04-应用/滤波与估计中的数学.md)
