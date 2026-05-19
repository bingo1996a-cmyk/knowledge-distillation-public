---
title: 科学智能体（Scientific Agent）的协议注册表与校准模式（Calibration Schemas）
layer: 06-applications
tags:
  - ai-applications
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 科学智能体（Scientific Agent）的协议注册表与校准模式（Calibration Schemas）

> **阅读顺序**：本页承接 [实验仪器/平台集成](./scientific-agents-and-lab-instrument-integration.md)，讨论 protocol registry 的数据模型与校准记录结构。与此并列的 [协议编译器与中间件](./scientific-agent-protocol-compilers-registry-services-and-lab-middleware.md) 侧重系统架构层面，建议并读。

## 1. 概念边界

在 scientific agent 场景中，单有“工具能调用实验仪器”仍然不够。真实系统需要一种更制度化的中间层，把：

- SOP（Standard Operating Procedure, 标准操作程序）；
- protocol；
- sample lineage；
- calibration record；
- approval state；
- audit trail；

组织成机器可读、人工可审核的结构化对象。

本页就是对这一中间层的整理。

## 2. 为什么要有 registry

如果每次实验都靠自由文本提示描述 protocol，会出现：

- 参数命名不一致；
- 单位混乱；
- 样品 lineage 断裂；
- 校准状态不可验证；
- 审批点无法自动触发；
- 复现实验困难。

因此需要 protocol registry：把每种实验操作、仪器方法、质量门限和异常处理规则作为版本化条目维护。

## 3. registry 的最小对象模型

### 3.1 protocol definition

至少包含：

- protocol_id；
- 名称与版本；
- 适用仪器与环境；
- 输入参数 schema；
- 输出数据 schema；
- 安全前置条件；
- stop condition；
- rollback 条件；
- 责任人与审批要求。

### 3.2 sample object

- sample_id；
- 来源；
- 前序处理历史；
- 当前状态；
- 存储条件；
- 允许的 protocol 列表；
- 污染、损伤或过期标记。

### 3.3 calibration object

- instrument_id；
- calibration_id；
- 校准时间；
- 校准方法；
- 基准物；
- 偏差范围；
- 有效期；
- 当前置信状态。

## 4. schema 设计原则

### 4.1 机器可解析

字段应尽量结构化，不依赖自然语言歧义。

### 4.2 单位显式

温度、体积、浓度、时间、速度等字段必须绑定单位与允许范围。

### 4.3 版本化

protocol / calibration / decision rule 都必须有版本，否则无法复现。

### 4.4 provenance-aware

每个实验输出都要能追溯到：

- 哪个样品；
- 哪个 protocol 版本；
- 哪台仪器；
- 哪次校准；
- 哪个审批流。

## 5. approval 与 quality gate

scientific agent 不应把所有 protocol 自动执行到底。更合理的设计是按风险层级设置 gate：

- 低风险：自动执行并记录；
- 中风险：自动生成建议，人工确认；
- 高风险：需要双人复核或主管批准；
- 异常状态：自动停机并转 incident 流程。

## 6. 与其他页面的关系

- 继续深化 [scientific agent 的协议映射、样品追踪与校准治理](./scientific-agents-protocol-mapping-sample-tracking-and-calibration-governance.md)；
- 与 [scientific agent 与实验仪器/平台集成](./scientific-agents-and-lab-instrument-integration.md) 构成“接口层 -> registry 层”的连续结构；
- 与 [事件分级、阈值与取证 schema](../07-evaluation-safety-governance/incident-taxonomy-thresholds-and-forensic-schemas.md) 相接；
- 与 [scientific knowledge base、图记忆与可验证 agent 推理](../04-systems-engineering/scientific-knowledge-bases-graph-memory-and-verifiable-agent-reasoning.md) 相接。

## 7. 常见失败模式

- protocol registry 与实际设备 firmware 不一致；
- schema 写得很全，但审批链没有被系统真正调用；
- calibration 记录存在，但调度器没有把其纳入执行前检查；
- sample lineage 缺失导致结果不可追溯；
- 大模型能解释 protocol，但不能严格执行 schema 约束。

## 8. 研究切口

- protocol registry 如何与 MCP / tool schema 一类接口协议对齐；
- calibration uncertainty 如何进入 agent 决策；
- 如何把 schema 约束转化为自动 verifier；
- 如何做跨实验平台的 protocol interoperability。
