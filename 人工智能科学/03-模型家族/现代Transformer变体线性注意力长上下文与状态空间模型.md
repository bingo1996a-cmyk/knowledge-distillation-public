---
title: 现代 Transformer 变体：线性注意力（Linear Attention）、长上下文（Long Context）与状态空间模型（State Space Models）
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 现代 Transformer 变体：线性注意力（Linear Attention）、长上下文（Long Context）与状态空间模型（State Space Models）

## 1. 为什么需要 Transformer 变体

原始 Transformer 的核心瓶颈在于自注意力（self-attention）复杂度随序列长度二次增长：

$$
O(n^2 d).
$$

`O(n^2 d)`

当上下文长度很长时，显存、带宽与延迟都会迅速恶化。因此，现代变体主要围绕三个目标展开：

1. 降低长序列计算成本
2. 提高长上下文记忆能力
3. 在效率与表达能力之间找到新折中

## 2. 线性注意力

线性注意力的基本想法是把 softmax attention 改写为可核化（kernelizable）形式，从而把复杂度从 $O(n^2)$ 降到近似线性。

标准 attention：

$$
\text{Attn}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt d}\right)V.
$$

线性注意力试图利用某种特征映射 $\phi(\cdot)$，写成：

$$
\text{Attn}(Q,K,V) \approx \frac{\phi(Q)\left(\phi(K)^\top V\right)}{\phi(Q)\left(\phi(K)^\top \mathbf 1\right)}.
$$

### 2.1 优点

- 长序列更省算力
- 更适合在线处理或流式推理

### 2.2 局限

- softmax 的精确归一化结构被近似
- 表达能力未必与标准 attention 等价
- 某些任务上精度下降明显

## 3. 长上下文 Transformer

长上下文方法不一定放弃标准 attention，而是通过结构/实现优化处理更长序列。

常见路线：

- 局部注意力 + 全局 token
- 稀疏注意力（sparse attention）
- 分块注意力（chunked attention）
- 位置编码改进（如 RoPE 延展）
- memory token / recurrence

### 3.1 关键挑战

- 长距离依赖是否真正被利用
- KV cache 是否可承受
- 训练长度与推理长度的不匹配
- 长上下文评测是否真实反映模型能力

## 4. 状态空间模型（State Space Models, SSM）

另一条重要路线是：不再依赖 attention 作为唯一序列建模机制，而转向状态空间递推。

一般离散状态空间形式：

$$
h_{t+1}=Ah_t+Bx_t, \quad y_t=Ch_t+Dx_t.
$$

这类模型的优势在于：

- 递推结构天然适合长序列
- 内存占用往往更可控
- 可与卷积或 selective mechanism 结合

现代 SSM 路线（如 S4、Mamba 一类）表明，序列建模并不一定必须完全依赖 attention。

## 5. Transformer 与 SSM 的关系

二者并非简单替代关系。

- Transformer 强在全局内容寻址（content-based addressing）
- SSM 强在高效长程递推

未来更可能的路线是混合结构：

- attention 负责全局检索
- SSM / recurrence 负责高效记忆传播

## 6. 与大模型工程的关系

现代 Transformer 变体不是单纯模型家族问题，而直接影响：

- 长上下文服务成本
- 边端部署可能性
- 推理吞吐与延迟
- RAG 与 memory system 的替代关系

若模型本身能高效处理长上下文，那么对外部检索系统的依赖可能下降；但若长上下文只是“容量上支持”而非“有效利用”，则 RAG 仍重要。

## 7. 常见误区

1. **误区：长上下文等于长记忆。**  
   不成立。能接收长输入，不代表能有效利用远距离信息。

2. **误区：线性注意力一定比标准 attention 更优。**  
   不成立。它主要是复杂度优化，不保证所有任务都更强。

3. **误区：SSM 会完全替代 Transformer。**  
   目前更合理的判断是互补，而非完全取代。

## 8. 建议阅读

- Attention Is All You Need
- Linear Transformer / Performer 系列论文
- Longformer / BigBird / sparse attention 系列
- S4 / Mamba 一类状态空间模型论文
- 长上下文评测与工程系统论文
