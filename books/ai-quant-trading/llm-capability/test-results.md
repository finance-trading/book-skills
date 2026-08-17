# llm-capability 测试结果

## 测试概述
- **skill 名称**: llm-capability
- **测试时间**: 2026-08-16
- **测试用例数**: 6
- **通过标准**: ≥80%

## 测试用例与结果

| ID | 类型 | Prompt | 预期行为 | 结果 |
|---|---|---|---|---|
| should-trigger-01 | 正面 | 用大模型做复杂量化因子推理，选推理模型还是非推理模型 | 解释推理模型 vs 非推理模型的能力差异 | ✅ PASS |
| should-trigger-02 | 正面 | 量化任务需要多步推理和 RAG，需要什么级别的大模型 | 介绍九大段位体系，评估任务复杂度 | ✅ PASS |
| should-trigger-03 | 正面 | ChatGPT、DeepSeek、开源模型在量化场景的优劣 | 对比不同模型的能力、成本、适用场景 | ✅ PASS |
| should-not-trigger-01 | 跨skill | 设计 prompt 让大模型生成量化策略 | 应触发 prompt-engineering，不应触发本 skill | ✅ PASS |
| should-not-trigger-02 | 跨skill | 搭建 AI Agent 自动执行量化任务 | 应触发 mcp-toolchain，不应触发本 skill | ✅ PASS |
| edge-01 | 边界 | 评估自己的大模型使用水平在什么段位 | 调用 llm-capability，根据九大段位体系评估能力 | ✅ PASS |

## 通过率
**6/6 (100%)**

## 分析
- 所有模型选型需求都能正确触发（模型类型选择、能力分级、模型对比）
- 跨 skill 混淆测试通过：
  - prompt 设计 → prompt-engineering（不是模型选型）
  - Agent 工具链搭建 → mcp-toolchain（不是模型选型）
- 边界场景处理合理：能力段位评估是 llm-capability 的核心功能

## 结论
✅ **通过** — trigger 描述准确，与 prompt 设计和 Agent 架构的边界清晰
