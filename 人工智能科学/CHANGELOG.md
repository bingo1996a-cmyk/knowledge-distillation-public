---
title: CHANGELOG
layer: root
tags:
  - evaluation
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# CHANGELOG

## V39 — 2026-05-08
### Added
- **mkdocs 静态站点**（V39.1）：基于 mkdocs 1.6.1 + mkdocs-material 9.7.6 搭建。文档根目录设为 `docs/`，保留原有目录结构。完整 nav 配置覆盖全部 13 个知识库层。
- **自定义主题样式**：`docs/stylesheets/extra.css` 提供 indigo 主题色、表格/代码块/引用块/导航样式增强。
- **全文搜索**（V39.2）：mkdocs-material search 插件配置为支持中文（zh）和英文（en）索引，可全文检索 300+ 个内容文件。
- **持续集成管道**（V39.3）：`.github/workflows/deploy-mkdocs.yml`——推送到 main 分支时自动构建并部署 mkdocs 站点到 GitHub Pages。

### Changed
- **项目结构重构**：全部 `.md` 文件（含内容目录、根级文件）从根目录迁移至 `docs/` 子目录，遵循 mkdocs 标准项目结构。内部相对链接保持不变，无需更新。
- **`README.md`**：版本号更新至 V39，添加 mkdocs 静态站点说明。
- **`V39-structure-index.md`**：新增 V39 结构索引文件，记录所有变更。

### Removed
- **docs/ 遗留 HTML 文件**：移除了旧版 `index.html`、`08-application-node-graph.html`、`08-thought-history-timeline.html`、`frontier-dashboard-2026-04-11.html`（与 mkdocs 生成的页面冲突）。
### Added
- **元数据基础设施**：全库 355 个 `.md` 文件添加 YAML 前置元数据（覆盖率 100%）。
  - 四个必填字段：title（从一级标题提取）、layer（从目录映射）、tags（按层默认分配）、status（全部 stable）。
  - 三个可选字段：prerequisites、see-also、last-updated。
- `00-overview/metadata-specification.md`：元数据规范文档，定义七个核心字段、受控词表（layer 13 个值 / tags 20 个一级标签 / status 4 个状态）、4 类文件范本、维护规则、与后续版本的接口格式。
- `scripts/add-metadata.py`：批量添加脚本，支持逐层处理、干跑预览、强制覆盖。
- `scripts/metadata-check.py`：完整性检查脚本，扫描覆盖率、字段缺失、状态分布。
- `scripts/generate-index.py`：JSON 索引生成脚本。
- `metadata-index.json`：机器可读索引，355 条记录，可按 layer/status/tags 过滤，供 V39 搜索和 V40 图谱使用。

### Changed
- `TODO.md`：V37 路线的 V37.2 状态从"计划"改为"已完成"；V38 路线标记为进行中。
- `V38-structure-index.md`：新增 V38 结构索引，记录所有变更。

## V37.2 — 2026-05-08
### Added
- **05-problem-spaces 层扩展**：新增 6 个文件，层内容文件数从 8 扩展至 14，超越 V37.2 目标下限。
  - `perception-subtypes-and-modality-challenges.md`（5.57 KB）：视觉/听觉/触觉感知子空间分类与跨模态对齐、缺失模态鲁棒性等挑战。
  - `reasoning-subtypes-and-verification-paradigms.md`（7.25 KB）：演绎/归纳/溯因/类比/常识推理五种范式，含形式验证与科学假设生成等典型场景。
  - `generation-subtypes-and-distribution-properties.md`（6.91 KB）：按输出结构（离散序列/连续信号/结构化）和目标（条件/无条件、开放域/受限、单次/迭代）分类。
  - `problem-space-conflict-and-priority-framework.md`（7.08 KB）：三类复合模式（流水线/紧耦合/混合）、四步主空间判定流程、五种冲突类型与解决策略。
  - `evaluation-metrics-across-problem-spaces.md`（7.72 KB）：各问题空间指标表、五个通用评测维度、跨空间可比性分析。
  - `open-challenges-in-problem-space-analysis.md`（7.34 KB）：问题空间↔模型家族映射缺口、新兴空间、运行时漂移、任务难度度量、自我验证五个开放挑战。

### Changed
- `05-problem-spaces/README.md`：V36→V37，导航新增分组（主干概念/五大问题空间/子类型深化/元方法论）。

## V37.1 — 2026-05-08
### Added
- 完全态评估报告 `knowledge-base-completeness-assessment.md`，基于全库 344 个文件 1.2MB 内容的系统统计，识别结构性问题并给出 P0-P2 方向建议。
- 远景规划路线图 `00-overview/vision-roadmap.md`，制定 V37（深度补齐）→ V38（元数据化）→ V39（搜索+CI 工具化）→ V40（图谱+Agent 接口）四阶段发展路径。
- V37 结构索引 `V37-structure-index.md`。

### Changed
- **02-paradigms 层**：5 个 <1KB 存根全数扩写至 2.8-3.5KB。connectionism（连接主义，补充 PDP 框架、历史里程碑、与符号主义对比表）、symbolicism（符号主义，补充 PSSH 假设、关键系统、现代神经符号回归）、probabilistic-ai（概率主义 AI，补充从贝叶斯到概率编程的 250 年主线）、generative-ai（生成式 AI，补充五大家族对比表、关键里程碑、核心理论问题）、statistical-machine-learning-from-erm（补充 ERM→核方法→结构化预测→贝叶斯→深度模型连续谱）。
- **03-model-families 层**：4 个旧版重定向页格式统一为"重定向说明"模板；修复 2 组循环引用（OPE 双页互指解除、离策略修正双页互指解除），全部指向真实内容页。
- **索引文件**：README.md V36→V37、TODO.md 新增 V37 完成项与远景路线表、02-paradigms/README.md V36→V37、03-model-families/README.md V36→V37、00-overview/README.md 新增 vision-roadmap 链接。

## V35
### Added
- 自动驾驶页补入工程案例：Waymo/Cruise/Tesla 三条技术路线对比（传感器配置、系统架构、运营数据、安全策略）。
- 医疗 AI 页补入工程案例：FDA 批准 AI 医疗设备时间线（2018-2025，累计超 1,400 款）、代表性产品（Arterys/Viz.ai/IDx-DR/Aidoc/Paige Prostate）及关键里程碑年份。
- AI for SE 页补入工程案例：测试生成工具链（Copilot/Diffblue/Qodo/EvoSuite）、代码审查（CodeGuru/SonarQube/Meta ACH）、重构迁移（OpenRewrite/GPT-4o）、形式化验证（FVEL/CoqPilot）及行业趋势（Harness 2025 报告）。
- 机器人/AMR 页补入工程案例：Amazon Robotics 百万机器人发展史、Geek+（极智嘉）全球 AMR 市场份额第一仓储实践、Locus Robotics 50 亿拣选里程碑、全球仓储自动化市场展望。
- 新增 90-appendices 附录：[常见参考文献著录示例](./90-appendices/common-reference-examples.md) 和 [史学类材料的证据等级说明](./90-appendices/historical-evidence-hierarchy.md)。
- 新增 [V35 结构索引](./V35-structure-index.md)。

### Changed
- 06-applications 工程案例密度大幅提升：4 个应用页面平均新增 500-800 字行业案例内容。
- 06-applications 模板统一：4 个应用页面统一添加"这页解决什么问题"、"常见误区"、"联读"和"参考文献"章节。
- 全库模板统一（V35.5）：完成 01/02/03/04/07/08 层共 27 个核心页面的"联读 + 参考文献"补齐。统一了"阅读接口"/"建议联读"/"继续阅读"/"参考入口"/"建议阅读位置"/"联动阅读"等变体命名为"联读"。
- 90-appendices 新增"常见参考文献著录示例"和"史学类材料的证据等级说明"两个附录页面，补充模板与证据规范。

### Changed (V35.6)
- 主干页 GB/T 7714 参考文献补齐（V35.6）：系统补齐 04-systems-engineering 和 03-model-families 两层共 24 个主干页面的"## 联读"（统一变体标题命名）与"## 参考文献"（GB/T 7714 风格）章节。
  - 04-systems-engineering：补齐 9 个主干页面（README、总览、LLM 全栈、预训练/后训练、多智能体、推理服务、数据、评测驱动开发、ML 生命周期）。
  - 03-model-families：补齐 15 个主干页面（README、模型家族总览、生成式模型、Transformer、神经网络、LLM、世界模型、机器学习模型、经典学习算法、经典统计学习、深度网络家族、架构原理、RL 算法谱系、Transformer/GPT/MoE、知识图谱）。
  - 统一了"推荐阅读" / "建议联读" / "经典文献" / "经典教材与文献" / "推荐阅读路径" / "与本库其他页面的关系" / "与其他笔记的连接" 等变体命名为"## 联读"。

### Pending (V35.6-V36)
- 全库模板统一检查：已完成 01-08 层共 51 个核心页面的"联读 + 参考文献"补齐。剩余页面以补充性为主，非核心页面。
- V35.6 参考文献补齐：04/03 两层主干页面已补齐，剩余专业深化页按需推进。
- P1 阶段（V36）：HTML 时间轴导航、应用节点图谱、全库去重最终检查、附录完备性检查。

## V34
### Added
- 新增 [计算机视觉产业史：从图像工程到视觉基础模型](./08-thought-history-culture/history-of-computer-vision-industry.md)。
- 新增 [语音识别与机器翻译产业演进史：从孤立词识别到多模态语音 AI](./08-thought-history-culture/history-of-speech-and-mt-industry.md)。
- 新增 [机器人与具身系统史：从工业机械臂到操作基础模型](./08-thought-history-culture/history-of-robotics-and-embodied-systems.md)。
- 新增 [大模型应用生态的细分行业史：从 GPT-3 到 Agent 工作流](./08-thought-history-culture/history-of-llm-application-ecosystem.md)。
- 新增 [V34 结构目录](./V34-structure-index.md)。
- 新增完全态目录与远景规划文档。

### Changed
- 更新 08 层 README，新增"细分产业史"主线 D。
- 更新 TODO.md 降低已补齐项的优先级。

### Refactored
- 08 层覆盖范围从 13 页扩展至 17 页，产业史缺口全部补齐。
- 收束 03 层 6 组重叠页：Transformers 缩编为入门摘要；推理时计算三文件（概念总览/机制主文件/轨迹工程）明确分工；Tokenization 双文件（经济学视角/字节技术对比）明确边界；PEFT 训练侧（A12/A13）与服务侧（C9）明确定位并互相引用。
- 收束 04 层 serving/inference 文件组：综合概述页（C2）与 3 个专题深化页（调度策略/KV Cache/推测解码）添加交叉页面关系声明。
- 03 层 README 与 04 层 README 已在各页内标注页面关系。

## V33
### Added
- 新增 [人工智能应用史：从实验室原型到大规模部署](./08-thought-history-culture/history-of-ai-applications-from-labs-to-mass-deployment.md)。
- 新增 [V33 结构目录](./V33-structure-index.md)。

### Changed
- 系统重写 `08-thought-history-culture` 主干页面，突出“年份 + 提出来源 + 历史意义”的三点式写法。
- 重新组织人工智能历史总览、时间线、范式转移、神经网络/Transformer 谱系、强化学习谱系、专家系统与寒冬、统计转向、深度学习复兴工程条件等专题。
- 增强思想史附录，使关键人物、实验室、会议、里程碑和注释阅读单更适合作为博士阶段的历史入口。
- 继续推进“深入简出”：在保留技术细节的前提下，为历史主线页统一补入“基本思想”和“如何阅读这一段历史”的解释。

### Refactored
- 将 `08-thought-history-culture` 的阅读路径从“单线概览”改为“总览页 + 时间线 + 范式线 + 学科线 + 应用线 + 机构线”结构。
- 收束部分附录中的重复说明，把相近材料改成“主页 + 指向型附录”的组织方式。

## V32
### Added
- 新增“推理时扩展、自适应计算与审慎推理”专题。
- 新增“智能体协议：MCP、A2A 与工具契约”专题。
- 新增“智能体身份、认证与凭据委托”专题。
- 新增“数据谱系、内容溯源与训练语料治理”专题。
- 新增“过程监督、验证器与推理审计”专题。
- 新增“内容溯源、水印与指纹”专题。

### Changed
- 将 `05-problem-spaces` 全层补厚，形成可独立阅读的任务结构页。
- 增强 AI 加速器、集群网络、通信墙、自动驾驶、医疗与偏好优化等薄页。
- 继续落实“前置基本思想 + 中文主体 + 首现术语中英对照”写法。

### Refactored
- 对离策略修正、离策略评估、KV 缓存/推测解码等主题继续执行“主文件 + 并入说明”式去重。
- 更新根入口、分层 README 与 V32 结构目录。
