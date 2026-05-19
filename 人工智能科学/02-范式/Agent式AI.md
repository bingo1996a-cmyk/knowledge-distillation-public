---
title: 智能体式人工智能（Agentic AI）
layer: 02-paradigms
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 智能体式人工智能（Agentic AI）

## 定位

agentic AI 不是“会说话的模型”，而是能够把目标分解、工具调用、环境交互、记忆管理和执行回滚组织成闭环的系统范式。

## 基本思想

- 模型只是一部分，系统还需要 memory、tool、planner、critic、policy 和 runtime governance；
- 决策不是单步输出，而是多步任务图上的执行；
- 评测对象不只是答案质量，还包括过程质量、权限边界、证据链和恢复能力。

## 关键难点

- 幻觉被写入长期记忆；
- 工具调用越权；
- 多步任务漂移；
- 失败恢复与人工审批链薄弱；
- 评测难以覆盖真实环境。

## 联读

- [多智能体系统：编排、协调与共识机制](./multi-agent-systems-orchestration-coordination-and-consensus.md)
- [检索增强、工具使用与记忆系统](./retrieval-augmentation-tool-use-and-memory.md)
- [智能体记忆、任务图与长时执行](../03-model-families/agent-memory-task-graphs-and-long-horizon-execution.md)

## 参考文献

1. Weng L. LLM-powered autonomous agents. Lil'Log, 2023. https://lilianweng.github.io/posts/2023-06-23-agent/
2. Xi Z, Chen W, Guo X, et al. The rise and potential of large language model based agents: A survey. arXiv:2309.07864, 2023.
3. Park J S, O'Brien J C, Walker C J, et al. Generative agents: Interactive simulacra of human behavior. In: Proceedings of the 36th UIST, 2023.
