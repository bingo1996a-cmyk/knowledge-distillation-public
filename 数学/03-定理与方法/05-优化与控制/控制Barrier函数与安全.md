# 控制障碍函数与约束安全控制

## 作用

控制障碍函数（Control Barrier Function, CBF）用于把“状态不能进入危险区域”转化为可计算、可实时检查的控制约束。

## 一个基本形式

设安全集合定义为

$$
\mathcal{C}=\{x\mid h(x)\ge 0\}
$$

若对控制系统

$$
\dot{x}=f(x)+g(x)u
$$

能够选择控制 $u$ 使得

$$
\dot{h}(x,u) + \alpha(h(x)) \ge 0
$$

则常可保证集合 $\mathcal{C}$ 的前向不变性。

## 为什么重要

### 1. 它把安全约束直接嵌入控制律或在线优化中

### 2. 它适合与二次规划、MPC 和安全滤波器结合

### 3. 它在机器人避障、自动驾驶、无人系统编队与人机协作中很常见

## 常见结构

- CBF 与控制 Lyapunov 函数（CLF）联合
- 基于二次规划的最小改动安全控制
- 与 MPC 结合形成多层安全控制架构

## 最小例子

### 例 1：单积分器避障 CBF

考虑一维系统 $\dot x = u$，安全区域 $\mathcal C = \{x \mid h(x) = x - x_{\text{obs}} \geq 0\}$，其中 $x_{\text{obs}} = 2$。

- **问题陈述**：当前 $x=2.5$，前方障碍物位于 $x=2$。可选择控制 $u=-2$（快速靠近）或 $u=0$（停止）。应用 CBF 约束检查安全性。
- **数学表达**：要求 $\dot h(x,u) + \alpha h(x) = u + \alpha(x-2) \geq 0$。取 $\alpha=1$。
- **计算/推理步骤**：$h(2.5)=0.5$。若 $u=-2$，则 $\dot h + \alpha h = -2 + 1\times 0.5 = -1.5 < 0$，违反约束。若 $u=0$，则 $0 + 0.5 = 0.5 \geq 0$，安全。因此 CBF 约束过滤掉 $u=-2$。
- **结果解读**：CBF 将"不要撞到障碍物"的安全要求转化为控制输入的线性不等式约束，可在每个时间步用 QP 求解。

### 例 2：CBF-CLF 联合 QP——追逐与安全平衡

- **问题陈述**：系统 $\dot x = u$，目标追逐用 CLF $V(x)=(x-10)^2$ 要求 $\dot V + \gamma V \leq 0$（$\gamma=1$），安全用 CBF $h(x)=x-2$ 要求 $\dot h + h \geq 0$。当前 $x=3$。
- **数学表达**：QP 形式 $\min_{u,\delta} u^2 + p\delta^2$ s.t. CLF 松弛约束和 CBF 硬约束。
- **计算/推理步骤**：CLF 约束：$\frac{\partial V}{\partial x}u + V = 2(x-10)u + (x-10)^2 \leq \delta$。当 $x=3$ 时，$-14u + 49 \leq \delta$。CBF 约束：$u + (x-2) \geq 0$，即 $u + 1 \geq 0$，$u \geq -1$。若 CLF 严格满足（$\delta=0$），则 $-14u + 49 \leq 0 \Rightarrow u \geq 3.5$，同时 CBF 要求 $u \geq -1$。折中解为 $u=3.5$，但优先保证安全性。
- **结果解读**：CBF（硬约束）保证安全，CLF（可松弛）引导向目标收敛，二者组合在安全前提下追求性能最优。

## 风险与约束

- 需要可微建模与相对阶分析
- 多个障碍约束并存时，可行性可能下降
- 安全约束与性能目标可能冲突
- 若模型误差较大，则需要鲁棒化处理

## 在资源受限条件下的可行最优路径

1. 先理解 [不变集与安全约束](../../02-核心概念/不变集与安全约束.md)
2. 再掌握 [Lyapunov 稳定性](../05-优化与控制/Lyapunov稳定性.md)
3. 然后结合 [模型预测控制](../05-优化与控制/模型预测控制.md) 和 [鲁棒、随机与分布式 MPC](../05-优化与控制/鲁棒随机与分布式MPC.md) 学习

## 与其他条目的关系

- 前置： [不变集与安全约束](../../02-核心概念/不变集与安全约束.md)
- 相关： [Lyapunov 稳定性](../05-优化与控制/Lyapunov稳定性.md)
- 相关： [鲁棒、随机与分布式 MPC](../05-优化与控制/鲁棒随机与分布式MPC.md)
- 应用： [安全自主系统中的数学](../../04-应用/安全自主与机器人系统中的数学.md)

## 推荐教材与延伸阅读

- Ames, A., Coogan, S., Egerstedt, M. & Notomista, G. "Control Barrier Functions: Theory and Applications." *European Control Conference*, 2019. — CBF 理论与应用的综述性核心文献
- Khalil, H. *Nonlinear Systems*. 3rd ed., Pearson, 2002. — 非线性系统稳定性与控制的基础参考
- Rawlings, J., Mayne, D. & Diehl, M. *Model Predictive Control: Theory, Computation, and Design*. 2nd ed., Nob Hill, 2017. — MPC 与安全约束结合的工程参考
