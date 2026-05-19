# 案例 16：小批量随机优化的学习率调度

## 问题陈述

训练一个简单神经网络对 MNIST 手写数字分类。使用 SGD 优化，但固定学习率要么太大（不收敛）要么太小（收敛太慢）。如何设计学习率调度策略使其在训练初期大步前进、后期精细收敛？这是深度学习训练中最基本的工程问题。

## 数学建模

**优化问题**（经验风险最小化）：
$$
\min_\theta \frac{1}{N}\sum_{i=1}^N \ell(f_\theta(x_i), y_i)
$$

**SGD 更新**（批量大小 $B$）：
$$
\theta_{t+1} = \theta_t - \eta_t \cdot \frac{1}{B}\sum_{i\in\mathcal{B}_t}\nabla_\theta\ell(f_\theta(x_i), y_i)
$$

**学习率调度策略**：
- 阶梯衰减：$\eta_t = \eta_0 \cdot \gamma^{\lfloor t/T\rfloor}$（每 $T$ 步乘 $\gamma$）
- 余弦退火：$\eta_t = \eta_{\min} + \frac12(\eta_0-\eta_{\min})(1+\cos(\pi t/T))$
- 线性预热+余弦：前 $W$ 步从 0 线性增至 $\eta_0$，再余弦衰减

## 数值实现（伪代码）

```python
import numpy as np

# 模拟一个简单的二次优化问题（强凸 + 噪声）
np.random.seed(42)
d = 100
theta_star = np.random.randn(d)
# 目标：f(theta) = 0.5 * ||theta - theta_star||^2 + noise

def noisy_gradient(theta, batch_size=32):
    """模拟带噪声的梯度"""
    true_grad = theta - theta_star
    noise = 0.3 * np.random.randn(d) / np.sqrt(batch_size)
    return true_grad + noise

# 比较三种学习率调度
T = 2000
theta0 = np.zeros(d)

strategies = {
    "constant_0.1": lambda t: 0.1,
    "constant_0.01": lambda t: 0.01,
    "step_decay": lambda t: 0.1 * (0.5 ** (t // 500)),
    "cosine": lambda t: 0.01 + 0.5*(0.1-0.01)*(1+np.cos(np.pi*t/T)),
    "warmup_cosine": lambda t: (0.1*t/200 if t<200 else
        0.01+0.5*(0.1-0.01)*(1+np.cos(np.pi*(t-200)/(T-200)))),
}

results = {}
for name, lr_schedule in strategies.items():
    theta = theta0.copy()
    losses = []
    for t in range(T):
        lr = lr_schedule(t)
        g = noisy_gradient(theta)
        theta -= lr * g
        loss = 0.5 * np.sum((theta - theta_star)**2)
        losses.append(loss)
    results[name] = (losses[-1], losses[-100:])

for name, (final_loss, last_100) in sorted(results.items(),
                                            key=lambda x: x[1][0]):
    print(f"{name:20s}: final_loss={final_loss:.4f}, "
          f"avg_last_100={np.mean(last_100):.4f}")
```

## 结果解释

- **常数 0.1**：初期快速下降，但后期在最优值附近振荡，无法收敛——噪声放大了大步长的振荡
- **常数 0.01**：稳定收敛，但前 500 步下降慢——浪费了初期快速进展的机会
- **阶梯衰减**：每 500 步学习率减半，平衡了速度与精度——但衰减时机需要手工设定
- **余弦退火**：平滑地从大到小，最后阶段极小的学习率使收敛精度最高
- **预热+余弦**：最稳健——前 200 步小学习率避免初期梯度方向不可靠时的发散

**最优策略**：预热让优化器在初期建立可靠的梯度方向估计，余弦衰减在后期精细搜索最小值。

## 局限性

- **二维/强凸问题**的结论不能完全推广到深度网络的非凸景观
- **批量大小与学习率耦合**：大批量允许更大学习率（线性缩放法则）
- **自适应方法**（Adam, AdamW）自带宽学习率调整，对手动调度的需求较低

## 关联知识库入口

- 方法：[梯度下降](../03-定理与方法/05-优化与控制/梯度下降.md)
- 方法：[镜像下降与自然梯度](../03-定理与方法/05-优化与控制/镜像下降与自然梯度.md)
- 方法：[随机逼近与 Robbins-Monro](../03-定理与方法/04-概率与统计/随机逼近与Robbins-Monro.md)
