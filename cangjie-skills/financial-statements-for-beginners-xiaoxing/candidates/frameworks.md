- id: f01
  title: 经营-投资-融资三分法
  type: framework
  source_chapter: 资产负债表：企业的照相机
  source_quote: |
    虽然一家企业会做各种各样的事情，但是在会计看来，企业一辈子其实只做了三件事：经营、投资和融资。
  summary: |
    将企业纷繁交易先归入经营、投资、融资三类，再追踪每类活动如何改变现金、资产、负债和权益。以此建立跨行业、跨生命周期的统一分析坐标。
  tags: [mental-model, business-model, three-activities]

- id: f02
  title: 现金到现金循环
  type: framework
  source_chapter: 资产负债表：企业的照相机
  source_quote: |
    无论是什么行业的企业，都可以把日常经济活动抽象成一个过程。在这个从现金开始又回到现金的循环过程中，经营、投资、融资循环往复。
  summary: |
    把企业看成“现金→资源/生产→销售与应收→现金”的循环，而不是静态科目集合。分析时检查每个环节的转化速度、断点和资金来源。
  tags: [mental-model, cash-cycle, operations]

- id: f03
  title: 未来相关性分类
  type: framework
  source_chapter: 资产负债表：企业的照相机
  source_quote: |
    如果这笔钱可以换来一个对将来有用的东西，那它就是资产；如果这笔钱花完就完了，那它就是费用。
  summary: |
    面对一项支出先问“是否对未来有用”。未来有用的支出先作为资产并在以后摊销，无未来效用的支出当期费用化；再核查这种判断是否可靠。
  tags: [decision, accounting-judgment, future-value]

- id: f04
  title: 现金转换速度排序
  type: framework
  source_chapter: 资产负债表：企业的照相机
  source_quote: |
    各项流动资产在资产负债表中是按照它们各自转换为现金的速度来排序的。存货需要先变成应收账款，然后才能变成现金。
  summary: |
    用资产距离现金的步骤和时间评估流动性：现金最直接，应收账款次之，存货更慢。比较资产结构时，优先识别转化链条长、依赖销售或回款的项目。
  tags: [liquidity, asset-quality, mental-model]

- id: f05
  title: 会计恒等式与剩余求偿
  type: framework
  source_chapter: 资产负债表透露了什么信息
  source_quote: |
    资产等于负债加上股东权益，这就是资产负债表上最基础的逻辑关系。股东只有在公司还清债务后才能获得剩余利益。
  summary: |
    先用“资产=负债+权益”检查报表闭合，再从清偿顺序理解风险归属：债权人获得固定偿付，股东承担升值或贬值的剩余风险与收益。
  tags: [mental-model, balance-sheet, residual-claim]

- id: f06
  title: 时点与时段匹配
  type: framework
  source_chapter: 利润表：企业的摄像机
  source_quote: |
    资产负债表是一个时点的概念，而利润表则是一个时段的概念。资产负债表像照片，利润表像盈利状况的视频。
  summary: |
    先确认指标分子分母的时间维度，再进行比较。期末资产是快照，收入和利润是期间流量，避免把不匹配的时点数直接与时段数相除。
  tags: [reasoning, time-matching, financial-analysis]

- id: f07
  title: 收入费用与现金分离
  type: framework
  source_chapter: 利润表：企业的摄像机
  source_quote: |
    有收入不等于收到现金，收到了钱却可能没有收入；有费用也不等于要付出现金，付出了现金不一定会产生费用。
  summary: |
    将每笔交易分别问四个问题：是否确认收入、是否收现、是否确认费用、是否付现。用应收、预收、折旧和预付等项目解释利润与现金的错位。
  tags: [reasoning, accrual, cash-flow]

- id: f08
  title: 成本流转与库存识别
  type: framework
  source_chapter: 财务报表的诞生和内在逻辑
  source_quote: |
    生产成本首先被记录在资产负债表中的“存货”一项；随着存货被卖掉，生产成本才反映在利润表的营业成本中。
  summary: |
    追踪成本从投入到存货、再到销售成本的迁移。分析利润时同步观察库存变化，防止把尚未售出的生产投入误当成当期业绩。
  tags: [cost-flow, inventory, reasoning]

- id: f09
  title: 固定成本增量决策
  type: framework
  source_chapter: 财务报表的诞生和内在逻辑
  source_quote: |
    固定成本无论如何都不会发生变化，企业无论生产多少产品都必须支付固定成本；因此区分变动成本和固定成本会重大影响决策。
  summary: |
    接受订单或扩产时只比较新增收入与新增变动成本，固定成本在相关范围内视为既定。该框架帮助判断看似亏损的增量交易是否仍能减少总体亏损。
  tags: [decision, cost-structure, marginal-analysis]

- id: f10
  title: 库存驱动的毛利质疑
  type: framework
  source_chapter: 财务报表的诞生和内在逻辑
  source_quote: |
    毛利润的提升不一定由业绩提升引起，还有可能是产成品库存增加。如果库存积压的同时毛利润提升，这个毛利润其实不可信。
  summary: |
    看到毛利改善先对照销量、产量和库存。高固定成本行业中，过量生产会把固定成本留在存货、暂时抬高毛利；库存下降导致毛利下降也未必是坏事。
  tags: [diagnosis, earnings-quality, inventory]

- id: f11
  title: 三表联读恒等式
  type: framework
  source_chapter: 三张报表之间有何关联
  source_quote: |
    净利润和现金净流量之间的差额，永远等于资产负债表上除现金之外其他资产和负债的变化。
  summary: |
    用“利润-现金流=非现金资产与负债变动”联结三表。利润现金差异扩大时，拆解应收、存货、折旧、应付等科目，定位经营质量或会计确认原因。
  tags: [reasoning, three-statements, reconciliation]

- id: f12
  title: 同型分析基准化
  type: framework
  source_chapter: 活用三张报表，打通财务数据经脉
  source_quote: |
    资产负债表的同型分析为每个项目除以总资产，利润表的同型分析为每个项目除以营业收入。
  summary: |
    将资产负债表转换为资产结构百分比，将利润表转换为收入成本费用百分比，再比较不同规模企业或跨期结构变化，避免绝对额误导。
  tags: [analysis, normalization, benchmarking]

- id: f13
  title: 指标成组而非单指标
  type: framework
  source_chapter: 活用三张报表，打通财务数据经脉
  source_quote: |
    通过同型分析和比率分析企业的盈利能力、营运能力、短期偿债能力和长期偿债能力，才能打通财务数据经脉。
  summary: |
    把盈利、效率、短期偿债、长期偿债和投资回报放在同一组指标中交叉验证。单一比率异常只能生成问题，不能直接下结论。
  tags: [decision, ratio-analysis, triangulation]

- id: f14
  title: 周转率时间匹配
  type: framework
  source_chapter: 活用三张报表，打通财务数据经脉
  source_quote: |
    资产负债表上的项目是时点数据，利润表表现一段时期的数据；实际计算周转率，应以期初与期末资产的平均值计算更为准确。
  summary: |
    计算周转率时用期间收入或成本除以平均资产，而不是机械使用期末余额；再将周转次数换算成天数，识别采购、销售、回款的现金周期。
  tags: [analysis, turnover, time-matching]

- id: f15
  title: 现金流八象限生命周期
  type: framework
  source_chapter: 控制风险的要诀
  source_quote: |
    现金流量表按经营、投资、融资三项活动，将企业分成8类；不同状态的企业处在不同发展阶段，具有不同风险特性。
  summary: |
    用经营、投资、融资现金流的正负组合形成八种状态，再结合初创、成长、成熟、衰退生命周期解释。正负号只提示阶段，必须继续追问来源和持续性。
  tags: [framework, cash-flow, lifecycle, risk]

- id: f16
  title: 经营现金流优先级
  type: framework
  source_chapter: 控制风险的要诀
  source_quote: |
    在经营、投资、融资三种现金流中，经营活动的现金流是最稳定、最可靠的，因此把经营活动现金流放在最前面。
  summary: |
    评价现金质量时先看主营经营是否造血，再看投资回报和融资补充。经营现金流为负时，融资或资产处置不能被视为可持续改善。
  tags: [risk, cash-generation, prioritization]

- id: f17
  title: 投资规模与节奏压力测试
  type: framework
  source_chapter: 控制风险的要诀
  source_quote: |
    投资风险不仅来源于投资方向，也取决于是否能控制投资规模和节奏，使资金保持在相对安全的范围之内。
  summary: |
    对扩产或新项目同时压力测试投资规模、回收周期、经营现金和融资能力。即使方向正确，若前期现金流出超过可承受支撑，仍会造成资金链断裂。
  tags: [decision, investment, liquidity-risk]

- id: f18
  title: 行业五力盈利诊断
  type: framework
  source_chapter: 找出影响财务数据的因素
  source_quote: |
    五种力量决定行业盈利能力：供应商议价能力、购买者议价能力、潜在竞争者进入、替代品威胁和行业内竞争。
  summary: |
    先用五力扫描行业利润空间和议价权，再解释企业毛利、周转和现金流。把外部竞争约束纳入财务数据解读，避免脱离行业基准评价公司。
  tags: [strategy, five-forces, industry-analysis]

- id: f19
  title: 环境-战略-执行三层归因
  type: framework
  source_chapter: 找出影响财务数据的因素
  source_quote: |
    企业决策和经济活动至少受三方面影响：外部环境存在差异，企业战略定位不同，战略执行能力也影响现状及未来发展。
  summary: |
    解释财务差异时依次检查行业环境、战略选择和执行能力。相同环境可能因战略不同而分化，相同战略又可能因执行差异产生完全不同结果。
  tags: [reasoning, strategy, execution]

- id: f20
  title: 效益-效率战略取舍
  type: framework
  source_chapter: 怎样的公司才算是好公司
  source_quote: |
    奉行成本领先战略，意味着选择效率并在一定程度上牺牲效益；选择差异化战略，意味着在一定程度上放弃效率而主抓效益。
  summary: |
    将总资产回报拆成效益（利润率）与效率（周转率），识别企业是在低毛利高周转还是高毛利低周转上取胜。两头都弱通常指向执行问题。
  tags: [strategy, profitability, efficiency]

- id: f21
  title: ROIC-WACC经济利润门槛
  type: framework
  source_chapter: 怎样的公司才算是好公司
  source_quote: |
    投资资本回报率的及格线应该是投资资本成本；用投资资本回报率减去投资资本成本，得到超额收益率。
  summary: |
    用税后营业净利润/投资资本得到 ROIC，再与加权平均资本成本 WACC 比较。ROIC>WACC 才创造正经济利润，不能以净利润为正替代价值判断。
  tags: [valuation, capital-allocation, ROIC, WACC]

- id: f22
  title: 机会成本与资本成本
  type: framework
  source_chapter: 怎样的公司才算是好公司
  source_quote: |
    股东把钱投给一家企业，也就意味着放弃把钱投给另一家企业；他在另一家公司可能赚到的钱就是机会成本。
  summary: |
    评估资本成本时把股东放弃的同风险替代回报纳入，并将债务成本和权益成本按资本占比加权。没有显性分红不代表股东资金没有成本。
  tags: [mental-model, opportunity-cost, capital-cost]

- id: f23
  title: 财务杠杆双刃剑
  type: framework
  source_chapter: 怎样的公司才算是好公司
  source_quote: |
    总资产报酬率×权益乘数=净资产报酬率；多借钱提高权益乘数，只有在借钱后总资产报酬率不下降时才有效。
  summary: |
    将股东回报拆解为企业整体回报和权益乘数，先判断新增债务能否带来不低于原水平的资产回报，再决定加杠杆，避免借钱放大亏损。
  tags: [decision, leverage, ROE]

- id: f24
  title: 利润与现金流的风险收益取舍
  type: framework
  source_chapter: 三张报表之间有何关联
  source_quote: |
    当一家企业遭遇巨大风险时，关注风险是第一位的，现金流更重要；当经营活动风险可控时，利润就显得更为重要。
  summary: |
    不把“利润重要”或“现金为王”当成固定口号。先评估行业替代、周期和经营风险，再决定当前优先保护现金生存还是追求利润增长。
  tags: [decision, risk-return, cash-flow]

- id: f25
  title: 利润可持续性拆解
  type: framework
  source_chapter: 利润表：企业的摄像机
  source_quote: |
    利润表不仅告诉企业今年赚了多少钱、从哪里赚的，还能在区分可持续和不可持续项目的基础上推测未来收益。
  summary: |
    将营业利润与营业外收入、补贴和资产处置收益分开，优先依据可重复的主营来源预测未来，避免一次性收益支撑的利润被高估。
  tags: [earnings-quality, forecasting, analysis]
