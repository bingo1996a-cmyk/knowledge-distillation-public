---
title: WebGPU 入门
category: 人机交互与图形学
tags:
  - webgpu
  - graphics
  - gpu
  - web
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 官方文档
---

# WebGPU 入门

## 1. 一句话定义

WebGPU 是新一代 Web 图形和计算 API，为浏览器提供对现代 GPU 的低开销、高性能访问，是 WebGL 的继任者。

## 2. 核心问题

- WebGL 有什么不足促使 WebGPU 的出现？
- WebGPU 如何更高效地利用现代 GPU？
- 除了图形渲染，WebGPU 还能做什么？

## 3. 知识框架

| 主题 | 核心内容 |
|------|----------|
| 与 WebGL 对比 | WebGL 基于 OpenGL ES 3.0（2012 年代的 API），WebGPU 基于 Vulkan/Metal/DX12 |
| 渲染管线 | 类似现代图形 API 的显式管线管理 |
| 计算着色器 | GPU 通用计算（GPGPU）的一等公民支持 |
| 资源管理 | 显式的缓冲和纹理管理，减少隐式开销 |

## 4. 关键概念

- **显式 API vs 隐式 API**：WebGL 隐藏了 GPU 资源管理的细节（驱动自动处理），WebGPU 让开发者显式控制——更复杂但更高性能
- **适配器、设备、队列**：Adapter（物理 GPU）→ Device（逻辑 GPU 连接）→ Queue（提交命令）
- **渲染管线（Render Pipeline）**：顶点着色器 + 片元着色器 + 管线状态——预编译，减少运行时开销
- **绑定组（Bind Group）**：将资源（缓冲、纹理、采样器）预绑定到管线——减少每帧的状态切换
- **WGSL（WebGPU Shading Language）**：WebGPU 的原生着色语言——类似 Rust 语法，类型安全

## 5. 典型机制

### 5.1 WebGL vs WebGPU 核心差异

| 维度 | WebGL | WebGPU |
|------|-------|--------|
| 底层 API | OpenGL ES | Vulkan/Metal/DX12 |
| 着色语言 | GLSL | WGSL（也支持 SPIR-V）|
| 计算着色器 | 不支持（需 WebGL 2.0 Compute 扩展）| 一等公民 |
| 多线程 | 不友好 | 原生支持 |
| 管线管理 | 隐式 | 显式（PSO）|
| 开销 | 较高 | 显著更低 |

### 5.2 基本使用流程

```
1. 获取 GPU 适配器: navigator.gpu.requestAdapter()
2. 获取逻辑设备: adapter.requestDevice()
3. 创建着色器模块: device.createShaderModule()
4. 创建渲染管线: device.createRenderPipeline()
5. 创建缓冲和绑定组
6. 每一帧: 创建 CommandEncoder → 记录绘制命令 → 提交到队列
```

## 6. 经典问题

- WebGPU 的浏览器兼容性仍在推进中
- 着色器编译时间——首次加载需编译管线
- WGSL 的学习成本——不同于 GLSL
- 与现有 WebGL 生态的迁移路径

## 7. 工程实践

- 用 WebGPU 渲染三角形——"Hello Triangle"
- 使用 WebGPU 计算着色器做矩阵乘法（GPGPU 示例）
- 对比 WebGL 和 WebGPU 在相同场景下的帧率和功耗
- 探索基于 WebGPU 的 ML 推理（如 ONNX Runtime Web）

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| 计算机图形学 | WebGPU 是 Web 端的现代图形 API |
| GPU 架构 | WebGPU 设计反映现代 GPU 架构 |
| 深度学习 | WebGPU 计算着色器可用于浏览器端 ML 推理 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 标准 | W3C WebGPU Spec | 官方规范 |
| 教程 | webgpufundamentals.org | WebGPU 入门教程 |
| 工具 | WebGPU 示例集合 | 在线示例 |

## 10. 待核查问题

- WebGPU 在所有主流浏览器中的可用日期
- WebGPU vs WebGL 的实际性能提升幅度（基准测试）
- TensorFlow.js / ONNX Runtime Web 对 WebGPU 后端的支持进度
