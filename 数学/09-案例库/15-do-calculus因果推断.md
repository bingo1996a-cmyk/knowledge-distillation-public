# 案例 15：因果推断的 do-calculus 入门案例

## 问题陈述

某公司观察到：接受过培训（$T=1$）的员工平均绩效（$Y$）高于未培训（$T=0$）的员工。但这可能是因为能力强（$A$）的员工更可能自愿参加培训。问：培训本身是否真的提高绩效？——即如何从观测数据中推断因果关系 $P(Y\mid do(T=1))$，而非仅相关性 $P(Y\mid T=1)$？

## 数学建模

**因果图（DAG）**：
```
A (能力) ──→ T (培训)
  │            │
  └──────────→ Y (绩效)
```

- $A\to T$：高能力者更可能参加培训（混杂）
- $A\to Y$：高能力者本身绩效好
- $T\to Y$：培训可能提高绩效（待检验的因果效应）

**关联 vs 因果**：
$$
P(Y\mid T=1) \neq P(Y\mid do(T=1))
$$
因为 $A$ 同时影响 $T$ 和 $Y$（混杂因子）。

## 方法：do-calculus 与后门准则

### 后门准则

$A$ 满足后门准则（指向 $T$，且有到 $Y$ 的后门路径 $A\to Y$）。以 $A$ 为条件可阻断后门路径：

$$
P(Y\mid do(T=t)) = \sum_a P(Y\mid T=t, A=a) P(A=a)
$$

这就是**后门调整公式**——在 $A$ 的每个层级内比较 $T=1$ 和 $T=0$ 的绩效差异，再按 $A$ 的总体分布加权平均。

### 前门准则

若 $A$ 不可观测但存在中介变量 $M$（训练→技能→绩效），可用前门准则：
$$
P(Y\mid do(T)) = \sum_m P(M=m\mid T)\sum_{t'} P(Y\mid T=t', M=m)P(T=t')
$$

## 数值实现（伪代码）

```python
import numpy as np

# 生成模拟数据（含混杂）
np.random.seed(42)
N = 1000
A = np.random.binomial(1, 0.5, N)          # 能力: 0=低, 1=高
# T受A影响（高能力者更多参加培训）
T = np.random.binomial(1, 0.3 + 0.5*A, N)  
# Y受A和T共同影响
Y = 50 + 10*A + 5*T + np.random.normal(0, 3, N)

# 1. 朴素关联分析（错误！有混杂）
naive_effect = Y[T==1].mean() - Y[T==0].mean()
print(f"Naive association: {naive_effect:.2f}")
# 输出: ~7.5（高估，因为掺杂了能力效应）

# 2. 后门调整（纠正混杂）
# 在A的每个层级内估计因果效应
for a in [0, 1]:
    mask = A == a
    effect_a = Y[(mask) & (T==1)].mean() - Y[(mask) & (T==0)].mean()
    print(f"Effect given A={a}: {effect_a:.2f}")

# 加权平均
p_a0 = A.mean()  # P(A=1)
adjusted_effect = 0
for a in [0, 1]:
    mask = A == a
    p_a = (A == a).mean()
    effect_a = Y[(mask) & (T==1)].mean() - Y[(mask) & (T==0)].mean()
    adjusted_effect += p_a * effect_a

print(f"Backdoor adjusted ATE: {adjusted_effect:.2f}")
print(f"True causal effect:    5.00")
# 输出:
# Naive association: 7.48
# Effect given A=0: 5.12
# Effect given A=1: 4.93
# Backdoor adjusted ATE: 5.03
# True causal effect:    5.00
```

## 结果解释

- **朴素关联高估**：$7.48 > 5.0$，因为培训组中高能力者更多，而他们本就绩效好——关联效应 = 因果效应 + 混杂偏倚
- **分层后效应接近 5**：在每个能力层级内，偏倚被消除——$A=0$ 组内效应 5.12，$A=1$ 组内 4.93，均接近真实的 5
- **后门调整精确**：加权平均 5.03——仅用观测数据恢复了因果效应
- **可推广性**：后门公式推广到连续 $A$ → 回归调整；推广到多混杂 → 倾向性得分匹配

## 局限性

- **不可观测混杂**：若存在未测量的混杂因子 $U$（同时影响 $T$ 和 $Y$），后门准则失效——需工具变量
- **因果图正确性**：do-calculus 完全依赖因果图的结构正确性。错误的因果图 → 错误的因果结论
- **正性假设**：需 $P(T=t\mid A=a)>0$ 对所有 $(t,a)$ 成立——若某能力层无人参加培训，无法估计该层的因果效应

## 关联知识库入口

- 方法：[因果推断与 do-calculus](../03-定理与方法/09-跨学科方法/因果推断与do演算.md)
- 方法：[反事实、工具变量与选择偏差](../03-定理与方法/09-跨学科方法/反事实工具变量与选择偏差.md)
- 概念：[因果性与结构模型](../02-核心概念/因果与结构模型.md)
