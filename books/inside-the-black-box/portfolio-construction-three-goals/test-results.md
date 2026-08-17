# Test Results: portfolio-construction-three-goals

## 测试统计
- 总测试用例: 6
- 通过: -
- 失败: -
- 通过率: -%
- 最低要求: 80%

## 测试结果

### should-trigger-01
**Prompt**: "投资组合构建需要在哪些目标之间平衡？"

**期望行为**: 应激活 portfolio-construction-three-goals，解释收益、风险、成本的三目标平衡

**实际行为**: -

**结果**: -

---

### should-trigger-02
**Prompt**: "我想优化我的投资组合，应该考虑哪些因素？"

**期望行为**: 应激活 portfolio-construction-three-goals，使用三目标框架指导用户优化组合

**实际行为**: -

**结果**: -

---

### should-trigger-03
**Prompt**: "如何在追求高收益的同时控制风险和交易成本？"

**期望行为**: 应激活 portfolio-construction-three-goals，解释三目标之间的权衡和平衡方法

**实际行为**: -

**结果**: -

---

### should-not-trigger-01
**Prompt**: "如何控制投资组合的风险敞口？"

**期望行为**: 不应激活 portfolio-construction-three-goals，应激活 risk-management-two-dimensions

**实际行为**: -

**结果**: -

---

### should-not-trigger-02
**Prompt**: "量化策略应该采用理论驱动还是数据驱动的方法？"

**期望行为**: 不应激活 portfolio-construction-three-goals，应激活 alpha-model-taxonomy

**实际行为**: -

**结果**: -

---

### edge-01
**Prompt**: "市场滑点突然上升时，我的投资组合应该如何调整？"

**期望行为**: 应激活 portfolio-construction-three-goals（调整成本目标权重）和 fat-tail-principle（考虑极端市场条件）

**实际行为**: -

**结果**: -

---

## 测试总结

**主要发现**: -

**改进建议**: -

**结论**: 待完成测试后填写
