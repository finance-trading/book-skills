---
name: mcp-toolchain
description: |
  当用户需要搭建大模型智能体（Agent）与量化交易工具/数据的连接时激活。
  具体场景：用户要用 MCP 协议连接大模型与量化数据源（Tushare/AKShare
  等）；用户要构建 AI 智能体自动执行量化任务（数据获取→分析→信号生成
  →执行）；用户要理解 A2A 协议实现多智能体协作；用户要搭建量化交易的
  Agent 工具链。不适用于：纯 prompt 设计、非 Agent 架构的量化系统、
  传统 API 集成。关键 trigger：MCP、Model Context Protocol、智能体、
  agent、A2A、Agent2Agent、工具链、tool chain、function calling。
source_book: 《AI量化交易：高效构建交易策略的新路径》罗勇 卢洪波 王光伟 罗天奇
source_chapter: 第2章 2.5节 (页97-123)
tags: [mcp, agent, a2a, toolchain, llm-integration, quant-trading]
related_skills: [prompt-engineering, data-pipeline, factor-mining]
---

# MCP/智能体工具链搭建方法

## R — 原文 (Reading)

> MCP 的设计理念主要基于以下几个方面：上下文感知能力——现代大模型能
> 够理解并利用丰富的上下文信息；工具调用能力——大模型可以通过标准化
> 接口调用外部工具和数据源；安全与隐私——严格的访问控制与数据保护
> 机制。
>
> — 罗勇 等, 第2章 2.5.2节

> 打个比方：MCP 为 AI Agent 配了一个"工具箱"，而 A2A 协议是给 AI
> Agent 找了"队友"。两者可以一起使用。
>
> — 罗勇 等, 第2章 2.5.3节

> A2A 协议的推出，标志着 AI 进入了一个新的阶段——协作智能时代。我们
> 可以期待更多 AI Agent 的加入：越来越多的公司将开发兼容 A2A 协议的
> AI Agent。我们可以期待更复杂的任务：AI 团队能够解决以前单个 AI
> Agent 无法完成的复杂任务。
>
> — 罗勇 等, 第2章 2.5.4节

---

## I — 方法论骨架 (Interpretation)

本书对 MCP（Model Context Protocol）和 A2A（Agent2Agent）协议做了系统性解读，提出了智能体量化的工具链搭建方法：

**MCP 核心概念**: MCP 是大模型与外部工具/数据源的标准化连接协议。它让大模型能够：(1) 理解上下文信息；(2) 通过标准化接口调用外部工具（如数据 API、交易系统）；(3) 在安全框架内访问数据。MCP 相当于给 AI Agent 配了一个"工具箱"。

**MCP Server 搭建**: 用 Python SDK（如 `fastmcp`）定义工具函数，通过装饰器注册可调用工具。例如定义"获取股票行情"、"计算技术指标"、"执行回测"等工具，大模型通过 MCP 协议调用这些工具。

**A2A 协议**: 让多个 AI Agent 之间直接交流协作。一个 Agent 负责数据获取，一个负责因子分析，一个负责信号生成——它们通过 A2A 协议自动协作完成复杂任务。A2A 相当于给 AI Agent 找了"队友"。

**量化应用架构**: 数据采集 Agent → 因子分析 Agent → 策略决策 Agent → 执行 Agent，形成完整的 AI 量化工作流。

---

## A1 — 书中的应用 (Past Application)

### 案例 1: MCP Server 搭建示例
- **问题**: 如何让大模型调用本地文件统计工具
- **方法论的使用**: 用 `fastmcp` Python SDK 创建 MCP Server，通过 `@mcp.tool()` 装饰器定义工具函数（如统计桌面 .txt 文件数量）
- **结论**: MCP 让大模型能标准化地调用外部工具
- **结果**: 形成了可复用的 MCP Server 代码模板

### 案例 2: 多智能体协作架构设计
- **问题**: 复杂的量化任务（数据→分析→决策→执行）单个 Agent 难以完成
- **方法论的使用**: 设计多 Agent 架构——数据采集 Agent 负责获取行情，因子分析 Agent 负责计算因子，策略 Agent 负责生成信号，执行 Agent 负责下单
- **结论**: A2A 协议让 Agent 之间可以高效协作
- **结果**: 形成了完整的 AI 量化工作流架构

### 案例 3: 与新兴技术融合的展望
- **问题**: MCP/A2A 如何与量子计算、5G、区块链等新技术结合
- **方法论的使用**: 探索 MCP 在边缘计算、实时交互、安全溯源等场景的应用
- **结论**: MCP 有望在企业级应用、开发者工具、个人生产力中发挥关键作用
- **结果**: 推动了 AI 生态系统向标准化、互操作性和安全性方向发展

---

## A2 — 触发场景 (Future Trigger) ★

### 用户会在什么情境下需要这个 skill?

1. 用户要用 MCP 协议连接大模型与量化数据源/交易工具
2. 用户要搭建 AI Agent 自动执行量化任务流水线
3. 用户要理解 A2A 协议实现多 Agent 协作
4. 用户要在现有量化系统中集成大模型能力
5. 用户要评估 MCP vs 传统 API 集成的优劣

### 语言信号

- "MCP" / "Model Context Protocol"
- "智能体" / "agent"
- "A2A" / "Agent2Agent"
- "工具链" / "tool chain"
- "function calling"
- "让大模型调用外部工具"
- "多 agent 协作"

### 与相邻 skill 的区分 (定稿)

- 与 `prompt-engineering` 的分工: 本 skill 是**系统架构层**（Agent 如何通过 MCP 协议连接工具和数据源），prompt-engineering 是**交互接口层**（如何写 prompt 让 Agent 正确调用工具）。本 skill 以 prompt-engineering 为前置——Agent 的工具调用语义由 prompt 定义
- 与 `data-pipeline` 的对比: 两者都是"让量化系统接入外部数据/工具"，但**架构范式不同**。data-pipeline 是**传统 ETL**（Python 脚本 + 定时任务 + 数据库），本 skill 是**Agent 架构**（MCP 协议 + 工具注册 + 大模型动态决策）。当任务可以写死脚本时用 data-pipeline；当需要大模型**实时判断**调什么工具、按什么顺序调用时用本 skill
- 与 `factor-mining` 的关系: 本 skill 提供 factor-mining 的**基础设施**（通过 MCP 把数据源、回测引擎、交易接口封装为 Agent 可调用的工具），factor-mining 在此基础设施上**跑方法论**

---

## E — 可执行步骤 (Execution)

当 skill 被激活后, agent 应按以下步骤执行:

1. **评估需求，选择架构**
   - 单 Agent + MCP 工具 → 简单任务（数据查询、因子计算）
   - 多 Agent + A2A → 复杂任务（完整量化工作流）
   - 完成标准: 已确定架构方案

2. **搭建 MCP Server**
   - 安装 `fastmcp` 或等效 Python SDK
   - 用 `@mcp.tool()` 装饰器定义量化工具函数
   - 注册工具：数据获取、因子计算、回测、信号生成等
   - 完成标准: MCP Server 可启动，工具可被调用

3. **配置 Agent 连接**
   - 将大模型（ChatGPT/DeepSeek/本地模型）连接到 MCP Server
   - 配置工具的输入输出格式
   - 测试 Agent 能否正确调用工具
   - 完成标准: Agent 能成功调用至少一个工具

4. **设计多 Agent 协作（如需要）**
   - 定义各 Agent 的职责边界
   - 配置 A2A 协议的通信方式
   - 设计任务分发和结果汇总机制
   - 完成标准: 多 Agent 协作流程可运行

5. **安全与监控**
   - 配置访问控制和数据保护
   - 设置 Agent 行为的边界约束
   - 监控 Agent 调用的工具执行情况
   - 完成标准: 安全机制上线

---

## B — 边界 (Boundary) ★

### 不要在以下情况使用此 skill

- 用户只需要简单的 API 调用（用 requests 一行搞定）—— 不需要 MCP 的复杂性
- 用户的任务不涉及大模型 —— MCP 是专门为 LLM 设计的协议
- 用户在做传统量化系统开发（不需要 AI Agent）—— 用常规软件工程方法

### 作者在书中警告的失败模式

- **过度工程化**: 简单任务用 MCP 反而增加复杂度
- **安全风险**: Agent 调用外部工具时可能的数据泄露和未授权操作
- **协议成熟度**: MCP 和 A2A 都是新兴协议，生态和工具链尚不完善
- **调试困难**: 多 Agent 协作的问题定位比单 Agent 复杂得多

### 作者的盲点 / 时代局限

- MCP 和 A2A 协议在 2025 年仍处于早期阶段，书中描述可能已过时
- 书中对 MCP 的讲解偏概念性，缺少生产级别的部署经验
- 未讨论 MCP 在高频交易等低延迟场景的适用性
- 多 Agent 协作的成本（token 消耗、延迟）未讨论

### 容易混淆的邻近方法论

- 传统微服务架构 —— MCP 是面向 LLM 的工具调用协议，不是通用微服务
- Function Calling（OpenAI）—— MCP 是更通用的标准化协议，不绑定特定模型厂商

---

## 相关 skills

- **depends-on**: `prompt-engineering`（Agent 的工具调用语义由 prompt 定义，prompt 是本 skill 的前置）
- **contrasts-with**: `data-pipeline` — Agent 架构工具链 vs 传统 ETL 数据工程；动态决策 vs 静态脚本
- **composes-with**: `factor-mining`（本 skill 提供 MCP 基础设施，factor-mining 在此之上跑因子挖掘方法论）

---

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 待测 (详见 test-prompts.json)
- **蒸馏时间**: 2026-08-16
