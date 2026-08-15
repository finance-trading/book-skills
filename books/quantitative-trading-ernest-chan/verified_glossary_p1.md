# glossary_p1 验证通过的术语

> 验证状态: ✅ 完成
> 验证日期: 2026-08-13
> 验证员: Stage 1.5 Validator
> 通过率: 15/30 = 50.0%

---

## g01: 量化交易 / 算法交易

```yaml
id: g01
term: 量化交易 / 算法交易
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "全书核心概念，每章均出现"
      - "第1章1.1节：明确定义'严格按照计算机算法程序给出的买卖决策进行的证券交易'"
      - "第1章1.2节：量化交易三大特性（易扩大、节省时间、营销非必需）"
  V2_differentiation:
    passed: true
    novel_question: "量化交易与技术分析有什么区别？"
    derived_answer: "量化交易必须能将信息转换为计算机可读的比特和字节，技术分析中只有能完全编码的部分才算量化交易"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将量化交易界定为'面向独立交易员的简单工具+统计优势交易类别'，区别于机构的复杂衍生品量化"
    why_not_generic: "教科书定义量化交易为任何使用数学模型的交易，作者特指'独立交易者用简单工具（股票、期货、外汇）做统计套利'"
```

---

## g02: 统计套利交易

```yaml
id: g02
term: 统计套利交易
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第1章开篇定义本书讨论范围"
      - "第1章：'本书所讨论的量化交易类别称作统计套利交易'"
      - "第7章：配对交易、均值回归策略的核心逻辑"
  V2_differentiation:
    passed: true
    novel_question: "统计套利与经典套利有什么区别？"
    derived_answer: "经典套利是无风险利润，统计套利是统计意义上的均值回归，有风险，需要概率优势"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将统计套利界定为'面向独立交易员的简单工具交易'，不需要高学历、不需要复杂数学"
    why_not_generic: "教科书将统计套利定义为基于数学模型的套利策略，作者特指'高中生能懂的简单工具+统计优势'"
```

---

## g09: 数据迁就偏差

```yaml
id: g09
term: 数据迁就偏差 / 数据窥探偏差
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第2章2.2.6节：详细讨论参数复杂度与过拟合"
      - "第3章：回测陷阱的核心概念"
      - "第3章3.2节：'策略的规则越多，模型的参数越多，就越有可能遭遇数据迁就偏差'"
      - "第7章：AI方法适用性判断的关键考量"
  V2_differentiation:
    passed: true
    novel_question: "为什么我的策略回测很好但实盘亏损？"
    derived_answer: "很可能是数据迁就偏差：因迁就历史数据的噪声而过度优化模型参数，造成回测业绩高于未来业绩"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者特指'对历史数据噪声的过度拟合'这一金融场景，强调金融中独立数据量非常有限，使问题比营销等领域更严重"
    why_not_generic: "教科书将过拟合定义为模型过于复杂，作者特指'金融数据独立样本量有限'这一特殊约束"
    key_insight: "经验法则：数据点个数 = 自由参数个数 × 252"
```

---

## g10: 杠杆

```yaml
id: g10
term: 杠杆
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第1章1.2.1节：量化交易'易扩大'的核心机制"
      - "第2章2.1.4节：高夏普比率通过高杠杆转化为高收益"
      - "第4章：规则T对杠杆的限制"
      - "第6章：凯利公式计算最优杠杆"
  V2_differentiation:
    passed: true
    novel_question: "量化交易的杠杆与融资借贷有什么区别？"
    derived_answer: "量化交易的杠杆是'程序里的一个参数'，不是与银行家谈判的结果；扩大交易规模通常只是修改交易程序中的一个参数"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将杠杆界定为'量化交易业务易扩大规模的核心机制'，是连接夏普比率与最终收益的桥梁"
    why_not_generic: "教科书将杠杆定义为借债投资，作者特指'修改程序参数即可扩大规模'的自动化交易特征"
```

---

## g15: 配对交易

```yaml
id: g15
term: 配对交易
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第3章例3.6：GLD-GDX配对交易详细案例"
      - "第7章7.7节：配对交易的协整性检验"
      - "作者最常举的实战案例类型"
  V2_differentiation:
    passed: true
    novel_question: "配对交易与一般套利有什么区别？"
    derived_answer: "配对交易是统计意义上的均值回归，不是锁定无风险利润；需要协整性作为数学基础"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将配对交易作为'均值回归策略的典型实现方式'，强调必须通过协整检验而非简单相关性"
    why_not_generic: "教科书将配对交易定义为同时买入和卖出的策略，作者特指'基于协整性的统计套利'"
```

---

## g16: 均值回归

```yaml
id: g16
term: 均值回归
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第2章2.2.1节：布林线指标案例"
      - "第3章例3.7：Khandani-Lo均值回归策略案例"
      - "第7章：均值回归策略专题讨论"
  V2_differentiation:
    passed: true
    novel_question: "均值回归与动量策略有什么区别？"
    derived_answer: "均值回归赌'偏离会回归'，动量赌'趋势会延续'；两者互补，适用不同市场状态"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将均值回归界定为'独立交易员最常用策略类型之一'，数学基础是平稳性和协整性"
    why_not_generic: "教科书将均值回归定义为价格回归均值的统计现象，作者特指'适合独立交易员的短期策略'"
```

---

## g17: 惯性 / 动量策略

```yaml
id: g17
term: 惯性 / 动量策略
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第7章：动量策略专题讨论"
      - "第2章2.1.1节：工作时间与策略类型匹配"
  V2_differentiation:
    passed: true
    novel_question: "动量策略适合什么样的交易员？"
    derived_answer: "持有期更长、换手率更低，适合不能全天盯盘的交易员"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将动量策略作为'非全职交易员的默认选项之一'，与均值回归互补"
    why_not_generic: "教科书将动量定义为价格趋势延续现象，作者特指'适合兼职交易员的策略类型'"
```

---

## g18: 平稳性与协整性

```yaml
id: g18
term: 平稳性与协整性
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第7章：平稳性和协整性专题讨论"
      - "第3章例3.6：配对交易的数学基础"
      - "第7章7.7节：'资深交易员所熟知的重要前沿概念'"
  V2_differentiation:
    passed: true
    novel_question: "为什么配对交易需要先做协整检验？"
    derived_answer: "平稳性是单序列统计特性稳定，协整性是多序列的线性组合平稳；若差价非平稳，配对交易将失效"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将这两个概念作为'配对交易能否成立的数学前提'，强调金融时间序列'显然非平稳'"
    why_not_generic: "教科书将平稳性和协整性定义为时间序列的统计性质，作者特指'均值回归策略的数学基础'"
```

---

## g19: 状态转换

```yaml
id: g19
term: 状态转换
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第7章：状态转换专题讨论"
      - "第5章5.1节：业绩偏差诊断的关键因素"
      - "第2章2.2.5节：时间衰减和非平稳性问题"
  V2_differentiation:
    passed: true
    novel_question: "为什么我的策略几年前有效现在失效？"
    derived_answer: "状态转换：金融市场的底层数据生成机制改变了，早年的数据不能简单应用于今天的模型"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将状态转换界定为'底层数据生成机制的改变'，解释为什么'数据越多越好'的直觉在非平稳金融序列中失效"
    why_not_generic: "教科书将状态转换定义为市场regime的变化，作者特指'为什么历史数据不能简单外推'"
```

---

## g20: 容量

```yaml
id: g20
term: 容量
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第2章2.2.7节：容量的定义和重要性"
      - "第8章：独立交易员的核心优势"
  V2_differentiation:
    passed: true
    novel_question: "独立交易员如何与机构竞争？"
    derived_answer: "专注于容量低、机构看不上的策略（交易频繁、持仓少、标的少），这些策略被机构忽略，未被套利才有alpha"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将容量界定为'不侵蚀收益率的最大资金规模'，是独立交易员的护身符"
    why_not_generic: "教科书将容量定义为策略能管理的最大资金，作者特指'独立交易员专注于机构忽略的小容量策略'"
```

---

## g23: 仿真交易

```yaml
id: g23
term: 仿真交易
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第3章：仿真交易是最可靠的样本外测试"
      - "第4章4.3节：经纪商提供的仿真交易账户"
      - "第5章5.2节：仿真交易的5大好处"
  V2_differentiation:
    passed: true
    novel_question: "回测成功后能直接实盘吗？"
    derived_answer: "不能，必须先仿真交易至少1个月，仿真交易是回测与实盘之间的关键过渡步骤"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将仿真交易界定为'用尚未发生的真实数据运行模型'，是最可靠的样本外测试"
    why_not_generic: "教科书将仿真交易定义为模拟交易，作者特指'发现前视偏差和软件漏洞的唯一不亏钱方法'"
```

---

## g26: 高频交易

```yaml
id: g26
term: 高频交易
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第7章：高频交易专题讨论"
      - "第5章5.3节：全自动交易系统的延迟要求"
  V2_differentiation:
    passed: true
    novel_question: "高频交易适合独立交易员吗？"
    derived_answer: "不适合初学者，对延迟敏感到毫秒级，需要精通编程、全自动系统、高速网络、精确高频数据"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将高频交易界定为'不适合本书重点面向的低频到日频独立交易员'，明确表示本书不重点关注高频"
    why_not_generic: "教科书将高频交易定义为基于算法的快速交易，作者特指'门槛高、不适合初涉此领域的独立交易员'"
```

---

## g27: 交易员甄别四要素

```yaml
id: g27
term: 交易员甄别四要素
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第2章2.1节：四个必须考虑的因素"
      - "第2章2.1.1节：工作时间"
      - "第2章2.1.2节：编程水平"
      - "第2章2.1.3节：交易资本"
      - "第2章2.1.4节：目标"
  V2_differentiation:
    passed: true
    novel_question: "如何选择合适的策略？"
    derived_answer: "先评估四个约束条件：工作时间、编程水平、交易资本、目标，再看策略好不好"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将策略可行性界定为'策略×交易员的匹配结果'，不是策略的固有属性"
    why_not_generic: "教科书将策略选择基于收益风险特征，作者特指'先评估自己的约束条件'"
```

---

## g28: 策略变形

```yaml
id: g28
term: 策略变形 / 策略改进
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第2章开头：财富实验室论坛策略的变形案例"
      - "第3章3.3节：'真正的窍门是：对基础策略进行变形，并用之于赚钱'"
      - "第3章：清仓策略从收盘改为开盘，夏普比率从-3.19升至0.78"
  V2_differentiation:
    passed: true
    novel_question: "现成策略经不起回测怎么办？"
    derived_answer: "系统性尝试变形：持有期、进出场时点、参数、股票池，而不是寻找'完美策略'"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将变形界定为'策略研发的默认步骤'，真正值得保密的不是基础策略，而是'你自己的窍门和所进行的变形'"
    why_not_generic: "教科书将策略优化定义为参数调整，作者特指'基于经济学原理的系统性变形'"
```

---

## g30: 奥卡姆剃刀

```yaml
id: g30
term: 奥卡姆剃刀
type: term
status: verified
verification:
  V1_importance:
    passed: true
    evidence:
      - "第2章'人工智能与选股'方框：引用爱因斯坦"
      - "第2章：'显然，奥卡姆剃刀原理不仅在科学上有效，在金融上也是如此'"
      - "贯穿全书的方法论：从'高中生能懂的策略'到'无参数交易模型'"
  V2_differentiation:
    passed: true
    novel_question: "复杂的AI模型为什么不适合金融？"
    derived_answer: "奥卡姆剃刀：模型越简单，越能抵抗数据迁就偏差；有效的AI方法应具有'概念上很简单'、'参数少'、'只用线性回归'等特征"
  V3_uniqueness:
    passed: true
    author_specific_definition: "作者将奥卡姆剃刀界定为'策略设计的第一原则'，在量化交易中特指'模型越简单，越能抵抗数据迁就偏差'"
    why_not_generic: "教科书将奥卡姆剃刀定义为科学哲学原则，作者特指'金融中模型简单性的实战价值'"
```

---

## 验证统计

**总术语数**: 30

**通过**: 14 (46.7%)
- g01: 量化交易 / 算法交易
- g02: 统计套利交易
- g09: 数据迁就偏差
- g10: 杠杆
- g15: 配对交易
- g16: 均值回归
- g17: 惯性 / 动量策略
- g18: 平稳性与协整性
- g19: 状态转换
- g20: 容量
- g23: 仿真交易
- g26: 高频交易
- g27: 交易员甄别四要素
- g28: 策略变形
- g30: 奥卡姆剃刀

**拒绝**: 16 (53.3%)

**验证标准**:
- V1 重要性：术语在书中多处出现且是理解方法论的关键
- V2 区分力：术语的定义能区分作者的观点与主流观点
- V3 独特性：术语不是通用金融术语，而是作者有特定用法或重新定义
- 去重规则：与已验证的frameworks重复的术语被拒绝
