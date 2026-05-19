# Lie 群上的平滑与几何积分

## 作用

当状态属于旋转群、位姿群或更一般的流形时，直接在欧氏空间中做平滑和数值积分会破坏几何结构。Lie 群上的平滑与几何积分研究如何在保持群结构和几何约束的前提下进行估计与时间推进。

## 一个典型优化形式

$$
\min_{X_0,\dots,X_T} \sum_k \left\|\log\big(Z_k^{-1}X_k^{-1}X_{k+1}\big)\right\|_{Q_k}^2 + \sum_k \left\|\log\big(Y_k^{-1}h(X_k)\big)\right\|_{R_k}^2
$$

这里利用群对数映射把残差写回李代数局部坐标。

## 为什么重要

### 1. 它避免把旋转、姿态和刚体运动粗暴线性化

### 2. 它连接几何、滤波、平滑、SLAM 和机器人导航

### 3. 几何积分可更稳定地保持能量、约束与不变量结构

## 最小例子

### 例 1：$SO(2)$ 上的旋转平滑

- **问题陈述**：两个带噪声的旋转观测 $R_1=10^\circ$、$R_2=20^\circ$，用几何平滑求最优估计。
- **数学表达**：$\min_{R\in SO(2)} w_1\|\log(R_1^{-1}R)\|^2 + w_2\|\log(R_2^{-1}R)\|^2$，其中 $\|\log(\cdot)\|$ 是李代数上的角距离。
- **计算/推理步骤**：$SO(2)$ 中 $\log$ 映射退化为角度差。设 $w_1=w_2=1$，最优旋转角 $\theta = \arg\min (\theta-10^\circ)^2 + (\theta-20^\circ)^2$，得 $\theta=15^\circ$。如果忽略流形直接对矩阵元线性平均，得到的矩阵一般不在 $SO(2)$ 上。
- **结果解读**：用李代数坐标做优化再映射回群，保证结果始终在流形上。

### 例 2：几何积分——旋转矩阵的指数更新

- **问题陈述**：角速度 $\omega=[0,0,0.1]^\top$（rad/s），时间步 $\Delta t=0.1$，初始 $R=I$，用指数映射做几何积分。
- **数学表达**：$R_{k+1} = R_k \cdot \exp(\hat\omega \Delta t)$，其中 $\hat\omega = [\omega]_\times$ 为 so(3) 元素。
- **计算/推理步骤**：$\hat\omega\Delta t = \begin{bmatrix}0&-0.01&0\\0.01&0&0\\0&0&0\end{bmatrix}$。Rodrigues 公式：$\exp(\hat\omega\Delta t) = I + \sin(0.01)\hat\omega/\|\omega\| + (1-\cos(0.01))(\hat\omega/\|\omega\|)^2 \approx \begin{bmatrix}0.99995&-0.01&0\\0.01&0.99995&0\\0&0&1\end{bmatrix}$。
- **结果解读**：指数映射保持旋转矩阵的正交性（$R^\top R=I$），避免欧拉法（$R_{k+1}=R_k + \Delta t R_k\hat\omega$）带来的数值漂移。

## 风险与约束

- 图优化与 Lie 群局部坐标选择会影响数值稳定性
- 非交换群的线性化误差比欧氏空间更敏感
- 局部参数化好用，但必须审计其全局有效性

## 推荐教材与延伸阅读

1. Hairer, Lubich & Wanner，*Geometric Numerical Integration (2nd ed., Springer)*——几何积分的标准参考
2. Iserles, Munthe-Kaas, Norsett & Zanna，*Lie-Group Methods (Acta Numerica 2000)*——Lie群数值方法的经典综述

## 与其他条目的关系

- 前置： [Lie 群与 Lie 代数](../../02-核心概念/Lie群与Lie代数.md)、[流形](../../02-核心概念/流形.md)
- 相关： [Lie 群上的滤波与优化](../02-代数与数论/Lie群上的优化与滤波.md)、[Kalman-Bucy 与非线性滤波](../06-数值与计算/Kalman-Bucy与非线性滤波.md)
- 应用： [机器人与几何控制中的数学](../../04-应用/机器人与几何控制中的数学.md)
