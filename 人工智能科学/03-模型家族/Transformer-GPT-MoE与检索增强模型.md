---
title: Transformer 架构、生成式预训练 Transformer（GPT）、混合专家（MoE）与检索增强模型
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# Transformer 架构、生成式预训练 Transformer（GPT）、混合专家（MoE）与检索增强模型

## 1. 为什么这一页必须写得更深

如果只把 Transformer 写成“用自注意力替代循环神经网络（Recurrent Neural Network, RNN）”，那么这一页仍然过浅。Transformer 真正重要的地方在于：

1. 它把序列建模从**递归计算图**重写成**基于内容寻址的并行注意力计算图**；
2. 它使表示学习、生成建模、上下文学习（in-context learning）和工具使用型智能体能够共享一套统一骨架；
3. 它为大语言模型（Large Language Models, LLMs）与多模态基础模型（foundation models）提供了最核心的结构起点。

## 2. 经典文献脉络

Transformer 这一页应至少与以下经典文献联动阅读：

1. Vaswani et al., **Attention Is All You Need**（2017）——Transformer 起点；
2. Devlin et al., **BERT**（2018）——双向编码预训练；
3. Radford et al. / Brown et al. ——GPT 路线与大规模自回归预训练；
4. Shazeer et al. ——Mixture of Experts 稀疏扩展；
5. Lewis et al. ——Retrieval-Augmented Generation（RAG）。

本页的结构组织，也以这条演化线为主。

## 3. 从序列递推到自注意力（Self-Attention）

### 3.1 RNN 路线的限制

RNN/LSTM/GRU 的核心问题不是“不能建模序列”，而是：

- 计算必须沿时间步串行进行；
- 长程依赖需要通过长链状态传播；
- 并行性差；
- 隐状态压缩容易造成信息瓶颈。

### 3.2 自注意力的思想

Transformer 用自注意力机制让每个 token 直接与其余 token 交互。最基本的缩放点积注意力（scaled dot-product attention）为：

$$
\mathrm{Attention}(Q, K, V)=\mathrm{softmax}\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V.
$$

其中：

- $Q$ 为查询（query）；
- $K$ 为键（key）；
- $V$ 为值（value）；
- $d_k$ 为键向量维数。

直观理解：

- 查询代表“当前 token 想找什么信息”；
- 键代表“其他 token 各自能提供什么索引”；
- 值代表“真正被读取出来的信息内容”。

## 4. 多头注意力（Multi-Head Attention）为什么有效

多头注意力不是简单“多复制几份注意力”，而是在不同子空间中并行学习不同关系：

$$
\mathrm{MultiHead}(Q,K,V)=\mathrm{Concat}(\text{head}_1,\dots,\text{head}_h)W^O.
$$

每个头可以偏向不同类型的依赖：

- 词法关联；
- 句法结构；
- 指代关系；
- 长距离语义依赖；
- 程序结构与表格对齐。

它的核心收益是：把单一注意力矩阵的表达限制改造成多个低维关系子空间的组合。

## 5. 编码器—解码器、仅编码器、仅解码器三条路线

### 5.1 原始 Transformer：编码器—解码器结构

《Attention Is All You Need》中的原始结构是典型的序列到序列（sequence-to-sequence）模型，适合机器翻译等任务。

### 5.2 仅编码器（encoder-only）路线

BERT 路线强调：

- 双向上下文建模；
- 掩码语言建模（masked language modeling）；
- 更适合表征学习与判别任务。

### 5.3 仅解码器（decoder-only）路线

GPT 路线强调：

- 自回归生成；
- 下一 token 预测；
- 统一文本生成接口；
- 规模扩展后形成上下文学习能力。

因此，GPT 不是“另一个模型族”，而是 Transformer 的解码器主线。

## 6. 为什么 Transformer 能支撑大语言模型

### 6.1 并行训练

与 RNN 相比，Transformer 在训练时可大规模并行。这一点在大规模预训练中几乎是决定性的。

### 6.2 长距离依赖与上下文整合

自注意力让模型能直接建立远距离 token 之间的联系，而不必全部通过递归状态压缩。

### 6.3 可扩展性

Transformer 层结构统一、模块化程度高，便于：

- 堆叠更深；
- 扩宽隐藏维度；
- 扩大上下文窗口；
- 替换注意力与前馈层；
- 接入稀疏路由、检索、工具调用与多模态接口。

## 7. GPT：从语言建模到通用文本接口

GPT 的基本训练目标是自回归似然最大化：

$$
\max_\theta \sum_{t=1}^{T} \log p_\theta(x_t \mid x_{<t}).
$$

它的重要性有三层：

1. **语言建模层**：学习序列概率分布；
2. **能力涌现层**：规模扩展后形成上下文学习和任务迁移能力；
3. **系统接口层**：通过后训练（post-training）变成对话、编程、检索、工具使用和智能体调度的统一入口。

## 8. Transformer 的关键结构细节

### 8.1 位置编码（Positional Encoding）

自注意力本身不带顺序信息，因此必须显式注入位置信号。早期方法使用正弦位置编码，后续发展为：

- 可学习位置嵌入；
- 相对位置编码；
- Rotary Positional Embedding（RoPE）；
- ALiBi 等长上下文方法。

### 8.2 前馈网络（Feed-Forward Network, FFN）

Transformer 的每一层不只有注意力，还有逐位置前馈网络，用于提升非线性表示能力。

### 8.3 残差连接与层归一化

残差连接（residual connection）与层归一化（Layer Normalization）对深层可训练性至关重要。没有它们，深堆叠训练会明显更难。

## 9. MoE：参数容量与计算成本的折中

混合专家（Mixture of Experts, MoE）的思想是：

- 保持极大总参数量；
- 但每个 token 只激活少数专家；
- 因此单次前向计算成本可控。

其核心难点包括：

- 负载均衡（load balancing）；
- 路由稳定性（routing stability）；
- 专家塌缩（expert collapse）；
- 跨设备通信成本。

MoE 不是“参数变多的 GPT”，而是参数容量、稀疏激活与系统工程共同设计的结果。

## 10. 检索增强模型：参数记忆不是全部

RAG（Retrieval-Augmented Generation）的思想是：

- 模型参数记忆负责压缩共性模式；
- 外部知识库负责新鲜、细粒度、可追踪信息；
- 检索、重排、引用与工具调用共同构成可验证回答链。

这说明 Transformer 路线最终并不止于“模型更大”，还会自然走向：

- 检索增强；
- 工具增强；
- 外部记忆；
- 智能体式工作流。

## 11. Transformer 的局限与改进方向

### 11.1 复杂度问题

标准注意力的时间与空间复杂度通常与序列长度平方相关，因此长上下文成本高。

### 11.2 长上下文与记忆问题

尽管窗口更长，但“看到更多 token”不等于“真正长期记住并可稳定推理”。

### 11.3 推理一致性与校准问题

Transformer 强于模式拟合，但未必天然可靠：

- 置信度未必校准；
- 长推理链中易累积错误；
- 工具调用和外部知识接入需要额外治理。

因此，现代系统会进一步加入：

- verifier；
- search；
- self-consistency；
- external memory；
- runtime governance。

## 12. 与 CNN / RNN / GNN 的联系与区别

### 12.1 与 CNN

- CNN 依赖局部卷积和空间平移等变；
- Transformer 用全局注意力建模依赖。

### 12.2 与 RNN

- RNN 强调递归状态传播；
- Transformer 强调基于内容的并行交互。

### 12.3 与 GNN

图神经网络（Graph Neural Networks, GNN）中的 message passing 与注意力机制在思想上相通，都属于关系建模；但 GNN 更强调显式拓扑结构，而 Transformer 通常在完全连接图上学习关系权重。

## 13. 训练与工程实践要点

Transformer 路线的工程核心包括：

- tokenization；
- 优化器与学习率调度；
- 混合精度训练；
- 数据混配（data mixture）；
- KV cache；
- 并行与推理服务；
- 对齐（alignment）与后训练；
- 检索、工具调用与外部记忆。

## 联读

- [大语言模型](./large-language-models.md)
- [推理轨迹、验证循环与深思推理](./reasoning-traces-verification-loops-and-deliberate-inference.md)
- [大模型训练、推理、对齐与评测栈](../04-systems-engineering/large-model-training-inference-alignment-and-evaluation-stack.md)
- [生成式模型总览](./generative-model-families-gans-vaes-diffusion-and-autoregressive-models.md)

## 参考文献

[1] Vaswani, A. et al. *Attention Is All You Need*. NeurIPS, 2017.
[2] Devlin, J. et al. *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*. NAACL, 2019.
[3] Brown, T. et al. *Language Models are Few-Shot Learners*. NeurIPS, 2020.
[4] Lewis, P. et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS, 2020.
[5] Goodfellow, I., Bengio, Y., & Courville, A. *Deep Learning*. MIT Press, 2016.

## 信息状态

- 本页性质：稳定知识层
- 时效性：结构稳定，工程实现与模型规模快速变化
- 更新建议：架构原理留在本页，最新模型与产品进展单独进入 `archive/updates/`
