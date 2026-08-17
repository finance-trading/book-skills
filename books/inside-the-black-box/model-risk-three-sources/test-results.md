# Test Results: model-risk-three-sources

## 测试统计
- 总测试用例: 6
- 通过: -
- 失败: -
- 通过率: -%
- 最低要求: 80%

## 测试结果

### should-trigger-01
**Prompt**: "量化策略的模型风险有哪些来源？"

**期望行为**: 应激活 model-risk-three-sources，解释模型风险的三种来源：不适宜性、错误设定、执行错误

**实际行为**: -

**结果**: -

---

### should-trigger-02
**Prompt**: "我的策略最近表现异常，可能是模型哪方面出了问题？"

**期望行为**: 应激活 model-risk-three-sources，帮助诊断模型风险的三种可能来源

**实际行为**: -

**结果**: -

---

### should-trigger-03
**Prompt**: "如何评估一个量化策略的模型风险？"

**期望行为**: 应激活 model-risk-three-sources，提供评估模型风险的方法

**实际行为**: -

**结果**: -

---

### should-not-trigger-01
**Prompt**: "如何控制投资组合的风险敞口？"

**期望行为**: 不应激活 model-risk-three-sources，应激活 risk-management-two-dimensions

**实际行为**: -

**结果**: -

---

### should-not-trigger-02
**Prompt**: "为什么VaR模型会低估极端风险？"

**期望行为**: 不应激活 model-risk-three-sources，应激活 fat-tail-principle

**实际行为**: -

**结果**: -

---

### edge-01
**Prompt**: "如何避免机器学习策略中的模型风险？"

**期望行为**: 应激活 model-risk-three-sources（模型风险）和 alpha-model-taxonomy（数据驱动型方法论）

**实际行为**: -

**结果**: -

---

## 测试总结

**主要发现**: -

**改进建议**: -

**结论**: 待完成测试后填写
