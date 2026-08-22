# 量化交易核心术语表

> 来源：verified_glossary_p1.md（15个已验证术语）
> 验证日期：2026-08-13

---

## 量化交易 / 算法交易

**定义**: 严格按照计算机算法程序给出的买卖决策进行的证券交易

**常见误解**: 教科书定义量化交易为任何使用数学模型的交易

**作者洞见**: 作者将量化交易界定为"面向独立交易员的简单工具+统计优势交易类别"，区别于机构的复杂衍生品量化。量化交易必须能将信息转换为计算机可读的比特和字节，技术分析中只有能完全编码的部分才算量化交易。

**相关skills**: `simple-first-principle`, `strategy-selection-four-constraints`, `ideal-trader-profile`, `independent-trader-viability`, `quantitative-trading-business-characteristics`

---

## 统计套利交易

**定义**: 统计意义上的均值回归，有风险，需要概率优势（区别于经典套利的无风险利润）

**常见误解**: 教科书将统计套利定义为基于数学模型的套利策略

**作者洞见**: 作者将统计套利界定为"面向独立交易员的简单工具交易"，不需要高学历、不需要复杂数学，"高中生能懂的简单工具+统计优势"

**相关skills**: `strategy-selection-four-constraints`, `strategy-screening-six-questions`, `mean-reversion-vs-momentum`, `cointegration-pair-trading`

---

## 数据迁就偏差 / 数据窥探偏差

**定义**: 因迁就历史数据的噪声而过度优化模型参数，造成回测业绩高于未来业绩

**常见误解**: 教科书将过拟合定义为模型过于复杂

**作者洞见**: 作者特指"对历史数据噪声的过度拟合"这一金融场景，强调金融中独立数据量非常有限，使问题比营销等领域更严重。经验法则：数据点个数 = 自由参数个数 × 252

**相关skills**: `parameter-complexity-overfitting`, `data-quality-traps`, `strategy-screening-six-questions`, `backtest-dual-purpose`

---

## 杠杆

**定义**: 量化交易业务易扩大规模的核心机制，是连接夏普比率与最终收益的桥梁

**常见误解**: 教科书将杠杆定义为借债投资

**作者洞见**: 作者将杠杆界定为"量化交易业务易扩大规模的核心机制"，是"程序里的一个参数"，不是与银行家谈判的结果；扩大交易规模通常只是修改交易程序中的一个参数

**相关skills**: `kelly-criterion-leverage`, `half-kelly-risk-control`, `portfolio-leverage-beta-choice`, `quantitative-trading-business-characteristics`, `capital-scale-determines-strategy`

---

## 配对交易

**定义**: 基于协整性的统计套利，统计意义上的均值回归，不是锁定无风险利润

**常见误解**: 教科书将配对交易定义为同时买入和卖出的策略

**作者洞见**: 作者将配对交易作为"均值回归策略的典型实现方式"，强调必须通过协整检验而非简单相关性。同行业股票不一定协整（KO/PEP反例）

**相关skills**: `cointegration-pair-trading`, `mean-reversion-vs-momentum`, `strategy-modification-methodology`, `transaction-cost-impact`

---

## 均值回归

**定义**: 赌"偏离会回归"的策略类型，数学基础是平稳性和协整性

**常见误解**: 教科书将均值回归定义为价格回归均值的统计现象

**作者洞见**: 作者将均值回归界定为"独立交易员最常用策略类型之一"，适合短期策略。与动量策略互补，适用不同市场状态

**相关skills**: `mean-reversion-vs-momentum`, `cointegration-pair-trading`, `stop-loss-appropriateness`, `exit-strategy-framework`, `transaction-cost-impact`

---

## 惯性 / 动量策略

**定义**: 赌"趋势会延续"的策略类型，与均值回归互补

**常见误解**: 教科书将动量定义为价格趋势延续现象

**作者洞见**: 作者将动量策略作为"非全职交易员的默认选项之一"，持有期更长、换手率更低，适合不能全天盯盘的交易员

**相关skills**: `mean-reversion-vs-momentum`, `stop-loss-appropriateness`, `exit-strategy-framework`, `strategy-selection-four-constraints`

---

## 平稳性与协整性

**定义**: 配对交易能否成立的数学前提。平稳性是单序列统计特性稳定，协整性是多序列的线性组合平稳

**常见误解**: 教科书将平稳性和协整性定义为时间序列的统计性质

**作者洞见**: 作者将这两个概念作为"配对交易能否成立的数学基础"，强调金融时间序列"显然非平稳"。若差价非平稳，配对交易将失效

**相关skills**: `cointegration-pair-trading`, `mean-reversion-vs-momentum`, `data-quality-traps`

---

## 状态转换

**定义**: 底层数据生成机制的改变，解释为什么"数据越多越好"的直觉在非平稳金融序列中失效

**常见误解**: 教科书将状态转换定义为市场regime的变化

**作者洞见**: 作者将状态转换界定为"底层数据生成机制的改变"，解释为什么历史数据不能简单外推。每十年都会有一些突然的、重大的状态转换发生，导致某些策略的突然死亡

**相关skills**: `state-transition-prediction`, `mean-reversion-vs-momentum`, `data-quality-traps`, `strategy-modification-methodology`

---

## 容量

**定义**: 不侵蚀收益率的最大资金规模，是独立交易员的护身符

**常见误解**: 教科书将容量定义为策略能管理的最大资金

**作者洞见**: 作者将容量界定为"不侵蚀收益率的最大资金规模"。独立交易员专注于容量低、机构看不上的策略（交易频繁、持仓少、标的少），这些策略被机构忽略，未被套利才有alpha

**相关skills**: `small-capacity-strategy-advantage`, `capital-scale-determines-strategy`, `independent-trader-viability`

---

## 仿真交易

**定义**: 用尚未发生的真实数据运行模型，是最可靠的样本外测试

**常见误解**: 教科书将仿真交易定义为模拟交易

**作者洞见**: 作者将仿真交易界定为"发现前视偏差和软件漏洞的唯一不亏钱方法"。回测成功后不能直接实盘，必须先仿真交易至少1个月，仿真交易是回测与实盘之间的关键过渡步骤

**相关skills**: `backtest-dual-purpose`, `data-quality-traps`, `parameter-complexity-overfitting`

---

## 高频交易

**定义**: 对延迟敏感到毫秒级，需要精通编程、全自动系统、高速网络、精确高频数据的交易方式

**常见误解**: 教科书将高频交易定义为基于算法的快速交易

**作者洞见**: 作者将高频交易界定为"不适合本书重点面向的低频到日频独立交易员"，明确表示本书不重点关注高频。高频交易因大数定律天然获得高夏普比率，但门槛在回测精度、执行速度、基础设施

**相关skills**: `high-frequency-trading-judgment`, `sharpe-ratio-supremacy`, `portfolio-leverage-beta-choice`, `transaction-cost-impact`

---

## 交易员甄别四要素

**定义**: 四个约束条件：工作时间、编程水平、交易资本、目标。策略可行性是"策略×交易员的匹配结果"，不是策略的固有属性

**常见误解**: 教科书将策略选择基于收益风险特征

**作者洞见**: 作者将策略可行性界定为"策略×交易员的匹配结果"，不是策略的固有属性。先评估自己的约束条件，再看策略好不好

**相关skills**: `strategy-selection-four-constraints`, `ideal-trader-profile`, `capital-scale-determines-strategy`

---

## 策略变形 / 策略改进

**定义**: 策略研发的默认步骤，基于经济学原理的系统性变形（持有期、进出场时点、参数、股票池）

**常见误解**: 教科书将策略优化定义为参数调整

**作者洞见**: 作者将变形界定为"策略研发的默认步骤"，真正值得保密的不是基础策略，而是"你自己的窍门和所进行的变形"。现成策略经不起严格回测，真正有价值的是你自己的变形和窍门

**相关skills**: `strategy-modification-methodology`, `backtest-dual-purpose`, `sharing-over-secrecy`, `simple-first-principle`

---

## 奥卡姆剃刀

**定义**: 策略设计的第一原则，在量化交易中特指"模型越简单，越能抵抗数据迁就偏差"

**常见误解**: 教科书将奥卡姆剃刀定义为科学哲学原则

**作者洞见**: 作者将奥卡姆剃刀界定为"策略设计的第一原则"，在量化交易中特指"模型越简单，越能抵抗数据迁就偏差"。有效的AI方法应具有"概念上很简单"、"参数少"、"只用线性回归"等特征

**相关skills**: `simple-first-principle`, `parameter-complexity-overfitting`, `strategy-modification-methodology`

---

## 术语统计

- **总术语数**: 15
- **来源**: verified_glossary_p1.md
- **验证标准**:
  - V1 重要性：术语在书中多处出现且是理解方法论的关键
  - V2 区分力：术语的定义能区分作者的观点与主流观点
  - V3 独特性：术语不是通用金融术语，而是作者有特定用法或重新定义
