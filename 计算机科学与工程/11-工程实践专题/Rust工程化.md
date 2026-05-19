---
title: Rust 工程化
category: 工程实践专题
tags:
  - rust
  - cargo
  - systems-programming
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# Rust 工程化

## 1. 一句话定义

Rust 是注重内存安全、并发安全和零成本抽象的系统编程语言，Cargo 是其内置的构建系统和包管理器——Rust 工程化即用这套工具链高效、安全地构建和发布 Rust 项目。

## 2. 核心问题

- 所有权和借用的心智模型如何掌握？
- 如何利用 Cargo 的工具生态提高开发效率？
- 如何在保持安全性的前提下优化性能？

## 3. 知识框架

| 主题 | 核心内容 | 关键工具 |
|------|----------|----------|
| 构建系统 | 项目管理、依赖解析 | Cargo、crates.io |
| 所有权模型 | 所有权、借用、生命周期 | rustc 借用检查器 |
| 错误处理 | Result、Option、? 运算符 | anyhow、thiserror |
| 测试 | 单元测试、集成测试、文档测试 | cargo test |
| 性能分析 | Profiling、基准测试 | criterion、flamegraph |
| FFI | 与 C/其他语言互操作 | bindgen、cbindgen |

## 4. 关键概念

- **所有权（Ownership）**：每个值有唯一所有者，所有者离开作用域值被释放——无需 GC，无需手动 free
- **借用（Borrowing）**：&T（不可变引用，可多个同时存在）和 &mut T（可变引用，独占）——借用规则在编译时检查
- **生命周期（Lifetimes）**：标注引用的有效范围——确保引用永远不悬垂
- **Cargo 工具链**：`cargo build/test/run/clippy/fmt` 一体化开发工具
- **unsafe**：允许绕过部分安全保证的关键字——用于 FFI、裸指针操作、自引用结构等必要场景

## 5. 典型实践

### 5.1 Cargo 项目结构

```
my_project/
├── Cargo.toml              # 项目元数据 + 依赖
├── Cargo.lock              # 锁定依赖版本
├── src/
│   ├── main.rs             # 二进制入口
│   └── lib.rs              # 库根
├── tests/                  # 集成测试
├── benches/                # 基准测试
└── examples/               # 示例代码
```

### 5.2 核心工具速查

| 命令 | 用途 |
|------|------|
| `cargo clippy` | 静态分析 + 惯用法检查 |
| `cargo fmt` | 自动格式化 |
| `cargo test` | 运行全部测试 |
| `cargo bench` | 运行性能基准测试 |
| `cargo doc --open` | 生成并打开文档 |

## 6. 经典问题

- 与借用检查器的搏斗——初学者最大的挫败来源
- 异步 Rust 的复杂性——Tokio vs async-std，Pin、Future
- 编译时间长——大型项目的增量编译仍在改善
- 泛型与 trait 的工程设计——何时用泛型、何时用 trait object

## 7. 工程实践

- 将简单的 C/C++ 函数用 Rust 重写并对比安全性
- 用 `cargo clippy` 学习 Rust 惯用法
- 用 `rayon` 库体验数据并行
- 用 `serde` 进行序列化/反序列化

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| C/C++ 工程化 | Rust 是 C/C++ 在系统编程领域的主要替代 |
| WebAssembly | Rust 是 WASM 的一流语言 |
| 操作系统 | Rust for Linux 项目将 Rust 引入内核开发 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 书籍 | The Rust Programming Language（官方"书"）| Rust 入门 |
| 书籍 | Rust for Rustaceans (Gjengset) | 进阶 |
| 工具 | rust-analyzer + VSCode | 开发环境 |

## 10. 待核查问题

- Rust 在 Linux 内核中的实际进展和接受度
- Rust 异步生态（Tokio）的长期稳定性
- Rust 在 AI/ML 领域的增长潜力
