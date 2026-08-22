# data-pipeline 测试结果

## 测试概述
- **skill 名称**: data-pipeline
- **测试时间**: 2026-08-16
- **测试用例数**: 6
- **通过标准**: ≥80%

## 测试用例与结果

| ID | 类型 | Prompt | 预期行为 | 结果 |
|---|---|---|---|---|
| should-trigger-01 | 正面 | 从 Tushare 批量获取财务数据，API 限流怎么处理 | 介绍 API 调用、批量下载、限流处理 | ✅ PASS |
| should-trigger-02 | 正面 | 量化数据有很多缺失值（停牌日、财务数据不全），怎么清洗 | 介绍缺失值处理方法 | ✅ PASS |
| should-trigger-03 | 正面 | AKShare、Tushare、Wind 有什么区别？该用哪个 | 对比三个数据源，给出推荐 | ✅ PASS |
| should-not-trigger-01 | 跨skill | 用大模型从研报里自动提取量化因子 | 应触发 factor-mining，不应触发本 skill | ✅ PASS |
| should-not-trigger-02 | 跨skill | 搭建 MCP Server 让大模型调用数据查询工具 | 应触发 mcp-toolchain，不应触发本 skill | ✅ PASS |
| edge-01 | 边界 | 采集财经新闻和社交媒体数据做舆情分析 | 调用 data-pipeline 提供数据采集方案，提示 sentiment-quant 有情绪分析方法 | ✅ PASS |

## 通过率
**6/6 (100%)**

## 分析
- 所有数据工程需求都能正确触发（API 调用、数据清洗、数据源评估）
- 跨 skill 混淆测试通过：
  - 因子提取方法论 → factor-mining（不是数据工程）
  - Agent 工具链架构 → mcp-toolchain（不是传统 ETL）
- 边界场景处理合理：舆情数据采集是本 skill 的职责，情绪分析是 sentiment-quant 的职责

## 结论
✅ **通过** — trigger 描述准确，与因子挖掘和 Agent 架构的边界清晰
