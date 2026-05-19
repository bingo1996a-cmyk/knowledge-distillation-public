---
title: 提示词工程、上下文工程、技能与多智能体 Harness 工程（Prompt Engineering, Context Engineering, Skills, and Multi-Agent Harnesses）
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 提示词工程、上下文工程、技能与多智能体 Harness 工程（Prompt Engineering, Context Engineering, Skills, and Multi-Agent Harnesses）

## 1. 为什么这页必须写厚

大模型系统从“单轮聊天”走向“长任务智能体”以后，系统瓶颈通常不再是某一句提示词，而是整个运行框架：

- 提示词工程（Prompt Engineering）
- 上下文工程（Context Engineering）
- 技能（Skills）与工具（Tools）
- 智能体 Harness
- 权限、审批与运行时治理

这几部分共同决定：

- agent 是否稳定；
- agent 是否可审计；
- agent 是否能在长任务中不崩溃；
- agent 是否能复用、测试与迭代。

## 2. 提示词工程

提示词工程研究的是：

> 如何用指令、示例、角色、输出约束和工具说明，使模型在单轮或短程任务中更可能给出正确输出？

常见构件包括：

- system prompt；
- role / persona；
- 少样本示例；
- 输出 schema；
- 思维过程约束；
- 工具调用说明。

### 它的局限

提示词工程重要，但它不能替代：

- 上下文组织；
- 记忆管理；
- 工具质量；
- 调度器与 harness。

## 3. 上下文工程

Anthropic 明确把上下文工程定义为：

> 在推理时整理并维持最优 token 集合的策略集合。

因此，上下文工程不是“长 prompt”，而是：

- 哪些历史该保留；
- 哪些检索结果该注入；
- 哪些 memory 应该压缩；
- 哪些工具说明应显式放进上下文；
- 当前审批、权限、任务状态如何编码进上下文。

### 核心问题

- 预算有限，什么信息最值得进入上下文？
- 旧信息如何压缩、摘要与遗忘？
- 多 agent 之间如何共享还是隔离上下文？

## 4. Skills 与 Tools

### 4.1 Tool

工具是模型可调用的外部功能接口，例如：

- shell 执行；
- 文件读写；
- 数据库查询；
- Web / API 请求；
- MCP server 暴露的资源与操作。

### 4.2 Skill

技能更像可复用的能力模块，通常包含：

- 目标任务定义；
- 输入输出 schema；
- 所依赖工具；
- 行为约束；
- 评测样例与回归基准。

一个成熟 skill 的价值在于：

- 可组合；
- 可测试；
- 可版本化；
- 可迁移到不同模型或 harness。

## 5. Multi-Agent Harness 是什么

Harness 是智能体外层的编排系统，而不是单个模型。

它通常负责：

- 任务分解；
- agent 角色划分；
- 子任务调度；
- 上下文裁剪与补全；
- tool / skill 调用；
- 审批与权限流；
- 失败恢复；
- 评测与日志。

### 为什么需要多智能体 harness

因为单个 agent 在长任务中容易遭遇：

- 上下文爆炸；
- 角色混乱；
- 计划漂移；
- 工具调用错误；
- 审批疲劳。

多智能体 harness 的意义，在于把任务拆成：

- 规划 agent；
- 执行 agent；
- 验证 agent；
- 回滚 / 审批 agent；
- 监测 agent。

## 6. MCP 与标准化工具接入

模型上下文协议（Model Context Protocol, MCP）把工具与资源标准化暴露给模型或 agent。它的重要性不在于“多了一个协议”，而在于：

- tools 可以标准化；
- skills 可以复用工具描述；
- harness 不必为每个工具写专用胶水层；
- agent 评测更容易对齐输入输出。

## 7. 失败模式

### 7.1 只优化 prompt，不做 context 管理

结果通常是：

- 前几轮看起来很好；
- 长任务迅速漂移；
- 历史信息污染当前决策。

### 7.2 工具很多，但没有 schema 和测试

这会导致：

- 调用格式错误；
- 返回结果不可解析；
- 失败后没有 fallback。

### 7.3 有 agent，没有 harness

这意味着：

- 任务不能稳定分解；
- 权限不可追踪；
- 失败恢复只能靠人工救火。

## 8. 实际工程中最该关注什么

如果目标是“让 agent 真正可用”，应优先做：

1. 明确 skill 的输入输出与测试样例；
2. 把工具文档写成模型友好形式；
3. 建立 context compaction 与 memory policy；
4. 建立 harness 级日志、审批与回滚；
5. 用长期任务 eval 而不是单轮 prompt eval 判断系统质量。

## 9. 与本知识库的联读建议

- `frontier-model-ecosystem-claude-openai-qwen-deepseek-gemini-grok-and-seed.md`
- `ai-coding-agents-claude-code-codex-and-openclaw.md`
- `reasoning-systems-routing-caching-and-scheduling.md`
- `runtime-governance-policy-enforcement-and-safe-degradation.md`
- `multi-adapter-routing-serving-and-version-governance.md`
