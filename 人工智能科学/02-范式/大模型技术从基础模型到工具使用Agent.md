---
title: 大模型技术：从基础模型到工具使用型智能体
layer: 02-paradigms
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 大模型技术：从基础模型到工具使用型智能体

## 1. 这页的定位

本页不把“大模型技术”只理解为更大的语言模型，而把它视为一条完整路线：

- 预训练（pretraining）；
- 适配（adaptation）；
- 后训练（post-training）；
- 推理时扩展（test-time scaling / deliberate inference）；
- 工具使用（tool use）；
- 智能体化（agentic system）。

## 2. 基础模型的基本思想

基础模型（foundation models）的思想不是为某一个任务单独设计模型，而是在大规模、多任务、多模态数据上预训练出一个可迁移的通用表示与生成器，再通过微调、提示、检索、工具和后训练进入具体任务。

核心转变是：

- 从 task-specific model 到 reusable backbone；
- 从手工设计任务特征到大规模预训练表示；
- 从静态预测器到可交互、可调用工具的决策组件。

## 3. 预训练的基本原理

### 3.1 语言建模目标

大模型通常先学习条件分布：

$$
p(x_t \mid x_{<t}).
$$

这是 next-token prediction 的核心形式。其本质是压缩、建模与生成序列结构。

### 3.2 多模态扩展

在多模态基础模型中，目标变成：

- 跨模态对齐；
- 共享表征空间；
- 多模态条件生成；
- perception-action-language 的联合建模。

## 4. 后训练与行为塑形

预训练学到的是统计结构，不等于实际可用行为。后训练用于把模型推向具体角色：

- instruction tuning；
- preference optimization；
- RLHF / RLAIF；
- rejection sampling；
- process supervision；
- verifier-based refinement。

## 5. 推理时计算与 deliberate inference

大模型能力越来越不只是参数规模，还包括推理时的额外计算：

- self-consistency；
- search；
- tree / graph exploration；
- verifier loop；
- tool-assisted reasoning；
- budgeted inference。

## 6. 从模型到智能体

大模型进入 agent 之后，关注点从“回答对不对”转向：

- 工具调用是否稳定；
- 计划是否可执行；
- 状态与记忆如何管理；
- 错误如何回滚；
- 审批流如何配置；
- 风险边界如何控制。

## 7. 你在算法清单里没有明确写出，但应纳入的大模型栏目

至少还应包括：

- tokenization 与 vocabulary design；
- position encoding；
- KV cache 与 inference efficiency；
- mixture-of-experts；
- retrieval-augmented generation；
- multimodal alignment；
- reasoning / verifier / search；
- tool use / computer use；
- distillation、quantization、serving；
- safety / eval / system card。

## 8. 与其他主线的关系

- 与深度学习主线相连：因为大模型是深度学习规模化后的重要阶段；
- 与统计学习主线相连：因为其训练目标仍然来自概率建模与风险最小化；
- 与强化学习主线相连：因为后训练与 agent 行为塑形经常依赖 RL 或 RL-like optimization；
- 与系统工程主线相连：因为真正的大模型技术包含 serving、tooling、policy、evaluation 与 monitoring。

## 9. 建议联读

- [基础模型范式：预训练、适配与部署](./foundation-model-paradigm-pretraining-adaptation-and-deployment.md)
- [大语言模型：预训练、尺度扩展、后训练与测试时计算](../03-model-families/large-language-model-pretraining-scaling-post-training-and-test-time-compute.md)
- [reasoning language model：verifier、search 与 adaptive compute](../03-model-families/reasoning-language-models-verifiers-search-and-adaptive-compute.md)
- [reasoning trace、verification loop 与 deliberate inference](../03-model-families/reasoning-traces-verification-loops-and-deliberate-inference.md)


## 10. 当前前沿生态与 agent 工程

建议继续阅读：

- [前沿大模型生态：Claude、OpenAI、Qwen、DeepSeek、Gemini、Grok 与 Seed](../03-model-families/frontier-model-ecosystem-claude-openai-qwen-deepseek-gemini-grok-and-seed.md)
- [代码智能体：Claude Code、Codex 与 OpenClaw](../03-model-families/ai-coding-agents-claude-code-codex-and-openclaw.md)
- [提示词工程、上下文工程、技能与多智能体 Harness 工程](../04-systems-engineering/prompt-context-engineering-skills-and-multi-agent-harnesses.md)
