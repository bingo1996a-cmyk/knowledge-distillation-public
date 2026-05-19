---
title: UI 框架比较
category: 人机交互与图形学
tags:
  - ui
  - frontend
  - framework
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# UI 框架比较

## 1. 一句话定义

本文档比较 Web、移动端和桌面端的主流 UI 框架，从响应式模型、组件化、生态和性能维度帮助技术选型。

## 2. 核心问题

- 不同 UI 框架的核心理念差异是什么？
- 虚拟 DOM、编译器优化、信号（Signals）等渲染策略各有何优劣？
- 如何为不同平台和项目规模选择合适的框架？

## 3. Web 框架对比

| 维度 | React | Vue | Svelte | Solid |
|------|-------|-----|--------|-------|
| 响应式模型 | 状态+渲染 | 响应式数据 | 编译器 | 细粒度信号 |
| 更新机制 | 虚拟 DOM | 虚拟 DOM | 编译时优化 | 无虚拟 DOM |
| 学习曲线 | 中等 | 较低 | 较低 | 中等 |
| TypeScript | 好 | 好 | 中 | 极好 |
| 生态 | 极丰富 | 丰富 | 发展中 | 较小 |
| 性能 | 中 | 中 | 高 | 极高 |

## 4. 关键概念

- **虚拟 DOM（Virtual DOM）**：先计算 UI 的虚拟表示的变化（diff），再批量更新真实 DOM——React 和 Vue 的基础
- **编译器优化**：Svelte 在编译时将声明式组件转化为高效的原生 DOM 操作代码——无需虚拟 DOM
- **信号（Signals）**：自动追踪依赖并精确更新 DOM——Solid、Preact Signals、Angular Signals 的共同趋势
- **JSX vs 模板**：JSX（JavaScript 中写 HTML，灵活）vs 模板（HTML 中嵌入表达式，更接近标准 HTML）
- **服务端组件（React Server Components）**：在服务端渲染组件，只发送结果不给客户端发 JS——Next.js 引领

## 5. 移动端框架

| 框架 | 渲染方式 | 语言 | 特点 |
|------|----------|------|------|
| React Native | 原生组件桥接 | JavaScript/TS | 生态最广 |
| Flutter | Skia 自绘引擎 | Dart | 性能一致、UI 自定义 |
| SwiftUI | 原生渲染 | Swift | iOS/macOS 原生 |
| Jetpack Compose | 原生渲染 | Kotlin | Android 原生 |

## 6. 桌面端

| 框架 | 技术基础 | 语言 |
|------|----------|------|
| Electron | Chromium + Node.js | JS/TS |
| Tauri | 系统 WebView + Rust 后端 | Rust + JS/TS |
| Flutter Desktop | Skia | Dart |
| WPF / WinUI | .NET 原生 | C# |

## 7. 经典问题

- 服务端渲染（SSR）vs 客户端渲染（CSR）vs 静态生成（SSG）的选择
- 组件库的设计与一致性维护
- 状态管理——局部状态 vs 全局状态 vs 服务端状态
- 跨平台的一致性 vs 原生体验

## 8. 工程实践

- 用 React/Vue 构建完整的 SPA 应用
- 用 Flutter 构建移动端和桌面端共享代码的应用
- 用 Tauri 替代 Electron 减少打包体积和内存占用
- 对比 Next.js、Nuxt、SvelteKit 的全栈开发体验

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 文档 | React / Vue / Svelte 官方文档 | 各框架入门 |
| 社区 | State of JS 年度调查报告 | 框架使用趋势 |

## 10. 待核查问题

- 信号（Signals）是否将成为所有主流框架的统一原语
- WebAssembly 对前端框架的未来影响
- AI 辅助 UI 生成（从设计稿/自然语言到组件）的成熟度
