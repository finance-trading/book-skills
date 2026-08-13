```yaml
- id: f14
  title: 马科维茨投资组合理论的四假设框架
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "2.2.1节：均值-方差模型的四个假设完整列出"
      - "2.3.1节：贝塔策略基本假设部分将马科维茨假设与Smart Beta假设对比，构成独立语境"
    reason: "V1通过，跨2.2节和2.3节两个策略章节"
  V2_predictive_power:
    passed: true
    evidence: "能推导出假设四（同时最小化风险+最大化收益）不成立时的模型降级方案"
    reason: "V2通过"
  V3_exclusivity:
    passed: false
    why_unique_or_common: "马科维茨投资组合理论是1952年诺贝尔经济学奖级别的经典理论，四个假设是任何金融学教材、CFA考试、量化金融课程中的必讲内容，书中只是引用和解释，无作者独特诠释或反直觉改造"
  final_decision: REJECT
  reject_reason: "V3不通过：马科维茨四假设是经典金融理论教材内容，任何聪明人学过金融都会说的常识"
```
