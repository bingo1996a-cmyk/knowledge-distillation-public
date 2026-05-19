---
title: 人工智能在航天系统与航空航天中的应用
layer: 06-applications
tags:
  - ai-applications
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能在航天系统与航空航天中的应用

## 定位

本页将 AI 航天应用组织成一条研究导向主线，而不是零散罗列场景。  
它关注四个层次：

1. 地面数据分析系统；
2. 任务规划与运行支持系统；
3. 在轨自治与 onboard intelligence；
4. 评测、验证、容错与航天工程约束。

## 一、概念边界

“AI 航天应用”不能只理解为遥感图像分析。更完整的应用谱系至少包括：

- 地球观测与空间数据分析；
- 任务规划、调度与运行支持；
- 故障诊断与健康管理；
- 在轨自治、编队/星群协同；
- onboard AI 与 edge inference；
- 科学载荷数据筛选与事件触发；
- 航天器运行中的 TEVV 与 assurance。

## 二、两条主线：地面智能与在轨智能

### 1. 地面智能系统

这条线强调：

- 大规模遥感数据分析；
- foundation model for geospatial / EO；
- 数据同化与环境监测；
- mission support、预报与分析；
- 地面管控中心中的计划、异常识别与决策支持。

### 2. 在轨智能系统

这条线更强调：

- onboard autonomy；
- 延迟敏感条件下的局部决策；
- 通信受限与计算受限；
- fault tolerance；
- 在轨异常检测、重规划与安全壳。

## 三、典型任务

### 1. 遥感与地球观测

- 云检测、地表分类、目标与变化分析；
- 多时相遥感建模；
- geospatial foundation model；
- 多源遥感数据融合。

### 2. 任务规划与调度

- observation planning；
- downlink scheduling；
- multi-satellite coordination；
- resource allocation；
- conflict resolution。

### 3. 故障诊断与健康管理

- anomaly detection；
- prognostics and health management；
- subsystem fault isolation；
- graceful degradation；
- recovery planning。

### 4. 在轨自治与 onboard intelligence

- event-driven science；
- 载荷自主触发；
- 编队/星群自主协同；
- autonomous GNC support；
- onboard model inference 与 edge AI。

## 四、系统约束

AI 航天系统与普通互联网系统的差异很大，关键约束包括：

- radiation / reliability / fault tolerance；
- power、memory、thermal budget；
- certification / assurance；
- 通信时延与窗口限制；
- 上行干预成本高；
- 回滚与安全模式设计的重要性。

## 五、失败模式

- 在地面数据上有效的模型不适合 onboard 部署；
- 高准确率模型在稀缺异常和分布漂移下失效；
- 规划器忽视能源、热控、姿态和通信约束；
- onboard AI 缺少健康监测与 fallback；
- 训练 benchmark 与 mission success 脱节。

## 六、评测指标

- mission utility；
- onboard latency；
- energy efficiency；
- false alarm / missed detection；
- fault isolation accuracy；
- recovery success rate；
- autonomous replanning success；
- robustness under comms delay / packet loss。

## 七、研究切口

- foundation model 如何进入遥感与空间数据分析；
- onboard autonomy 的 assurance 边界是什么；
- distributed spacecraft autonomy 如何与 MARL、planning、verification 结合；
- AI 与航天 fault management、mission operations 的统一接口如何设计。

## 八、与其他页面的关系

- 与 [人工智能在遥感、地球观测与空间数据分析中的应用](./ai-for-remote-sensing-earth-observation-and-space-data-analysis.md) 相接；
- 与 [空间任务中的自治、规划、故障诊断与在轨智能](./autonomy-planning-fault-diagnosis-and-onboard-intelligence-for-space-missions.md) 相接；
- 与 [控制科学与工程中的人工智能：总论](./control-science-and-engineering-overview.md) 相接；
- 与 [人工智能在天气、气候与物理建模中的应用](./ai-for-weather-climate-and-physical-modeling.md) 相接。
