# 代码框架图生成器

[English](README.md)

一个用于分析代码项目结构并生成层次化 Mermaid 框架图的技能，可清晰展示模块关系、依赖关系和数据流。

## 背景

随着 AI Agent 的快速发展，软件开发效率呈指数级提升，新项目如雨后春笋般涌现。对于开发者而言，快速理解一个陌生项目变得越来越具有挑战性。传统的项目理解方式——阅读文档、浏览源码、追踪导入关系——往往耗时且不够全面。

**代码框架图生成器** 正是为解决这一痛点而生。它能够自动从源代码生成可视化的架构图，将复杂的代码结构转化为清晰直观的层次化图表，一目了然地展示：

- 入口点与执行流程
- 模块组织与依赖关系
- 组件关系（导入、继承、组合、调用）
- 系统边界与层次结构

只需一眼，开发者即可掌握项目的整体架构，大幅降低新项目的学习成本。

## 特性

- **多语言支持**：分析 Python、JavaScript/TypeScript、Rust、Go、Java 等多种语言
- **层次化可视化**：生成从高层概览到细节的多层架构视图
- **关系检测**：识别导入、继承、组合和调用关系
- **语义增强**：为关系添加业务上下文，使图表更清晰易懂
- **Mermaid 输出**：生成标准 Mermaid 语法，兼容 GitHub、GitLab 及各类文档工具

## 工作流程概览

```
1. 扫描项目 → 2. 识别组件 → 3. 分析关系 → 4. 构建图结构 → 5. 生成 Mermaid
```

---

## 案例研究

以下案例展示了代码框架图生成器在不同编程语言和项目架构下的可靠性和准确性。

### 案例 1：[nanobot](https://github.com/dwburks/nanobot) (Python)

**项目**：轻量级个人 AI 助手，支持多渠道接入。

**分析结果**：
- **语言**：Python
- **入口点**：`__main__.py`, `cli/commands.py`
- **核心模块**：`agent/loop.py`, `channels/manager.py`, `providers/registry.py`
- **节点总数**：35
- **关系总数**：31

**架构亮点**：
- 模块化渠道系统，支持 Telegram、WhatsApp、Discord、Slack 等
- 可插拔的 LLM 提供者架构（LiteLLM、OpenAI Codex）
- 事件驱动的消息总线，支持异步通信
- 可扩展的技能系统，支持自定义能力

**框架图**：

![nanobot Architecture](diagrams/nanobot.png)

---

### 案例 2：[zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) (Rust)

**项目**：100% Rust 编写的零开销、零妥协 AI 助手。

**分析结果**：
- **语言**：Rust
- **入口点**：`main.rs`, `lib.rs`
- **核心模块**：`agent/loop_.rs`, `channels/mod.rs`, `tools/browser.rs`
- **节点总数**：45
- **关系总数**：40

**架构亮点**：
- 全面的渠道支持：Telegram、WhatsApp、Discord、Slack、Matrix、iMessage、IRC、Signal 等
- 丰富的工具生态：浏览器自动化、Shell 执行、文件操作、Git、HTTP 请求
- 硬件和外设支持，可用于 IoT 集成
- 安全性和可观测性模块，满足生产环境需求

**框架图**：

![zeroclaw Architecture](diagrams/zeroclaw.png)

---

### 案例 3：[nanoclaw](https://github.com/qwibitai/nanoclaw) (TypeScript)

**项目**：使用 Apple Container 进行隔离执行的 WhatsApp AI 助手。

**分析结果**：
- **语言**：TypeScript
- **入口点**：`index.ts`
- **核心模块**：`container-runner.ts`, `db.ts`
- **节点总数**：15
- **关系总数**：28

**架构亮点**：
- 基于容器的 Agent 隔离，确保安全执行
- SQLite 数据库，用于消息持久化和状态管理
- 基于群组的消息队列，支持并发处理
- IPC 监听器，处理外部命令
- 任务调度器，支持自动化操作

**框架图**：

![nanoclaw Architecture](diagrams/nanoclaw.png)

---

## 可靠性总结

| 项目 | 语言 | 节点数 | 边数 | 准确性 |
|---------|----------|-------|-------|----------|
| nanobot | Python | 35 | 31 | ✅ 已验证 |
| zeroclaw | Rust | 45 | 40 | ✅ 已验证 |
| nanoclaw | TypeScript | 15 | 28 | ✅ 已验证 |

**关键发现**：
1. **入口点检测**：成功识别所有三个项目的主要入口点
2. **模块组织**：正确映射层次化模块结构
3. **关系类型**：准确检测导入、继承和调用关系
4. **跨语言支持**：无缝支持 Python、Rust 和 TypeScript

---

## 使用方法

### 作为技能使用

本技能专为 AI 助手设计，用于分析代码项目。工作流程包括：

1. **阶段 1 - 项目扫描**：识别入口点，映射目录结构
2. **阶段 2 - 组件识别**：按类型分类节点（文件、模块、目录、外部）
3. **阶段 3 - 关系分析**：检测导入、继承、组合和调用关系
4. **阶段 4 - 图构建**：构建层次化图结构
5. **阶段 5 - Mermaid 生成**：将图结构转换为 Mermaid 图表语法

### 快速上手示例

只需使用自然语言提示词即可调用此技能：

**示例 1 - 基本用法：**
```
为这个项目生成框架图
```

**示例 2 - 指定关注点：**
```
分析这个代码库的架构，生成一个专注于核心模块的 Mermaid 图
```

**示例 3 - 指定语言：**
```
为这个 Python 项目创建依赖图，展示模块间的关系
```

**示例 4 - 指定输出格式：**
```
生成框架图，并保存为 Mermaid 和 PNG 两种格式
```

### 文件结构

```
code-framework-graph/
├── SKILL.md              # 技能说明和工作流程
├── reference.md          # 详细参考指南
├── scripts/
│   └── graph_to_mermaid.py  # JSON 转 Mermaid 转换器
├── diagrams/
│   ├── nanobot.json      # nanobot 图结构
│   ├── nanobot.mmd       # nanobot Mermaid 图表
│   ├── nanobot.png       # nanobot 渲染图表
│   ├── zeroclaw.json
│   ├── zeroclaw.mmd
│   ├── zeroclaw.png
│   ├── nanoclaw.json
│   ├── nanoclaw.mmd
│   └── nanoclaw.png
└── README.md             # 本文件
```

---

## 许可证

MIT License
