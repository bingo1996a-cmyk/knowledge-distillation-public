---
title: DevOps
category: 软件工程
tags:
  - devops
  - ci-cd
  - infrastructure-as-code
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# DevOps

## 1. 一句话定义

DevOps 是打破开发（Dev）和运维（Ops）壁垒的文化哲学和工程实践，通过自动化流水线和基础设施即代码实现软件的高频、可靠交付。

## 2. 核心问题

- 如何从"扔过墙"式交付转变为持续、安全、自动化的交付？
- 如何让基础设施配置可版本化、可复现、可审计？
- 如何在加速交付的同时不降低可靠性？

## 3. 知识框架

| 主题 | 核心内容 | 关键工具 |
|------|----------|----------|
| CI（持续集成）| 自动构建 + 自动测试 | GitHub Actions、Jenkins |
| CD（持续交付/部署）| 自动部署 + 环境管理 | ArgoCD、Spinnaker |
| 基础设施即代码 | 声明式管理基础设施 | Terraform、Pulumi、Ansible |
| 监控与告警 | 指标、日志、追踪 | Prometheus + Grafana + AlertManager |
| 配置管理 | 环境配置与秘密管理 | ConfigMap/Secret、Vault |

## 4. 关键概念

- **CI/CD 流水线**：Push → Build → Test → Staging Deploy → 自动化测试 → Production Deploy
- **声明式 vs 命令式**：声明式（描述期望状态，如 K8s YAML、Terraform）vs 命令式（描述执行步骤，如脚本）
- **不可变基础设施**：部署后不修改运行中的服务器，任何改变通过重建实现
- **蓝绿部署/金丝雀部署**：蓝绿（两套完整环境切换）、金丝雀（逐比例引流验证）
- **GitOps**：以 Git 仓库为唯一真实来源，通过声明式配置自动同步集群状态

## 5. 典型实践

### 5.1 CI/CD 流水线

```
开发者 Push 代码
    ↓
CI: 构建 → 单元测试 → 集成测试 → 安全扫描 → 构建镜像
    ↓
CD: 部署到 Staging → 自动化验收测试
    ↓
CD: 金丝雀部署到 5% 流量 → 观察指标 → 全量部署
    ↓
监控：应用指标 + 基础设施指标 + 告警规则
```

### 5.2 DevOps 四大指标（DORA 指标）

| 指标 | 精英级 |
|------|--------|
| 部署频率 | 每日多次 |
| 变更前置时间 | 小于 1 小时 |
| 变更失败率 | 0-15% |
| 故障恢复时间 | 小于 1 小时 |

## 6. 经典问题

- 开发和运维的文化冲突——速度 vs 稳定性的矛盾
- CI 流水线过慢影响开发体验
- 秘密管理——敏感信息不应出现在代码中
- 配置漂移（Configuration Drift）——手动修改导致实际状态偏离声明

## 7. 工程实践

- 为项目配置 GitHub Actions CI 流水线
- 用 Terraform 管理云资源并纳入版本控制
- 实现 Docker 镜像的自动构建和推送
- 搭建 Prometheus + Grafana 监控面板

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| 软件工程 | CI/CD 是 DevOps 在工程流程中的具体体现 |
| 容器与 K8s | K8s 是 DevOps 部署的主流平台 |
| 云计算 | 云 API 使 IaC 成为可能 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 书籍 | The DevOps Handbook (Kim et al.) | DevOps 实践指南 |
| 书籍 | Accelerate (Forsgren et al.) | DevOps 的科学研究 |
| 书籍 | Site Reliability Engineering (Google) | Google SRE 工程实践 |

## 10. 待核查问题

- 平台工程（Platform Engineering）对传统 DevOps 的替代/增强趋势
- AI 辅助运维（AIOps）在故障预测和自动修复方面的实际效果
