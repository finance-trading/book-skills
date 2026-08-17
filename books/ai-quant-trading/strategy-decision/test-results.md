# strategy-decision 测试结果

## 测试概述
- **skill 名称**: strategy-decision
- **测试时间**: 2026-08-16
- **测试用例数**: 6
- **通过标准**: ≥80%

## 测试用例与结果

| ID | 类型 | Prompt | 预期行为 | 结果 |
|---|---|---|---|---|
| should-trigger-01 | 正面 | 500万资金，风险中等，不知道从哪类策略入手 | 评估资金规模、风险偏好，推荐资产配置量化或阿尔法量化 | ✅ PASS |
| should-trigger-02 | 正面 | 趋势跟踪策略最近三个月亏损，是否该换策略 | 分析策略失效原因，评估是否需要切换策略类型 | ✅ PASS |
| should-trigger-03 | 正面 | 阿尔法量化和贝塔量化有什么区别？该做哪个？ | 解释两类策略差异，根据用户情况推荐 | ✅ PASS |
| should-not-trigger-01 | 诱饵 | 用 Python 写双均线策略回测代码 | 不应调用（具体实现，不是策略选择） | ✅ PASS |
| should-not-trigger-02 | 跨skill | 想挖掘新的量价因子 | 应触发 factor-mining，不应触发本 skill | ✅ PASS |
| edge-01 | 边界 | A 股涨停板策略详细介绍 | 调用 strategy-decision 介绍策略类型，提示 a-share-patterns 更专精 | ✅ PASS |

## 通过率
**6/6 (100%)**

## 分析
- 所有正面场景都能正确触发
- 诱饵测试通过：实现层面的需求不会误触发策略选择
- 跨 skill 混淆测试通过：因子挖掘需求正确路由到 factor-mining
- 边界场景处理合理：A 股特色模式可以先介绍策略类型，再引导到专精 skill

## 结论
✅ **通过** — trigger 描述准确，边界清晰
