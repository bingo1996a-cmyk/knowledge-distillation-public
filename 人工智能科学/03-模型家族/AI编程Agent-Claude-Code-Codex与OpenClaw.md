---
title: 代码智能体：Claude Code、Codex 与 OpenClaw（AI Coding Agents）
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 代码智能体：Claude Code、Codex 与 OpenClaw（AI Coding Agents）

## 1. 代码模型不等于代码智能体

“代码模型”回答的是：

- 给定代码上下文，模型能否补全、解释、修改、调试。

“代码智能体”还要额外回答：

- 如何读取整个代码库；
- 如何理解多文件依赖；
- 如何调用 shell、测试、构建与浏览器；
- 如何在长任务中持续维护计划、状态与权限；
- 如何把失败恢复、审批、回归测试纳入工作流。

因此，代码智能体是“模型 + 工具 + 上下文 + 调度 + 权限 + 评测”的复合系统。

## 2. Claude Code

Claude Code 当前官方定位已经很清楚：

- 读取整个代码库；
- 修改多个文件；
- 运行命令与测试；
- 与终端、IDE、桌面端与浏览器结合；
- 在代码任务中体现 agentic coding system 的完整形态。

### 2.1 它最突出的地方

Claude Code 的一个显著特点，不只是代码生成，而是：

- 对大型代码库的理解；
- 对长任务的上下文管理；
- 对权限与审批疲劳的显式关注；
- 对 harness、tool quality 和 eval 的工程化强调。

### 2.2 它适合什么场景

- 代码审查；
- 多文件重构；
- 自动修复 bug；
- 测试生成与回归；
- 以代码库为中心的长期任务。

## 3. Codex

Codex 的当前公开路线不是早期“代码补全模型”意义上的 Codex，而是一个更完整的编码系统与工作流层。

### 3.1 关键特征

- 推荐以 GPT‑5.4 作为多数 Codex 任务的核心模型；
- 对轻量子任务可委派给 GPT‑5.4 mini；
- 支持 subagents（子代理）分工；
- 与更广义的专业工作流相连，而不局限于单个代码文件。

### 3.2 它的工程意义

Codex 的代表性不只在“代码好不好”，而在于：

- 多 agent 协作
- 模型分级调用
- 代码工作流与文档、表格、搜索、工具使用的统一

## 4. OpenClaw

OpenClaw 的意义与前两者不同。它更像：

- 开放 agent 平台；
- 个人/团队 assistant runtime；
- 可通过 Telegram、WhatsApp、Slack 等入口调用；
- 强调“让 agent 真正去做事”。

它不是以“封装某一家模型”为核心，而是以：

- 持续运行；
- 多渠道入口；
- 工具接入；
- 开放控制平面

为核心。

## 5. 三者的真实区别

### Claude Code

- 以代码库为中心；
- 强调 agentic coding、代码理解、执行与安全审批；
- 更适合工程代码工作流。

### Codex

- 以多 agent 编码与更广义专业工作流为中心；
- 强调模型分工、subagents 和更统一的任务系统。

### OpenClaw

- 以开放 agent 平台和常驻助手为中心；
- 强调跨消息入口、外部服务接入和个人/团队自动化。

## 6. 代码智能体真正依赖什么

一个代码智能体是否稳定，不主要取决于模型名字，而取决于：

- prompt 设计是否明确；
- context 是否被良好裁剪和组织；
- tools 与 skills 是否有清晰 schema；
- harness 是否有调度、回滚和权限机制；
- eval 是否能持续发现退化。

## 7. 与本知识库的联读建议

- `frontier-model-ecosystem-claude-openai-qwen-deepseek-gemini-grok-and-seed.md`
- `prompt-context-engineering-skills-and-multi-agent-harnesses.md`
- `large-model-training-inference-alignment-and-evaluation-stack.md`
- `runtime-governance-policy-enforcement-and-safe-degradation.md`
