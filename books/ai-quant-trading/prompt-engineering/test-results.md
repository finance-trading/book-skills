# prompt-engineering 测试结果

## 测试概述
- **skill 名称**: prompt-engineering
- **测试时间**: 2026-08-16
- **测试用例数**: 6
- **通过标准**: ≥80%

## 测试用例与结果

| ID | 类型 | Prompt | 预期行为 | 结果 |
|---|---|---|---|---|
| should-trigger-01 | 正面 | 用大模型从研报提取量化因子，不知道怎么设计 prompt | 推荐 ICIO 框架，构建提取研报因子的 prompt | ✅ PASS |
| should-trigger-02 | 正面 | 大模型给的量化策略方案很笼统，怎么改进 | 推荐 CRISPE/BROKE 框架，通过角色设定提升质量 | ✅ PASS |
| should-trigger-03 | 正面 | CRISPE 和 BROKE 框架有什么区别？ | 解释两个框架适用场景差异 | ✅ PASS |
| should-not-trigger-01 | 跨skill | 从研报里提取所有量化因子 | 应触发 factor-mining，不应触发本 skill | ✅ PASS |
| should-not-trigger-02 | 跨skill | ChatGPT 和 DeepSeek 哪个更适合量化分析 | 应触发 llm-capability，不应触发本 skill | ✅ PASS |
| edge-01 | 边界 | 写一个让大模型分析股票走势的 prompt | 调用 prompt-engineering，需确认是 prompt 设计还是直接分析 | ✅ PASS |

## 通过率
**6/6 (100%)**

## 分析
- 所有 prompt 设计需求都能正确触发
- 跨 skill 混淆测试通过：
  - 直接执行因子提取 → factor-mining（不是 prompt 设计）
  - 模型选型 → llm-capability（不是 prompt 设计）
- 边界场景处理合理：明确是 prompt 设计需求则触发，如果用户只是想分析股票则不触发

## 结论
✅ **通过** — trigger 描述准确，与相邻 skill 边界清晰
