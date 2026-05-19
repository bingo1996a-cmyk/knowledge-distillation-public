---
title: AI 在医疗、基因组学与临床决策支持中的应用
layer: 06-applications
tags:
  - ai-applications
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# AI 在医疗、基因组学与临床决策支持中的应用

## 这页解决什么问题

医疗 AI 不是把通用模型搬进医院那么简单，它同时面对高错误代价、强监管、异质数据、多学科流程和因果解释需求。本页梳理医疗 AI 的三大主线——基因组学、医学影像与临床决策支持——并给出 FDA 批准 AI 医疗设备的时间线，帮助读者建立从研发到监管的可操作视角。

## 基本思想

医疗 AI 不是"把通用模型搬进医院"那么简单。它同时面对高错误代价、强监管、异质数据、多学科流程和因果解释需求。基因组学问题、医学影像问题、临床文本问题、决策支持问题虽然都属于医疗 AI，但它们的数据结构、验证方式和伦理约束差异很大。

## 三条主线

### 1. 基因组学与生物序列模型

目标是从 DNA、RNA、蛋白质序列及其上下游信息中学习结构、功能、调控与变异影响。这里常涉及基础模型、序列建模与生物先验融合。

### 2. 医学影像与多模态诊断

目标是从 CT、MRI、超声、病理切片等影像中识别病灶、辅助分型，并与临床文本、检验指标联合形成更完整判断。

### 3. 临床决策支持

目标是帮助医生完成风险分层、鉴别诊断、治疗建议与流程管理。这里最关键的问题不是"模型说得像不像医生"，而是是否真的提高了决策质量并降低了系统性风险。

## FDA 批准 AI 医疗设备演进

FDA 对 AI/ML 医疗设备的批准自 2018 年以来呈现爆发式增长。2015 年仅批准 6 款，2023 年达约 221 款，2024 年约 253 款，2025 年约 295 款，累计已超 1,400 款。约 76.7% 属于放射学领域，95.8% 走 510(k) 审批途径。头部厂商 GE 医疗（81 款）和西门子医疗（70 款）领跑 [1]。

关键里程碑产品及其技术意义：Arterys Cardio DL（2017.01）为首个 FDA 批准的云端深度学习医学影像软件，实现心脏 MRI 自动量化分析 [2]；Viz.ai（2018.02）为首个 AI 卒中检测与分诊软件，将中风响应时间从 57 分钟降至 6 分钟 [3]；IDx-DR（2018.04）为首个无需医生解读的自主 AI 诊断系统，用于糖尿病视网膜病变筛查 [4]；Aidoc（2018.08）为首个放射科 AI 分诊工具，后扩展至 14 种以上适应症，2026 年获首个多条件综合 AI 基础模型批准 [5]；Paige Prostate（2021.09）为首个 FDA 授权的 AI 病理产品，用于前列腺癌检测，是 150 年病理学史上的里程碑突破 [6]。

在基因组学领域，23andMe 于 2017 年获批首个直接面向消费者的基因健康风险检测，2018 年获批 BRCA1/BRCA2 癌症风险检测 [7]；Tempus 于 2023 年获批基于 NGS 的大 panel 伴随诊断试剂盒。

在大语言模型方向，Google 的 Med-PaLM（2022.12）成为首个通过 USMLE 的 AI 系统（67.6%），Med-PaLM 2（2023.03）提升至 86.5% 达到人类专家水平 [8]；GPT-4 在 2023 年以通用模型身份超越所有医学专用模型。截至 2025 年，尚无生成式 AI / LLM 产品作为医疗设备获得 FDA 批准，但 FDA 已发布相关指南草案积极推动审评。

## 工程关注点

- 医疗标签往往噪声大、定义不完全统一；
- 数据分布具有强医院依赖、设备依赖和人群依赖；
- 评测不能只看 AUC，还要看校准、亚群体偏差、工作流适配和真实临床收益；
- 上线必须考虑责任归属、留痕、医生主导和人工复核。

## 常见误区

- 把 benchmark 分数当作临床可用性；
- 忽视数据治理、隐私与知情同意；
- 把生成式解释误当作因果解释；
- 让模型替代临床责任，而不是辅助临床判断。

## 联读

- [隐私保护学习：差分隐私、联邦学习与安全推理](../07-evaluation-safety-governance/privacy-preserving-learning-dp-fl-and-secure-inference.md)
- [科学发现、设计与闭环优化](../05-problem-spaces/scientific-discovery-design-and-closed-loop-optimization.md)
- [AI for Science：科学发现](../../06-applications/ai-for-scientific-discovery.md)

## 参考文献

[1] FDA. Artificial Intelligence-Enabled Medical Devices[EB/OL]. 2025.
[2] Arterys. Arterys Cardio DL Receives FDA Clearance[EB/OL]. 2017.
[3] FDA. FDA Permits Marketing of Viz.ai Contact Stroke Detection[EB/OL]. 2018.
[4] FDA. FDA Authorizes First AI Screening for Diabetic Retinopathy[EB/OL]. 2018.
[5] Aidoc. Aidoc Receives FDA Clearance for First AI Triage Tool[EB/OL]. 2018.
[6] Paige. Paige Prostate Receives First FDA Authorization in Digital Pathology[EB/OL]. 2021.
[7] 23andMe. 23andMe and the FDA[EB/OL]. 2017-2018.
[8] Singhal K, Azizi S, Tu T, et al. Large Language Models Encode Clinical Knowledge[J]. Nature, 2023, 620(7972): 172-180.
