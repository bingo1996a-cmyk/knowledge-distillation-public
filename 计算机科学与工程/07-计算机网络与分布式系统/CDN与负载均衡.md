---
title: CDN 与负载均衡
category: 计算机网络与分布式系统
tags:
  - cdn
  - load-balancing
  - dns
status: draft
version: 0.1.0
created: 2026-05-11
updated: 2026-05-11
source_level: 教材
---

# CDN 与负载均衡

## 1. 一句话定义

CDN（内容分发网络）将静态和动态内容缓存到全球边缘节点以减少延迟，负载均衡器将请求分发到多个后端服务器以实现扩展性和高可用——二者是互联网"速度和可靠性"的基础设施。

## 2. 核心问题

- 如何将用户请求引导到最近的 CDN 节点或最优的后端服务器？
- 如何在后端服务器健康状态动态变化时保持正确分发？
- 如何防护 DDoS 攻击？

## 3. 知识框架

| 主题 | 核心内容 | 代表性技术 |
|------|----------|------------|
| CDN | 边缘缓存、DNS 调度、动态加速 | Cloudflare、Akamai、CloudFront |
| DNS 负载均衡 | 基于 DNS 的流量分发 | 加权轮询、GeoDNS、Anycast |
| 反向代理 | 终止 TLS、缓存、路由 | Nginx、Envoy、HAProxy |
| 四层 vs 七层 | 传输层 vs 应用层分发 | L4（TCP/UDP）、L7（HTTP/gRPC）|
| 全局负载均衡 | 跨数据中心/区域的流量管理 | Anycast、GSLB |

## 4. 关键概念

- **CDN 工作原理**：用户请求 example.com → DNS 返回最近的 CDN 边缘节点 IP → 边缘节点有缓存直接返回，没有则回源拉取
- **反向代理**：对客户端伪装成源站——接收请求，通过负载均衡算法选择后端，转发请求并返回响应
- **负载均衡算法**：轮询（Round Robin）→ 最少连接 → 一致性哈希（会话保持）→ 加权变体
- **健康检查**：主动（定期探测后端健康状态）vs 被动（根据实际请求的失败情况）
- **Anycast**：多个节点通告同一 IP——BGP 将流量路由到拓扑上最近的节点

## 5. 典型机制

### 5.1 四层（L4）vs 七层（L7）负载均衡

| 维度 | L4（TCP/UDP）| L7（HTTP/gRPC）|
|------|-------------|----------------|
| 转发依据 | IP + Port | HTTP Header + Path + Cookie |
| 性能 | 极高 | 高（需解析协议）|
| 功能 | 简单分发 | 内容路由、TLS 终结、缓存 |
| 代表 | HAProxy（TCP mode）、AWS NLB | Nginx、Envoy、AWS ALB |

### 5.2 CDN 缓存策略

```
缓存控制头：
  Cache-Control: max-age=3600     → 浏览器和 CDN 缓存 1 小时
  Cache-Control: s-maxage=3600    → 仅 CDN 缓存
  Cache-Control: no-cache         → 每次需验证
  Surrogate-Control（CDN 专用头）

缓存 Key：通常为 URL，可自定义（按设备/区域差异化）
缓存驱逐：TTL 过期、CDN Purge API（主动清理）
```

## 6. 经典问题

- 缓存一致性——源站更新后 CDN 边缘的旧内容何时过期
- 粘性会话——有状态应用需要同一用户的请求到同一后端
- 健康检查的延迟——后端异常到从负载均衡池移除的窗口期
- CDN 对动态内容的加速局限

## 7. 工程实践

- 配置 Nginx 作为反向代理和负载均衡器
- 使用 Cloudflare 或 AWS CloudFront 为网站添加 CDN
- 实现基于 Header/Cookie 的灰度发布路由
- 设计 CDN 缓存策略——哪些路径缓存多久、何时主动清除

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| DNS | DNS 是 CDN 和全局负载均衡的流量调度入口 |
| HTTP | 缓存头和协议特性是 CDN 的工作基础 |
| TLS | 反向代理通常是 TLS 的终结点 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 书籍 | Web Operations (Allspaw & Robbins) | Web 运维 |
| 书籍 | High Performance Browser Networking (Grigorik) | CDN 和 HTTP/2 章节 |
| 文档 | Nginx / Envoy 官方文档 | 反向代理 |
| 文档 | Cloudflare Learning Center | CDN 基础 |

## 10. 待核查问题

- Edge Computing（Cloudflare Workers、Deno Deploy）对传统 CDN 的扩展
- AI 在 CDN 缓存预测和智能调度中的应用
