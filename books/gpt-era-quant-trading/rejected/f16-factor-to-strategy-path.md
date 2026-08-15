```yaml
- id: f16
  title: 从因子有效性到策略构建的路径
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: false
    evidence:
      - "1.5.1节：AI在量化中的三维应用（算法/结构化数据/元知识）"
      - "2.4.3节：彼得·林奇策略三次迭代隐含从数据到策略的过程"
    reason: "候选所描述的四阶段路径（数据结构化→因子挖掘→模型构建→策略执行）是提炼综合，并非书中任何一处明确陈述的框架；两处引用分别讲AI工具和策略迭代，都未明确列出这四个阶段"
  V2_predictive_power:
    passed: false
    reason: "框架本身是宽泛的工作流描述，推导出的结论容易流于常识"
  V3_exclusivity:
    passed: false
    why_unique_or_common: "数据→因子→模型→执行的量化工作流是任何量化交易书籍中的标准描述，无作者独特视角"
  final_decision: REJECT
  reject_reason: "V1不通过：四阶段工作流是提炼综合，书中无任何一处明确陈述这个框架；V3也不通过：属于行业标准描述"
```
