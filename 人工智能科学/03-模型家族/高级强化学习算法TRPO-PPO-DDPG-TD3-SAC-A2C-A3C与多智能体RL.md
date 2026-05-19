---
title: 深度强化学习进阶算法：TRPO、PPO、DDPG、TD3、SAC、A2C、A3C、MARL 与 MRL
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 深度强化学习进阶算法：TRPO、PPO、DDPG、TD3、SAC、A2C、A3C、MARL 与 MRL

> **阅读顺序**：本页是深度强化学习进阶算法的公式推导与变体说明页，承接 [强化学习算法谱系：DP、MC、TD、SARSA、Q-learning、DQN、actor-critic 与 PPO](./reinforcement-learning-algorithm-family-dp-mc-td-sarsa-q-learning-dqn-actor-critic-and-ppo.md) 的第五、六层（连续控制与现代 policy optimization + MARL/MRL）。建议先阅读 J 页获得全景后再进入本页获取数学细节。

## 1. 这页要回答什么

本页承接“值函数强化学习：DP、TD、SARSA、Q-learning、DQN 与 Double DQN”和“模型化强化学习、世界模型与规划”两条线，重点回答：

1. 为什么深度强化学习（Deep Reinforcement Learning, Deep RL）会从值函数法进一步分化出策略梯度、actor-critic、连续控制与多智能体方法；
2. 这些方法在数学上如何连接；
3. 训练不稳定性来自哪里；
4. 它们分别适合什么任务，失败模式是什么。

说明：缩写 **MRL** 在文献中并不唯一，本页将其主要按“元强化学习（Meta Reinforcement Learning, Meta-RL）”处理；模型化强化学习则放在相关页面中单独展开。

## 2. 从值函数到策略优化

值函数法通过 Bellman 方程学习动作价值 $Q(s,a)$；策略梯度法则直接优化参数化策略：

$$
J(\theta)=\mathbb{E}_{\tau\sim \pi_\theta}[R(\tau)].
$$

策略梯度定理写为：

$$

abla_\theta J(\theta)=\mathbb{E}_{s,a\sim \pi_\theta}\left[
abla_\theta \log \pi_\theta(a\mid s)Q^{\pi}(s,a)
ight].
$$

根本差别在于：

- 值函数法先估 $Q$，再隐式选策略；
- 策略梯度法直接对策略参数求导；
- actor-critic 处在两者之间：actor 更新策略，critic 估计价值。

## 3. A3C 与 A2C：并行经验与优势估计

### 3.1 A3C

异步优势行动者—评论家（Asynchronous Advantage Actor-Critic, A3C）的关键思想是：

- 并行启动多个环境线程；
- 每个线程独立收集轨迹；
- 共享全局参数并异步更新；
- 用并行性打破样本相关性。

优势函数定义为：

$$
A^{\pi}(s,a)=Q^{\pi}(s,a)-V^{\pi}(s).
$$

### 3.2 A2C

同步优势行动者—评论家（Advantage Actor-Critic, A2C）可看作 A3C 的同步版本：

- 并行环境收集一批样本；
- 同步计算梯度；
- 用统一批更新参数。

A2C 在现代实现中更自然，也更容易与 GPU/TPU 框架整合。

## 4. TRPO：为什么要有信赖域

信赖域策略优化（Trust Region Policy Optimization, TRPO）解决的是：策略梯度一步走太远，策略可能崩坏。

TRPO 用约束优化控制新旧策略差异：

$$
\max_\theta \; \mathbb{E}\left[\frac{\pi_\theta(a\mid s)}{\pi_{\theta_{old}}(a\mid s)}A^{\pi_{old}}(s,a)
ight]
$$

同时限制 KL 散度（Kullback–Leibler divergence）不超过阈值。

深层意义：TRPO 并不是“复杂版本的策略梯度”，而是在非凸、噪声大、目标会随策略变化的场景中，为更新步长加入几何约束。

## 5. PPO：TRPO 的工程化近似

近端策略优化（Proximal Policy Optimization, PPO）通常用裁剪目标：

$$
L^{\text{clip}}(\theta)=\mathbb{E}\Big[\min\big(r_t(\theta)\hat A_t,\; \mathrm{clip}(r_t(\theta),1-\epsilon,1+\epsilon)\hat A_t\big)\Big],
$$

其中

$$
r_t(\theta)=\frac{\pi_\theta(a_t\mid s_t)}{\pi_{\theta_{old}}(a_t\mid s_t)}.
$$

PPO 的成功来自三点：

- 保留了 TRPO 的“不要走太远”思想；
- 避免复杂二阶近似与约束求解；
- 在工程上更容易稳定训练。

## 6. 连续控制：DDPG、TD3 与 SAC

### 6.1 DDPG

深度确定性策略梯度（Deep Deterministic Policy Gradient, DDPG）适合连续动作空间。它把：

- DQN 的离策略经验回放；
- actor-critic 结构；
- 确定性策略梯度

组合起来。

但 DDPG 容易过高估计、对超参数敏感、训练不稳。

### 6.2 TD3

Twin Delayed DDPG（TD3）对 DDPG 的关键修正包括：

- 双 critic 取较小值，缓解过高估计；
- 延迟更新 actor；
- 目标动作加入平滑噪声。

TD3 的重要意义在于：它展示了连续控制不稳定性的核心来源之一是 critic 偏差被 actor 放大。

### 6.3 SAC

软行动者—评论家（Soft Actor-Critic, SAC）把最大熵强化学习引入 actor-critic：

$$
J(\pi)=\sum_t \mathbb{E}\big[r(s_t,a_t)+\alpha \mathcal{H}(\pi(\cdot\mid s_t))\big].
$$

其中熵项鼓励策略保持随机性，从而改善探索与鲁棒性。SAC 在连续控制中长期表现强势，原因在于它兼顾了：

- 离策略样本效率；
- 随机策略探索；
- 相对稳定的优化目标。

## 7. 优势估计与信用分配

PPO、A2C、TRPO 等方法都依赖优势估计。广义优势估计（Generalized Advantage Estimation, GAE）通过引入折中参数 $\lambda$ 平衡偏差与方差：

$$
\hat A_t^{\mathrm{GAE}(\gamma,\lambda)} = \sum_{l=0}^{\infty}(\gamma \lambda)^l \delta_{t+l}.
$$

其中 $\delta_t$ 是 TD 误差。

这说明 actor-critic 的核心并不只是“多加一个 value head”，而是通过 critic 构造低方差、可训练的策略更新信号。

## 8. 多智能体强化学习（MARL）

多智能体强化学习（Multi-Agent Reinforcement Learning, MARL）的难点比单智能体多至少三层：

1. 环境对单个智能体而言非平稳；
2. 信用分配更困难；
3. 观测、通信、合作与博弈结构耦合更复杂。

常见结构包括：

- 参数共享；
- 集中训练、分散执行（Centralized Training, Decentralized Execution, CTDE）；
- value decomposition；
- counterfactual baseline；
- 通信学习。

## 9. 元强化学习（Meta-RL）

Meta-RL 的目标不是只在一个任务上表现好，而是：

- 在任务分布上训练；
- 在新任务上快速适应；
- 用少量交互完成迁移。

它与上下文学习、世界模型、适应性控制有天然连接。

## 10. 这些算法之间的关系图

可把这组算法看成四条主线：

1. **值函数近似线**：DQN → DDQN → 分布式/改进型 DQN；
2. **策略梯度线**：REINFORCE → actor-critic → A2C/A3C → TRPO/PPO；
3. **连续控制线**：确定性策略梯度 → DDPG → TD3 / SAC；
4. **多任务与多主体线**：Meta-RL / MARL / CTDE / 信用分配。

## 11. 训练时最常见的失败模式

- critic 目标漂移；
- 策略更新过大；
- 探索不足或探索噪声错误；
- replay buffer 分布与当前策略脱节；
- reward hacking；
- 多智能体协同中的信用分配失败；
- sim2real gap。

## 12. 经典文献与教材

1. Sutton, R. S., & Barto, A. G. *Reinforcement Learning: An Introduction*. MIT Press, 2018.
2. Schulman, J. et al. *Trust Region Policy Optimization*. ICML, 2015.
3. Schulman, J. et al. *Proximal Policy Optimization Algorithms*. 2017.
4. Lillicrap, T. et al. *Continuous Control with Deep Reinforcement Learning*. 2015.
5. Fujimoto, S. et al. *Addressing Function Approximation Error in Actor-Critic Methods*. 2018.
6. Haarnoja, T. et al. *Soft Actor-Critic*. 2018.

## 13. 联动阅读

- `03-model-families/value-based-reinforcement-learning-dp-td-sarsa-q-learning-dqn-and-double-dqn.md`
- `03-model-families/policy-gradient-actor-critic-trpo-ppo-and-advantage-estimation.md`
- `03-model-families/continuous-control-ddpg-td3-sac-and-off-policy-actor-critic.md`
- `04-systems-engineering/reinforcement-learning-training-loops-benchmarks-and-failure-modes.md`
- `04-systems-engineering/reinforcement-learning-evaluation-off-policy-estimation-and-safe-deployment.md`
