---
title: TCP/IP 协议族
category: 计算机网络与分布式系统
tags:
  - networking
  - tcp
  - ip
  - http
  - dns
  - tls
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# TCP/IP 协议族

## 1. 一句话定义

TCP/IP 协议族是互联网的核心协议栈，定义了数据如何从一台主机可靠（或不可靠地）传输到另一台主机，包括 IP 路由、TCP 可靠传输、UDP 轻量传输和应用层协议。

## 2. 核心问题

- 如何在不可靠的 IP 网络之上建立可靠的端到端连接？
- 如何避免发送方淹没接收方或中间网络？
- 应用层协议如何利用传输层的服务？

## 3. 知识框架

| 层次 | 主要协议 | 核心功能 |
|------|----------|----------|
| 应用层 | HTTP、DNS、TLS、SMTP | 面向用户的服务 |
| 传输层 | TCP、UDP、QUIC | 端到端通信、可靠性/拥塞控制 |
| 网络层 | IP、ICMP、BGP | 路由、分片、寻址 |
| 链路层 | Ethernet、Wi-Fi | 物理帧传输 |

## 4. 关键概念

### 4.1 IP（网际协议）

- **尽力而为（Best Effort）**：不保证送达、不保证顺序、不保证不重复
- **IP 地址**：32 位（IPv4）或 128 位（IPv6），标识网络接口
- **路由**：每台路由器根据目标 IP 前缀查表转发

### 4.2 TCP（传输控制协议）

- **面向连接**：三次握手建立连接，四次挥手断开
- **可靠传输**：序列号 + 确认 + 超时重传
- **流量控制**：滑动窗口，接收方告知可用缓冲区大小
- **拥塞控制**：慢启动、拥塞避免、快速重传、快速恢复

### 4.3 UDP（用户数据报协议）

- 无连接，不保证送达，不保证顺序
- 开销小（头部仅 8 字节 vs TCP 的 20 字节）
- 适合实时应用（音视频、游戏、DNS）

## 5. 典型机制

### 5.1 TCP 状态机

```
CLOSED → LISTEN（服务器监听）
LISTEN → SYN_RCVD → ESTABLISHED（三次握手完成）
ESTABLISHED → FIN_WAIT → TIME_WAIT → CLOSED（断开）
```

### 5.2 TLS 1.3 握手（简略）

```
客户端 → ClientHello（支持的密码套件 + 密钥共享）→ 服务端
客户端 ← ServerHello + 加密的证书 + 完成   ← 服务端
客户端 → 完成（应用数据开始加密传输）      → 服务端
全程 1-RTT（首次）/ 0-RTT（恢复会话）
```

## 6. 经典问题

- TCP 队头阻塞（Head-of-Line Blocking）
- TIME_WAIT 状态的意义与端口耗尽问题
- 粘包/拆包——TCP 的流式特性导致应用层需要消息边界
- DNS 缓存中毒与 DNSSEC
- QUIC 协议如何解决 TCP 队头阻塞

## 7. 工程实践

- 用 Wireshark 抓包分析 TCP 三次握手、数据流和四次挥手
- 用 `tcpdump` 分析 HTTP 请求和响应的网络时序
- 实现简易 HTTP 服务器理解协议格式
- 配置 Nginx 的 TCP/UDP 反向代理

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| 操作系统 | TCP/IP 栈在 OS 内核中实现 |
| 分布式系统 | RPC、共识协议依赖 TCP/UDP 传输 |
| 网络安全 | TLS、防火墙、入侵检测基于协议 |
| 微服务架构 | 服务间通信依赖 HTTP/gRPC |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 教材 | TCP/IP Illustrated, Volume 1 (Stevens) | TCP/IP 经典 |
| RFC | RFC 793 (TCP)、RFC 791 (IP)、RFC 9000 (QUIC) | 协议标准 |
| 书籍 | High Performance Browser Networking (Grigorik) | Web 网络性能 |

## 10. 待核查问题

- QUIC/HTTP3 对传统 TCP+TLS 的替代进度
- IPv6 在全球的实际部署率
- BBR 拥塞控制算法 vs 传统 CUBIC 的实际性能差异
