---
title: 似然比检验、Wald 检验、Score 检验、Bootstrap 与功效分析（Likelihood Ratio, Wald, Score, Bootstrap, and Power Analysis）
layer: 01-foundations
tags:
  - ai-theory
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 似然比检验、Wald 检验、Score 检验、Bootstrap 与功效分析（Likelihood Ratio, Wald, Score, Bootstrap, and Power Analysis）

## 1. 为什么这一页要独立出来

“假设检验、参数估计及其统计应用”给出了统计推断的总框架，但真正进入研究设计与论文实验时，最常反复出现的是五类具体工具：

- 似然比检验（Likelihood Ratio Test, LRT）
- Wald 检验（Wald Test）
- Score 检验（又称 Lagrange Multiplier Test）
- Bootstrap（自助法）
- 功效分析（Power Analysis）

它们构成了“如何比较模型、如何给出显著性、如何设计样本量”的操作核心。

## 2. 似然比检验

设完整参数空间为 $\Theta$，原假设对应的约束空间为 $\Theta_0 \subset \Theta$。定义似然比：

$$
\Lambda(x)=\frac{\sup_{\theta\in \Theta_0} L(\theta;x)}{\sup_{\theta\in \Theta} L(\theta;x)}.
$$

常用的检验统计量是

$$
-2\log \Lambda(x).
$$

在正则条件下，它渐近服从卡方分布。LRT 的思想最直接：

> 如果受限模型解释数据的能力显著弱于完整模型，则拒绝原假设。

### 适用场景

- 嵌套模型比较；
- 广义线性模型参数约束检验；
- 最大似然框架下的模型选择辅助判断。

## 3. Wald 检验

Wald 检验围绕“估计值与原假设值的距离是否足够大”构造。最简单形式为

$$
W = \frac{\hat\theta-\theta_0}{\widehat{\mathrm{SE}}(\hat\theta)}.
$$

它依赖：

- 参数估计量的渐近正态性；
- 标准误估计的稳定性。

### 优点

- 只需要拟合完整模型；
- 计算上方便。

### 局限

- 在小样本或边界参数问题上可能不稳；
- 对参数化形式敏感。

## 4. Score 检验

Score 检验只在原假设下拟合模型，考察似然在该点附近的斜率是否显著偏离零。它的思想是：

> 如果在原假设点，似然函数已经明显“想离开这里”，那么原假设就不可信。

### 适用场景

- 原假设模型易拟合、完整模型难拟合；
- 大规模统计建模中的快速筛查；
- 某些受限推断问题。

## 5. 三类检验的关系

它们都建立在似然框架上，但出发点不同：

- **LRT** 比较受限模型与完整模型的拟合优度；
- **Wald** 比较估计值与假设值的距离；
- **Score** 比较原假设点处的局部斜率。

在正则大样本条件下，它们往往渐近等价；但在有限样本、参数边界或模型错设时，表现可能明显不同。

## 6. Bootstrap：当解析近似不够可靠时

Bootstrap 通过对样本重采样来估计统计量的经验分布。常见用途：

- 估计标准误；
- 构造置信区间；
- 检查模型比较差异的稳定性；
- 对复杂指标做不依赖解析公式的误差评估。

### 常见形式

- 非参数 bootstrap；
- 参数 bootstrap；
- 配对 bootstrap；
- block bootstrap（时间序列场景）。

## 7. 功效分析

功效分析回答的问题不是“有没有显著性”，而是：

- 给定样本量与效应量，检验有多大概率发现真实差异；
- 要达到目标功效（如 0.8），需要多少样本。

这在以下场景尤为关键：

- 模型比较中的小幅提升；
- 人工评测预算有限时的样本设计；
- 在线实验和离线基准之间的取舍。

## 8. 在人工智能研究中的常见用法

### 8.1 模型对比

对两个模型做多随机种子训练，用 bootstrap 构造差值区间，比“只报一个平均值”更可靠。

### 8.2 消融实验

使用配对检验或 bootstrap 评估某个模块是否确实带来稳定增益。

### 8.3 大模型人工评测

当人工偏好打分存在波动时，bootstrap 能估计偏好差异是否稳定。

### 8.4 强化学习离策略评估

离策略估计量通常方差大、偏差复杂，bootstrap 与 DR（Doubly Robust）估计可联合使用评估稳定性。

## 9. 与本知识库的联读建议

- `hypothesis-testing-parameter-estimation-and-statistical-applications.md`
- `statistical-inference-consistency-bias-variance-concentration-and-asymptotics.md`
- `off-policy-evaluation-fqe-wis-and-doubly-robust-comparisons.md`
- `off-policy-evaluation-doubly-robust-estimators-and-ope-benchmarks.md`
