---
title: 受约束强化学习（Constrained RL）、MPC 桥接与屏蔽控制（Shielded Control）
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 受约束强化学习（Constrained RL）、MPC 桥接与屏蔽控制（Shielded Control）

## 1. 主题定位

在控制与强化学习的结合中，最重要的问题不是“RL 能不能替代控制”，而是：

- 约束如何进入学习过程；
- 模型预测控制（Model Predictive Control, MPC）与 RL 如何形成桥接；
- 在高风险环境下，如何通过 shielded control 把学习策略限制在安全可接受集合中。

这一页正是连接 `RL -> control -> deployment governance` 的桥页。

## 2. 为什么这条桥重要

纯 RL 的典型优势是：

- 可以直接从回报学习；
- 对复杂高维任务有表达能力；
- 适合处理长期 credit assignment。

纯控制方法的典型优势是：

- 约束表达清晰；
- 稳定性和鲁棒性分析更成熟；
- 在高风险场景中更容易形成 assurance。

真正有工程价值的路线，通常不是二选一，而是混合。

## 3. constrained RL 的核心思想

constrained RL 通常把问题写成带约束的优化：

$$
\max_{\pi} J_R(\pi) \quad \text{s.t.} \quad J_{C_i}(\pi) \le d_i, \; i=1,\dots,m
$$

其中 $J_R$ 是主任务回报，$J_{C_i}$ 是安全、能耗、风险或资源约束成本。

这类写法常见于 constrained Markov decision process（CMDP）。

## 4. 约束的来源

- 状态约束：位置、姿态、温度、电量；
- 输入约束：控制量幅值、速率、切换频率；
- 安全约束：碰撞、进入危险区、越界动作；
- 任务约束：时间窗、资源预算、通信窗口；
- 组织约束：审批边界、自治级别上限。

## 5. MPC 的角色

MPC 的关键价值在于：

- 用显式模型预测未来；
- 在每个时刻解有限时域优化；
- 自然处理状态/输入约束；
- 通过滚动时域形成反馈。

因此它常被用作 RL 的：

- teacher；
- safety filter；
- backup controller；
- value approximation oracle；
- trajectory generator。

## 6. RL–MPC bridge 的主要形式

### 6.1 MPC 教 RL

MPC 提供高质量轨迹、动作标签或局部最优解，供 RL 模仿或 warm start。

### 6.2 RL 学 MPC 的代价与模型残差

RL 可以学习：

- stage cost 的隐式部分；
- 动态模型残差；
- 终端价值函数近似。

### 6.3 MPC 作为在线 safety filter

RL 给出候选动作，MPC 负责检查并修正，确保动作不违反关键约束。

### 6.4 层级结构

- 高层 RL 决定目标或模式；
- 低层 MPC / controller 负责可行与稳定执行。

这是现实系统中最常见、也最易治理的结构。

## 7. shielded control 是什么

shielded control 指在策略输出与真实执行之间加入一个安全壳（shield），当策略建议违反已知约束或不变量时，系统执行替代动作或保守动作。

shield 的来源可以是：

- 规则库；
- reachability 分析；
- barrier function；
- control invariant set；
- MPC 求解器；
- runtime monitor。

## 8. shield 的三种用法

### 8.1 训练时 shield

防止 agent 在探索过程中进入危险状态。

### 8.2 执行时 shield

策略在线输出后，先过安全壳，再下发给执行器。

### 8.3 评测时 shield

用来分析若无 shield 会发生什么，以及 shield 对性能与安全的 trade-off。

## 9. 失败模式

### 9.1 奖励与约束错位

奖励鼓励高回报，但约束定义不完整，导致系统学会钻空子。

### 9.2 MPC 模型失配

MPC 所用模型与真实系统偏差过大，导致 filter 失效或过度保守。

### 9.3 shield 过强

安全壳频繁覆盖策略输出，最终系统几乎退化为固定控制器，失去学习价值。

### 9.4 shield 过弱

只覆盖少量已知风险，导致边界外行为仍可能漏检。

## 10. 评测指标

- 约束违反率；
- 安全干预频率；
- shield override 比例；
- 任务成功率；
- 样本效率；
- sim2real 性能下降；
- 在 disturbance / model mismatch 下的鲁棒性。

## 11. 典型系统结构

一个面向高风险系统的现实部署结构通常是：

`planner / RL policy -> safety filter / MPC -> low-level controller -> plant -> monitor`

在这个结构中：

- RL 负责长期目标；
- MPC 负责短期可行性；
- low-level controller 负责执行稳定性；
- monitor 负责异常检测与降级。

## 12. 研究切口

- CMDP 与 barrier certificate 的统一；
- learning-enhanced MPC；
- distribution shift 下的 safety filter 校准；
- multi-agent constrained RL 与 distributed MPC；
- shielded control 与 runtime governance 的接口标准。

## 13. 交叉阅读

- [offline RL、安全 RL 与 sim2real 流水线](./offline-rl-safe-rl-and-sim2real-pipelines.md)
- [多智能体强化学习与信用分配](./multi-agent-reinforcement-learning-and-credit-assignment.md)
- [部分可观测多智能体协同与控制](./partially-observable-multi-agent-coordination-and-control.md)
- [runtime governance、策略执行与安全降级](./runtime-governance-policy-enforcement-and-safe-degradation.md)
- [控制科学与工程中的人工智能：总论](../06-applications/control-science-and-engineering-overview.md)
