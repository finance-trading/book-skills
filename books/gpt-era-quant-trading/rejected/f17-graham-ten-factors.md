```yaml
- id: f17
  title: 格雷厄姆十因子选股框架
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "2.1.2节：10个因子（简化为8个）完整列出，分两组详解（便宜程度5个+企业质量3个）"
      - "2.1.1节：格雷厄姆价值投资理论提到选股方法基础，构成独立铺垫语境"
    reason: "V1通过，两处在2.1章不同小节"
  V2_predictive_power:
    passed: true
    evidence: "能推导出'前五个因子满足但后三个质量因子不满足'是价值陷阱的量化特征"
    reason: "V2通过"
  V3_exclusivity:
    passed: false
    why_unique_or_common: "格雷厄姆十因子来自1934年《证券分析》，是价值投资领域最经典的选股方法之一；书中引用斯坦福大学Charles Lee教授的现代回测（1999-2013年有效）；整体框架是对格雷厄姆经典内容的引用，书中无作者独特诠释；'80年后仍有效'的强调有说服力但不是独特见解"
  final_decision: REJECT
  reject_reason: "V3不通过：格雷厄姆十因子是1934年《证券分析》的经典内容，是任何价值投资学习者的必读内容，非作者独特视角"
```
