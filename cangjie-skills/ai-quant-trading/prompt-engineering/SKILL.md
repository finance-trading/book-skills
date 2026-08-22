---
name: prompt-engineering
description: |
  当用户需要设计量化交易相关的 prompt/提示词时激活。具体场景：用户要
  用大模型做因子生成、策略设计、研报解析、数据分析等量化任务但不知
  道如何写 prompt；用户想用结构化框架（CRISPE/BROKE/ICIO）提升与大
  模型的交互质量；用户需要为量化工作流配置系统提示词。不适用于：纯
  闲聊、通用写作、非量化领域的 prompt 设计。关键 trigger：prompt、
  提示词、CRISPE、BROKE、ICIO、system prompt、few-shot、chain-of-thought。
source_book: 《AI量化交易：高效构建交易策略的新路径》罗勇 卢洪波 王光伟 罗天奇
source_chapter: 第2章 2.2节 (页47-75)
tags: [prompt-engineering, llm, framework, quant-trading]
related_skills: [factor-mining, data-pipeline, strategy-decision]
---

# 量化交易提示词工程框架

## R — 原文 (Reading)

> 掌握提示词工程不仅是高效使用大模型的核心技能，更是量化交易员
> 与大模型交互的关键能力。无论是通过 CRISPE、BROKE、ICIO 框架设
> 计提示词，还是利用思维链技术引导大模型推理，都能帮助你创造出更
> 精准、更高质量的交互体验。
>
> — 罗勇 等, 第2章 2.2节

> 量化交易的核心目标是预测下一根 K 线的走势，而大模型的任务是预
> 测下一个字符或词。无论是数据分析还是模型预测，背后都离不开海量
> 的数据、精妙的算法和强大的算力。
>
> — 罗勇, 序言

---

## I — 方法论骨架 (Interpretation)

本书提出了三大提示词框架，各有适用场景：

**CRISPE**（面向策略设计）：按 能力角色(Capability)→见解(Recommendation)→声明(Statement)→个性(Personality)→实验(Experiment) 五步构建 prompt，让大模型扮演特定量化角色输出策略方案。

**BROKE**（面向策略生成与迭代）：按 背景(Background)→角色(Role)→目标(Objective)→关键结果(Key Results)→改进(Evolve) 构建，特别适合需要多轮迭代优化的场景。

**ICIO**（面向数据处理）：按 说明(Instruction)→输入数据(Input)→上下文(Context)→输出指示(Output Indicator) 构建，适合数据清洗、特征提取、因子解析等结构化任务。

此外，书中还强调了**思维链技术**（Few-Shot CoT 和 Zero-Shot CoT）作为通用增强手段，以及**系统提示词 vs 用户提示词**的分工：系统提示词设定能力边界和工作规范，用户提示词提供具体任务输入。

---

## A1 — 书中的应用 (Past Application)

### 案例 1: 基于 CRISPE 框架设计量化交易策略
- **问题**: 需要设计一个基于动量效应的量化交易策略
- **方法论的使用**: 用 CRISPE 框架构建 prompt——设定"量化交易策略设计师"角色、明确"捕捉中短期趋势"的见解、声明信号生成逻辑、要求专业简洁的语言风格、实验性输出信号逻辑+回测结果+优化建议
- **结论**: 大模型输出了完整的入场/出场条件、信号生成逻辑和回测方案
- **结果**: 形成可直接用于代码实现的策略框架

### 案例 2: 基于 ICIO 框架解析研报因子
- **问题**: 需要从券商研报中自动提取量化因子及其公式
- **方法论的使用**: 用 ICIO 框架构建 prompt——说明"提取所有量化因子"、输入研报文本、上下文"作为因子解析专家"、输出指示"标准JSON格式，可直接用于生成代码"
- **结论**: 大模型结构化输出了因子名称、公式、参数、方法
- **结果**: 可直接接入代码生成管线

### 案例 3: 多轮对话式策略开发（BROKE框架）
- **问题**: 需要基于A股LV2盘口设计买卖力量失衡指标
- **方法论的使用**: 用BROKE框架分多轮迭代——先定义背景和目标，大模型询问前几档统计和撒单率需求，用户补充后大模型输出完整因子公式与Python代码
- **结论**: 通过BROKE的Evolve步骤实现迭代优化
- **结果**: 得到考虑了前5档盘口不平衡与撤单率的完整因子

---

## A2 — 触发场景 (Future Trigger) ★

### 用户会在什么情境下需要这个 skill?

1. 用户要用大模型生成量化策略、因子、代码，但不知道如何写 prompt
2. 用户发现大模型输出的量化内容质量不稳定，需要结构化方法提升
3. 用户需要为量化工作流配置系统提示词（如因子解析机器人、策略助手）
4. 用户想选择最适合当前量化任务的 prompt 框架（CRISPE vs BROKE vs ICIO）
5. 用户需要用思维链技术让大模型做复杂的量化推理

### 语言信号

- "怎么写 prompt 让大模型帮我..."
- "用大模型生成量化策略"
- "提示词框架" / "prompt framework"
- "CRISPE" / "BROKE" / "ICIO"
- "chain of thought" / "思维链" / "few-shot"
- "system prompt" / "系统提示词"
- "大模型输出质量不稳定"

### 与相邻 skill 的区分 (定稿)

- 与 `llm-capability` 的分工: 本 skill 关注**如何与选定的大模型交互**（写 prompt），llm-capability 关注**选哪个大模型 / 模型能做什么**（能力评估）。先选模型（llm-capability），再写 prompt（本 skill）。两者是"模型选型"vs"模型使用"的两层问题
- 与 `factor-mining` 的边界: 本 skill 是因子挖掘的**前置工具**（教你写 prompt 让大模型帮你挖因子），factor-mining 是**因子挖掘的完整工作流**（数据源、特征工程、IC 验证）。当你问"怎么写 prompt 让大模型帮我生成因子"→本 skill；问"如何系统挖掘并验证一个 alpha 因子"→factor-mining
- 与 `mcp-toolchain` 的边界: 本 skill 是 prompt 层面的**接口设计**，mcp-toolchain 是系统架构层面的**工具链搭建**。两者在"Agent 如何调用工具"这个点上交汇：prompt 决定 Agent 的输入语义，MCP 决定 Agent 的工具可达范围

---

## E — 可执行步骤 (Execution)

当 skill 被激活后, agent 应按以下步骤执行:

1. **判断任务类型，选择框架**
   - 策略设计/生成类 → CRISPE
   - 迭代优化/多轮对话类 → BROKE
   - 数据处理/结构化提取类 → ICIO
   - 通用复杂推理 → 思维链 (CoT)
   - 完成标准: 已明确当前任务最适合的框架

2. **按所选框架构建 prompt**
   - CRISPE: 依次填写 C-R-I-S-P-E 六个维度
   - BROKE: 依次填写 B-R-O-K-E 五个维度
   - ICIO: 依次填写 I-C-I-O 四个维度
   - 完成标准: prompt 草稿已生成，包含所有框架维度

3. **添加思维链增强（如需要）**
   - 简单任务: 加 "让我们一步步思考" (Zero-Shot CoT)
   - 复杂任务: 提供 2-3 个量化推理示例 (Few-Shot CoT)
   - 完成标准: prompt 包含推理引导

4. **配置系统提示词与用户提示词的分工**
   - 系统提示词: 设定角色能力、输出格式规范、边界约束
   - 用户提示词: 提供具体任务输入、数据、上下文
   - 完成标准: 两者分工明确，无职责重叠

5. **测试与迭代**
   - 运行 prompt，评估输出质量
   - 根据 BROKE 的 E (Evolve) 维度迭代优化
   - 完成标准: 输出满足任务需求

---

## B — 边界 (Boundary) ★

### 不要在以下情况使用此 skill

- 用户只是问一般性问题（如"什么是量化交易"），不需要结构化 prompt
- 用户的任务不涉及大模型交互（如纯 Python 编程、数据库查询）
- 用户已有成熟的 prompt 方案，只是想优化细节

### 作者在书中警告的失败模式

- 提示词过于笼统（如"帮我分析股票"），导致大模型输出泛泛而谈
- 不给大模型明确的角色设定，导致输出风格不专业
- 不提供输出格式要求，导致结果难以直接用于代码
- 忽略思维链，在复杂推理任务中直接要答案，导致大模型"跳步"出错

### 作者的盲点 / 时代局限

- 书中框架基于 2025 年 8 月的大模型能力，模型迭代后某些 prompt 技巧可能过时
- 书中以中文 prompt 为主要示例，英文 prompt 的最佳实践可能有差异
- "10000 倍效率提升"的说法缺乏严谨验证

### 容易混淆的邻近方法论

- 通用 prompt engineering（非量化场景）—— 本 skill 专门面向量化交易的 prompt 设计
- 微调/蒸馏 —— 这是模型层面的优化，不是 prompt 层面的

---

## 相关 skills

- **depends-on**: _(无前置)_
- **contrasts-with**: `llm-capability` — 模型选型 vs prompt 设计，两层不同的问题
- **composes-with**: `factor-mining`（prompt 是因子挖掘的交互工具）, `mcp-toolchain`（prompt 定义 Agent 输入语义，MCP 定义工具可达范围）

---

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 待测 (详见 test-prompts.json)
- **蒸馏时间**: 2026-08-16
