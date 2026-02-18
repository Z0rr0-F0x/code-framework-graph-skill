# Code Framework Graph Generator

[中文文档](README_CN.md)

A skill for analyzing code project structure and generating hierarchical Mermaid framework diagrams showing module relationships, dependencies, and data flow.

## Background

With the rapid evolution of AI agents, software development velocity has skyrocketed. Projects are emerging at an unprecedented pace, making it increasingly challenging for developers to quickly grasp new codebases. Traditional methods of understanding a project—reading documentation, browsing source files, or tracing imports—are time-consuming and often incomplete.

**Code Framework Graph Generator** addresses this challenge by automatically generating visual architecture diagrams from source code. It transforms complex code structures into clear, hierarchical diagrams that reveal:

- Entry points and execution flow
- Module organization and dependencies
- Component relationships (imports, inheritance, composition, calls)
- System boundaries and layers

With a single glance, developers can understand the architecture of any project, dramatically reducing the learning curve for new codebases.

## Features

- **Multi-language Support**: Analyzes Python, JavaScript/TypeScript, Rust, Go, Java, and more
- **Hierarchical Visualization**: Generates layered architecture views from high-level to detailed
- **Relationship Detection**: Identifies imports, inheritance, composition, and call relationships
- **Semantic Enrichment**: Adds business context to relationships for clearer diagrams
- **Mermaid Output**: Produces standard Mermaid syntax compatible with GitHub, GitLab, and documentation tools

## Workflow Overview

```
1. Scan Project → 2. Identify Components → 3. Analyze Relationships → 4. Build Graph → 5. Generate Mermaid
```

---

## Case Studies

The following case studies demonstrate the reliability and accuracy of the Code Framework Graph Generator across different programming languages and project architectures.

### Case 1: [nanobot](https://github.com/dwburks/nanobot) (Python)

**Project**: A lightweight personal AI assistant with multi-channel support.

**Analysis Result**:
- **Language**: Python
- **Entry Points**: `__main__.py`, `cli/commands.py`
- **Core Modules**: `agent/loop.py`, `channels/manager.py`, `providers/registry.py`
- **Total Nodes**: 35
- **Total Relationships**: 31

**Architecture Highlights**:
- Modular channel system supporting Telegram, WhatsApp, Discord, Slack, and more
- Pluggable LLM provider architecture (LiteLLM, OpenAI Codex)
- Event-driven message bus for asynchronous communication
- Extensible skill system for custom capabilities

**Framework Diagram**:

![nanobot Architecture](diagrams/nanobot.png)

---

### Case 2: [zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) (Rust)

**Project**: Zero overhead, zero compromise AI assistant written in 100% Rust.

**Analysis Result**:
- **Language**: Rust
- **Entry Points**: `main.rs`, `lib.rs`
- **Core Modules**: `agent/loop_.rs`, `channels/mod.rs`, `tools/browser.rs`
- **Total Nodes**: 45
- **Total Relationships**: 40

**Architecture Highlights**:
- Comprehensive channel support: Telegram, WhatsApp, Discord, Slack, Matrix, iMessage, IRC, Signal, and more
- Extensive tool ecosystem: browser automation, shell execution, file operations, git, HTTP requests
- Hardware and peripheral support for IoT integration
- Security and observability modules for production readiness

**Framework Diagram**:

![zeroclaw Architecture](diagrams/zeroclaw.png)

---

### Case 3: [nanoclaw](https://github.com/qwibitai/nanoclaw) (TypeScript)

**Project**: A WhatsApp AI assistant using Apple Container for isolated agent execution.

**Analysis Result**:
- **Language**: TypeScript
- **Entry Point**: `index.ts`
- **Core Modules**: `container-runner.ts`, `db.ts`
- **Total Nodes**: 15
- **Total Relationships**: 28

**Architecture Highlights**:
- Container-based agent isolation for secure execution
- SQLite database for message persistence and state management
- Group-based message queuing for concurrent handling
- IPC watcher for external command processing
- Task scheduling for automated actions

**Framework Diagram**:

![nanoclaw Architecture](diagrams/nanoclaw.png)

---

## Reliability Summary

| Project | Language | Nodes | Edges | Accuracy |
|---------|----------|-------|-------|----------|
| nanobot | Python | 35 | 31 | ✅ Verified |
| zeroclaw | Rust | 45 | 40 | ✅ Verified |
| nanoclaw | TypeScript | 15 | 28 | ✅ Verified |

**Key Findings**:
1. **Entry Point Detection**: Successfully identified main entry points in all three projects
2. **Module Organization**: Correctly mapped hierarchical module structures
3. **Relationship Types**: Accurately detected imports, inheritance, and call relationships
4. **Cross-language Support**: Worked seamlessly across Python, Rust, and TypeScript

---

## Usage

### As a Skill

This skill is designed to be used by AI assistants to analyze code projects. The workflow includes:

1. **Phase 1 - Project Scanning**: Identify entry points and map directory structure
2. **Phase 2 - Component Identification**: Classify nodes by type (file, module, directory, external)
3. **Phase 3 - Relationship Analysis**: Detect imports, inheritance, composition, and calls
4. **Phase 4 - Graph Building**: Construct hierarchical graph structure
5. **Phase 5 - Mermaid Generation**: Convert graph to Mermaid diagram syntax

### Quick Start Examples

Simply invoke the skill with a natural language prompt:

**Example 1 - Basic Usage:**
```
Generate a framework diagram for this project
```

**Example 2 - With Specific Focus:**
```
Analyze the architecture of this codebase and generate a Mermaid diagram focusing on the core modules
```

**Example 3 - For a Specific Language:**
```
Create a dependency graph for this Python project showing module relationships
```

**Example 4 - With Output Format:**
```
Generate a framework diagram and save it as both Mermaid and PNG files
```

### Files

```
code-framework-graph/
├── SKILL.md              # Skill instructions and workflow
├── reference.md          # Detailed reference guide
├── scripts/
│   └── graph_to_mermaid.py  # JSON to Mermaid converter
├── diagrams/
│   ├── nanobot.json      # nanobot graph structure
│   ├── nanobot.mmd       # nanobot Mermaid diagram
│   ├── nanobot.png       # nanobot rendered diagram
│   ├── zeroclaw.json
│   ├── zeroclaw.mmd
│   ├── zeroclaw.png
│   ├── nanoclaw.json
│   ├── nanoclaw.mmd
│   └── nanoclaw.png
└── README.md             # This file
```

---

## License

MIT License
