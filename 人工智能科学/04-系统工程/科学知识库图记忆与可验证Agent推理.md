---
title: 科学知识库、图记忆与可验证智能体推理
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 科学知识库、图记忆与可验证智能体推理

## 定位

这篇笔记把 `knowledge-graphs-and-neural-symbolic-systems.md` 拉回到系统主干，讨论它如何服务 scientific agent 与可验证推理。

重点包括：

- graph memory 与 document memory 的差异；
- entity / relation grounding；
- provenance-aware retrieval；
- 图约束检查；
- reasoning loop 的可验证化。

## 一、概念边界

### 1. document memory 解决“找到文本”，graph memory 解决“保持结构”

document memory 适合保存：

- 论文片段；
- SOP 文本；
- 仪器说明；
- 实验记录。

graph memory 更适合表示：

- 样品之间的 lineage；
- 实体间的依赖关系；
- 约束、规则与上下位关系；
- 计划步骤之间的因果顺序。

### 2. scientific knowledge base 的目标不是知识堆积

更重要的目标是：

- 支持 grounding；
- 支持 provenance；
- 支持 constraint checking；
- 支持结果可追溯。

## 二、知识库对象

在 scientific agent 场景中，建议至少显式建模：

- 实验对象：样品、试剂、材料、设备、任务；
- 结构对象：实体、关系、层级、流程边；
- 证据对象：文档、图片、日志、数据文件、审批记录；
- 规则对象：SOP、参数边界、QC 规则、停机条件；
- 版本对象：模型版本、协议版本、工具版本、环境版本。

## 三、graph memory 与 document memory 的协同

### 1. document-to-graph grounding

把非结构化文档中的关键信息映射到图结构，有助于：

- 减少同名异义；
- 暴露隐式约束；
- 建立跨文档一致性检查。

### 2. graph-to-document provenance

图中的边和属性不应孤立存在，理想状态下每个关键关系都可追溯到：

- 原始文档；
- 结构化记录；
- 仪器输出；
- 人工签发。

## 四、provenance-aware retrieval

### 1. 问题

很多 agent 检索系统只能返回“相似文本”，却无法回答：

- 这条结论来自哪里；
- 这条规则是否过期；
- 这条关系是推断出来的还是人工确认的。

### 2. 改进思路

检索结果至少应同时返回：

- 内容片段；
- 来源对象；
- 版本；
- 时间戳；
- 置信度；
- 适用范围；
- 是否已验证。

## 五、graph-based constraint checking

图结构的关键价值之一是可做约束检查，例如：

- 样品 lineage 是否闭合；
- 实验步骤顺序是否满足前置条件；
- 某个参数是否与设备状态冲突；
- 某条结论是否跨越了证据支持范围。

这使 agent 推理从“看起来合理”转向“结构上可检查”。

## 六、可验证 reasoning loop

建议把 reasoning loop 写成五步：

1. 检索文本与图对象；
2. 做 entity / relation grounding；
3. 生成候选推理链；
4. 用 graph constraint 与 provenance 进行检查；
5. 输出结论并附上证据与未验证部分。

## 七、典型系统结构

可采用“三存储 + 一验证”的模式：

- 文档存储：承载原始文档；
- 图存储：承载实体、关系、lineage 与规则；
- 日志存储：承载执行和审批记录；
- 验证层：承载一致性检查、证据链检查与约束满足判断。

## 八、失败模式

- 实体消歧失败；
- 图谱与文档不同步；
- provenance 丢失；
- 图结构太稀疏，无法承载约束；
- 图结构太密，导致检索和推理成本过高；
- reasoning loop 没有把“不可验证”显式暴露出来。

## 九、评测指标

- entity grounding 准确率；
- relation consistency；
- provenance completeness；
- constraint violation detection rate；
- reasoning trace verifiability；
- 结论的可复核率；
- 样品/协议/设备对象的一致性。

## 十、研究切口

1. 如何把 scientific SOP、仪器日志与论文文本统一进图记忆；
2. 如何让 graph memory 与向量检索系统协同；
3. 如何在 agent 推理中显式维护 provenance 与 applicability boundary；
4. 如何把图约束检查写入 planner-critic；
5. 如何建立可验证 scientific agent 的 benchmark 与 trace format。
