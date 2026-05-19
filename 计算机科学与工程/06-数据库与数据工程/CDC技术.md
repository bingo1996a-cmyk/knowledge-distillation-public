---
title: CDC 技术
category: 数据库与数据工程
tags:
  - cdc
  - change-data-capture
  - data-pipeline
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# CDC 技术

## 1. 一句话定义

CDC（Change Data Capture，变更数据捕获）实时捕获数据库的变更事件（INSERT、UPDATE、DELETE）并将其以流的方式传递给下游系统，是数据同步、缓存失效和实时分析的枢纽技术。

## 2. 核心问题

- 如何在不影响业务数据库性能的前提下捕获变更？
- 如何保证变更事件的顺序和完整性？
- 下游系统如何消费变更事件？

## 3. 知识框架

| 实现方式 | 捕获源 | 特点 |
|----------|--------|------|
| 触发器（Trigger）| 数据库触发器写变更表 | 简单，性能差 |
| 查询日志（Query Log）| 数据库 binlog/WAL | 基础设施级，最常用 |
| 表差异（Table Diff）| 定时全量/增量比对 | 延迟大，适合存量同步 |
| 应用级埋点 | 应用中显式记录事件 | 灵活，但侵入性强 |

## 4. 关键概念

- **WAL（Write-Ahead Log）**：数据库在修改数据前先将变更写入日志——PostgreSQL 的 WAL、MySQL 的 binlog 都是 CDC 的天然数据源
- **Debezium**：最流行的开源 CDC 引擎——基于 Kafka Connect，支持 MySQL/PostgreSQL/MongoDB/Oracle
- **binlog 格式（MySQL）**：Statement（记录 SQL 语句）、Row（记录每行变更，CDC 所需格式）、Mixed
- **逻辑复制（PostgreSQL）**：通过 Publication/Subscription 模型流式复制 WAL 中的逻辑变更——从 PG 10 开始原生支持
- **事件顺序**：变更事件按事务提交顺序排列——一个事务的所有变更原子地传递

## 5. 典型架构

### 5.1 CDC 数据流

```
业务数据库（MySQL/PG）
    ↓ binlog/WAL 读取
CDC 引擎（Debezium/Kafka Connect）
    ↓ 转化 + 发布
Kafka Topic（分区按主键）
    ↓ 消费
下游系统（数仓/缓存/搜索索引/审计日志）
```

### 5.2 典型下游应用

| 场景 | 下游系统 |
|------|----------|
| 实时数仓 | ClickHouse、Snowflake |
| 缓存失效 | Redis——监听数据变更自动刷新 |
| 搜索索引 | Elasticsearch——实时更新索引 |
| 审计日志 | S3、HDFS |
| 微服务通信 | 其他服务监听领域事件 |

## 6. 经典问题

- 初始快照——已有数据的全量同步如何与新变更无缝衔接
- Schema 变更——DDL 变更（加列、改类型）对 CDC 的影响
- 大事务——binlog 中一个大事务可能阻塞后续事件的投递
- Exactly-Once 语义——保证不丢不重的端到端投递

## 7. 工程实践

- 用 Debezium + Kafka 从 MySQL 捕获变更到 ClickHouse
- 配置 PostgreSQL 逻辑复制 Publication/Subscription
- 处理 CDC 中的 Schema 兼容性（Avro Schema Registry）
- 监控 CDC 的延迟（源端提交到下游消费的时间差）

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| 数据库 | binlog/WAL 是 CDC 的数据源 |
| 消息队列 | Kafka 是 CDC 事件的传输层 |
| 数据仓库 | CDC 是实时数仓的数据供给 |
| 微服务 | CDC 作为事件驱动的数据源 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 框架 | Debezium 官方文档 | CDC 实践 |
| 文档 | MySQL binlog / PostgreSQL WAL 文档 | 变更日志 |
| 架构 | Netflix DBLog: A Generic Change-Data-Capture Framework | 工业级 CDC |

## 10. 待核查问题

- 无服务器 CDC（如 Fivetran/Airbyte）vs 自建 CDC 的成本权衡
- 基于 Streaming SQL 的 CDC 处理（如 RisingWave、Materialize）
