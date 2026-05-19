---
title: PAC 学习、稳定性与基于压缩的泛化解释
layer: 01-foundations
tags:
  - ai-theory
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# PAC 学习、稳定性与基于压缩的泛化解释

## 1. 这一页解决什么问题

前面几页已经解释了经验风险最小化（Empirical Risk Minimization, ERM）、偏差—方差、PAC-Bayes 与信息几何，但仍然缺一条更“离散化、算法化、可证明”的泛化主线：

- 为什么同样训练误差接近 0 的模型，测试误差会不同？
- 为什么某些训练算法比另一些更稳定？
- 为什么压缩后的模型常常更容易解释泛化？

这一页补上三条经典解释链：

1. PAC 学习（Probably Approximately Correct Learning）
2. 算法稳定性（Algorithmic Stability）
3. 基于压缩的泛化解释（Compression-based Generalization）

## 2. PAC 学习的基本思想

PAC 学习关心的问题不是“某一次训练是否成功”，而是：在给定样本规模 $n$ 时，一个学习算法能否以高概率输出近似最优的假设。

最常见的 PAC 叙述包含两层误差控制：

- **近似误差**：假设空间本身是否足够表达目标规律；
- **估计误差**：有限样本下经验风险与总体风险之间的差距。

若对任意 $
ho>0$ 与 $\eta 	o 0$，存在样本复杂度 $n(
ho,\eta)$，使得学习器输出的假设 $h$ 满足

$$
\Pr\big(R(h) \le R^* + \rho\big) \ge 1-\beta,
$$

则可说该问题在相应假设空间内是 PAC 可学习的。

这里：

- $R(h)$ 是总体风险；
- $R^*$ 是最优假设的总体风险；
- $\rho$ 是允许的精度；
- $\beta$ 是失败概率。

PAC 的根本意义是把“学习是否有效”转化为“样本复杂度能否控制”。

## 3. VC 维与容量控制

PAC 学习最经典的容量刻画是 VC 维（Vapnik–Chervonenkis Dimension）。

直观上，VC 维衡量一个假设空间对样本进行任意二值划分的能力。容量越大，表达能力越强，但过拟合风险也越大。

经验风险与总体风险之间的典型界可写成：

$$
R(h) \le \hat R(h) + O\!\left(\sqrt{\frac{d_{VC}\log n + \log(1/\delta)}{n}}\right),
$$

其中 $d_{VC}$ 为 VC 维，$\delta$ 为失败概率。

这个结果的结构比常数更重要：

- 随样本数 $n$ 增大，泛化间隙缩小；
- 随模型容量 $d_{VC}$ 增大，泛化间隙变大；
- 这为“容量控制—正则化—结构风险最小化”提供了理论基础。

## 4. Rademacher 复杂度与数据依赖泛化界

VC 维是分布无关、最坏情况的容量度量。Rademacher 复杂度则更接近“给定数据集上模型能否拟合噪声”的能力。

经验 Rademacher 复杂度写作

$$
\hat{\mathfrak{R}}_n(\mathcal{H})
= \mathbb{E}_{\sigma}\left[\sup_{h\in\mathcal{H}} \frac{1}{n}\sum_{i=1}^n \sigma_i h(x_i)\right],
$$

其中 $\sigma_i \in \{-1,+1\}$ 为 Rademacher 随机变量。

它告诉我们：若一个假设空间可以轻易拟合随机符号，那么它的复杂度较高，泛化更危险。

Rademacher 复杂度的价值在于：

- 比 VC 维更细；
- 能处理实值函数；
- 更容易与 margin、norm、Lipschitz 性等结合。

## 5. 算法稳定性：从函数类转向训练过程

PAC/VC/Rademacher 主要从“假设空间”解释泛化，算法稳定性则问：

> 若训练集只改动一个样本，学习器输出会不会剧烈变化？

若变化很小，则说明算法不容易过度依赖单个样本，泛化通常更好。

统一稳定性（uniform stability）的典型形式是：对任意相邻数据集 $S,S^{(i)}$，以及任意测试点 $z$，有

$$
\big|\ell(A(S), z)-\ell(A(S^{(i)}), z)\big| \le \epsilon_n.
$$

这意味着算法输出对单样本扰动敏感度受控。

稳定性理论的重要意义在于：

- 它直接分析“算法”，而不只分析“函数类”；
- 特别适合解释带随机梯度下降（Stochastic Gradient Descent, SGD）的现代训练；
- 它与早停、权重衰减、噪声注入、小步长训练等技术自然相连。

## 6. SGD 为什么可能具有隐式稳定性

随机梯度下降之所以能在过参数化场景中仍保持较好泛化，一个经典解释就是：

- 小步长会抑制对单样本的敏感度；
- 随机批采样相当于给训练动态加入噪声；
- 早停限制了参数沿高曲率方向过度放大；
- 参数范数与 margin 常一起被间接控制。

因此，SGD 的“隐式偏置（implicit bias）”既可以从优化几何解释，也可以从稳定性解释。

## 7. 基于压缩的泛化解释

压缩型泛化解释的直觉很简单：

> 如果一个模型训练完后还能被显著压缩，而性能几乎不掉，说明它真正使用的有效自由度比表面参数量小得多。

常见压缩方式包括：

- 权重量化；
- 低秩分解；
- 剪枝；
- 蒸馏；
- 稀疏子网络抽取。

压缩泛化界通常把“模型描述长度”与“泛化误差”挂钩。若一个假设可由较短编码表示，则其有效复杂度更低。

这与最小描述长度（Minimum Description Length, MDL）思想一致：

- 可压缩性强，意味着冗余大；
- 冗余大，意味着并非所有参数都承担独立拟合任务；
- 因而泛化能力可能比表面参数量更好。

## 8. 压缩、稳定性、PAC-Bayes 的关系

这三条线并不冲突，而是互补：

- **PAC/VC/Rademacher**：解释函数类容量；
- **稳定性**：解释训练算法为何不对样本过敏；
- **压缩**：解释训练完成后模型的有效复杂度为何较低；
- **PAC-Bayes**：把先验、后验和复杂度统一进一个概率界框架。

一个可以记忆的理解方式是：

- PAC 问“能否学到”；
- 稳定性问“为何不易过拟合”；
- 压缩问“为何大模型仍可泛化”；
- PAC-Bayes 问“如何把先验与复杂度一并计入”。

## 9. 在深度学习中的现实作用

这些理论并不能完全解释现代深度网络的全部行为，但它们已经提供了几种高价值工具：

1. 解释为什么参数量不是唯一复杂度指标；
2. 解释 SGD、早停、权重衰减等训练机制为何有用；
3. 为蒸馏、剪枝、量化等工程手段提供理论支持；
4. 为高风险系统中的“泛化保证”提供更可审计的表述方式。

## 10. 与其他页面的关系

建议把本页与以下页面联合阅读：

- `probability-statistics-and-statistical-learning.md`
- `statistical-inference-consistency-bias-variance-concentration-and-asymptotics.md`
- `pac-bayes-information-geometry-and-modern-generalization-explanations.md`
- `optimization-landscapes-curvature-conditioning-and-scale-aware-training.md`
- `tokenization-distillation-quantization-and-inference-optimization.md`

## 参考文献

以下条目按 GB/T 7714—2025 数字顺序体例做最小化整理；因原文未提供完整元数据，缺失字段不补造。

[1] Valiant, L. G. *A Theory of the Learnable*. CACM, 1984.
[2] Vapnik, V. *Statistical Learning Theory*. Wiley, 1998.
[3] Shalev-Shwartz, S., Ben-David, S. *Understanding Machine Learning*. Cambridge University Press, 2014.
[4] Bousquet, O., Elisseeff, A. *Stability and Generalization*. JMLR, 2002.
[5] Arora, S. et al. *Stronger Generalization Bounds for Deep Nets via a Compression Approach*. ICML, 2018.
[6] Neyshabur, B. et al. *Towards Understanding the Role of Over-Parametrization in Generalization of Neural Networks*. ICLR Workshop, 2019.
