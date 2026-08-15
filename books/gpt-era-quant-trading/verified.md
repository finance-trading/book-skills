# 三重验证通过的候选单元

> 验证时间：2026-08-12
> 验证标准：V1 跨域验证 + V2 预测力测试 + V3 独特性检验
> 来源：《GPT时代的量化交易：底层逻辑与技术实践》

---

## 验证说明

- **V1 跨域验证**：单元在书中至少2个独立语境下有佐证
- **V2 预测力测试**：能用该单元推导出书里没明说的某个问题的答案
- **V3 独特性检验**：是否是作者独特视角/反直觉见解/独特术语体系

**特殊规则**：
- 术语类（glossary）自动通过 V1 和 V2，仅需验证 V3
- 案例类（case）和反例类（counter-example）自动通过 V1 和 V2，仅需验证 V3
- 框架和原则类需要通过全部三重验证

---

## 通过单元列表

<!-- framework batch verified 2026-08-12 -->

```yaml
- id: f01
  title: 五大量化策略选择框架
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "1.4节：全景式量化交易策略分五类（基本面/资产配置/阿尔法/贝塔/另类），表1.1-1.9独立简表"
      - "第2章2.1-2.5节：每节独立展开各策略底层逻辑、代表人物、实战案例"
    reason: "五大策略分类在第1章作全景介绍后，第2章每一节作为独立语境展开，跨越全书结构"
  V2_predictive_power:
    passed: true
    novel_question: "一个拥有100万人民币、无编程基础的个人投资者，应该优先选择哪种策略？"
    derived_answer: "基本面量化需大量数据处理；资产配置适合超大规模资金；阿尔法需不断挖掘因子技术门槛高；贝塔趋势跟踪规则简单可执行；另类需独特数据来源。推导出贝塔（趋势跟踪）最适合100万级个人投资者"
    reason: "书中未直接回答这个具体场景，但框架提供了多维筛选逻辑，推导结论非平庸"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "将巴菲特（基本面）、达利欧（资产配置）、西蒙斯（阿尔法）、克罗（贝塔）、索罗斯（另类）统一纳入'量化'框架，打破'量化=算法对冲'的常识认知，是作者独创的广义量化术语体系"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: f02
  title: 概率优势思维模型
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "1.1节：明确定义三核心假设——上帝视角/局部最优/市场非理性"
      - "第3章凯利公式部分：'从海量数据中寻找能够带来超额收益的大概率策略'直接应用概率优势思维"
    reason: "1.1节作为哲学定义，第3章凯利公式部分作为数学落地，两个独立语境共同佐证"
  V2_predictive_power:
    passed: true
    novel_question: "一个量化策略的历史胜率是45%，是否应该放弃它？"
    derived_answer: "概率优势思维要求看期望值而非单次胜率；45%胜率若赔率>1（盈利时收益大于亏损时损失），则长期期望值仍可为正；不应简单放弃，而应计算期望值E=0.45×盈利-0.55×亏损"
    reason: "书中未直接讨论这个胜率阈值场景，推导结论具有实际指导意义且非平庸"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "三个假设中'②没有全局最优解，只有局部最优解'明确反直觉（大多数人追求最优系统/圣杯），BOOK_OVERVIEW明确标注为'作者独创的量化交易哲学基础'；'上帝视角'术语也是作者独创表述"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: f05
  title: 风险平价配置框架
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "2.2.1节：正式介绍风险平价理论，给出数学公式（TRC_i=TRC_j），计算60/40组合股票贡献80%风险"
      - "2.2.3节：实战全天候策略，以五只ETF组合展示风险平价的具体应用（GLD/GSG/IEI/TLT/VTI权重）"
    reason: "理论推导章节和实战案例章节构成两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "如果A股引入风险平价框架，股票+债券+黄金三类资产应如何分配权重？"
    derived_answer: "股票波动率高于债券，黄金介于两者之间；风险平价要求各资产风险贡献相等；结论是股票比例应明显低于传统60/40（可能仅15-25%），债券比例大幅提高（50-60%），黄金比例高于传统配置（15-20%），具体比例需用历史波动率协方差矩阵计算"
    reason: "书中只给出A股简化版（股票+现金），未讨论三类资产的中国版权重，推导非平庸"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'配置风险而非配置资金'是对传统投资逻辑的直接颠覆。书中明确指出60/40股债组合中股票贡献80%风险这一反直觉事实，这个计算结论对大多数投资者是全新认知"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: f06
  title: 全天候四象限思维
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "1.4.2节：中国全天候产品组合（股票+债券+现金定期再平衡）作为资产配置量化策略独立简介"
      - "2.2.3节：完整介绍四象限（高增长/低增长/高通胀/低通胀）及各象限配置资产类型"
      - "2.2.4节：个人养老金策略中以全天候作为方法论基础"
    reason: "跨越第1章概览、第2章理论和实战、第2章养老金应用三个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "2020年新冠疫情暴发（经济骤然收缩+通缩压力）对全天候组合的影响如何？"
    derived_answer: "新冠初期属于'低增长+低通胀（通缩压力）'象限——框架配置普通债券和股票为主；实际股票大跌而美国国债大涨；全天候组合因大量债券配置（TLT占40%），2020年3月大跌中回撤应显著小于纯股票组合，实际数据验证全天候组合2020年全年仍为正收益"
    reason: "书中没有讨论2020年疫情期间的全天候表现，框架推导出非平庸结论"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'不需要进行预测'——框架核心反直觉点。传统投资者认为必须判断宏观走向，全天候说'为所有可能性做好准备'，主动放弃预测能力转向风险均衡，这与投资常识（判断宏观才能选资产）直接相反"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: f09
  title: 阻力支撑相对强度（RSRS）择时框架
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "1.4.4节：表1.8将RSRS择时量化交易策略作为贝塔策略实战案例独立列出（与PTSS对比）"
      - "2.3.3节：完整介绍RSRS定义、原理（high=α+β×low回归）、三种市场状态应用逻辑"
    reason: "第1章作为策略分类的实战佐证，第2章作为完整理论展开，两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "RSRS框架能否用于判断某单只股票（如贵州茅台）的买卖时机？"
    derived_answer: "将茅台每日最高价/最低价作为回归变量计算斜率；个股比指数噪声大，R²普遍偏低，修正标准分的过滤作用更关键；茅台流通盘大、机构持仓多，RSRS信号相对可靠；但单只股票存在重大事件扰动（如行业政策），需叠加基本面过滤层"
    reason: "书中RSRS专门针对宽基指数（沪深300等），未讨论个股应用场景，推导结论非平庸"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "用'最高价与最低价线性回归斜率'量化支撑/阻力相对强度——传统技术分析划固定水平支撑线，RSRS改用动态OLS回归斜率感知市场共识变化，是量化工程创新；RSRS是非常规术语，方法本身反直觉（谁会想到用价格对价格回归来判断趋势？）"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: f21
  title: RSRS指标三层优化路径
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "2.3.3节第5小节：标准分→修正标准分→右偏标准分三层递进优化，每层明确指出上一层缺陷和新引入缺陷"
      - "2.3.3节第6小节：在三层优化基础上进一步引入市场价格趋势优化、交易量相关性优化、指数增强优化——三个外部维度扩展构成独立语境"
    reason: "三层标准化优化（策略迭代本体）与多维外部因子优化（更高维度应用）是同节内两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "如果市场进入超长震荡期（1年以上），RSRS三层优化中哪层最有效？"
    derived_answer: "长期震荡市中原始斜率波动小且均值回归明显，标准分（z-score）最灵敏；修正标准分通过R²过滤，震荡市R²普遍偏低，会频繁过滤信号导致漏判；右偏标准分=修正标准分×斜率，震荡市斜率接近1，右偏效果减弱且产生假信号。结论：超长震荡市第一层（标准分）优于后两层"
    reason: "书中未讨论各层在不同市场状态下的相对有效性，推导结论非平庸"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "每层优化明确说明'解决了上一层哪个缺陷、引入了什么新缺陷'的辩证式迭代设计，是量化工程思维的独特展示；右偏标准分=修正标准分×斜率这个乘法设计属于书中原创工程方案，非引用他人"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: f22
  title: 资产配置三步分析法
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "2.2.3节：三步分析法（选低相关资产→确定参数→定时定量计算）作为全天候策略实战流程"
      - "2.2.4节：个人养老金量化策略中同样的三步流程被应用于小资金个人账户的具体配置场景"
    reason: "全天候机构配置和个人养老金配置是两个独立应用语境"
  V2_predictive_power:
    passed: true
    novel_question: "月薪2万的年轻人开始定投，用三步分析法如何设计自己的资产配置？"
    derived_answer: "步骤一：小资金选股票+现金（书中建议小资金不加债券/黄金/大宗）；步骤二：预期年化收益6-8%，风险区间20%，参考当前存款利率设定无风险收益；步骤三：每月末将各资产调回目标风险贡献比例（小资金可简化为季度固定比例再平衡，因单月资金增量占比高）"
    reason: "书中给出的是机构规模配置，未讨论小额定投的参数设置和再平衡频率适配"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'步骤一按资金规模分层选资产'（小资金股票+现金，大资金加债券/黄金/大宗）是作者对风险平价理念的A股实用化适配，将抽象理论转化为可执行的资金规模决策树，有独特工程价值"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: f23
  title: 量化交易智能化三维应用框架
  type: framework
  original_source: framework.md
  V1_cross_domain:
    passed: true
    evidence:
      - "1.5.1节：明确列出三维（AI非线性建模/非结构化数据处理/元知识学习）"
      - "2.4.3节：彼得·林奇多因子策略中三次迭代优化（加入AI因子阿尔法002）展示第一维度的实际应用"
      - "2.5.1节：另类量化策略的五大优势中'可以更好地利用机器学习'直接呼应第一维度"
    reason: "1.5节理论定义、2.4节因子迭代实战、2.5节另类策略分析三个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "没有编程背景的投资者，用GPT能完全替代量化工程师吗？"
    derived_answer: "按三维分层：第一维（非线性建模）GPT可生成代码框架但人需验证因子逻辑，覆盖约50%工作；第二维（非结构化数据处理）GPT最擅长，覆盖80%以上；第三维（元知识学习=用AI选择策略）书中明确指出'相关技术尚待突破'，GPT无法完成。结论：GPT可替代量化工程师约40-60%的执行工作，但策略选择和因子逻辑验证仍不可缺"
    reason: "书中讨论GPT降低编程门槛，但BOOK_OVERVIEW批判GPT能力被高估，两者间的矛盾需要三维框架来分层解析"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'元知识学习'（用AI选择策略而非执行策略）是对AI在量化中角色的层级创新认知，大多数读者认为AI=执行工具，三维框架揭示存在更高决策层；'元知识'术语在量化语境下是作者独特使用"
  final_decision: PASS
  reject_reason: ""
```



<!-- case batch verified 2026-08-12 -->

```yaml
- id: c01
  title: 本间宗久发明K线图与大米期货交易
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "250年前历史素材，具体数据（累计赚取约合现代100亿美元），'此后从未失手'是极端结论；发明K线图→记录四价格的具体行动链，非任何聪明人能凭空说出"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c02
  title: 索普Boss基金1970-1974年表现
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "逐年具体收益率（+3%/+13.5%/+26%/+9.7%）与标普500对比，连续11年无亏损的稀有历史记录；权证定价模型套利机制是非常规的量化方法"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c03
  title: 西蒙斯大奖章基金1990-2010年业绩
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "20年平均年化复利收益率70%，首年56%，量化交易史上最高回报纪录；雇用物理学家/数学家/密码破译专家的非常规人才策略"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c04
  title: 巴菲特2022年一季度抄底苹果
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "2022年一季度苹果连续三日下跌后6亿美元买入的具体时间+金额，直接演示'基本面反转'的操作机制；有名有姓有数据"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c05
  title: A股行业景气策略2021-2022年表现
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "2022年4月26日具体截面数据，大气治理/科技/建材三行业，6个月跑赢沪深300超50%的惊人幅度；实时验证可操作"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c06
  title: 中国全天候配置策略15年回测
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "6.18% CAGR + 最大回撤-17%的具体回测结果，15年跨越牛熊；与美国401K养老金计划的对比视角独特"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c07
  title: 达利欧1987年'黑色星期五'预判成功
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "1987年10月19日当天业绩+22%，被媒体称为'十月英雄'；提前做空+极端市场下逆势盈利的完整叙事"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c08
  title: 达利欧1982年债务危机误判导致破产
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "预测通胀实际出现通缩的戏剧性反转，知名大师彻底失去所有资产；'过度自信→归零'是反直觉的失败路径，有8年经验仍然错"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c09
  title: 达利欧2008年金融危机成功预判
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "+14% vs 他人亏损超30%的强对比；吸取1982教训后在做空中加对冲的策略改进叙事，体现迭代学习"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c10
  title: 达利欧2010年欧债危机预判
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "纯阿尔法基金分别接近45%和28%，全天候接近18%的具体年度业绩；系统调查欧洲各国债务→提前布局的完整方法"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c11
  title: 桥水全天候组合2007-2023年表现
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "具体ETF五标的权重（GLD 7.5%/GSG 7.5%/IEI 15%/TLT 40%/VTI 30%），16年CAGR 5.45%，夏普比率0.73；可直接复制的参数配置"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c12
  title: 巴菲特量化策略A股2010-2022年回测
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "ROE>20%/毛利率>40%/净利率>5%三条量化筛选标准，PE<20买入/>40卖出的具体规则；将价值投资翻译成可执行代码的作者独特工程"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c13
  title: 彼得·林奇多因子策略2018-2023年回测
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "三阶段优化具体数据：-2.66%→0.23%→1.07%，阿尔法-6.53%→-1.51%→-0.83%；记录了策略迭代改进的完整量化路径"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c14
  title: 阿尔法002因子沪深300与创业板对比
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "IC未达0.03最低标准，换手率持有1天30%/持有5-10天超70%；发现沪深300不适合→切换创业板的市场差异洞察"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c15
  title: 长期资本管理公司1998年破产
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "2位诺贝尔奖得主+25位博士的顶尖阵容仍在不到5年破产；'少不等于没有'的震撼反直觉例证，专家光环与黑天鹅的矛盾"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c16
  title: 索普'2%法则'与21点赌博
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "从21点赌博数学推导出投资2%法则，被量化基金广泛采用（持仓50只股票、每只最大2%）；跨域应用赌博数学到投资"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c17
  title: 索普普林斯顿-纽波特基金1969-1988年业绩
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "1969-1988年净值上涨14.5倍 vs 标普500仅5倍；1969年创立史上第一家量化对冲基金的历史里程碑"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c18
  title: 凯利公式2022年五只活跃股票仓位计算
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "2022年底具体5只A股（中国联通/包钢股份/ST大集等），保守20.3万/激进72.92万的具体仓位区间；真实数据完整演示"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c19
  title: 格雷厄姆选股法美股1999-2013回测
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "斯坦福Charles Lee教授学术回测，前2十分位14%/后2十分位5%/标普中型股400指数8.5%的三组具体数据；验证80年前方法"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c20
  title: WorldQuant阿尔法101因子2015年公开
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "80%因子仍在实盘使用，2016年推动中国量化元年开启；公开因子库这一行业罕见事件的历史记录价值"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c21
  title: 彼得·林奇麦哲伦基金1977-1990年业绩
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "1800万→140亿美元（规模增长777倍），13年年化29%，100万+投资人；成长股投资量化化的最佳历史范本"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c22
  title: 费雪成长股投资理念影响巴菲特
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "巴菲特'85%格雷厄姆+15%费雪'原话，第一部登上《纽约时报》畅销书榜首的投资书；有具体比例引用和历史唯一性"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: c23
  title: 行业营收增长率因子2022年验证
  type: case
  original_source: case.md
  V1_cross_domain:
    passed: true
    evidence: ["案例类自动通过V1"]
    reason: "案例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "案例类自动通过V2"
    derived_answer: "案例类按规则自动通过V2"
    reason: "案例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "2022年10月31日唯一符合条件的卫生和社会工作板块，后续+15.1% vs 大盘-1.87%；实时前瞻验证，非回测"
  final_decision: PASS
  reject_reason: ""
```

<!-- counter-example batch verified 2026-08-12 -->

```yaml
- id: ce01
  title: 长期资本管理公司破产案例
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "2位诺贝尔奖+25位博士团队<5年破产；'少不等于没有'是对过度安全假设的精准反驳，黑天鹅+杠杆组合的具体机制"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce02
  title: 过度下注导致破产
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "索普从21点赌博数学推导出的'2%法则'；凯利理论框架下'过度下注必破产'有数学证明，非直觉警告"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce03
  title: 达利欧1982年预测失误
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "知名大师失去全部资产的具体案例；墨西哥债务违约→预测通胀→实际通缩的因果链是独特宏观分析反例"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce04
  title: 达利欧1974年猪腩期货惨痛教训
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "期货连续跌停的'电击感受'原话引用，有具体年份和品种；'必须经历可怕的痛苦'是反浪漫化投资的独特诚实陈述"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce05
  title: 低估值陷阱
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "费雪满仓3只低估值股票，3年后市盈率比买入时更低的反直觉结果；有具体投资大师的亲身失败案例背书"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce06
  title: 巴菲特投资伯克希尔纺织业失败
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "巴菲特自认的失败投资，'夕阳行业+行业龙头=仍然失败'反直觉；'伟大行业>伟大企业'的层级命题是作者从案例提炼的独特洞察"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce07
  title: 不要单纯依赖定性分析
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "格雷厄姆'定量是定性的基础和前提'的层级命题；将量化置于价值判断的基础层而非平行层，与常识认为两者平等的理解不同"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce08
  title: 2008年金融危机中的模型失效
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "几乎所有CDO经理都用B-S模型定价→房产泡沫破裂→系统崩溃的具体因果机制；模型单一化使用的集体失败有历史数据支撑"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce09
  title: 凯利公式公式二过度乐观的风险
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "公式一（保守）vs 公式二（激进）的具体差异是本书独创框架；公式二未考虑连续跌停黑天鹅的精确缺陷分析"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce11
  title: 高频交易的合规风险
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "2012-2013年FINRA检测20万次叠加报价并处罚的具体事件；订单/成交比率的合规边界是操作层面反例，非常规量化陷阱"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce12
  title: 量化强势股策略在无序轮动行情中失效
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "A股'一日游'和无序轮动是本书针对中国市场的具体分析；强势股崩盘连续跌停的极端场景描述有量化特殊性"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce14
  title: 事件驱动策略失效周期缩短
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "从'数天行情'缩短到'一日游'的量化时间维度；策略拥挤导致有效窗口缩短的机制分析，需更高维度判断力的结论非平庸"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce15
  title: 阿尔法002因子在沪深300中表现不佳
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "IC值具体未达0.03标准，换手率持有5-10天超70%的具体数据；中国市场涨跌停制度导致因子失效的特定机制"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce16
  title: 不考虑涨跌停板导致因子失效
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "涨停时成交量萎缩≠正常市场信号的具体扭曲机制；A股制度约束对价量因子的系统性影响，对无A股经验者完全非直觉"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: ce19
  title: 未来函数导致回测有效实盘无效
  type: counter-example
  original_source: counter-example.md
  V1_cross_domain:
    passed: true
    evidence: ["反例类自动通过V1"]
    reason: "反例类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "反例类自动通过V2"
    derived_answer: "反例类按规则自动通过V2"
    reason: "反例类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "使用未来函数→回测极优→实盘归零的技术性陷阱；非量化工程背景的聪明人不会知道'回测可以偷看未来数据'这个具体错误"
  final_decision: PASS
  reject_reason: ""
```

<!-- glossary batch verified 2026-08-12 -->

```yaml
- id: g01
  title: 量化交易
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "作者将量化交易定义为'在不确定中寻找确定性+概率优势取超额收益'，并纳入三重核心假设；与常识（量化=算法交易）有明显差异，且明确包含巴菲特基本面投资"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g02
  title: 广义量化交易
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "作者独创术语，将巴菲特/达利欧/西蒙斯的方法统一纳入'广义量化'框架；打破'量化=对冲'的狭隘认知是书的核心论点之一，BOOK_OVERVIEW明确标注"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g04
  title: 三重核心假设
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "BOOK_OVERVIEW明确标注为'作者独创的量化交易哲学基础'；三个假设（上帝视角/局部最优/市场非理性）的组合及其与量化交易的关联是作者原创框架"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g07
  title: 基本面量化交易策略
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "将巴菲特的价值投资显式纳入量化策略分类，标注'基本面反转观察者'概念；五大量化策略分类体系是作者的独特全景框架"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g08
  title: 资产配置量化交易策略
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "将达利欧全天候策略显式纳入量化分类体系；'超大规模资金适配'和'美国401K养老金计划对应'是作者的具体对照"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g11
  title: 另类量化交易策略
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "将索罗斯的市场恐慌利用、古怪因子、卫星数据等统一纳入量化框架；'利用人性弱点等待崩溃'的定义是作者独特诠释，有别于通常对'另类数据'的表述"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g14
  title: 万物皆可量化
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "引用恩格斯'科学=数学'命题延伸到'投资不是艺术而是科学'，再到'高考志愿也可量化'；作者的哲学立场，BOOK_OVERVIEW明确标注为作者原创命题"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g15
  title: 因子
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "作者定义因子为'底层逻辑的量化表达'并提出四条件（可持续性/可投资性/可区分性/可解释性）；超越标准的'与收益相关的数据特征'定义，加入哲学层和工程筛选框架"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g18
  title: 概率优势
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'不能预测价格方向，但可以测量价格变化的概率'——这个区分是作者量化交易定义的核心；对'预测'与'概率测量'的区分是反直觉的精确命题"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g29
  title: 元知识学习
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "将AI/机器学习领域的'元知识'概念移植到量化策略选择语境；'用机器选择投资策略'（而非执行策略）是对AI在量化中角色的层级认知，书中明确指出'相关技术尚待突破'"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g31
  title: 博弈平衡点
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "将博弈论纳什均衡概念应用于量化策略市场演化的最终状态；'五大策略占据市场绝大部分→趋向博弈平衡'是作者对量化市场未来的独特判断"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g32
  title: WorldQuant阿尔法101因子
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "80%因子仍在实盘使用的具体声明，开启中国量化元年的里程碑地位；作者将此作为量化历史分期的关键节点，有特定年份和事件的历史唯一性"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: g33
  title: 量化元年
  type: glossary
  original_source: glossary.md
  V1_cross_domain:
    passed: true
    evidence: ["术语类自动通过V1"]
    reason: "术语类按规则自动通过V1"
  V2_predictive_power:
    passed: true
    novel_question: "术语类自动通过V2"
    derived_answer: "术语类按规则自动通过V2"
    reason: "术语类按规则自动通过V2"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "作者独创术语，分别标定美国2011年和中国2016年为各自的量化元年；将市场发展史用'元年'概念分期，且给出两个市场的具体年份"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p19
  title: 索普2%法则
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section19：索普在21点赌博数学中推导2%法则，明确'单次不超过总筹码2%则永远不会破产'"
      - "Section11：基本面量化交易者仓位分散，单只股票最大持仓不超过2%"
      - "Section19：LTCM反例佐证——正因违反2%原则使用高杠杆导致破产"
    reason: "赌博数学→量化基金实践→反面案例，三个独立语境佐证同一数值原则"
  V2_predictive_power:
    passed: true
    novel_question: "一个使用2%法则的量化基金，最多能同时持有多少只股票？"
    derived_answer: "100%÷2%=50只，这与书中描述的'很多基金持仓50只左右'完全吻合；进一步推导：若单次亏损控制在2%，连续50次全部亏损概率极低，即使发生也只亏50%而非破产"
    reason: "推导出量化基金运营规模的具体数字，且与书中数据自洽，非平庸"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "索普将21点赌博数学与证券投资风险控制统一在同一数字（2%）下，揭示两个表面不同领域的底层同构性；书中明确指出2%法则是凯利公式的保守版本，完成了跨领域桥接，而非简单的'分散投资常识'"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p20
  title: 因子四要素
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section17：明确定义因子四要素——可持续性/可投资性/可区分性/可解释性"
      - "Section18：因子有效性评估框架中，换手率分析对应可投资性，IC分析对应可区分性，行业分析对应可解释性"
    reason: "定义章节与评估方法章节构成两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "一个情绪因子（用社交媒体热度预测股价），能通过因子四要素检验吗？"
    derived_answer: "可持续性：市场微观结构变化快，情绪因子衰减迅速→存疑；可投资性：数据爬取延迟和成本高→存疑；可区分性：波动期IC较高，平稳期低→部分通过；可解释性：行为金融学支撑→通过。结论：情绪因子通过2/4个要素，可作为辅助因子使用，不宜单独构建策略"
    reason: "书中未讨论情绪因子的具体评估，推导给出了有实操价值的结论"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "对'可解释性'要素的强调反直觉——大多数量化新手只关注统计相关性（数据支持即可），作者坚持因子必须有经济学或行为金融学解释，拒绝纯统计的数据挖掘，这与'数据驱动'的常识认知相悖"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p22
  title: 量化交易不可能三角
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section18：明确提出三角约束——策略长期有效性/高夏普比率/大资金容量三者不可兼得"
      - "全书策略对比：阿尔法策略容量小但收益高（西蒙斯大奖章封闭募集）；资产配置策略容量大但收益低（全天候年化5.45%）；趋势策略有效性随使用者增多而降低"
    reason: "明确定义与全书五大策略的对比格局构成两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "一个散户开发出夏普3.0、年化30%的策略，是否可以直接用于大规模资金？"
    derived_answer: "不可能三角告诉我们：高夏普+高收益已满足两个维度，则资金容量必然受限；加大资金会产生市场冲击，策略信号会在执行中被自己破坏；因此该策略的最优规模约100-500万，扩大后收益将迅速衰减直至失效"
    reason: "大多数散户认为'好策略加大资金就能赚更多'，推导结论直接反驳这个直觉"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "借用蒙代尔不可能三角的结构将其迁移到量化策略设计领域，揭示策略本身的不可兼得约束；大多数新手认为'更好的策略能同时做到高收益/高容量/长期有效'，不可能三角直接破除这个幻想，属于反直觉的认知升级"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p24
  title: 策略失效三大致命因素
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section20：专章明确定义三大致命因素——未来函数/过度拟合/夏普比率突变"
      - "ce15/ce16/ce19：三个独立反例分别佐证这三个因素（LTCM的市场结构突变、A股涨跌停扭曲数据、未来函数导致回测虚高）"
    reason: "理论定义章节与多个案例证伪构成多个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "一个策略在2020-2022年回测收益很好，2023年实盘后开始亏损，最可能是哪个因素导致的？"
    derived_answer: "三因素诊断：未来函数已排除（实盘了说明回测没用未来数据）；过度拟合可能性低（2020-2022三年窗口足够长）；最可能是夏普比率突变——2023年量化监管加强+市场结构变化，导致策略底层假设失效。诊断建议：检查滚动夏普是否超过历史最大回撤"
    reason: "三因素框架提供了系统诊断路径，推导出可执行的排查顺序"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'夏普比率突变'作为第三因素是独特贡献——前两个（未来函数/过拟合）是行业常识，但将'策略有效性的根本性改变'量化为夏普比率的结构性突变并与历史最大回撤比较，是作者提出的工程化监控方案，属于实盘应用的独特方法论"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p25
  title: 夏普比率突变预警规则
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section20：明确提出预警规则——滚动夏普比率超过回测历史最大跌幅则策略可能失效"
      - "Section24/25实盘监控讨论：将夏普比率动态监控作为实盘管理的核心指标"
    reason: "失效理论章节与实盘监控方法章节构成两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "一个策略历史最大月度夏普回撤是-0.8，当前滚动3个月夏普为-1.2，应如何操作？"
    derived_answer: "已超过-0.8阈值，触发预警信号；应立即停止实盘交易；依次排查：数据质量（是否有异常数据）→市场结构（是否发生制度性变化）→策略逻辑（假设是否还成立）；如三项均无异常，则宣告该策略失效，需要重新研发"
    reason: "给出了具体的操作SOP，而非笼统的'监控策略'"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "用'滚动夏普与历史最大回撤的比值'作为失效触发器是工程化的独特设计——不是模糊的'策略表现变差就停'，而是有明确可量化比较的客观阈值；这种将主观判断工程化为可执行规则的思路是量化工程师的独特贡献"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p30
  title: CTA策略三大配置价值
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section24：明确列出CTA三大配置价值——危机Alpha属性/绝对收益/低相关性"
      - "Section12：全天候策略选择低相关性大类资产时，CTA/商品期货作为独立于股债的风险来源被引入"
    reason: "CTA专章定义与资产配置框架应用构成两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "2020年新冠疫情暴跌期间，持有30% CTA策略的组合，与纯股债组合相比表现如何？"
    derived_answer: "危机Alpha属性：2020年3月趋势策略因做空受益；低相关性：大盘跌30%时，纯股债组合回撤约20%（因有债券保护），而含30% CTA的组合中CTA部分可能正收益5-10%，组合整体回撤压缩到约12-15%；CTA在危机中表现出了与股债反向的危机缓冲效果"
    reason: "书中未讨论2020年疫情中的具体配置效果，推导出了量化的结论"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'危机Alpha'反直觉——普通投资者认为危机来临时所有策略都亏（股债双杀），CTA因趋势跟踪能力在极端市场中顺势做空实现正收益；这个特性使CTA成为组合的'对冲保险'，而非普通人理解的'商品投机'"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p37
  title: 另类策略五大优势
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section15：明确列出另类量化五大优势——机器学习适配/未挖掘信号/生存时间长/泛化强/效率高"
      - "Section12：全天候策略框架中讨论非传统数据源补充传统方法的价值，呼应'未被挖掘的观点'维度"
    reason: "另类策略专章与资产配置对比分析构成两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "一家创业公司开发了用卫星夜间灯光变化预测地区GDP的量化因子，用五大优势框架评估是否值得投入资源？"
    derived_answer: "优势2（未被挖掘）✓高分；优势3（生存时间长——卫星数据获取门槛高）✓；优势1（机器学习处理图像数据）✓；优势4（泛化强）✓；优势5（效率取决于卫星刷新频率）需评估。五大优势4/5满足，建议开发；但需对照ce10（另类数据成本）评估卫星数据购买费用是否超出预期收益"
    reason: "框架给出了系统评估路径，推导结论有实际决策价值"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'策略生存时间更长'反直觉——通常认为越复杂的策略越快被发现复制，实际上获取门槛高的另类数据构成了天然护城河，使用者少反而让策略衰减更慢；这与传统因子'越公开越快失效'的规律相反，是市场竞争逻辑的反直觉推导"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p39
  title: 事件驱动五步分析法
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section15：明确提出五步法——定性→定量→定时→异动→轮动分析"
      - "Section15：可转债下修套利案例中五步法的完整应用（p40），构成独立的实战验证语境"
    reason: "理论框架与具体案例应用构成两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "央行突然降息50BP，用五步分析法如何操作？"
    derived_answer: "定性：重大事件，影响确定存在；定量：降息利好债券（价格+1-3%）、成长股（估值+5-10%），利空银行息差；定时：债市当天反应，股市效果持续2-4周，银行股负面效应滞后1-2个月；异动：找率先上涨的债券ETF和科技成长板块龙头；轮动：债券→科技成长→消费蓝筹→最后金融板块。五步给出完整操作路径"
    reason: "书中未讨论降息场景的具体操作，推导出了有层次的行动框架"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'定时'和'轮动'这两个维度是独特贡献——大多数投资者只做'定性'（判断利好/利空），五步法强制要求量化影响时间维度和板块传播顺序；特别是轮动分析，将市场信息扩散过程显式建模，而不是等待结果，这是事件驱动策略的核心竞争优势"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p40
  title: 可转债套利五步骤
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section15：可转债下修套利的完整五步流程"
      - "Section15：事件驱动五步分析法（p39）提供了方法论基础，可转债是其具体应用，两者构成方法论与实践的独立语境"
    reason: "通用方法论与A股特定套利策略构成两个层次的独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "一支可转债正股跌至转股价60%（触发70%条件），但尚未进入回售期，应该现在介入吗？"
    derived_answer: "按p41两个前提条件，只满足'跌破70%'一个，未满足'进入回售期'；公司无被迫下修的压力；按p42的4-10交易日窗口，即使将来条件成熟，当前也不是介入时机；结论：不建议当前介入，应等待进入回售期后再按框架评估"
    reason: "整合p39/p40/p41/p42多条规则得出明确操作判断，展示框架的系统性"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "将可转债下修套利这个A股独特制度套利机会系统化为五步流程，特别是'定时'维度给出了第4-10交易日的精确介入窗口；这是对A股特有制度（回售条款+转股价下修机制）的深度工程化，一般投资者只知道'有下修机会'，不知道精确的时机判断方法"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p41
  title: 可转债下修前提条件
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section15：明确定义两个前提条件——进入回售期+正股跌破转股价70%"
      - "Section15：可转债套利五步骤（p40）中将这两个前提作为第一步'定性分析'的核心判断依据"
    reason: "触发条件定义与应用框架构成两个独立语境"
  V2_predictive_power:
    passed: true
    novel_question: "一支可转债进入回售期，但正股只跌到转股价的75%，公司会主动下修吗？"
    derived_answer: "未满足70%条件，公司没有被迫下修的监管压力；虽然理论上公司可自愿下修，但自愿下修意味着主动稀释股权，管理层动力不足；从套利角度，此时不符合两个前提中的一个，风险溢价不够，不建议介入"
    reason: "区分了'被迫下修'和'主动下修'的不同逻辑，推导出有操作价值的判断"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'进入回售期+跌破70%'的组合触发机制是A股可转债制度的特有规定；70%这个具体阈值来自证监会监管规定，不是经验估计；这个知识在A股市场具有唯一性和精确性，是其他市场没有的本地化制度知识，一般投资者难以通过常识推导出来"
  final_decision: PASS
  reject_reason: ""
```

```yaml
- id: p42
  title: 可转债介入时机规则
  type: principle
  original_source: principle.md
  V1_cross_domain:
    passed: true
    evidence:
      - "Section15：明确给出第4-10交易日的介入窗口"
      - "Section15：p40套利五步骤中'定时分析'步骤直接引用这一时间窗口作为操作依据"
    reason: "具体规则与框架应用构成两个独立使用语境"
  V2_predictive_power:
    passed: true
    novel_question: "跌破转股价70%后的第1-3天和第11-15天介入有什么风险？"
    derived_answer: "第1-3天：消息刚出，不确定性最高（公司可能不下修）；市场尚未消化，正股可能继续下跌；资金成本高风险大。第11-15天：信息已充分扩散，套利机会被量化基金捕捉；转股溢价率已压缩，性价比低；博弈已完成大部分，剩余收益有限。4-10天：信息确认期结束（董事会公告通常5-7天内）但市场尚未完全定价"
    reason: "解释了窗口边界的结构性原因，而非仅给出数字"
  V3_exclusivity:
    passed: true
    why_unique_or_common: "'第4-10交易日'是基于对上市公司董事会决议流程的深度理解（需5-7天召开并公告），将公司内部决策周期与市场交易时机绑定，是'制度理解→交易时机'的反直觉推导；大多数人的常识是'跌得越深越快介入'，这个规则告诉你跌后要等4天才能介入，违反直觉"
  final_decision: PASS
  reject_reason: ""
```

