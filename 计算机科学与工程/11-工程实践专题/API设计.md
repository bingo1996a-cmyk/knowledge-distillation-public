---
title: API 设计
category: 工程实践专题
tags:
  - api
  - rest
  - grpc
  - graphql
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# API 设计

## 1. 一句话定义

API 设计定义软件组件之间的接口协议——好的 API 易于理解、难以误用、可扩展且向后兼容。

## 2. 核心问题

- 如何设计直观、一致的 API 风格？
- REST、gRPC、GraphQL 各适合什么场景？
- 如何在不破坏现有用户的前提下演化 API？

## 3. 知识框架

| 风格 | 核心思想 | 典型场景 |
|------|----------|----------|
| REST | 资源 + HTTP 方法 | 公开 Web API |
| gRPC | Protocol Buffers + HTTP/2 | 微服务间高性能通信 |
| GraphQL | 客户端指定查询字段 | 灵活前端数据获取 |
| 消息队列 | 异步、解耦 | 事件驱动架构 |

## 4. 关键概念

- **REST 约束**：资源导向（名词式 URL）、无状态、统一接口（GET/POST/PUT/DELETE）、HATEOAS
- **幂等性**：多次相同请求的效果与一次相同——GET（天然）、PUT（幂等）、POST（非幂等）
- **向后兼容性**：不改已有的字段语义，只新增可选字段、不删不改已有路径
- **版本管理**：URL 版本（`/v1/`）、Header 版本（`Accept: version=2`）或查询参数——各有优劣
- **限流（Rate Limiting）**：防止滥用——令牌桶、滑动窗口、固定窗口

## 5. 典型设计

### 5.1 REST vs gRPC vs GraphQL

| 维度 | REST | gRPC | GraphQL |
|------|------|------|---------|
| 数据格式 | JSON | Protobuf | JSON |
| 协议 | HTTP/1.1 | HTTP/2 | HTTP/1.1 |
| 类型安全 | 弱（靠文档）| 强（.proto 文件）| 中等（Schema）|
| 性能 | 一般 | 高（二进制+多路复用）| 中等 |
| 灵活性 | 中等 | 低（固定接口）| 高（客户端决定）|
| 浏览器支持 | 原生 | 需 grpc-web | 原生 |

### 5.2 RESTful URL 设计原则

```
GET    /users          # 列表
GET    /users/:id      # 详情
POST   /users          # 创建
PUT    /users/:id      # 全量更新
PATCH  /users/:id      # 部分更新
DELETE /users/:id      # 删除
GET    /users/:id/orders  # 子资源
```

## 6. 经典问题

- 过度获取（Over-fetching）和不足获取（Under-fetching）——GraphQL 的设计动机
- REST 中复杂操作（搜索、批量操作）的 URL 设计
- API 分页策略——偏移量分页 vs 游标分页
- 错误响应的标准化格式

## 7. 工程实践

- 使用 OpenAPI/Swagger 规范文档化 REST API
- 使用 gRPC + Protocol Buffers 定义服务接口
- 为 API 编写自动化测试（合约测试）
- 实现 API 网关的认证和限流

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| 微服务架构 | API 是微服务之间通信的契约 |
| 网络安全 | API 认证、授权、防滥用 |
| 数据库 | API 往往暴露对数据模型的操作 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 书籍 | RESTful Web APIs (Richardson & Amundsen) | REST API 设计 |
| 书籍 | Web API Design (Arnaud Lauret) | API 设计实践 |
| 文档 | Google AIP (API Improvement Proposals) | Google API 设计指南 |

## 10. 待核查问题

- gRPC vs REST 在微服务通信中的市场份额
- AsyncAPI 对事件驱动 API 的标准化进程
- AI 辅助 API 设计（从需求自动生成 API Schema）的成熟度
