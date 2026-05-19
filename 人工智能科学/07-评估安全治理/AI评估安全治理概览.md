---
title: 人工智能评测、安全与治理概览
layer: 07-evaluation-safety-governance
tags:
  - ai-safety
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能评测、安全与治理概览

## 基本思想
治理层不是写制度文件的附属页，而是把模型能否安全、可靠、可追责地进入真实系统这一问题系统化。它同时涉及算法机制、测试方法、运行时约束、隐私保护、对抗防御和组织流程。

## 三条主线
- 评测：能力测量、鲁棒性、泛化、校准和失效模式分析。
- 安全：红队测试、越狱防御、注入攻击防护、隐私与数据治理。
- 治理：模型规格、发布门、审计证据包与责任分配。

## 为什么不能只看 benchmark
- 离线榜单只能反映某些任务切片，不能代表真实部署风险。
- 高风险系统的关键是“在边界条件下如何失败”。

## 与本库其他页面的关系
- [偏好优化：RLHF、DPO、KTO 与 RLAIF](./preference-optimization-rlhf-dpo-kto-and-rlaif.md)
