---
title: C/C++ 工程化
category: 工程实践专题
tags:
  - cpp
  - cmake
  - build-system
  - memory-safety
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# C/C++ 工程化

## 1. 一句话定义

C/C++ 工程化关注如何用现代工具链和工程实践管理系统级语言项目，平衡性能、可维护性和安全性。

## 2. 核心问题

- 如何管理跨平台编译的复杂依赖？
- 如何在不牺牲性能的前提下保证内存安全？
- 如何在大型 C++ 项目中控制编译时间和二进制体积？

## 3. 知识框架

| 主题 | 核心内容 | 关键工具/标准 |
|------|----------|---------------|
| 编译系统 | 跨平台构建配置 | CMake、Bazel、Meson |
| 包管理 | 依赖获取与版本锁定 | vcpkg、Conan、FetchContent |
| 内存安全 | 动态分析、智能指针 | ASan、Valgrind、RAII |
| 代码质量 | 静态分析、格式化 | clang-tidy、clang-format |
| 现代 C++ | C++17/20/23 特性 | RAII、智能指针、concepts |

## 4. 关键概念

- **RAII（资源获取即初始化）**：资源（内存、文件、锁）的生命周期绑定到对象——C++ 最重要的设计惯用法
- **智能指针**：`unique_ptr`（独占所有权）、`shared_ptr`（共享所有权）、`weak_ptr`（打破循环引用）——避免手动 `new`/`delete`
- **三/五法则**：如果自定义了析构函数/拷贝构造/赋值，应同时考虑移动语义——控制对象生命周期
- **ABI 稳定性**：不同编译器/版本间二进制接口的兼容性——大型项目的关键考虑
- **Sanitizer（消毒器）**：AddressSanitizer（内存错误）、UndefinedBehaviorSanitizer（UB）、ThreadSanitizer（数据竞争）

## 5. 典型实践

### 5.1 现代 CMake 项目结构

```
project/
├── CMakeLists.txt          # 顶层
├── src/
│   ├── CMakeLists.txt      # 库定义
│   └── *.cpp
├── include/project/        # 公共头文件
├── tests/
│   ├── CMakeLists.txt
│   └── *.cpp
├── cmake/                  # CMake 模块
└── vcpkg.json              # 依赖清单
```

### 5.2 编译选项速查

| 用途 | GCC/Clang 标志 |
|------|----------------|
| 开发调试 | `-g -O0 -Wall -Wextra -fsanitize=address` |
| 生产优化 | `-O3 -march=native -flto` |
| 安全加固 | `-fstack-protector-strong -D_FORTIFY_SOURCE=2` |
| 警告全开 | `-Wall -Wextra -Wpedantic -Werror` |

## 6. 经典问题

- 头文件包含顺序与循环依赖
- 编译时间过长——前置声明、Pimpl 惯用法、预编译头
- 模板的编译错误可读性差
- ABI 不兼容导致链接错误

## 7. 工程实践

- 将手动 Makefile 项目迁移到 CMake
- 集成 clang-tidy 到 CI 流程做静态分析
- 使用 Valgrind/ASan 检测内存泄漏/UAF
- 阅读 C++ Core Guidelines 并逐步应用

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| 编译原理 | 理解编译过程有助于调试构建问题 |
| 操作系统 | C/C++ 是开发 OS 和驱动的主要语言 |
| 系统安全 | 内存安全是 C/C++ 安全的重中之重 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 书籍 | Effective Modern C++ (Meyers) | 现代 C++ 最佳实践 |
| 标准 | C++ Core Guidelines (Stroustrup & Sutter) | C++ 编程规范 |
| 工具 | CMake 官方文档 + Professional CMake | CMake 权威 |

## 10. 待核查问题

- C++26 的模块（Modules）系统对传统头文件编译模型的改变
- Rust 在系统编程领域对 C/C++ 的替代趋势
