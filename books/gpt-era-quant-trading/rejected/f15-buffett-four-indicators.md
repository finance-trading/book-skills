```yaml
- id: f15
  title: 巴菲特四指标选股框架
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "2.1.3节：ROE>20%/毛利率>40%/净利率>5%/市盈率20-40倍（A股适配）完整列出并有回测"
      - "2.1.1节：价值投资底层逻辑中提到选优质企业需分析基本面指标，构成独立铺垫语境"
      - "1.4.1节：基本面量化策略简介提到巴菲特是代表人物，独立简表"
    reason: "V1通过，跨第1章和第2章多处"
  V2_predictive_power:
    passed: true
    evidence: "能推导出四指标能否适用于成长期科技股（如新能源汽车公司）的场景：净利率和ROE门槛会过滤掉所有成长期亏损公司，框架需要改为毛利率+未来净利率预期"
    reason: "V2通过，书中未讨论科技股适配问题"
  V3_exclusivity:
    passed: false
    why_unique_or_common: "ROE/毛利率/净利率三个指标是巴菲特在历年股东信中反复公开谈及的，在全球价值投资圈广泛传播；A股市盈率20-40倍的适配是对巴菲特原版（15倍以内）的本地化调整，有一定实用价值但不构成独特视角；整体框架是对公开内容的整理，非作者原创"
  final_decision: REJECT
  reject_reason: "V3不通过：四指标是巴菲特在公开信中反复谈及的内容，是价值投资圈的广泛常识；A股PE适配是小调整，不构成独特视角"
```
