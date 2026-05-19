# 案例 03：简单 MPC——双积分器控制

## 问题陈述

控制一个质量为 $m$ 的物体（双积分器系统），使其位置 $p$ 从起点移动到目标点，同时最小化控制力 $u$ 的能量消耗，并尊重位置和速度约束。这是工业过程控制、无人机导航和自动驾驶的简化模型。

## 数学建模

**系统动态**（连续时间）：
$$
\ddot p = \frac{1}{m}u
$$

**状态空间**（$x=(p,v)^\top$，$v=\dot p$，离散化步长 $\Delta t$）：
$$
x_{k+1} = \underbrace{\begin{pmatrix}1&\Delta t\\0&1\end{pmatrix}}_{A} x_k + \underbrace{\begin{pmatrix}\Delta t^2/2m\\ \Delta t/m\end{pmatrix}}_{B} u_k
$$

**优化目标**（MPC 的有限时域代价）：
$$
\min_{u_0,\dots,u_{N-1}} \sum_{k=0}^{N-1} (x_k^\top Q x_k + R u_k^2) + x_N^\top Q_f x_N
$$

**约束**：
- 输入约束：$|u_k|\le u_{\max}$
- 位置约束：$p_{\min}\le p_k\le p_{\max}$
- 速度约束：$|v_k|\le v_{\max}$

## 方法选择：模型预测控制（MPC）

MPC 在每一步求解一个有限时域的最优控制问题（通常为二次规划 QP），只执行第一步控制，然后重新规划（滚动时域）。

**QP 形式**：将 $N$ 步预测表达为初始状态 $x_0$ 和输入序列 $U=(u_0,\dots,u_{N-1})$ 的线性函数：

$$
\min_U \frac12 U^\top H U + x_0^\top F^\top U \quad \text{s.t. } GU\le h
$$

## 数值实现（伪代码）

```python
import numpy as np

# 系统参数
m, dt = 1.0, 1.0
A = np.array([[1, dt], [0, 1]])
B = np.array([[dt**2/(2*m)], [dt/m]])

# MPC参数
N = 10
Q = np.diag([10, 1])    # 位置权重高，速度权重低
R = np.array([[0.1]])
u_max, v_max = 2.0, 3.0

# 构建QP矩阵（密集形式，小规模时可行）
def build_qp(x0):
    # 预测：X = M * x0 + C * U
    M = np.zeros((2*(N+1), 2))
    C = np.zeros((2*(N+1), N))
    M[:2] = np.eye(2)
    for k in range(N):
        M[2*(k+1):2*(k+2)] = A @ M[2*k:2*(k+1)]
        C[2*(k+1):2*(k+2)] = A @ C[2*k:2*(k+1)]
        C[2*k:2*(k+2), k:k+1] += np.vstack([np.zeros((2,1)), B])
    # 代价矩阵
    Qbar = np.kron(np.eye(N+1), Q)
    H = C.T @ Qbar @ C + R * np.eye(N)
    f = (x0 @ M.T @ Qbar @ C).flatten()
    # 约束
    G = np.vstack([np.eye(N), -np.eye(N)])  # |u| <= u_max
    h = np.hstack([u_max*np.ones(N), u_max*np.ones(N)])
    return H, f, G, h

# 仿真
x = np.array([0.0, 0.0])  # 初始状态
target = np.array([5.0, 0.0])
from scipy.optimize import minimize

for t in range(50):
    x[0] -= target[0]  # 转换为误差坐标
    H, f, G, h = build_qp(x)
    x[0] += target[0]
    # 求解QP (简单约束: |u|<=umax)
    res = minimize(lambda u: 0.5*u@H@u + f@u, np.zeros(N),
                   constraints=[{'type':'ineq','fun':lambda u:u_max-abs(u)}])
    u = res.x[0]
    x = A @ x + B.flatten() * u
```

## 结果解释

- **约束满足**：MPC 通过在线优化显式处理输入和状态约束，当控制量接近上限时自动"饱和"。
- **预测时域效应**：$N$ 太短（如 $N=2$）→ 短视，可能撞墙；$N$ 足够大（如 $N=10$）→ 预见到远处的约束并提前减速。
- **计算代价**：每一步求解一个小规模 QP。$N=10$、变量 10 个时毫秒级可解，适合实时控制。

## 局限性

- **模型准确性**：真实系统与双积分器模型不匹配时性能退化（需鲁棒 MPC）
- **QP 求解可靠性**：约束不一致时 QP 无解——需软约束或可行性恢复策略
- **在线计算**：嵌入式平台可能无法承受实时 QP 求解

## 关联知识库入口

- 方法：[模型预测控制](../03-定理与方法/05-优化与控制/模型预测控制.md)
- 方法：[Riccati 方程与 LQR/LQG](../03-定理与方法/05-优化与控制/Riccati方程与LQR-LQG.md)
- 概念：[线性规划与二次规划](../03-定理与方法/05-优化与控制/线性规划.md)
