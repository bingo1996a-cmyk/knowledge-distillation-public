# 案例 18：强化学习——网格世界中的 Q-Learning

## 问题陈述

一个智能体在 $5\times5$ 网格世界中移动，某些格子有奖励（+10 到达目标），某些有惩罚（-10 陷阱）。智能体不知道环境动态——它必须通过试错学习最优策略。这是强化学习最经典的入门问题。

## 数学建模

**MDP 形式化**：
- 状态 $s\in\{1,\dots,25\}$：25 个格子
- 动作 $a\in\{\uparrow,\downarrow,\leftarrow,\rightarrow\}$：四方向移动
- 奖励：目标格 +10，陷阱格 -10，每步 -0.1（鼓励最短路径）
- 转移：以概率 0.8 向预定方向移动，各 0.1 向两侧滑移

**Q 函数**：$Q(s,a)$ 是在状态 $s$ 采取动作 $a$ 后，后续按最优策略的期望累积奖励。

**Bellman 最优方程**：
$$
Q^*(s,a) = R(s,a) + \gamma\sum_{s'}P(s'\mid s,a)\max_{a'}Q^*(s',a')
$$

## 方法：Q-Learning（无模型 TD 学习）

不需要知道 $P(s'\mid s,a)$！直接从经验中学习：
$$
Q(s,a) \leftarrow Q(s,a) + \alpha\left[r + \gamma\max_{a'}Q(s',a') - Q(s,a)\right]
$$

$\alpha$ 为学习率，$\gamma$ 为折扣因子。这是 off-policy TD(0) 算法——学习最优 $Q^*$ 的同时用 $\varepsilon$-贪心策略探索。

## 数值实现（伪代码）

```python
import numpy as np

# 网格世界设置
n = 5
goal = (4, 4)
trap = (2, 2)
actions = [(-1,0), (1,0), (0,-1), (0,1)]  # 上下左右

# Q-Learning参数
alpha, gamma, epsilon = 0.1, 0.95, 0.1
Q = np.zeros((n, n, 4))
episodes = 500

for ep in range(episodes):
    s = (0, 0)  # 起始状态
    while s != goal and s != trap:
        # ε-贪心选择动作
        if np.random.random() < epsilon:
            a = np.random.randint(4)
        else:
            a = np.argmax(Q[s[0], s[1]])
        
        # 执行动作（含随机滑移）
        p = np.random.random()
        if p < 0.8:
            a_actual = a
        elif p < 0.9:
            a_actual = (a + 1) % 4  # 右滑
        else:
            a_actual = (a + 3) % 4  # 左滑
        
        # 下一状态（边界截断）
        s_next = (max(0, min(n-1, s[0]+actions[a_actual][0])),
                   max(0, min(n-1, s[1]+actions[a_actual][1])))
        
        # 奖励
        if s_next == goal:   r = 10
        elif s_next == trap: r = -10
        else:                r = -0.1
        
        # Q-Learning更新
        Q[s[0], s[1], a] += alpha * (r + gamma*np.max(Q[s_next[0], s_next[1]]) - Q[s[0], s[1], a])
        s = s_next

# 输出最优策略
policy = np.array([['↑','↓','←','→'][np.argmax(Q[i,j])] for i in range(n) for j in range(n)]).reshape(n,n)
print("Optimal policy (arrows):")
print(policy)
```

## 结果解释

- **Q 值收敛**：约 300-500 episodes 后 Q 值稳定。目标格附近的 Q 值最高，沿最短路径递减
- **最优路径**：从 (0,0) 出发，策略学到绕过 (2,2) 陷阱到达 (4,4) 目标——约 8 步
- **ε-贪心的作用**：探索率 ε=0.1 保证智能体偶尔尝试"非最优"动作，发现更好的路径。纯贪心（ε=0）可能困在次优路径
- **TD 误差**：$r+\gamma\max Q'-Q$ 在收敛时趋于 0。TD 误差的均方值是监控学习进度的好指标
- **离策略性质**：Q-Learning 学的是最优策略的 Q 值（$\max_{a'}Q$），而行为策略是 ε-贪心——这是 off-policy 学习的关键

## 局限性

- **状态空间爆炸**：$5\times5=25$ 状态可表格存储，但连续状态（如机器人位置）需函数逼近（DQN）
- **奖励稀疏**：只有终点有显著奖励 → 随机探索效率低。需奖励塑形（reward shaping）
- **收敛保证**：Q-Learning 在表格情况下收敛到 $Q^*$（需每个状态-动作对被访问无穷多次）。函数逼近时可能不收敛

## 关联知识库入口

- 方法：[Markov 决策过程](../03-定理与方法/05-优化与控制/Markov决策过程.md)
- 方法：[Actor-Critic 与策略优化](../03-定理与方法/05-优化与控制/Actor-Critic与策略优化.md)
- 方法：[动态规划与递推](../03-定理与方法/05-优化与控制/动态规划与递推.md)
