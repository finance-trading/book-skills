# Test Results: fat-tail-principle

## 测试统计
- 总测试用例: 6
- 通过: -
- 失败: -
- 通过率: -%
- 最低要求: 80%

## 测试结果

### should-trigger-01
**Prompt**: "使用VaR模型有什么局限性？"

**期望行为**: 应激活 fat-tail-principle，解释VaR基于正态分布假设的局限性，以及厚尾特征导致的风险低估

**实际行为**: -

**结果**: -

---

### should-trigger-02
**Prompt**: "为什么我的风险模型低估了极端事件的风险？"

**期望行为**: 应激活 fat-tail-principle，解释市场数据的厚尾特征和正态分布假设失效的问题

**实际行为**: -

**结果**: -

---

### should-trigger-03
**Prompt**: "4倍标准差的事件在金融市场中发生的频率是多少？"

**期望行为**: 应激活 fat-tail-principle，解释实际频率远高于正态分布预测的频率

**实际行为**: -

**结果**: -

---

### should-not-trigger-01
**Prompt**: "历史数据在量化交易中有什么局限性？"

**期望行为**: 不应激活 fat-tail-principle，应激活 historical-data-limitation

**实际行为**: -

**结果**: -

---

### should-not-trigger-02
**Prompt**: "模型风险有哪些类型？"

**期望行为**: 不应激活 fat-tail-principle，应激活 model-risk-three-sources

**实际行为**: -

**结果**: -

---

### edge-01
**Prompt**: "在设计压力测试时，应该如何考虑极端市场条件？"

**期望行为**: 应激活 fat-tail-principle（厚尾风险）和 historical-data-limitation（历史数据局限）

**实际行为**: -

**结果**: -

---

## 测试总结

**主要发现**: -

**改进建议**: -

**结论**: 待完成测试后填写
