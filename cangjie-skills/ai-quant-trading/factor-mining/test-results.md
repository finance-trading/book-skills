# factor-mining 测试结果

## 测试概述
- **skill 名称**: factor-mining
- **测试时间**: 2026-08-16
- **测试用例数**: 6
- **通过标准**: ≥80%

## 测试用例与结果

| ID | 类型 | Prompt | 预期行为 | 结果 |
|---|---|---|---|---|
| should-trigger-01 | 正面 | 从 LV2 订单簿数据挖掘买卖力量失衡信号 | 介绍 LV2 订单簿不平衡因子构建方法 | ✅ PASS |
| should-trigger-02 | 正面 | 随机森林做量价特征工程，过拟合严重 | 讨论 ML 因子挖掘的过拟合问题 | ✅ PASS |
| should-trigger-03 | 正面 | 怎么验证新挖掘的因子是否有效？IC 值多少算好？ | 介绍因子有效性验证方法 | ✅ PASS |
| should-not-trigger-01 | 跨skill | 用 AKShare 获取 A 股日线数据并处理缺失值 | 应触发 data-pipeline，不应触发本 skill | ✅ PASS |
| should-not-trigger-02 | 跨skill | 写 prompt 让大模型从研报提取因子公式 | 应触发 prompt-engineering，不应触发本 skill | ✅ PASS |
| edge-01 | 边界 | 构建基于新闻情感的因子 | 调用 factor-mining，提示 sentiment-quant 更专精 | ✅ PASS |

## 通过率
**6/6 (100%)**

## 分析
- 所有因子挖掘需求都能正确触发（高频因子、ML 因子、因子验证）
- 跨 skill 混淆测试通过：
  - 数据获取与清洗 → data-pipeline（不是因子挖掘）
  - prompt 设计 → prompt-engineering（不是因子挖掘方法论）
- 边界场景处理合理：情绪因子可以用 factor-mining 覆盖，但 sentiment-quant 更专精

## 结论
✅ **通过** — trigger 描述准确，与数据工程和 prompt 设计的边界清晰
