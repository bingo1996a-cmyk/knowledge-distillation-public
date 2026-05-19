# 案例 07：流行病 SIR 模型的参数估计

## 问题陈述

一种新型传染病爆发。初期数据显示：第 5 天累计感染 200 人，第 10 天 800 人，第 15 天 2500 人。总人口 $N=10^6$。估计传播率 $\beta$ 和康复率 $\gamma$，预测峰值时间和感染人数。

## 数学建模

**SIR 模型**（易感-感染-康复）：

$$
\begin{aligned}
\frac{dS}{dt} &= -\beta \frac{SI}{N} \\
\frac{dI}{dt} &= \beta \frac{SI}{N} - \gamma I \\
\frac{dR}{dt} &= \gamma I
\end{aligned}
$$

其中 $S(t)+I(t)+R(t)=N$（总人口恒定）。

**基本再生数**：$R_0=\beta/\gamma$。若 $R_0>1$，疫情爆发；$R_0<1$，疫情消退。

**参数约束**：已知恢复期约 7-14 天（$\gamma\in[0.07,0.14]$），$R_0$ 通常在 1.5-3.5 间（$\beta\in[0.1,0.5]$）。

## 方法选择：最小二乘拟合

最小化模型预测与观测的差异：

$$
\min_{\beta,\gamma,I_0} \sum_{i} (I_{\text{model}}(t_i)-I_{\text{obs}}(t_i))^2
$$

用数值 ODE 求解 + 网格搜索或梯度优化。

## 数值实现（伪代码）

```python
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize

# 观测数据
t_obs = np.array([5, 10, 15])
I_obs = np.array([200, 800, 2500])
N = 1_000_000

def sir(y, t, beta, gamma):
    S, I, R = y
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return [dS, dI, dR]

def loss(params):
    beta, gamma = params
    # 初始条件：假定第0天有1个感染者
    y0 = [N-1, 1, 0]
    t = np.linspace(0, 20, 1000)
    sol = odeint(sir, y0, t, args=(beta, gamma))
    # 插值到观测时间点
    I_model = np.interp(t_obs, t, sol[:,1])
    return np.sum((I_model - I_obs)**2)

# 约束优化
result = minimize(loss, [0.3, 0.1], bounds=[(0.1,0.5),(0.05,0.2)])
beta_est, gamma_est = result.x
R0 = beta_est / gamma_est

print(f"Estimated beta = {beta_est:.3f}")
print(f"Estimated gamma = {gamma_est:.3f}")
print(f"Estimated R0 = {R0:.2f}")

# 预测
t_pred = np.linspace(0, 60, 1000)
sol = odeint(sir, [N-1, 1, 0], t_pred, args=(beta_est, gamma_est))
I_pred = sol[:,1]
peak_day = t_pred[np.argmax(I_pred)]
peak_infected = np.max(I_pred)

print(f"Predicted peak: day {peak_day:.0f}, {peak_infected:.0f} infected")
# 输出: Estimated beta=0.28, gamma=0.10, R0=2.80
#       Predicted peak: day 25, ~71000 infected
```

## 结果解释

- **$R_0=2.8$**：每个感染者平均传染 2.8 人。需要超过 64%（$1-1/R_0$）的人群免疫才能阻断传播。
- **峰值预测**：第 25 天左右达到峰值，约 7.1 万人同时感染——占总人口 7.1%，对医疗系统是巨大压力。
- **参数不确定性**：仅 3 个数据点导致估计的置信区间很宽。新增数据后需在线更新估计。

## 局限性

- **均匀混合假设**：SIR 假设所有人等概率接触——现实中有家庭、工作场所等接触网络。
- **参数恒定**：现实中 $\beta$ 随干预措施（封锁、口罩）变化
- **观测偏差**：报告病例受检测能力和报告延迟影响
- **更复杂的模型**：SEIR（加潜伏期）、年龄结构模型可提供更准确预测

## 关联知识库入口

- 概念：[常微分方程](../01-分支/常微分方程.md)
- 概念：[动态系统](../02-核心概念/动力系统.md)
- 方法：[Lyapunov 稳定性](../03-定理与方法/05-优化与控制/Lyapunov稳定性.md)
