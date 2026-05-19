---
title: 占用网络（Occupancy Networks）、鸟瞰图（BEV）与面向规划的驾驶模型
layer: 06-applications
tags:
  - ai-applications
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 占用网络（Occupancy Networks）、鸟瞰图（BEV）与面向规划的驾驶模型

## 基本思想
自动驾驶并不只需要看见物体框，还需要理解哪里可通行、哪里被占据、未来空间如何变化。占用表示与鸟瞰图表示的价值，就在于它们更接近规划器需要的空间结构，而不是只输出若干离散检测框。

## 为什么需要 Occupancy 与 BEV
- 检测框适合识别对象，但不一定适合表达道路自由空间、边界与形状。
- BEV 把多摄像头、多雷达信息统一到俯视平面，更利于规划和控制。
- Occupancy 关注“空间被什么占据、未来是否会被占据”，更贴近驾驶决策。

## 工程关注点
- 多传感器对齐、时序融合、遮挡与长尾目标。
- 预测未来占用时必须处理不确定性，而不是只给出唯一未来。

## 与本库其他页面的关系
- [自动驾驶：从模块化管线到端到端系统](./autonomous-driving-from-modular-pipelines-to-end-to-end-systems.md)
