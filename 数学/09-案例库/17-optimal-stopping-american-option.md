# 案例 17：最优停时与美式期权定价

## 问题陈述

你持有一份美式看跌期权：有权在 $T$ 到期前任何时刻以执行价 $K$ 卖出标的资产。标的资产价格 $S_t$ 遵循几何 Brown 运动。问：什么时候行权最优？期权的公平价格是多少？

这是最优停时（Optimal Stopping）的经典问题——在每一个时刻决定"现在行权"还是"继续等待"以使期望收益最大化。

## 数学建模

**资产动态**（风险中性测度下）：
$$
dS_t = r S_t dt + \sigma S_t dW_t
$$

**期权价值**（最优停时问题）：
$$
V(S_0) = \sup_{\tau\in[0,T]} \mathbb{E}\left[e^{-r\tau}\max(K-S_\tau, 0)\right]
$$

其中 $\tau$ 是停时（行权时刻），$r$ 是无风险利率。

**Snell 包络**：$V$ 是最小的上鞅控制 $\max(K-S_t,0)$ 的过程，满足动态规划原理：
$$
V_t = \max\left(\max(K-S_t,0),\; \mathbb{E}[e^{-r\Delta t}V_{t+\Delta t}\mid S_t]\right)
$$

## 方法：最小二乘 Monte Carlo（Longstaff-Schwartz）

1. 生成 $M$ 条资产价格路径 $\{S_t^{(m)}\}_{t=0}^T$
2. 从 $T$ 回溯：在每时刻 $t$，对"继续持有"的期望价值做回归（基函数：$1, S_t, S_t^2$）
3. 比较即时行权价值与回归估计的继续持有价值，决定最优策略
4. 沿最优策略计算每条路径的折现收益，取平均

## 数值实现（伪代码）

```python
import numpy as np

# 参数
S0, K, r, sigma, T = 100, 100, 0.05, 0.2, 1.0
N_steps = 50
dt = T / N_steps
M = 10000  # 模拟路径数

# 生成资产价格路径
np.random.seed(42)
S = np.zeros((M, N_steps+1))
S[:,0] = S0
for t in range(N_steps):
    dW = np.random.randn(M) * np.sqrt(dt)
    S[:,t+1] = S[:,t] * np.exp((r - 0.5*sigma**2)*dt + sigma*dW)

# 期权收益
payoff = np.maximum(K - S, 0)

# LSMC 回溯
V = payoff[:, -1].copy()  # 终端价值
exercise = np.zeros((M, N_steps), dtype=bool)

for t in range(N_steps-1, 0, -1):
    # 当前仍存活的路径（期权未行权 + 处于实值状态 S < K）
    in_money = (payoff[:,t] > 0)
    if in_money.sum() < 2:
        continue
    
    # 回归：V_next ~ a + b*S + c*S^2
    X = np.column_stack([np.ones_like(S[in_money,t]),
                          S[in_money,t],
                          S[in_money,t]**2])
    y = V[in_money] * np.exp(-r * dt)
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    
    # 继续持有所需的期望价值估计
    cont_value = beta[0] + beta[1]*S[in_money,t] + beta[2]*S[in_money,t]**2
    
    # 最优停时决策
    exercise_now = payoff[in_money,t] > cont_value
    exercise[in_money, t] = exercise_now
    V[in_money] = np.where(exercise_now, payoff[in_money,t], V[in_money]*np.exp(-r*dt))

# 期权价格 = 沿最优策略的平均折现收益
option_price = np.mean(V)
print(f"American put price: {option_price:.4f}")

# 对比欧式看跌（Black-Scholes）
from scipy.stats import norm
d1 = (np.log(S0/K) + (r+0.5*sigma**2)*T) / (sigma*np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)
european_put = K*np.exp(-r*T)*norm.cdf(-d2) - S0*norm.cdf(-d1)
print(f"European put price: {european_put:.4f}")
print(f"Early exercise premium: {option_price - european_put:.4f}")
# 输出: American put: ~5.82, European put: ~5.57, Premium: ~0.25
```

## 结果解释

- **早期行权溢价**：美式期权比欧式贵约 0.25（约 4.5%）——提前行权的权利有正价值
- **最优行权边界**：当 $S_t$ 低于某个临界值 $S^*(t)$ 时最优行权。$S^*(t)$ 通常随到期日临近而上升（越接近到期，越不值得等待）
- **分红效应**：若无分红（本例 $r>0$ 但无分红），看跌期权早期行权有价值（拿到 $K$ 后可赚利息）；看涨期权在无分红时绝不应提前行权

## 局限性

- **LSMC 的回归偏差**：基函数选择影响精度——需足够灵活的基函数族
- **高维问题**：多资产期权（$d>3$）的 LSMC 回归面临维数诅咒
- **路径依赖**：LSMC 仅适用于 Markov 型收益——障碍期权等需特殊处理

## 关联知识库入口

- 方法：[最优停时与随机最大值原理](../03-定理与方法/05-优化与控制/最优停时与随机最大值原理.md)
- 方法：[鞅与停时](../03-定理与方法/01-分析与测度/鞅与停时.md)
- 方法：[随机微积分与 Ito 公式](../03-定理与方法/01-分析与测度/随机微积分与Ito公式.md)
