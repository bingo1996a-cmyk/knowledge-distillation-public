---
title: scientific agent 的协议映射、样品追踪与校准治理
layer: 06-applications
tags:
  - ai-applications
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# scientific agent 的协议映射、样品追踪与校准治理

> **阅读顺序**：本页是 scientific agent 系列的收口页，讨论从概念到实际实验治理的完整路径。建议在阅读 [实验自动化总论](./scientific-agents-and-experiment-automation.md)、[仪器集成](./scientific-agents-and-lab-instrument-integration.md)、[协议编译器](./scientific-agent-protocol-compilers-registry-services-and-lab-middleware.md) 与 [注册表](./scientific-agent-protocol-registries-and-calibration-schemas.md) 之后进入本页。

## 定位

这篇笔记讨论 scientific agent 从“能接入平台”走向“能在真实实验环境中被约束地运行”所需要的治理层。

核心问题不是 agent 会不会调用仪器，而是：

- 实验标准操作流程（standard operating procedure, SOP）如何映射成 tool schema；
- 样品身份、流转关系与 lineage 如何被记录；
- 仪器校准、质控（quality control, QC）与停机条件如何进入执行逻辑；
- 哪些步骤必须审批，哪些步骤允许自动执行；
- 失败后如何回滚、重试与再验证。

它承接以下页面：

- `scientific-agents-and-experiment-automation.md`
- `scientific-agents-and-lab-instrument-integration.md`
- `agent-approval-flows-permissioning-and-guardrails.md`
- `ai-testing-evaluation-verification-and-validation.md`

## 一、概念边界

### 1. scientific agent 的难点不在“会不会规划”，而在“能否被约束地执行”

现实实验并不是通用问答环境，而是由以下对象共同组成：

- 样品（sample）；
- 试剂与耗材；
- 仪器与子模块；
- 校准状态；
- 安全边界；
- 审批与责任链；
- 数据记录与证据链。

因此，scientific agent 的关键是把自然语言目标转成一组可验证、可审计、可回滚的实验动作。

### 2. SOP 到 tool schema 的映射不是字符串转换

SOP 通常隐含大量结构性约束：

- 前置条件；
- 参数范围；
- 样品准备要求；
- 清洗/灭菌/预热等状态要求；
- 失败阈值与中止条件；
- 数据记录义务。

把 SOP 映射到 tool schema，本质上是在做“实验协议的形式化表示”。

### 3. 样品追踪是实验治理的主键

真实实验中，许多错误并不来自模型推理，而来自：

- 样品混淆；
- 试剂批次混淆；
- 标签错误；
- 样品污染；
- lineage 丢失；
- 结果与样品映射失真。

如果没有 sample identity 与 provenance，agent 再强也无法形成可信实验闭环。

## 二、SOP 到 tool schema 的分层映射

### 1. 建议的四层表示

#### 第一层：目标层

用于回答实验想达到什么目标，例如：

- 测某个样品的浓度；
- 评估某个化合物的稳定性；
- 验证某个假设在特定条件下是否成立。

#### 第二层：协议层

把目标拆成实验协议步骤，例如：

- 样品接收；
- 编号；
- 预处理；
- 仪器预热；
- 参数设定；
- 运行；
- 结果检查；
- 清洗与归档。

#### 第三层：工具层

将协议步骤映射为受控工具，例如：

- `register_sample()`
- `check_calibration_status()`
- `set_run_parameters()`
- `start_measurement()`
- `validate_qc()`
- `archive_result()`

#### 第四层：执行约束层

为每个工具调用附加：

- 权限；
- 参数上下界；
- 前置条件；
- 审批要求；
- stop condition；
- 日志字段。

### 2. schema 中应显式编码的字段

建议至少包含：

- `sample_id`
- `batch_id`
- `instrument_id`
- `calibration_state`
- `operator_role`
- `approval_state`
- `parameter_bounds`
- `qc_rule`
- `stop_condition`
- `rollback_strategy`
- `evidence_pointer`

## 三、样品 ID、lineage 与 provenance

### 1. 样品对象的最小治理单元

最小样品记录建议包括：

- 样品唯一标识；
- 来源与采集时间；
- 前处理历史；
- 存储条件；
- 当前状态；
- 责任人；
- 关联实验计划。

### 2. lineage 的作用

lineage 不是附件，而是把实验链条从“结果文件”提升为“可追溯过程”的核心机制。

典型关系包括：

- 父样品与子样品；
- 分装与混合；
- 反应前后状态；
- 测量数据与原始样品绑定；
- 同一样品跨仪器流转。

### 3. provenance 的作用

provenance 关注“结果是如何来的”，通常至少要能回答：

- 谁触发了这次运行；
- 用了哪个 SOP 版本；
- 使用了哪些参数；
- 当时仪器校准状态如何；
- 哪些工具自动执行，哪些步骤经人工批准；
- 结果是否经过 QC 审核。

## 四、校准状态、QC 与停机条件

### 1. calibration state 不能作为备注字段

更合理的建模方式是把校准状态作为执行前置条件：

- `valid`
- `warning`
- `expired`
- `unknown`
- `maintenance_lock`

其中 `expired` 与 `maintenance_lock` 一般应直接阻止写操作和正式测量。

### 2. QC 规则应进入执行图，而不是只在结果后检查

QC 规则至少可作用于三处：

- 执行前：样品状态、耗材状态、环境条件是否合格；
- 执行中：信号是否漂移、运行是否越界；
- 执行后：重复性、空白对照、标准品结果是否通过。

### 3. stop condition 的必要性

没有 stop condition 的自治实验系统容易产生两类问题：

- 继续在已失效的设备或样品上运行；
- 在异常状态下反复试错，扩大损失。

stop condition 例子包括：

- 参数超界；
- QC 失败；
- 校准失效；
- 温度/压力/功率异常；
- 样品 ID 冲突；
- 未获批准却触发高风险步骤。

## 五、审批链、责任链与执行分级

### 1. 不同风险等级对应不同审批策略

建议至少分为三层：

- 低风险：只读分析、数据整理、草拟计划，可自动执行；
- 中风险：参数可写但有边界，需同级复核或双确认；
- 高风险：涉及昂贵样品、危险化学条件、关键设备状态变更，必须人工审批。

### 2. 审批对象应细化到动作级

审批不应只对“整套实验”打一个总勾选，而应细化到：

- 是否允许启动；
- 是否允许改参数；
- 是否允许重复运行；
- 是否允许销毁/分装/转移样品；
- 是否允许覆盖既有结果。

### 3. 责任链建议最少覆盖四类主体

- 计划提出者；
- 执行批准者；
- 平台维护者；
- 结果签发者。

## 六、失败回滚与再运行条件

### 1. 回滚对象不只是软件状态

scientific agent 的回滚通常涉及：

- 计划状态回滚；
- 工具权限回滚；
- 样品状态变更记录；
- 仪器运行队列回滚；
- 结果作废标记；
- 审批状态重置。

### 2. 再运行不应等于简单重试

更合理的再运行条件包括：

- 失败原因已分类；
- 风险项已消除；
- 校准状态恢复；
- 样品仍然有效；
- 新运行与旧运行有明确区分的 execution ID。

## 七、系统结构建议

建议将系统拆为五个层级：

1. 任务解释层：把研究目标转换为协议候选；
2. 协议治理层：把 SOP、schema、参数边界、审批规则绑定起来；
3. 执行编排层：驱动工具、队列和仪器；
4. 证据与追踪层：记录 sample lineage、provenance、QC、审批与结果；
5. 再验证层：把 incident、QC 失败与 postmortem 回流到规则库。

## 八、失败模式

常见失败模式包括：

- SOP 被自然语言误解；
- schema 未编码隐含约束；
- 样品 lineage 中断；
- calibration state 被缓存污染；
- QC 规则写得过松或过严；
- 高风险动作未被审批流截住；
- 失败后没有冻结相关样品或结果。

## 九、评测指标

可考虑以下指标：

- 协议映射正确率；
- 样品身份一致率；
- lineage 完整率；
- 校准状态一致率；
- QC 通过前非法执行阻断率；
- incident 后证据链完整率；
- 回滚成功率；
- 再运行后结果可比性。

## 十、研究切口

对博士阶段读者，更值得研究的问题包括：

1. 如何把自然语言 SOP 解析为带约束的执行图；
2. 如何把 sample lineage 与 graph memory 统一建模；
3. 如何把 calibration/QC/approval 编译为可验证执行策略；
4. 如何让 scientific agent 在失败后进行受限再规划而不是盲目重试；
5. 如何建立“实验计划—仪器执行—证据链—结果签发”的闭环评价体系。

## 进一步阅读

- NIST 关于部署后 AI 监测与 incident monitoring 的技术报告
- MCP 相关规范与 server metadata / event 机制
- 自动化实验平台、自治实验室与 lab orchestration 公开论文
- 样品追踪、LIMS（laboratory information management system）与 provenance 相关标准
