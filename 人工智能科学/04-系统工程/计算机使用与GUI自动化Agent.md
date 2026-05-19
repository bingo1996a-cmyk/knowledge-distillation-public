---
title: 计算机使用与图形界面自动化智能体（Computer Use and GUI Automation Agents）
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 计算机使用与图形界面自动化智能体（Computer Use and GUI Automation Agents）

## 基本思想
这类智能体的目标不是只会调用 API，而是像人一样看见屏幕、理解窗口结构、定位按钮、输入文字、点击、拖拽并验证结果。它把“感知—动作—反馈”闭环直接放在图形界面上，因此比传统工具调用更接近通用软件操作。

## 基本链路
- 感知：读取屏幕截图、辅助功能树、DOM 结构或日志信号。
- 决策：把当前界面状态映射为下一步动作，例如点击、输入、滚动和复制。
- 验证：确认动作是否产生预期效果，失败时回滚或改写计划。

## 为什么更难
- 图形界面状态不稳定，元素位置会变化。
- 视觉理解、文本理解和动作控制必须统一到同一决策循环中。
- 错误会累积，长任务容易因一次误点击而整体失效。

## 工程关注点
- 动作空间抽象、失败恢复、权限边界、白名单与回滚机制。

## 与本库其他页面的关系
- [多模态 RAG、图记忆与有状态工具执行](./multimodal-rag-graph-memory-and-stateful-tool-execution.md)
