---
title: 容器与 Kubernetes
category: 工程实践专题
tags:
  - containers
  - docker
  - kubernetes
  - orchestration
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# 容器与 Kubernetes

## 1. 一句话定义

容器（Docker）将应用及其依赖打包为可移植、可复现的轻量镜像，Kubernetes（K8s）自动化容器的部署、扩缩容和管理，共同构成现代云原生基础设施的核心。

## 2. 核心问题

- 如何消除"在我机器上能跑"的部署问题？
- 如何管理成百上千个容器的部署和编排？
- 如何在故障自动恢复的同时保持服务可用？

## 3. 知识框架

| 层次 | 核心内容 | 关键概念 |
|------|----------|----------|
| 容器 | 镜像构建、层、运行时 | Dockerfile、OCI |
| 基础资源 | Pod、Service、Volume | 调度单元、网络、存储 |
| 编排 | 副本管理、滚动更新、回滚 | Deployment、StatefulSet |
| 网络 | Pod 间通信、服务发现、Ingress | ClusterIP、Ingress、CNI |
| 配置管理 | 配置注入、秘密管理 | ConfigMap、Secret |
| 可观测性 | 日志、指标、健康检查 | Liveness/Readiness Probe |

## 4. 关键概念

- **镜像（Image）**：分层构建的只读模板——每层对应 Dockerfile 一条指令，利用缓存加速构建
- **容器**：镜像的运行实例，通过 Linux namespace（隔离）和 cgroup（资源限制）实现
- **Pod**：K8s 最小调度单元——包含一组共享网络和存储的容器
- **Deployment**：声明式管理 Pod 副本数、滚动更新策略和回滚——最常用的工作负载
- **Service**：为一组 Pod 提供稳定的网络入口（ClusterIP 不随 Pod IP 变化）
- **声明式 API**：用户声明期望状态，控制器协调实际状态到期望状态——K8s 的核心设计哲学

## 5. 典型实践

### 5.1 Dockerfile 最佳实践

```
1. 多阶段构建（Multi-stage build）分离构建和运行环境
2. 最小化层数：合并 RUN 指令
3. 正确排序：变化频率低的指令放前面利用缓存
4. 不使用 latest 标签，使用具体版本号
5. 以非 root 用户运行
```

### 5.2 K8s 核心资源关系

```
Deployment ──管理──> ReplicaSet ──管理──> Pod
                                                ↓
Service ──提供稳定入口──> Pod（通过 Label Selector 关联）
Ingress ──外部路由──> Service
ConfigMap/Secret ──注入配置──> Pod
```

## 6. 经典问题

- 容器退出后数据丢失——Volume/PVC 持久化
- Pod 重启导致的短暂不可用——健康检查 + 就绪探针
- 资源竞争（Noisy Neighbor）——resource request/limit 设置
- 镜像仓库的安全和镜像签名
- 调试容器的困难（没有传统工具）

## 7. 工程实践

- 将应用容器化（编写 Dockerfile + docker-compose）
- 搭建本地 K8s（minikube/kind）并部署 Deployment + Service
- 实现滚动更新和回滚
- 配置 Liveness/Readiness Probe 和资源限制

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| Linux 工程实践 | namespace/cgroup 是容器的底层基础 |
| DevOps/CI | 容器镜像构建是 CI 管道的常见产出 |
| 云计算 | K8s 是云原生应用的通用平台 |
| 微服务 | K8s 是微服务部署的事实标准 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 文档 | Docker / Kubernetes 官方文档 | 权威参考 |
| 书籍 | Kubernetes in Action (Luksa) | K8s 实践 |
| 认证 | CKAD（K8s 应用开发者认证）| 结构化学习 |

## 10. 待核查问题

- 无服务器容器（如 AWS Fargate、GCP Cloud Run）对传统 K8s 的挑战
- WebAssembly 容器（WASM/WASI）的前景
- K8s 的复杂度问题——是否存在更简单的替代方案（如 Nomad）
