# 案例 02：Kalman 滤波——一维位置跟踪

## 问题陈述

一个物体沿直线匀速运动（位置 $p$，速度 $v$），但我们只能观测到含噪声的位置。如何从含噪观测中最优地估计物体的真实位置和速度？这是目标跟踪、导航和传感器融合的经典问题。

## 数学建模

**状态向量**：$x_k = (p_k, v_k)^\top$（$k$ 时刻的位置和速度）

**运动模型**（匀速假设，时间步长 $\Delta t$）：
$$
x_{k+1} = \begin{pmatrix}1&\Delta t\\0&1\end{pmatrix} x_k + w_k
$$
其中 $w_k\sim\mathcal{N}(0,Q)$ 是过程噪声，$Q=\begin{pmatrix}q_p&0\\0&q_v\end{pmatrix}$。

**观测模型**（只能观测位置）：
$$
y_k = \begin{pmatrix}1&0\end{pmatrix} x_k + v_k
$$
其中 $v_k\sim\mathcal{N}(0,R)$ 是观测噪声，$R=\sigma^2$。

## 方法选择：Kalman 滤波

Kalman 滤波是最优线性状态估计器（在 Gaussian 噪声下是最小均方误差最优的），包含两个步骤：

**预测步**（用运动模型向前推）：
$$
\begin{aligned}
\hat x_{k|k-1} &= F \hat x_{k-1|k-1} \\
P_{k|k-1} &= F P_{k-1|k-1} F^\top + Q
\end{aligned}
$$

**更新步**（用观测修正）：
$$
\begin{aligned}
K_k &= P_{k|k-1} H^\top (H P_{k|k-1} H^\top + R)^{-1} \\
\hat x_{k|k} &= \hat x_{k|k-1} + K_k (y_k - H\hat x_{k|k-1}) \\
P_{k|k} &= (I - K_k H) P_{k|k-1}
\end{aligned}
$$

## 数值实现（伪代码）

```python
import numpy as np
import matplotlib.pyplot as plt

# 参数
dt, T = 1.0, 50
F = np.array([[1, dt], [0, 1]])    # 状态转移
H = np.array([[1, 0]])             # 观测矩阵
Q = np.diag([0.01, 0.01])          # 过程噪声协方差
R = np.array([[1.0]])              # 观测噪声协方差

# 生成真实轨迹和观测
x_true = np.zeros((2, T))
x_true[:,0] = [0, 1]               # 起始位置0，速度1
y = np.zeros(T)
np.random.seed(42)
for k in range(T-1):
    x_true[:,k+1] = F @ x_true[:,k] + np.random.multivariate_normal([0,0], Q)
    y[k] = H @ x_true[:,k] + np.random.normal(0, np.sqrt(R[0,0]))

# Kalman滤波
x_est = np.zeros((2, T))
P = np.eye(2) * 10                  # 初始不确定性大
x_hat = np.array([0.0, 0.0])       # 初始猜测

for k in range(T):
    # 预测
    x_pred = F @ x_hat
    P_pred = F @ P @ F.T + Q
    # 更新
    K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)
    x_hat = x_pred + K @ (y[k] - H @ x_pred)
    P = (np.eye(2) - K @ H) @ P_pred
    x_est[:,k] = x_hat

# 结果
print(f"Final position: true={x_true[0,-1]:.2f}, est={x_est[0,-1]:.2f}")
print(f"Final velocity: true={x_true[1,-1]:.2f}, est={x_est[1,-1]:.2f}")
# 绘制位置轨迹：x_true[0,:] vs x_est[0,:] vs y
```

## 结果解释

- **滤波效果**：尽管只能观测到含噪位置（$R=1$），Kalman 滤波不仅平滑了位置估计，还推断出了不可直接观测的速度。
- **Kalman 增益**：$K$ 在初始几步较大（信任观测来修正不确定性），随 $P$ 收敛而稳定——滤波器从"利用观测校正"逐渐过渡到"信任模型预测"。
- **协方差收敛**：$P$ 从初始 $10I$ 收敛到一个稳态值。稳态 Kalman 增益等价于 Wiener 滤波。

## 局限性

- **线性假设**：真实运动若有加速、拐弯，需 EKF 或 UKF（非线性滤波）
- **Gaussian 假设**：非 Gaussian 噪声（如多峰、厚尾）下性能退化
- **模型准确度**：若 $Q$ 和 $R$ 选择不当（如低估过程噪声），滤波器会过于信任模型而忽略观测

## 关联知识库入口

- 方法：[Kalman 滤波](../03-定理与方法/06-数值与计算/Kalman滤波.md)
- 概念：[状态空间模型](../02-核心概念/状态空间模型.md)
- 延伸：[Kalman-Bucy 与非线性滤波](../03-定理与方法/06-数值与计算/Kalman-Bucy与非线性滤波.md)
