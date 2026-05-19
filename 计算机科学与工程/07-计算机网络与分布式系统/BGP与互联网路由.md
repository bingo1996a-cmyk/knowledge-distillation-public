---
title: BGP 与互联网路由
category: 计算机网络与分布式系统
tags:
  - bgp
  - routing
  - internet
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# BGP 与互联网路由

## 1. 一句话定义

BGP（Border Gateway Protocol，边界网关协议）是互联网的核心路由协议，通过自治系统（AS）之间的路径向量交换，决定数据包如何跨越不同网络到达目的地。

## 2. 核心问题

- 互联网由成千上万个独立网络（AS）组成，他们之间如何交换路由信息？
- 如何选择跨越多个网络的最优路径？
- 如何防止路由环路和错误路由宣告？

## 3. 知识框架

| 主题 | 核心内容 | 关键概念 |
|------|----------|----------|
| AS（自治系统）| 互联网的独立管理域 | AS 号（ASN）|
| BGP 会话 | AS 之间交换路由信息 | eBGP（AS 间）、iBGP（AS 内）|
| 路径属性 | 路由选择的依据 | AS_PATH、LOCAL_PREF、MED |
| 路由策略 | 流量工程与商业关系 | Transit、Peering |
| 安全 | BGP 的安全缺陷 | RPKI、BGPsec |

## 4. 关键概念

- **自治系统（AS）**：由单一机构管理的 IP 网络集合——互联网由约 10 万个 AS 组成
- **路径向量协议**：BGP 传播的是到达目标前缀的完整 AS 路径（AS_PATH），通过检查路径中是否已有自己的 AS 号来防环
- **BGP 选路**：先检查 LOCAL_PREF → AS_PATH 长度 → MED → 多种 tie-breaker（eBGP 优先、最低 IGP 度量等）
- **Transit vs Peering**：Transit（付费使对方帮你转发到全网）、Peering（免费互转双方的网络）、IXP（互联网交换中心）

## 5. 典型机制

### 5.1 BGP 路由传播

```
AS1 拥有前缀 10.0.0.0/24
    ↓ 宣告给 AS2
AS2 学到: 10.0.0.0/24 via AS_PATH [AS1]
    ↓ 宣告给 AS3
AS3 学到: 10.0.0.0/24 via AS_PATH [AS2, AS1]
```

### 5.2 BGP 的主要问题

| 问题 | 描述 | 影响 |
|------|------|------|
| 路由劫持 | 恶意宣告不属于自己的前缀 | 流量被重定向 |
| 路由泄露 | 错误地将学到的路由宣告给不该宣告的方 | 流量黑洞或过载 |
| 收敛时间 | 路由变化后全网稳定需要数分钟 | 此期间丢包和延迟增加 |
| 缺乏加密和认证 | 传统 BGP 没有内置安全机制 | 易受攻击 |

## 6. 经典问题

- 巴基斯坦电信 YouTube 劫持事件（2008）——配置错误导致 YouTube 全球中断
- BGP 路由表持续增长——IPv4 约 90 万条，IPv6 在快速增长
- 冷土豆 vs 热土豆路由——流量工程决策

## 7. 工程实践

- 使用 BGP Looking Glass（如 routeviews.org）查看实时路由表
- 用 `traceroute` / `mtr` 观察实际路由路径
- 使用 `bgp.he.net` 查询 AS 信息和路由策略
- 理解 CDN 如何利用 BGP Anycast 将流量路由到最近的节点

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| IP 协议 | BGP 负责 IP 地址的可达性信息 |
| 网络安全 | BGP 劫持和防御是网络安全的重要话题 |
| DNS | DNS 和 Anycast 共同工作分发流量 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| RFC | RFC 4271 (BGP-4) | BGP 协议标准 |
| 书籍 | BGP (van Beijnum) | BGP 实践指南 |
| 工具 | BGP Looking Glass、RIPE Atlas | 路由观测 |

## 10. 待核查问题

- RPKI（资源公钥基础设施）在全球的部署率
- 传统 BGP 与 SDN 集中控制模型的长远关系
