---
title: 智能体记忆分层：情节记忆、语义记忆与结构化记忆
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 智能体记忆分层：情节记忆、语义记忆与结构化记忆

## 基本思想
长周期智能体不能只靠当前上下文窗口工作。它需要把过去交互中的信息分层保存：有些是一次任务的局部过程，有些是长期稳定的知识，有些是表、图、状态机这类可精确检索的结构化信息。

## 三类常见记忆
- 情节记忆（episodic memory）：记录具体经历，如某次执行日志和失败步骤。
- 语义记忆（semantic memory）：记录较稳定的事实、概念与偏好。
- 结构化记忆（structured memory）：记录表、图、状态机和任务对象关系。

## 为什么需要分层
- 不同信息的更新频率、可靠性和检索方式不同。
- 把所有内容都塞进向量数据库，会导致召回噪声大、状态不精确。

## 工程关注点
- 什么值得记、何时压缩、何时删除，以及如何避免过时记忆污染当前决策。

## 与本库其他页面的关系
- [多模态 RAG、图记忆与有状态工具执行](./multimodal-rag-graph-memory-and-stateful-tool-execution.md)
