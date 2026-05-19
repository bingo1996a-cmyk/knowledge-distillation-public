---
title: VLA 的动作表示、端侧推理与安全壳
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# VLA 的动作表示、端侧推理与安全壳

## 定位

`vision-language-action-models.md` 主要回答“VLA 是什么”。
本页继续回答“VLA 如何落到真实执行层”。

重点包括：

- 动作 tokenization 与 chunking；
- 低时延与端侧（on-device）推理；
- policy 与 controller 的分层；
- semantic safety 与 physical safety 的联动；
- execution guardrails 与 safety shell。

## 一、概念边界

### 1. VLA 的难点不只是把动作作为输出模态

一旦模型进入执行层，问题就变成：

- 动作如何离散化或参数化；
- 推理延迟是否满足控制环；
- 低层控制误差如何反馈给高层策略；
- 哪些动作可以直接放行，哪些动作必须通过 safety shell。

### 2. 安全壳不是附加提醒，而是执行图中的强约束层

在物理系统中，semantic safety 关注“意图是否合理”，physical safety 关注“动作是否会突破物理或设备边界”。

两者必须联动，否则容易出现“语义上正确、物理上危险”的动作。

## 二、动作表示

### 1. 连续动作表示

适用于：

- 机械臂位姿；
- 速度、力矩、抓取参数；
- 连续轨迹跟踪。

优点是表达精细，缺点是：

- 对噪声敏感；
- 学习难度高；
- 更依赖低层控制器和状态估计。

### 2. 离散动作 tokenization

把动作编码为 token 或 macro action，优点包括：

- 更适合 transformer 风格建模；
- 可利用序列建模技术；
- 易于和语言/视觉 token 对齐。

缺点是：

- 精度可能受限；
- token 设计不当会导致动作语义碎裂。

### 3. action chunking

把动作按时间块或技能块输出，常见目的有两类：

- 降低解码频率；
- 提升短期执行稳定性。

但 chunk 过长会增加偏差累积，chunk 过短则会让时延问题更加尖锐。

## 三、端侧推理与低时延约束

### 1. 端侧推理的动机

在机器人或具身系统中，端侧推理常由以下需求驱动：

- 降低通信依赖；
- 提高闭环实时性；
- 保护隐私或敏感数据；
- 在网络不稳定环境下维持最小可用能力。

### 2. 端侧约束

典型约束包括：

- 算力；
- 显存/内存；
- 功耗；
- 热设计；
- 调度抖动；
- 传感器与执行器同步。

### 3. 系统层优化方向

- 模型压缩；
- 量化；
- 低时延 decoding；
- 多速率控制；
- 规划与控制分频运行；
- 局部缓存与容错执行。

## 四、policy 与 controller 的分层

### 1. 高层 policy

负责：

- 任务分解；
- 技能选择；
- 子目标生成；
- 语义层纠错。

### 2. 低层 controller

负责：

- 轨迹跟踪；
- 力/位姿控制；
- 稳定性约束；
- 局部反馈调节。

### 3. 分层接口

分层结构比单一端到端控制更适合工程落地，因为它允许：

- 把实时控制留在低层；
- 把泛化与语义能力留在高层；
- 把 safety shell 插入二者之间。

## 五、安全壳（safety shell）

### 1. 基本作用

safety shell 通常位于 policy 与 controller 之间或 controller 外层，用于：

- 检查动作是否越界；
- 拒绝不安全动作；
- 对动作做裁剪或投影；
- 在必要时触发停机或切换到保底控制器。

### 2. semantic safety 与 physical safety 的联动

可将约束分为两类：

- semantic constraints：对象、任务、语义规则、权限与场景规范；
- physical constraints：速度、力、碰撞、关节极限、禁入区域、功率与温度边界。

只有当动作同时满足两类约束，才允许进入执行链。

### 3. 常见 safety shell 结构

- 规则过滤；
- 模型预测安全过滤；
- reachability/constraint projection；
- supervisor controller；
- emergency stop；
- fallback policy。

## 六、失败模式

- action tokenization 过粗，导致动作语义不足；
- chunk 太长，执行误差不断累积；
- 端侧推理延迟超过控制闭环要求；
- 高层 policy 频繁振荡；
- safety shell 只管物理边界，不管语义边界；
- 安全过滤与任务目标冲突，导致系统长时间停滞。

## 七、评测指标

可从以下维度评估：

- 动作成功率；
- 任务完成率；
- 平均推理时延；
- 端侧资源占用；
- safety intervention rate；
- 误拦截率；
- 物理约束违规率；
- 语义约束违规率；
- fallback 成功率。

## 八、研究切口

1. 如何设计统一的 action tokenization，使 VLA 兼容多 embodiment；
2. 如何用 chunking 在稳定性与灵活性之间做平衡；
3. 如何构建高层 policy 与低层 controller 的形式化接口；
4. 如何把 semantic safety 与 physical safety 写成统一的 safety shell；
5. 如何在边缘算力条件下实现可接受的 on-device VLA 推理。
