---
title: scientific agent 的执行平面、调度器与实验室事务模型
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# scientific agent 的执行平面、调度器与实验室事务模型

## 1. 为什么需要执行平面

scientific agent 若只停留在“规划”和“协议映射”层，还不足以进入真实实验环境。真正落地时，还需要一个执行平面（execution plane）统一管理：

- 任务调度；
- 工具调用；
- 仪器状态同步；
- 审批与回滚；
- 证据记录与事务一致性。

## 2. 执行平面的核心组成

一个完整的执行平面通常包括：

1. 任务队列与调度器；
2. 工具运行时；
3. 仪器接口适配层；
4. 状态存储与审计日志；
5. 人工审批节点；
6. 回滚、补偿与失败隔离机制。

## 3. 为什么需要“事务模型”

实验系统的很多操作不能简单视为普通 API 调用。一次实验执行往往涉及：

- 样品状态改变；
- 仪器配置改变；
- 结果数据写回；
- 后续步骤的依赖触发。

因此更合理的建模方式是“实验室事务模型”：

- 操作要么完成，要么被标记为部分完成并进入补偿流程；
- 关键状态变更必须可追踪；
- 审批与证据链要能穿透整个执行流程。

## 4. 调度器关注什么

调度器不只决定先后顺序，还要同时考虑：

- 样品与仪器是否可用；
- 时序依赖是否满足；
- 风险等级是否需要人工审批；
- 失败后是否允许自动重试；
- 不同实验任务是否存在资源冲突。

## 5. 与其他页面的关系

建议与以下页面联动阅读：

- `../06-applications/scientific-agent-protocol-registries-and-calibration-schemas.md`
- `../06-applications/scientific-agent-protocol-compilers-registry-services-and-lab-middleware.md`
- `../06-applications/scientific-agent-execution-recovery-human-approval-and-failure-containment.md`
- `../90-appendices/lab-notebook-audit-trace-and-evidence-pack-templates.md`

## 参考文献

以下条目按 GB/T 7714—2025 数字顺序体例做最小化整理；因原文未提供完整元数据，缺失字段不补造。

[1] 文献与工程资料建议优先结合 scientific workflow systems、lab automation、workflow orchestration 与 transaction processing 方向阅读。
