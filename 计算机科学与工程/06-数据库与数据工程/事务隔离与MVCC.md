---
title: 事务隔离与 MVCC
category: 数据库与数据工程
tags:
  - database
  - transaction
  - mvcc
  - isolation
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# 事务隔离与 MVCC

## 1. 一句话定义

事务隔离决定了一个事务能看到其他并发事务的哪些修改——MVCC（多版本并发控制）是实现高并发隔离的主流技术，通过保留数据的多个版本来避免读写阻塞。

## 2. 核心问题

- 并发事务同时读写同一数据时会发生什么异常？
- 如何在隔离性和并发性之间取舍？
- MVCC 如何在不加锁的情况下提供快照一致性？

## 3. 知识框架

| 主题 | 核心内容 |
|------|----------|
| 隔离级别 | 从宽松到严格的四级标准（SQL 标准）|
| 并发异常 | 脏读、不可重复读、幻读、丢失更新 |
| MVCC 机制 | 版本链、可见性规则、快照 |
| 实现方式 | PostgreSQL（多版本元组）、MySQL InnoDB（undo log）、Oracle |

## 4. 关键概念

- **四种隔离级别（SQL 标准）**：
  - Read Uncommitted：看到未提交的修改（几乎不用）
  - Read Committed：只看到已提交的修改（默认推荐）
  - Repeatable Read：同一事务内同一查询返回相同结果
  - Serializable：并发执行结果等价于某种串行顺序
- **MVCC 核心思想**：不直接覆盖旧版本，而是创建新版本——读操作看到事务开始时的快照——读写不互相阻塞
- **可见性规则**：每个数据行存储创建它的事务 ID 和删除它的事务 ID——当前事务只看到在它开始前已提交且未被删除的行
- **事务 ID（XID）比较**：txid_current() → 与每行的 xmin（创建）、xmax（删除）比较 → 决定可见性

## 5. 典型机制

### 5.1 PostgreSQL MVCC

```
UPDATE 操作的实际行为：
1. 不原地修改旧元组
2. 插入新元组（包含新数据）
3. 将旧元组的 xmax 标记为当前事务 ID
4. 旧元组由 VACUUM 异步回收

SELECT 可见性检查：
可见的条件（简化）：
  - xmin 是已提交事务且不是当前事务的回滚
  - xmax 是空或未提交事务或未来事务
```

### 5.2 隔离级别下的异常

| 异常 | Read Uncommitted | Read Committed | Repeatable Read | Serializable |
|------|:--:|:--:|:--:|:--:|
| 脏读 | 是 | 否 | 否 | 否 |
| 不可重复读 | 是 | 是 | 否 | 否 |
| 幻读 | 是 | 是 | 是（PG 中否）| 否 |
| 写偏斜 | 是 | 是 | 是 | 否 |

注：PostgreSQL 的 Repeatable Read 通过快照隔离检测阻止了幻读；Serializable 通过 SSI（Serializable Snapshot Isolation）检测写偏斜。

## 6. 经典问题

- 写偏斜（Write Skew）——两个事务基于读取的数据做出冲突的写入决策
- 长时间运行的事务——持有旧快照导致 MVCC 膨胀（PostgreSQL 的膨胀问题）
- VACUUM 的开销——清理旧版本的空间和 IO 成本
- 串行化隔离的性能开销

## 7. 工程实践

- 用 `BEGIN` / `SET TRANSACTION ISOLATION LEVEL` 在不同隔离级别下测试并发行为
- 观察 PostgreSQL 的 `pg_stat_user_tables.n_dead_tup` 监控 MVCC 膨胀
- 理解 SELECT FOR UPDATE / SKIP LOCKED 的显式锁定
- 设计幂等操作以降低对高隔离级别的需求

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| 数据库系统 | 事务管理是数据库核心功能 |
| 分布式系统 | 分布式事务将隔离扩展到多节点 |
| 并发编程 | 数据库隔离是并发控制的一种形式 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 教材 | Designing Data-Intensive Applications (Kleppmann) | 事务章节 |
| 论文 | A Critique of ANSI SQL Isolation Levels (Berenson et al., 1995) | 隔离级别经典分析 |
| 文档 | PostgreSQL Concurrency Control 文档 | MVCC 实现参考 |

## 10. 待核查问题

- 不同数据库对 Repeatable Read 的实现差异（PG 用快照，MySQL 用间隙锁）
- 乐观并发控制（OCC）在高冲突场景中的实用性
