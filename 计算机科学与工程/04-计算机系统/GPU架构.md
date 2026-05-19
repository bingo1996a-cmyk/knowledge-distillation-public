---
title: GPU 架构
category: 计算机系统
tags:
  - gpu
  - cuda
  - simd
  - parallel-computing
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# GPU 架构

## 1. 一句话定义

GPU（Graphics Processing Unit）是面向大规模数据并行的专用处理器，通过数千个简单核心同时执行相同指令处理不同数据（SIMT 模型），是现代深度学习训练和推理的核心硬件。

## 2. 核心问题

- GPU 和 CPU 在架构哲学上的根本区别是什么？
- 如何编写代码充分利用 GPU 的并行能力？
- 显存层次如何影响性能？

## 3. 知识框架

| 层次 | 核心内容 | 关键概念 |
|------|----------|----------|
| 硬件架构 | SM（流式多处理器）、CUDA 核心、Tensor 核心 | SIMT 执行模型 |
| 内存层次 | 全局内存、共享内存、寄存器 | 合并访问、Bank 冲突 |
| 编程模型 | 线程网格、线程块、Warp | CUDA C++ / HIP |
| 优化技术 | 内存合并、占用率、异步传输 | 计算-传输重叠 |

## 4. 关键概念

- **SIMT（单指令多线程）**：一个 Warp（32 线程）同时执行同一指令但操作不同数据——GPU 并行的基本单位
- **Warp 分歧**：同一 Warp 内线程走不同分支 → 串行化执行——GPU 编程需要避免的主要性能陷阱
- **SM（流式多处理器）**：GPU 的调度单元——包含整数单元、浮点单元、Tensor 核心、共享内存
- **Tensor 核心**：专门加速矩阵乘加运算（D = A×B + C）的硬件单元——深度学习训练的主力
- **合并访问（Coalesced Access）**：同一 Warp 的线程访问连续内存地址时，可合并为一次宽访存

## 5. 典型机制

### 5.1 GPU 内存层次

```
慢/大 ──────────────────────────── 快/小
HBM(显存) > L2 Cache > L1/共享内存 > 寄存器
  ~1TB/s    ~3TB/s     ~10TB/s     ~100TB/s
  数十GB    数十MB      ~100KB/Warp  ~256KB/SM
```

### 5.2 CPU vs GPU 架构差异

| 维度 | CPU | GPU |
|------|-----|-----|
| 核心数 | 几个-几十个 | 数千个 |
| 单核性能 | 极高（复杂乱序）| 较低（简单顺序）|
| 晶体管预算 | 控制逻辑 + 大缓存 | 计算单元 + 小缓存 |
| 并行粒度 | 任务并行（多进程/线程）| 数据并行（SIMT）|
| 内存带宽 | ~100GB/s | ~1-2TB/s |
| 延迟容忍 | 通过缓存减少延迟 | 通过大量 Warp 切换隐藏延迟 |

## 6. 经典问题

- Warp 分歧——分支导致执行效率减半
- 全局内存非合并访问——性能下降 10×+
- 共享内存 Bank 冲突——多线程同时访问同一 Bank
- PCIe 传输瓶颈——CPU↔GPU 数据传输速度远小于 GPU 内存带宽

## 7. 工程实践

- 用 CUDA 实现向量加法和矩阵乘法
- 使用 `nvidia-smi` 监控 GPU 利用率和显存
- 用 Nsight Systems 分析 CUDA kernel 的时间线和瓶颈
- 理解 PyTorch 中 `.to('cuda')` 和 `.cpu()` 的隐式数据传输代价

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| 计算机体系结构 | GPU 是领域特定架构的典型实例 |
| 深度学习 | GPU 是 DL 训练和推理的核心硬件 |
| 并行算法 | 算法设计需适应 GPU 的 SIMT 模型 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 教材 | Programming Massively Parallel Processors (Kirk & Hwu) | CUDA 编程权威 |
| 文档 | NVIDIA CUDA C++ Programming Guide | CUDA 官方编程指南 |
| 课程 | NVIDIA DLI (Deep Learning Institute) | GPU 实操课程 |

## 10. 待核查问题

- GPU vs 专用 AI 芯片（TPU、NPU）的优劣势对比
- 存算一体（Processing-in-Memory）是否会改变 GPU 的统治地位
- CUDA 生态的锁定效应和开源替代方案（ROCm、SYCL）的进展
