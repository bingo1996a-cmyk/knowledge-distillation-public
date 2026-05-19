---
title: 科学智能体（Scientific Agent）：协议编译器、注册服务与实验室中间件
layer: 06-applications
tags:
  - ai-applications
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 科学智能体（Scientific Agent）：协议编译器、注册服务与实验室中间件

> **阅读顺序**：本页承接 [实验仪器/平台集成](./scientific-agents-and-lab-instrument-integration.md)，讨论 SOP 编译、工具注册与中间件的技术实现。与此并列的 [协议注册表与校准模式](./scientific-agent-protocol-registries-and-calibration-schemas.md) 侧重数据结构层面，建议并读。

## 位置

这一页继续承接 scientific agent 主线，但不再只讨论协议映射和校准治理，而是讨论实验室中“怎样把文本 SOP、结构化协议、工具注册中心和设备中间件真正接起来”。

## 概念边界

这里的关键不是“会不会调用仪器”，而是三类中间层是否存在：

1. protocol compiler：把 SOP、实验步骤和约束编译成可执行 schema；
2. registry service：管理工具、仪器、版本、权限、适用条件；
3. middleware：把 agent 与 LIMS、ELN、调度器、机器人平台、传感器与设备接口连起来。

## protocol compiler 的职责

- 把自然语言 SOP 转为结构化步骤；
- 标注前置条件、禁忌条件、容差、停机条件；
- 生成 tool schema、参数模板和状态机；
- 为每一步附加 provenance 字段与审计点。

一个成熟的 protocol compiler 不是“翻译器”，而是约束显式化器。

## registry service 的职责

registry 不只是工具列表，而是实验能力目录。它至少应记录：

- 工具名称、版本、维护者；
- 输入输出 schema；
- 校准状态；
- 风险级别与审批要求；
- 支持的样品类型、批次规则、环境条件；
- 依赖的外部服务与故障回退路径。

## laboratory middleware 的职责

middleware 负责在 agent 与真实实验系统之间做适配、缓冲和审计，常见连接对象包括：

- 电子实验记录（ELN）
- 实验室信息管理系统（LIMS）
- 仪器控制 API
- 调度器与队列系统
- 样品追踪系统
- 质控与告警系统

## 典型执行链

1. 任务提出；
2. protocol compiler 生成候选协议；
3. registry 检查工具适用性与权限；
4. middleware 完成设备与数据通道绑定；
5. 人工审批高风险步骤；
6. 执行并记录 evidence pack；
7. 失败则回滚、重调度或进入再验证。

## 失败模式

- SOP 语义被过度简化，关键实验条件丢失；
- registry 信息过旧，导致错误调用停用设备；
- middleware 只做接口转发，没有做状态一致性检查；
- 样品 ID、批次、校准记录与执行日志脱节；
- 审批流与自动执行链并行存在，责任链不闭合。

## 指标

- protocol compilation success rate
- schema coverage
- tool selection accuracy
- calibration consistency rate
- human approval latency
- failed run recovery time
- evidence completeness score

## 与本库其他页面的连接

- `scientific-agents-and-experiment-automation.md`
- `scientific-agents-and-lab-instrument-integration.md`
- `scientific-agents-protocol-mapping-sample-tracking-and-calibration-governance.md`
- `scientific-agent-protocol-registries-and-calibration-schemas.md`
- `scientific-knowledge-bases-graph-memory-and-verifiable-agent-reasoning.md`

## 研究切口

1. SOP 到 schema 的自动编译与形式验证；
2. registry 的版本治理与权限分层；
3. lab middleware 的状态一致性与失败回滚；
4. protocol-level simulation 与 experiment dry-run；
5. 跨实验室的 registry federation 与证据互认。
