---
title: 工业机器人、自动移动机器人（AMR）与仓储智能
layer: 06-applications
tags:
  - ai-applications
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 工业机器人、自动移动机器人（AMR）与仓储智能

## 这页解决什么问题

工业与仓储场景的核心目标不是展示机器人很聪明，而是稳定、安全、低成本地完成搬运、拣选、装配、巡检和调度。本页通过 Amazon Robotics、Geek+、Locus Robotics 等代表性企业的工程案例，展示 AMR 与仓储智能的产业演进和技术方案演变。

## 基本思想

工业与仓储场景的核心目标不是展示机器人很聪明，而是稳定、安全、低成本地完成搬运、拣选、装配、巡检和调度。这里的系统往往需要将感知、定位、规划、控制、调度和人机协作统一起来，且必须长时间稳定运行。

## 典型系统组成

- 固定机械臂负责高精度装配、抓取或分拣。
- 自动移动机器人（Autonomous Mobile Robot, AMR）负责搬运、配送和路径执行。
- 仓储智能系统负责全局任务分配、路径协调与库存联动。

## 为什么难

- 真实环境存在遮挡、动态障碍、人机混行和任务突发变化。
- 系统评价看的是吞吐、故障率、恢复时间和维护成本，而非单点精度。

## 行业工程案例

### 1. Amazon Robotics：从 Kiva Systems 到百万机器人部署

2003 年创立 Kiva Systems，开创"货到人"（Goods-to-Person）仓储自动化模式。2012 年 3 月亚马逊以 7.75 亿美元收购 Kiva Systems，更名为 Amazon Robotics，转为内部独家使用 [1]。截至 2025 年 7 月累计部署超过 100 万台机器人。产品矩阵涵盖：Proteus（首款完全自主 AMR，无需 QR 码导航）、Hercules（AGV，载重 1,360 kg）、Pegasus（Kiva 升级版）、Sparrow（AI 视觉拣选，可识别 65% 产品）、Cardinal（包裹拣选 50 磅）、Sequoia（存储速度提升 75%）、Vulcan（双臂机器人，力感应触觉）[2]。新一代履约中心机器人数量为当前设施的 10 倍，运营成本降低约 25%。DeepFleet 生成式 AI 协调路线，车队速度提升 10% [3]。

### 2. Geek+（极智嘉）：中国 AMR 领军企业

成立于 2015 年，截至 2025 年底全球部署超 66,000 台 AMR，覆盖 40+ 国家，服务 950+ 客户，全球仓储履约 AMR 市场份额连续七年第一。拣选效率提升 2 倍，库存空间利用率超 90%，能源消耗降低 30%。2025 年上半年约 79.5% 收入来自中国以外，同年于港股上市（02590.HK）[4]。

### 3. Locus Robotics：美国移动式货到人方案

全球 350+ 部署站点，150+ 品牌客户。累计拣选量 2025 年 4 月突破 50 亿件，增速持续加快。代表客户 DHL Supply Chain 于 2024 年使用 Locus AMR 完成 5 亿次拣选。采用 RaaS 商业模式 [5]。

### 4. 工业协作机器人趋势

Universal Robots 2008 年推出首款商用协作机器人，正与 NVIDIA 开发 AI 应用 [6]。ABB 推出 3D Visual SLAM 使 AMR 无需基础设施导航 [7]。KUKA 推出 iiQWorks.Copilot（自然语言编程 AI 助手）和 SmartBinPicking（神经网络无序抓取）[8]。全球仓储自动化市场 2024 年约 221 亿美元，预计 2030 年达 550-578 亿美元 [9]。

## 工程关注点

- 地图更新、定位漂移、拥堵管理和多机协同。
- 安全区域、紧急制动、任务优先级和人工接管机制。
- 多品牌异构机器人的互操作与统一调度平台。
- RaaS 商业模式下的运维成本与 ROI 模型。

## 常见误区

- 把机器人演示的定位精度等同于系统级吞吐量；
- 忽略人机混行环境中的安全合规和工人培训成本；
- 误以为 AMR 只需 SLAM，实际多机调度比单机定位更难。

## 联读

- [多模态落地与具身问题空间](../05-problem-spaces/multimodal-grounding-and-embodiment-problem-space.md)
- [具身智能与物理 AI](./embodied-intelligence-and-physical-ai.md)
- [控制科学与工程总论](./control-science-and-engineering-overview.md)

## 参考文献

[1] 信息待补齐. Kiva Systems Acquisition by Amazon[J]. SEC Filing, 2012.
[2] Amazon. Meet the Robots Inside Amazon Fulfillment Centers[EB/OL]. 2025.
[3] TechCrunch. Amazon Deploys Its 1 Millionth Robot[EB/OL]. 2025-07-01.
[4] 极智嘉. 极智嘉蝉联全球 AMR 市场份额第一[EB/OL]. 2025.
[5] Locus Robotics. Surpasses 5 Billion Pick Milestone[EB/OL]. 2025.
[6] Universal Robots. Reports Q1 2024 Revenue[EB/OL]. 2024.
[7] ABB. Visual SLAM Technology[EB/OL]. 2025.
[8] KUKA. Artificial Intelligence in Automation[EB/OL]. 2025.
[9] Grand View Research. Warehouse Automation Market Report[R]. 2024.
