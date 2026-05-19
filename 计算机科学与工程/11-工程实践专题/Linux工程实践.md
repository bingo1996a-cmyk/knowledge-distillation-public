---
title: Linux 工程实践
category: 工程实践专题
tags:
  - linux
  - shell
  - system-administration
status: draft
version: 0.1.0
created: 2026-05-10
updated: 2026-05-10
source_level: 教材
---

# Linux 工程实践

## 1. 一句话定义

Linux 工程实践覆盖开发者在 Linux 环境下高效工作的必要技能——命令行、Shell 脚本、进程管理、系统监控和性能调优。

## 2. 核心问题

- 如何高效地在命令行环境中操作文件、处理文本和管理进程？
- 如何诊断系统性能问题（CPU、内存、IO、网络）？
- 如何自动化重复性任务？

## 3. 知识框架

| 主题 | 核心内容 | 关键命令/工具 |
|------|----------|---------------|
| 命令行基础 | 文件操作、管道、重定向 | ls、grep、awk、sed |
| Shell 脚本 | 变量、条件、循环、函数 | bash、zsh |
| 进程管理 | 进程查看、信号、后台任务 | ps、kill、nohup、systemd |
| 系统监控 | CPU、内存、IO、网络 | top/htop、vmstat、iostat |
| 性能分析 | 瓶颈定位、profiling | perf、strace、ltrace |
| 文本处理 | 搜索、过滤、转换 | grep、awk、sed、jq |

## 4. 关键概念

- **管道（Pipeline）**：`cmd1 | cmd2`——将前一个命令的 stdout 连接到后一个命令的 stdin，是 Unix 哲学的核心
- **标准流**：stdin(0)、stdout(1)、stderr(2)——每个进程的三个默认文件描述符
- **进程 vs 守护进程**：守护进程（daemon）是脱离终端在后台长期运行的进程——systemd 管理
- **信号**：SIGTERM（优雅终止）、SIGKILL（强制杀死）、SIGHUP（重新加载配置）——进程间异步通知机制
- **cgroups + namespaces**：容器技术的 Linux 内核基础——资源限制 + 视图隔离

## 5. 典型实践

### 5.1 常用文本处理管道

```
# 统计日志中最频繁的 IP
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -20

# 查找所有 .log 文件中包含 ERROR 的行及其上下文
grep -rn -A 2 -B 2 "ERROR" /var/log/

# 用 jq 处理 JSON 日志
cat data.json | jq '.[] | {name: .name, count: .items | length}'
```

### 5.2 系统性能诊断快速检查

| 症状 | 检查命令 | 关注指标 |
|------|----------|----------|
| 系统慢 | `top` / `htop` | load average、CPU 使用率 |
| 内存不足 | `free -h`、`vmstat 1` | swap 使用、OOM |
| 磁盘瓶颈 | `iostat -x 1` | await、util% |
| 网络问题 | `ss -tlnp`、`netstat -i` | 连接状态、丢包 |
| 应用卡顿 | `strace -p <pid>` | 系统调用频率和耗时 |

## 6. 经典问题

- 管道中的错误处理——默认只有最后一个命令的退出码
- Shell 脚本中的引号规则——单引号（字面量）/ 双引号（变量展开）/ 反引号（`$()`替代）
- 僵尸进程——子进程已退出但父进程未 wait
- too many open files——文件描述符上限

## 7. 工程实践

- 编写 Shell 脚本自动化日常操作（备份、日志清理、部署）
- 使用 `systemd` 编写服务单元文件管理应用进程
- 用 `cron` 或 `systemd timer` 调度周期任务
- 配置 `.bashrc` / `.zshrc` 提升命令行效率（别名、函数、提示符）

## 8. 与其他主题的关系

| 相关主题 | 关系 |
|----------|------|
| 操作系统 | Linux 命令直接与 OS 子系统交互 |
| DevOps/CI/CD | Shell 脚本是 CI 流水线的基础 |
| 容器 | Docker/K8s 部署在 Linux 节点上 |

## 9. 推荐资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 书籍 | The Linux Command Line (Shotts) | 命令行入门 |
| 书籍 | UNIX and Linux System Administration Handbook (Nemeth et al.) | 系统管理圣经 |
| 手册 | `man` pages + Arch Wiki | Linux 文档 |

## 10. 待核查问题

- Nushell 等现代 Shell 对 bash 的替代趋势
- eBPF 对传统 perf / ftrace 等性能分析工具的替代
