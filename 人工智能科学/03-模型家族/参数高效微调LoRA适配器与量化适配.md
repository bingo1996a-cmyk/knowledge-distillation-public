---
title: 参数高效微调：LoRA、Adapter 与量化适配
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 参数高效微调：LoRA、Adapter 与量化适配

## 页面关系

本页关注 PEFT 的**训练侧机制**——LoRA、Adapter、QLoRA 的原理和比较。多 Adapter 的部署与服务（路由、版本治理、冷启动）请转至 04 层：
- [多 Adapter 路由、服务与版本治理](../04-systems-engineering/multi-adapter-routing-serving-and-version-governance.md) — **服务侧**

同层内 PEFT 页的分工：
- [参数高效微调中的路由、多 Adapter 组合与合并](./parameter-efficient-finetuning-routing-multi-adapter-composition-and-merging.md) — **组合与合并机制**（训练侧，多模块如何协同）

## 1. 为什么需要参数高效微调

大模型参数规模越来越大，若每个下游任务都全量微调（Full Fine-Tuning），会带来：

- 训练成本高；
- 显存占用大；
- 多任务部署难以管理；
- 模型版本爆炸。

因此发展出**参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）**路线，只更新少量附加参数，而冻结大部分主干权重。

## 2. Adapter 的基本思想

Adapter 在每个 Transformer 层中插入一个小瓶颈模块：

$$
h \mapsto h + W_{up}\sigma(W_{down} h).
$$

其中 $W_{down}$ 把维度降到较小隐空间，$W_{up}$ 再升回原空间。这样：

- 主干模型基本不动；
- 新任务只需训练小模块；
- 可为不同任务挂接不同 adapter。

## 3. LoRA 的基本思想

低秩适配（Low-Rank Adaptation, LoRA）不直接更新完整权重矩阵 $W$，而是假设增量近似为低秩分解：

$$
\Delta W = BA,
$$

其中 $A\in \mathbb{R}^{r\times d}$，$B\in \mathbb{R}^{k\times r}$，且 $r$ 很小。于是

$$
W' = W + BA.
$$

优点是：

- 参数量远小于全量微调；
- 能直接作用于注意力或前馈层；
- 训练完成后可合并到原权重中。

## 4. QLoRA 与量化适配

QLoRA 的核心是：

- 主模型采用低比特量化存储；
- 微调时只训练少量 LoRA 参数；
- 通过量化感知和优化器技巧降低显存。

这让中大型模型在单机有限资源下微调成为可能。

## 5. Adapter、LoRA 与全量微调的比较

### 全量微调

优点：表达能力最强。  
缺点：成本最高。

### Adapter

优点：模块化、多任务管理方便。  
缺点：引入运行时额外模块。

### LoRA

优点：简单、高效、易部署。  
缺点：低秩假设未必适合所有层。

### 量化适配

优点：大幅降显存。  
缺点：量化误差可能影响收敛与最终精度。

## 6. 与蒸馏、剪枝、量化的关系

PEFT 与蒸馏、剪枝、量化并不是同一件事：

- PEFT：减少“可训练参数”；
- 蒸馏：把知识从大模型迁移到小模型；
- 剪枝：删掉部分结构或权重；
- 量化：降低数值精度。

它们可以组合，例如：

- 先量化，再 LoRA；
- 先全量微调，再蒸馏；
- 先 LoRA 适配，再做结构压缩。

## 7. 多任务与服务视角

参数高效微调特别适合：

- 多租户模型服务；
- 针对不同机构/客户的定制化微调；
- 边缘设备或资源受限环境。

现实中常见做法是：

- 基座模型共享；
- 每个任务挂一个 adapter/LoRA；
- 推理时按路由装配对应适配参数。

## 8. 现实难点

1. 适配层插在什么位置最合适；  
2. LoRA rank 如何选择；  
3. 不同任务 adapter 如何组合；  
4. 量化与微调是否相互干扰；  
5. PEFT 是否足以胜任高难任务。

## 9. 与知识库其他页面的关系

- 与“分词、蒸馏、量化与推理优化”共同构成压缩—适配—部署主线；
- 与“大模型训练、推理、对齐与评测栈”形成训练—服务桥；
- 与“Serving、KV Cache、推测解码与连续批处理”共同构成部署成本视角。

## 10. 参考资料

1. Houlsby et al. *Parameter-Efficient Transfer Learning for NLP*.
2. Hu et al. *LoRA: Low-Rank Adaptation of Large Language Models*.
3. Dettmers et al. *QLoRA*.
