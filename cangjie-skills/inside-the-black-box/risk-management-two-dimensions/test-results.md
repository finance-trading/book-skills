# Test Results: risk-management-two-dimensions

## 测试统计
- 总测试用例: 6
- 通过: -
- 失败: -
- 通过率: -%
- 最低要求: 80%

## 测试结果

### should-trigger-01
**Prompt**: "风险管理的规模控制和种类限制有什么区别？"

**期望行为**: 应激活 risk-management-two-dimensions，解释风险管理的二维控制框架

**实际行为**: -

**结果**: -

---

### should-trigger-02
**Prompt**: "如何设计一个完整的风险控制体系？需要考虑哪些方面？"

**期望行为**: 应激活 risk-management-two-dimensions，使用二维控制框架指导用户设计风险控制体系

**实际行为**: -

**结果**: -

---

### should-trigger-03
**Prompt**: "我的策略总风险看起来合适，但最近在某个行业上损失很大，可能是什么问题？"

**期望行为**: 应激活 risk-management-two-dimensions，识别可能是种类限制（行业集中度）的问题

**实际行为**: -

**结果**: -

---

### should-not-trigger-01
**Prompt**: "如何构建最优的投资组合？"

**期望行为**: 不应激活 risk-management-two-dimensions，应激活 portfolio-construction-three-goals

**实际行为**: -

**结果**: -

---

### should-not-trigger-02
**Prompt**: "量化策略有哪些类型的风险？"

**期望行为**: 不应激活 risk-management-two-dimensions，应激活 model-risk-three-sources

**实际行为**: -

**结果**: -

---

### edge-01
**Prompt**: "在极端市场条件下，如何调整风险控制策略？"

**期望行为**: 应激活 risk-management-two-dimensions 和 fat-tail-principle，因为极端市场涉及厚尾风险

**实际行为**: -

**结果**: -

---

## 测试总结

**主要发现**: -

**改进建议**: -

**结论**: 待完成测试后填写
