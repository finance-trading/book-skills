# principles_p2.md

> 提取来源：chunks 5–8（约第 5 章尾声 ~ 第 8 章）
> 提取者：principle-extractor
> 提取条数：27

---

## 第 5 章 · 交易执行系统（尾声）

```yaml
- id: p01
  title: 单个指令不超过日均成交量的 1%
  type: rule
  source_chapter: 第 5 章 · 最小化交易成本
  source_quote: |
    "根据经验规则，单个指令的股数不宜超过平均日交易量的 1%。"
  summary: |
    为减小市场冲击，必须根据流动性限制指令规模。
    1% 是经验阈值——无论大盘股还是小盘股，一律适用。
    若达不到 1% 的门槛（如小盘股日均成交量极低），则不应交易该标的。
  tags: [rule, execution, market-impact, liquidity]

- id: p02
  title: 权重与市值四次方根成正比
  type: rule
  source_chapter: 第 5 章 · 最小化交易成本
  source_quote: |
    "最大大盘股的资本权重会是最小小盘股的 10 000 倍……在满足流动性条件下，这个权重比例不宜超过 10 倍。也就是说股票的资本权重与其市值的四次方根成正比。"
  summary: |
    决定指令规模时永远不要用线性比例方法（按市值线性分配资本）。
    线性比例会导致组合剔除绝大多数小盘股，失去分散化好处。
    用市值四次方根做权重，既保证分散化，又不违反流动性约束。
  tags: [rule, portfolio-construction, position-sizing]

- id: p03
  title: 避免交易低于 5 美元的股票
  type: rule
  source_chapter: 第 5 章 · 最小化交易成本
  source_quote: |
    "机构交易员不会交易任何一只价格低于 5 美元的股票。低价股票不仅会增加总佣金成本……还会有相对较高的买卖差价。"
  summary: |
    低价股票同时抬高佣金成本和流动性成本。
    对独立交易员而言，这是双重惩罚，必须规避。
  tags: [rule, execution, cost-minimization]

- id: p04
  title: 自动交易系统完成后必须先仿真交易
  type: checklist
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "仿真交易事实上是在不亏钱的情况下能够查找自动交易系统软件漏洞的唯一方法。"
  summary: |
    系统上线前的必做清单：
    1. 用仿真账户运行自动交易系统至少一个月
    2. 比较仿真交易盈亏与最新数据回测的理论盈亏
    3. 差异若非交易成本引起 → 大概率是软件漏洞
    4. 同时可发现前视偏差、数据迁就偏差、操作流程困难
    5. 估算真实交易成本、直观感受盈亏波动和资本使用
  tags: [checklist, testing, pre-launch]

- id: p05
  title: 业绩偏离预期的诊断顺序
  type: checklist
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "先从这个最简单的诊断开始：软件是否有漏洞？交易是否匹配？执行成本是否远高于预期？是否交易了流动性差的股票？"
  summary: |
    当实际业绩不如回测时，按以下顺序排查：
    1. 自动交易系统软件是否有漏洞？
    2. 自动交易生成的交易与回测程序生成的交易是否匹配？
    3. 执行成本是否远高于预期？
    4. 是否交易了流动性差的股票导致市场冲击？
    5. 以上排除后 → 检查数据迁就偏差（减少规则/参数，看回测是否崩溃）
    6. 最后才考虑状态转换（市场结构或宏观环境巨变）
    永远先排除简单原因，再面对复杂原因。
  tags: [checklist, debugging, diagnosis]

- id: p06
  title: 不要低估开盘前准备时间
  type: principle
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "不要低估开盘前准备指令所需的时间……如果你的策略需要开盘前 35 分钟之内的数据或新闻，你要么另建一个交易环境，要么修改策略。"
  summary: |
    每日开盘前需要下载、分析历史数据并传送指令，约需 35 分钟。
    如果策略依赖开盘前极短时间窗口的数据，操作上来不及执行。
    必须在仿真阶段测算出所需时间，否则只能放弃或修改策略。
  tags: [principle, operations, time-management]
```

---

## 第 6 章 · 资金和风险管理

```yaml
- id: p07
  title: 优化目标：长期财富最大化，先避免破产
  type: principle
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "我们的优化目标是长期财富最大化……这个目标意味着一定要避免赔光（净值为零或负数）。这是因为，如果在未来某时点赔光的概率大于零，则长期财富必然为零。"
  summary: |
    所有资金管理的最高原则：先活下来，再谈增长。
    破产概率 > 0 → 长期增长率必然为 0。
    任何策略、任何杠杆，都必须以保证不破产为前提。
  tags: [principle, capital-management, survival-first]

- id: p08
  title: 用凯利公式计算最优杠杆，实际操作用半凯利
  type: rule
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "由于参数估计存在误差，加上收益率不一定完全服从正态分布，交易员出于安全的考虑，所使用的杠杆只有最优杠杆的一半。这就是'半凯利'投机。"
  summary: |
    凯利公式给出理论最优杠杆 F* = C⁻¹M。
    但由于参数估计误差和收益率非正态分布，必须打折使用。
    规则：实际杠杆 = 凯利最优杠杆 × 0.5（半凯利）。
    若半凯利仍超过最大历史亏损下能承受的最大杠杆，取两者中较小值。
  tags: [rule, kelly-criterion, leverage, risk-management]

- id: p09
  title: 风险总是减少长期增长率
  type: principle
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "此处的教训是，风险总是可以减少长期增长率——由此可见风险管理的重要性！"
  summary: |
    几何平均收益率（复合增长率）总是小于算术平均收益率。
    波动率越高，复合增长率的损失越大（g = r + m - s²f/2）。
    这不是"可能"减少，而是"总是"减少——数学必然。
  tags: [principle, volatility-drag, compounding]

- id: p10
  title: 止损对均值回归策略有害
  type: rule
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "止损只有在惯性（趋势）状态时，才是有益的。……如果市场在这段时间内是均值回归的，不过快的清仓才能最终弥补亏损。"
  summary: |
    止损并非万能的风险管理方法。
    均值回归策略中：止损让你在更极端的情况下清仓，与模型假设相违背。
    惯性（趋势）策略中：止损是有益的，因为价格可能继续朝不利方向运动。
    判断标准：价格波动是否有消息/基本面原因？有 → 惯性状态 → 可止损。
    无消息的流动性事件 → 均值回归状态 → 不应止损。
  tags: [rule, stop-loss, mean-reversion, momentum]

- id: p11
  title: 风险管理黄金法则：投资组合规模始终可控
  type: principle
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "风险管理的黄金法则是：任何时刻都要将投资组合的规模保持在可控范围内。"
  summary: |
    恐惧和贪婪都会导致过度杠杆化：
    - 恐惧时：追加资本试图挽回损失
    - 贪婪时：策略刚开始盈利就过快追加资本
    两种情况都是破产的前兆。
    唯一防御：无论何时，组合规模都在你能承受亏损的范围内。
  tags: [principle, risk-management, golden-rule, leverage]

- id: p12
  title: 亏损时逐步降杠杆，不要突然弃用模型
  type: rule
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "随着交易亏损的增大，除了逐渐降低模型的杠杆直到零，没有更多办法可以降低模型风险……这比突然弃用一个发生了很多挫折的交易模型要好。"
  summary: |
    模型发生连续亏损时，理性做法是：
    - 根据最新历史收益率均值和标准差，用凯利公式不断调整杠杆
    - 随着回溯期内历史均值降为零，凯利杠杆将自动调整为零
    - 永远不要因为短期挫折而情绪化地彻底弃用一个模型
  tags: [rule, drawdown-management, systematic-deleveraging]

- id: p13
  title: 请独立方复制回测结果以消除模型风险
  type: rule
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "请合作伙伴或咨询顾问独立地复制出你的回测结果来确保其有效性是很有帮助的。结果复制是科学研究中的常用做法，在金融研究中也是必不可少的。"
  summary: |
    模型风险的重要来源是回测程序中的各种偏差和错误。
    消除方法：让独立第三方复制你的回测结果。
    这是科学研究的标准做法，量化交易同样必须执行。
  tags: [rule, model-risk, verification, reproducibility]

- id: p14
  title: 恐惧时不要关闭模型，贪婪时不要加倍杠杆
  type: rule
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "许多交易员要承受彻底关闭模型的巨大压力。其他过度自信且轻率冒险的交易员会进行反向操作：他们会在亏损模型上加倍投注……这两种行为都是不理性的。"
  summary: |
    模型处于巨大持续回撤时：恐惧会驱动你关闭模型。
    模型运行良好时：贪婪会驱动你迅速增加杠杆。
    两种冲动都是非理性的，都是破产之路。
    正确做法：始终按照凯利公式管理资本配置和杠杆。
  tags: [rule, psychology, fear-and-greed, discipline]

- id: p15
  title: 大额亏损后不要急于修改策略参数
  type: rule
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "大额亏损后，交易员倾向于立刻修改策略中的某些参数……这样的修改是不明智的，因为可能带来其他尚未发生的大额亏损，或者消除许多现有的盈利机会。"
  summary: |
    代表性偏差让交易员给近期经验赋予过多权重。
    大额亏损后立刻修改参数 → 过拟合最近一次亏损 → 引入新问题。
    规则：如果你认为系统有缺陷并打算调整，必须对修改后版本进行充分回测，
    确保它在足够长的回测期内（而非仅仅过去几周）优于原系统。
  tags: [rule, psychology, overfitting, parameter-tuning]

- id: p16
  title: 从小额组合开始，逐步做好心理准备
  type: rule
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "可以先从小组合做起，逐渐做好心理准备、训练有素并获得对模型的信心。当你有足够的心理承受能力去应对每日盈亏波动……投资组合的实际业绩便将趋近策略的理论预期业绩。"
  summary: |
    心理训练的路径：小额资金起步 → 适应盈亏波动 → 建立对模型的信心 → 逐步扩大。
    不要一开始就满仓运行——心理准备不足会导致情绪化决策，
    使实际业绩严重偏离理论预期。
  tags: [rule, psychology, gradual-scaling, discipline]

- id: p17
  title: 拥有其他收入来源有助于交易稳定
  type: principle
  source_chapter: 第 6 章 · 资金和风险管理
  source_quote: |
    "若想慢速、谨慎地发展，拥有其他的收入来源或业务有助于保持财务和情绪的稳定。确实应该寻找一件事情来分散注意力。"
  summary: |
    独立交易员面临巨大心理压力。拥有其他收入来源可以：
    1. 减轻财务压力（不必靠交易养活自己）
    2. 分散注意力（避免过度关注盈亏）
    3. 防止因缓慢发展而引起的烦躁
    这是情绪稳定的基础设施，不是可有可无的"备胎"。
  tags: [principle, psychology, income-diversification]
```

---

## 第 7 章 · 量化交易专题

```yaml
- id: p18
  title: 只有均值回归或趋势状态下策略才能盈利
  type: principle
  source_chapter: 第 7 章 · 量化交易专题
  source_quote: |
    "只有当证券价格是均值回归的或趋势的，交易策略才能盈利。否则，价格是随机漫步的，交易将无利可图。"
  summary: |
    构建策略的第一步：判断在特定条件和特定时间段，
    价格究竟是均值回归的还是趋势的。
    若两者都不是 → 随机漫步 → 任何策略都无法盈利。
  tags: [principle, strategy-design, market-regime]

- id: p19
  title: 均值回归策略回测必须清除异常报价和存活偏差
  type: rule
  source_chapter: 第 7 章 · 量化交易专题
  source_quote: |
    "许多历史金融数据库中都包含报价错误，而这些错误常常会人为拔高均值回归策略的业绩……只有在彻底清除了虚构报价之后，才能够完全相信均值回归策略的回测业绩。"
  summary: |
    均值回归策略回测的两大陷阱：
    1. 异常报价（虚假价格）：策略"买入"虚构低价、"卖出"正常价格 → 虚假盈利
    2. 存活偏差：经历极端价格的股票被收购或破产 → 若不在数据库中，人为拔高回测
    必须在使用前彻底清除数据中的异常报价，并使用无存活偏差的数据库。
  tags: [rule, backtesting, data-quality, mean-reversion]

- id: p20
  title: 协整性不等于相关性
  type: principle
  source_chapter: 第 7 章 · 量化交易专题
  source_quote: |
    "两个价格序列的相关性实际上是指在一段时间内其收益率的相关性……正相关无法保证两只股票在长期内价格偏离不会越来越大。但是，如果两只股票在目前与未来都是协整的，它们的价格就不大可能会偏离。"
  summary: |
    配对交易员常把相关性误认为协整性，这是致命错误。
    - 相关性：短期（日/周）收益率的同向运动程度
    - 协整性：长期价格偏离是否会收敛
    两只股票可以协整但不相关（如 KO 和 PEP）。
    做配对交易（均值回归），必须用协整检验，不能用相关性。
  tags: [principle, cointegration, correlation, pairs-trading]

- id: p21
  title: 高频交易策略具有更高的夏普比率
  type: principle
  source_chapter: 第 7 章 · 量化交易专题
  source_quote: |
    "根据大数定律，交易的次数越多，收益率相对于均值的偏差就越小……由于高频交易策略具有更高的夏普比率，与高频策略相比，可使用的杠杆水平更高，高杠杆进而大大提高策略的净值收益率。"
  summary: |
    如果目标是获取高夏普比率，交易应当采取高频而非隔夜持仓。
    逻辑链：交易次数多 → 大数定律 → 日收益率波动小 → 夏普比率高 →
    可用更高杠杆 → 净值收益率更高。
    但高频交易对回测（交易成本敏感）和执行速度有极高要求，
    不适合初涉此领域的独立交易员。
  tags: [principle, high-frequency, sharpe-ratio, law-of-large-numbers]

- id: p22
  title: 高杠杆低贝塔组合优于低杠杆高贝塔组合
  type: rule
  source_chapter: 第 7 章 · 量化交易专题
  source_quote: |
    "在使用凯利杠杆的条件下，投资组合的长期复合增长率与夏普比率的平方成正比……由低贝塔值股票构成的投资组合往往风险较低、夏普比率较高。"
  summary: |
    提高收益率的两种方法：加杠杆 或 选高贝塔股票。两者不等价。
    选择低贝塔股票组合 + 加杠杆，因为：
    - 低贝塔组合风险更低、夏普比率更高
    - 复合增长率与夏普比率的平方成正比（而非与平均收益率成正比）
    但注意：真实收益率有厚尾特征，对低贝塔股票使用过高杠杆并不明智。
  tags: [rule, portfolio-construction, beta, leverage, sharpe-ratio]

- id: p23
  title: 只交易有实际经济意义的季节性策略
  type: rule
  source_chapter: 第 7 章 · 量化交易专题
  source_quote: |
    "交易者必须记住，只能交易那些有实际经济意义的季节性交易策略。"
  summary: |
    季节性策略的筛选标准：必须有实际经济逻辑支撑。
    例如：汽油期货夏季驾驶高峰前上涨、天然气夏季空调用电需求。
    没有经济逻辑的"日历效应"大概率是数据迁就偏差。
    且商品期货的季节性策略比股票市场更可靠（因为需求来自实体经济）。
  tags: [rule, seasonality, economic-logic, commodities]

- id: p24
  title: 均值回归策略用半衰期确定最优持有期
  type: rule
  source_chapter: 第 7 章 · 量化交易专题
  source_quote: |
    "半衰期可以用来确定均值回归头寸的最优持有期。由于所有的历史时间序列数据都可以被用来估计 θ，通过这种方法估计的半衰期比直接从交易模型中获得的半衰期更加可靠。"
  summary: |
    均值回归策略的最优持有期不应凭感觉设定。
    用 Ornstein-Uhlenbeck 公式拟合差价时间序列 → 得到半衰期 → 即期望持有天数。
    优势：所有历史数据都参与估计，比仅用交易触发日的样本更可靠。
  tags: [rule, mean-reversion, holding-period, ornstein-uhlenbeck]
```

---

## 第 8 章 · 结语：独立交易员能否成功？

```yaml
- id: p25
  title: 独立交易员的核心优势是"容量"
  type: principle
  source_chapter: 第 8 章 · 结语
  source_quote: |
    "关键就是'容量'……相比于 1 亿美元的账户，10 万美元的账户获得较高夏普比率要容易得多。许多简单可盈利的策略对小容量有效，但对于大型对冲基金，这些策略可能都不适用。"
  summary: |
    独立交易员打败机构的根本原因：小容量天然适合高夏普策略。
    大基金被迫使用大容量策略 → 持仓时间长 → 遭遇宏观不利变化 → 大额回撤。
    独立交易员可以交易小容量、短持仓策略 → 更高夏普 → 更快复合增长。
  tags: [principle, independent-trader, capacity, competitive-advantage]

- id: p26
  title: 独立交易员免受机构约束和干预
  type: principle
  source_chapter: 第 8 章 · 结语
  source_quote: |
    "基金管理层施加的各种各样约束……任何施加在最优化问题上的约束条件都会降低最优值。……当策略表现出盈利迹象时，这些管理层就会施加强大压力，要求你迅速扩大投资规模。一旦出现亏损，他们又可能要求你马上平仓。"
  summary: |
    机构的约束（禁止纯多头、要求行业中性、强制弃用亏损模型、
    盈利时强制扩规模）都会降低策略的最优收益率。
    独立交易员没有这些约束，交易环境更接近数学最优。
    关键前提：性格坚定，能坚持量化交易的基本原则。
  tags: [principle, independent-trader, institutional-constraints, optimization]

- id: p27
  title: 策略终将因竞争而失效，必须持续研发
  type: principle
  source_chapter: 第 8 章 · 结语
  source_quote: |
    "随着越来越多的交易员发现这些策略并且加入竞争，这些策略就会失去盈利潜力。你必须不断研究新的策略。"
  summary: |
    没有任何策略可以永远盈利。
    均值回归策略：竞争使套利机会逐步消失，收益率降至零。
    惯性策略：竞争缩短最优持有期，最终无法盈利。
    独立交易员必须把策略研发作为持续性的核心活动。
    每十年还会有突然的重大状态转换，导致某些策略突然死亡。
  tags: [principle, strategy-lifecycle, continuous-rd, competition]

- id: p28
  title: 不要对低贝塔股票使用过高杠杆
  type: rule
  source_chapter: 第 7 章 · 量化交易专题
  source_quote: |
    "所有这些都是基于收益率服从正态分布的假设……因为真实收益率的分布具有厚尾特征，对低贝塔值股票使用过高的杠杆并不是明智的。"
  summary: |
    虽然高杠杆低贝塔组合理论上更优，但前提是收益率正态分布。
    真实收益率具有厚尾特征（极端事件概率远高于正态分布预期）。
    规则：即使选择低贝塔 + 高杠杆路径，杠杆也不能超过
    "最大历史亏损下能承受的最大杠杆"。厚尾风险必须被尊重。
  tags: [rule, leverage, fat-tail, risk-limit]
```
