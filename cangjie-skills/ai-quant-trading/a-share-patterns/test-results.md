# a-share-patterns 测试结果

## 测试概述
- **skill 名称**: a-share-patterns
- **测试时间**: 2026-08-16
- **测试用例数**: 6
- **通过标准**: ≥80%

## 测试用例与结果

| ID | 类型 | Prompt | 预期行为 | 结果 |
|---|---|---|---|---|
| should-trigger-01 | 正面 | 量化 A 股涨停板策略，怎么判断涨停持续性 | 介绍涨停原因归类、题材持续性评估 | ✅ PASS |
| should-trigger-02 | 正面 | 集合竞价阶段怎么捕捉主力资金动向 | 介绍竞价强度因子构建方法 | ✅ PASS |
| should-trigger-03 | 正面 | 通过龙虎榜数据跟踪游资操作模式 | 介绍游资席位行为分析 | ✅ PASS |
| should-not-trigger-01 | 诱饵 | 做美股的动量策略 | 不应触发（A 股模式不适用于美股） | ✅ PASS |
| should-not-trigger-02 | 跨skill | 用大模型分析财经新闻情感倾向 | 应触发 sentiment-quant，不应触发本 skill | ✅ PASS |
| edge-01 | 边界 | 判断市场情绪决定是否参与连板股 | 调用 a-share-patterns 介绍晋级率，提示 sentiment-quant 有更全面的情绪量化 | ✅ PASS |

## 通过率
**6/6 (100%)**

## 分析
- 所有 A 股特色模式需求都能正确触发（涨停板、竞价、游资席位）
- 诱饵测试通过：非 A 股市场的需求不会误触发
- 跨 skill 混淆测试通过：情感分析 → sentiment-quant（不是 A 股交易模式）
- 边界场景处理合理：市场情绪判断可以用晋级率指标，但全面的情绪量化需要 sentiment-quant

## 结论
✅ **通过** — trigger 描述准确，A 股特色模式的边界清晰
