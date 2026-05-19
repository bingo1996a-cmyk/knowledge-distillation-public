---
title: Git 与版本控制
category: 工程实践专题
tags:
  - git
  - version-control
  - collaboration
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# Git 与版本控制

## 1. 一句话定义

Git 是分布式版本控制系统，追踪代码的每一次变更，支持多人并行协作开发，是现代软件工程的基建工具。

## 2. 核心问题

- 如何安全地保存代码变更历史并支持回溯？
- 多人同时修改同一代码库时如何避免冲突？
- 如何管理发布节奏和热修复？

## 3. 知识框架

| 主题 | 核心内容 | 关键命令 |
|------|----------|----------|
| 基本操作 | 提交、分支、合并 | commit、branch、merge |
| 远程协作 | 推送、拉取、fetch | push、pull、fetch |
| 历史管理 | 查看、搜索、回溯 | log、diff、blame、bisect |
| 分支策略 | 工作流规范 | Git Flow、GitHub Flow、Trunk-Based |
| 高级操作 | 变基、cherry-pick、交互式暂存 | rebase、cherry-pick、stash |

## 4. 关键概念

- **快照而非差异**：Git 每次 commit 保存完整文件快照（而非文件差异）——这是 Git 速度快和灵活性高的根本原因
- **三区模型**：工作区（Working）→ 暂存区（Staging）→ 仓库（Repository）——理解 `add` 和 `commit` 的分工
- **分支即指针**：分支只是一个指向某个 commit 的可移动指针——因此创建分支快、切换快
- **合并 vs 变基**：merge 保留历史分叉，rebase 重写历史为直线——各有适用场景
- **HEAD、refs、detached HEAD**：HEAD 指向当前所在位置，detached HEAD 指 HEAD 直接指向 commit 而非分支

## 5. 典型实践

### 5.1 三种主流分支策略

| 策略 | 特点 | 适用 |
|------|------|------|
| Git Flow | main/dev/feature/release/hotfix，严格流程 | 有固定发布周期的项目 |
| GitHub Flow | feature → main → deploy，简单直接 | 持续部署项目 |
| Trunk-Based | 短存活分支或直接在主干提交 | 高协作频率的团队 |

### 5.2 常见操作速查

| 场景 | 命令 |
|------|------|
| 撤销未推送的 commit | `git reset --soft HEAD~1` |
| 丢弃工作区改动 | `git checkout -- <file>` 或 `git restore <file>` |
| 修改最后一次 commit 信息 | `git commit --amend` |
| 找回误删的分支 | `git reflog` + `git checkout -b <branch> <hash>` |

## 6. 经典问题

- 大文件的版本管理——Git LFS（Large File Storage）
- 合并冲突的解决策略
- `.gitignore` 的设计——什么该提交、什么不该
- 敏感性信息误提交后的清理（`git filter-branch` / BFG Repo-Cleaner）

## 7. 工程实践

- 为项目制定清晰的分支策略和 commit message 规范
- 使用 `.gitignore` 和 `.gitattributes` 规范化仓库
- 配置 Git hooks（pre-commit）做自动化检查
- 使用 `git bisect` 二分查找引入 bug 的 commit

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| DevOps/CI | CI 通常由 Git push/PR 事件触发 |
| 软件工程 | 版本控制是团队协作的基础 |
| 开源协作 | GitHub/GitLab 工作流是开源的标准模式 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 书籍 | Pro Git (Chacon & Straub) | Git 权威指南 |
| 文档 | Git 官方文档 | 命令参考 |
| 工具 | learngitbranching.js.org | 交互式学习 Git 分支 |

## 10. 待核查问题

- 新型版本控制系统（如 jj、sapling）对 Git 的替代潜力
- 大模型在自动解决合并冲突中的效果
