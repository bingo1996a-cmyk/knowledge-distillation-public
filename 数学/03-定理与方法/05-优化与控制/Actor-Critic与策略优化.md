# Actor-Critic 与策略优化

## 作用

Actor-Critic 方法把策略优化拆成两个相互耦合的部分：

- Actor：更新策略参数
- Critic：估计值函数、优势函数或梯度信号

它是现代强化学习从值函数方法走向策略优化与连续控制的重要框架。

## 一个典型更新思路

策略梯度常写成

$$
\nabla J(\theta)=\mathbb{E}_{\pi_\theta}\big[\nabla_\theta \log \pi_\theta(a\mid s)\,A^{\pi}(s,a)\big]
$$

Critic 的任务通常是提供 $A^{\pi}(s,a)$ 或其近似。

## 为什么重要

### 1. 它兼顾策略表达能力与样本效率

### 2. 它能自然进入连续动作与高维策略参数化

### 3. 它与随机近似、自然梯度、POMDP 和最优控制都有联系

## 最小例子

### 例 1：带 baseline 的策略梯度——CartPole 单步更新示意

考虑一个动作数为 2、状态为 4 维向量的 CartPole 环境。策略 $\pi_\theta(a|s)$ 用 softmax 输出。单步更新的核心计算为

$$
\nabla J(\theta) \approx (\hat A) \cdot \nabla_\theta \log \pi_\theta(a|s)
$$

其中 $\hat A = r + \gamma V_\phi(s') - V_\phi(s)$ 是 Critic 提供的优势估计。

- **问题陈述**：给定状态 $s=[0.1,-0.2,0.3,0.05]$，动作 $a=1$（向右推），奖励 $r=1$，下一状态 $s'=[0.12,-0.25,0.35,0.08]$，折扣因子 $\gamma=0.99$，当前 Critic 估值 $V_\phi(s)=0.8$、$V_\phi(s')=0.85$，计算优势 $\hat A$ 并更新 Actor。
- **计算步骤**：$\hat A = 1 + 0.99 \times 0.85 - 0.8 = 1 + 0.8415 - 0.8 = 1.0415$。Actor 更新方向为 $\nabla_\theta \log \pi_\theta(a|s) \times 1.0415$，即正优势增大该动作概率。
- **结果解读**：优势为正，说明该动作优于平均值，Actor 应向增大 $a=1$ 概率的方向更新参数。

### 例 2：Actor-Critic 的双闭环耦合——初值敏感

- **问题陈述**：若 Critic 初始估计 $V_\phi$ 偏大 50%（如 $V_\phi(s)=1.2$ 而非 0.8），则上例中的 $\hat A = 1 + 0.8415 - 1.2 = 0.6415$，方向仍正确但幅值减小。若 Critic 偏小 50%（$V_\phi(s)=0.4$），则 $\hat A = 1.4415$，增幅偏大。
- **结果解读**：Critic 偏差会缩放梯度幅值但不改变符号，说明 Actor-Critic 对 Critic 偏差有一定容忍度，但方差波动会随偏差增大而提高。

## 风险与约束

- Actor 与 Critic 同步学习，可能互相放大误差
- 估计偏差、方差控制和探索不足是常见难点
- 稳定训练通常需要约束更新步长或信赖域思想

## 在资源受限条件下的可行最优路径

1. 先掌握 [马尔可夫决策过程](../05-优化与控制/Markov决策过程.md)
2. 再掌握 [近似动态规划与策略梯度](../05-优化与控制/近似动态规划与策略梯度.md)
3. 然后学习 Actor-Critic、自然梯度与策略约束优化

## 推荐教材与延伸阅读

1. Boyd & Vandenberghe，*Convex Optimization (Cambridge)*——凸优化的标准参考，含对偶、KKT、内点法
2. Nocedal & Wright，*Numerical Optimization (2nd ed., Springer)*——数值优化算法的最全面参考
3. Bertsekas，*Dynamic Programming and Optimal Control (4th ed., Athena Scientific)*——动态规划与最优控制的权威教材

## 与其他条目的关系

- 前置： [马尔可夫决策过程](../05-优化与控制/Markov决策过程.md)、[近似动态规划与策略梯度](../05-优化与控制/近似动态规划与策略梯度.md)
- 相关： [随机近似与 Robbins-Monro 方法](../04-概率与统计/随机逼近与Robbins-Monro.md)、[镜像下降与自然梯度](../05-优化与控制/镜像下降与自然梯度.md)
- 应用： [强化学习中的数学](../../04-应用/强化学习中的数学.md)
