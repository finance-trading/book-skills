- id: ce01
  title: 拆分抵债与回购把亏损变盈利
  type: counter-example
  source_chapter: 引言：会计是什么？
  source_quote: |
    先用价值3000万元的房子抵掉1.6亿元贷款，再用1.6亿元现金把房子买回来，账面上把1亿元亏损变成盈利。
  failure_mode: |
    把一项经济上的还债行为拆成抵债和回购两笔交易，借出售资产确认收益来粉饰当期利润。
  mechanism: |
    出售资产会影响利润表，购买资产却不会产生当期费用；交易结构因此制造了账面收益和被抬高的资产价值，虽然现金和债务的经济实质没有改善。
  warning_signs:
    - 亏损年度出现异常大额资产处置收益
    - 处置后短期内以高价回购同一资产
    - 账面资产价值远高于可验证的市场或历史成本
  bound_to:
    - 会计选择与报表包装识别
    - 经济实质重于账面利润
  tags: [counter-example, accounting-judgment, earnings-quality]

- id: ce02
  title: 历史成本缺乏支撑却虚增资产
  type: counter-example
  source_chapter: 历史成本有哪些含义？
  source_quote: |
    种树其实只花了3000万元，其他5.7亿元都是虚增资产。
  failure_mode: |
    在没有真实支出或交易凭证的情况下，把项目或资源包装成巨额资产，导致收购方按虚假家底支付对价。
  mechanism: |
    历史成本要求资产以取得时实际付出的金额入账；若账面金额无法由付款、合同、产权和工程记录支持，资产就缺少确认基础，净资产和估值都会被高估。
  warning_signs:
    - 资产账面额与累计投入严重不匹配
    - 土地、项目或工程缺少付款和产权证据
    - 管理层无法解释资产形成成本
  bound_to:
    - 历史成本原则
    - 收购前资产核验
  tags: [counter-example, due-diligence, inflated-assets]

- id: ce03
  title: 卖出再买回资产制造增值
  type: counter-example
  source_chapter: 历史成本有哪些含义？
  source_quote: |
    一家公司把自己的一项资产卖出去了，过了一个星期，它又把这项资产买回来了。
  failure_mode: |
    通过缺乏实质变化的循环交易重置资产历史成本，制造资产升值或处置收益的表面改善。
  mechanism: |
    历史成本下资产没有新交易通常只能减值不能增值；卖出并回购让企业取得新的入账价格，但资产的使用价值和风险可能并未改变。
  warning_signs:
    - 同一资产短期内反复买卖
    - 交易对手与企业存在关联关系
    - 交易价格明显偏离独立估值或现金用途不合理
  bound_to:
    - 历史成本下的交易重置
    - 关联交易与资产循环识别
  tags: [counter-example, related-party, asset-valuation]

- id: ce04
  title: 关联方占用资金伪装成其他应收款
  type: counter-example
  source_chapter: 孤立的资产怎么组成鲜活的企业？
  source_quote: |
    这里所谓的“借”事实上是一种“拿”，是占用。因此，这笔钱又被称为“占用资金”。
  failure_mode: |
    关联方把公司现金长期占用，企业却把它记录为其他应收款，形成看似可收回、实则缺乏正常回款安排的资产。
  mechanism: |
    其他应收款增加会暂时维持资产负债表平衡，但不产生主营收入或现金；关联方偿付能力和意愿不足时，资产减值会突然侵蚀利润与流动性。
  warning_signs:
    - 其他应收款规模远超员工备用金等正常用途
    - 余额集中于关联方或长期挂账
    - 缺少利息、担保、期限和实际还款记录
  bound_to:
    - 资产结构反推商业模式
    - 应收账款压力扫描
  tags: [counter-example, related-party, cash-occupation]

- id: ce05
  title: 把租用和代销财物误当成自有资产
  type: counter-example
  source_chapter: 哪些概念容易与资产混淆？
  source_quote: |
    办公楼是陆玲公司租用的，不归陆玲公司所有；代销产品也不能算是陆玲公司的资产。
  failure_mode: |
    看到实物就把它计入企业资产，忽略所有权、控制权和未来经济利益归属，造成资产规模和抵押能力的误判。
  mechanism: |
    资产不是“看得见的东西”，而是企业控制的未来经济利益；租赁物和代销品的主要权利义务属于他人，不能直接当作企业可支配资源。
  warning_signs:
    - 资产盘点与产权、租约或代销合同不一致
    - 资产余额很大但企业无法自由处置
    - 抵押或出售需要第三方同意
  bound_to:
    - 资产结构反推商业模式
    - 收购前资产核验
  tags: [counter-example, asset-recognition, ownership]

- id: ce06
  title: 一次性费用化长期合同制造亏损
  type: counter-example
  source_chapter: 孤立的资产怎么组成鲜活的企业？
  source_quote: |
    球队把1亿美元全部记入当年的费用，从而导致当年亏损；这1亿美元应该记入长期待摊费用。
  failure_mode: |
    把跨多年受益的合同支出一次性计入当期费用，以夸大当年亏损或为压低薪酬、估值和分红寻找借口。
  mechanism: |
    支出受益期与费用确认期不匹配会扭曲利润；将长期受益集中到当期，使后续期间利润虚高，并掩盖真实经营能力。
  warning_signs:
    - 大额合同支出与受益期限明显不匹配
    - 当期亏损但现金支出对应多年服务或权利
    - 同行业同类合同采用完全不同的摊销口径
  bound_to:
    - 费用资本化与摊销时点
    - 报表异常的利益相关者核查
  tags: [counter-example, expense-timing, accounting-policy]

- id: ce07
  title: 通过组织结构把自研技术资本化
  type: counter-example
  source_chapter: 研发支出对财务报表产生了什么影响？
  source_quote: |
    有些公司的研发部门是独立的法人，必须向自己的研发部门购买技术，这项技术就变成了外购技术。
  failure_mode: |
    通过设立关联研发法人再回购技术，把本应费用化的自研投入包装为外购无形资产，短期抬高资产和利润。
  mechanism: |
    会计处理取决于交易形式和能否证明未来效用；组织结构改变了“自研”与“外购”的记录路径，却不必然改变技术的商业价值或成功概率。
  warning_signs:
    - 无形资产主要来自关联方技术采购
    - 研发部门与母公司高度依赖、交易定价不透明
    - 资本化金额增长快于产品收入或订单
  bound_to:
    - 研发支出的不确定性
    - 费用化与资本化边界
  tags: [counter-example, R-and-D, related-party]

- id: ce08
  title: 增产不增销把固定成本留在存货
  type: counter-example
  source_chapter: 固定成本“搞出”了什么乱子？
  source_quote: |
    今年生产2000件却只卖掉1000件，营业成本从2000万元降到1500万元，毛利润反而增加500万元。
  failure_mode: |
    在需求不足时过量生产，把尚未售出的固定成本留在存货中，利用成本结转时点制造毛利改善的假象。
  mechanism: |
    固定成本被更多产品分摊，只有已售部分进入营业成本；毛利上升并不代表销量或现金改善，库存积压最终可能减值并反转利润。
  warning_signs:
    - 毛利上升同时产量增速显著高于销量
    - 产成品库存和库龄同步上升
    - 经营现金流没有随利润改善
  bound_to:
    - 固定成本分摊造成的利润幻觉
    - 存货积压核查
  tags: [counter-example, inventory, gross-margin]

- id: ce09
  title: 赊销把存货风险转成坏账风险
  type: counter-example
  source_chapter: 造纸企业的财务数据经历了怎样的动态变化？
  source_quote: |
    把存货变为应收账款也许是一件好事，但也有可能是一件彻头彻尾的坏事。关键就在于，应收账款能不能收回来。
  failure_mode: |
    为应对竞争不断放宽信用，把卖不动的存货转成应收账款，却把客户违约和坏账风险推迟到未来。
  mechanism: |
    赊销能暂时减少库存并确认收入，但没有带来现金；当客户议价能力强或需求恶化时，应收账款回收周期拉长，坏账和减值会吞噬先前利润。
  warning_signs:
    - 应收账款增长快于收入和现金回款
    - 回款期限、折扣和坏账率持续放宽
    - 存货下降但经营现金流没有改善
  bound_to:
    - 回款后才算真正赚钱
    - 应收账款压力扫描
  tags: [counter-example, credit-sales, receivables]

- id: ce10
  title: 用单一流动比率标准误判破产风险
  type: counter-example
  source_chapter: 一家公司的短期偿债能力怎么样？
  source_quote: |
    如果一家企业的老板看到自己公司的流动比率为2，就误以为自己的公司很安全，那后果无疑相当严重。
  failure_mode: |
    把流动比率2或所谓3到4的经验阈值当成跨行业、跨国家的安全线，忽略负债结构、融资习惯和资产变现质量。
  mechanism: |
    流动资产未必能立即变现，中国企业还可能借新债还旧债；同一比率在不同制度、行业和现金循环下对应完全不同的偿债风险。
  warning_signs:
    - 只报告比率不拆分短期借款和经营性负债
    - 存货、应收账款占流动资产比重很高
    - 依赖滚动融资而非经营现金偿债
  bound_to:
    - 指标成组而非单指标
    - 情境化偿债分析
  tags: [counter-example, liquidity, ratio-misuse]

- id: ce11
  title: 用长期资产变现假设衡量长期偿债
  type: counter-example
  source_chapter: 一家公司的长期偿债能力怎么样？
  source_quote: |
    如果一家公司连自己的厂房、设备、办公室和品牌全都变卖了，那它一定不是想还债，而是想关门。
  failure_mode: |
    机械套用“长期资产除以长期负债”来判断长期偿债，假定企业会出售核心生产资产还债，得出脱离经营现实的结论。
  mechanism: |
    长期负债通常靠持续经营产生的利润、现金和再融资偿还；变卖核心资产会摧毁经营能力，因此资产处置价值不能替代持续偿债能力。
  warning_signs:
    - 偿债分析只看资产覆盖倍数
    - 没有利息保障倍数和经营现金流分析
    - 抵押资产是企业维持收入所必需的核心资产
  bound_to:
    - 长期偿债与利息保障分析
    - 经营现金流优先级
  tags: [counter-example, solvency, ratio-misuse]

- id: ce12
  title: 用净利润除利息重复计算偿债能力
  type: counter-example
  source_chapter: 一家公司的长期偿债能力怎么样？
  source_quote: |
    净利润本身就是一个扣除了利息的结果，用净利润除以利息，就是计算在还完利息之后，企业赚的钱还可以再还几次利息。
  failure_mode: |
    用已经扣除利息和所得税的净利润去除以利息，虚构一个看似稳健的利息覆盖指标。
  mechanism: |
    分子已承担利息成本，再除以利息会重复扣除；正确的覆盖逻辑应回到息税前收益，匹配偿付利息之前可用于还息的利润。
  warning_signs:
    - 指标定义没有说明分子是否扣除利息和税
    - 利息覆盖倍数与 EBIT/利息结果不一致
    - 净利润很低却声称利息保障很高
  bound_to:
    - 利息保障倍数计算
    - 指标成组而非单指标
  tags: [counter-example, interest-coverage, ratio-misuse]

- id: ce13
  title: 用期末资产直接除期间收入
  type: counter-example
  source_chapter: 一家公司的营运能力怎么样？
  source_quote: |
    资产负债表上的项目通通是时点数据，而利润表则表现了一段时期的数据；二者是不匹配的。
  failure_mode: |
    把全年收入或成本直接除以某个期末资产余额，忽略分母在期间内的变化，导致周转率和周转天数失真。
  mechanism: |
    流量与存量的时间维度不同；期末余额可能受季节性、并购或年末突击交易影响，不能代表全年占用，应使用期初期末平均值并结合趋势。
  warning_signs:
    - 季节性行业周转率年度波动异常
    - 期末资产突然大增或大减
    - 报告没有披露平均资产口径
  bound_to:
    - 时点与时段匹配
    - 周转率时间匹配
  tags: [counter-example, turnover, time-matching]

- id: ce14
  title: 只看净现金增加额掩盖融资依赖
  type: counter-example
  source_chapter: 现金流量表为什么存在？
  source_quote: |
    A、B两家公司净现金流都为1000万元，但A靠经营造血，B靠融资弥补经营和投资缺口。
  failure_mode: |
    看到现金余额或净现金流为正就判断企业健康，不拆分经营、投资和融资现金的来源。
  mechanism: |
    借款或股权融资可以掩盖经营现金流为负；融资一旦收紧，原本的净现金增长无法持续，企业会同时面对偿债和经营缺口。
  warning_signs:
    - 净现金为正但经营现金流连续为负
    - 融资流入覆盖采购、工资或利息
    - 现金增长主要来自借款或增发
  bound_to:
    - 现金流来源质量
    - 经营现金流优先级
  tags: [counter-example, cash-flow, funding-risk]

- id: ce15
  title: 无投资计划仍大量融资导致闲钱或掏空
  type: counter-example
  source_chapter: 各种现金流都为正的企业是不是好企业？
  source_quote: |
    有些企业此时的融资行为蕴藏着不良动机，它可能准备把这些钱转给一些关联企业，这也就是企业掏空行为。
  failure_mode: |
    在经营和投资现金流都为正、没有明确项目时仍大额融资，把闲置资金低效持有或转给关联方。
  mechanism: |
    无投资用途的融资不能提升经营回报，闲置现金会稀释盈利；关联方占用则把股东资金变成难以回收的风险资产。
  warning_signs:
    - 融资规模与已披露投资计划不匹配
    - 现金长期闲置且收益率低于资本成本
    - 融资后关联方应收款快速增加
  bound_to:
    - 现金流八象限生命周期
    - 关联交易与资产循环识别
  tags: [counter-example, financing, tunneling]

- id: ce16
  title: 方向正确却扩张过快引发资金链断裂
  type: counter-example
  source_chapter: 投资活动现金流为负的企业要关注什么？
  source_quote: |
    这家方便面企业主业经营仍很好，却因为投资规模扩张太快而破产，账户里只剩下3000元。
  failure_mode: |
    因主业成功就快速扩大产能，忽视投资回收周期和现金支撑能力，把正确方向变成流动性危机。
  mechanism: |
    投资在产生效益前持续消耗现金；若经营现金和融资能力不足以覆盖高峰期支出，资金链会先于利润恶化，迫使企业停摆或破产。
  warning_signs:
    - 资本开支增速远超经营现金流增速
    - 项目投产和回款周期长于短期债务期限
    - 现金余额下降而仍持续开工扩产
  bound_to:
    - 投资规模与节奏压力测试
    - 现金流扩张与资金链分析
  tags: [counter-example, investment, liquidity-risk]

- id: ce17
  title: 把资产处置现金流当成可持续投资收益
  type: counter-example
  source_chapter: 经营活动现金流为负的企业怎么样？
  source_quote: |
    如果现金流入属于处置资产，企业并没有找到一个能带来持续现金流入的项目，而只是处置了盈利状况不好的资产。
  failure_mode: |
    看到投资活动现金流为正就当作投资能力改善，忽略现金来自出售资产或一次性金融交易。
  mechanism: |
    资产处置是消耗存量换取现金，不会重复发生；若经营现金流仍为负，处置只能延缓而不能解决造血不足，甚至削弱未来收入能力。
  warning_signs:
    - 投资现金流入主要来自固定资产或股权处置
    - 处置后资产规模和产能持续下降
    - 投资收益与经营现金流方向相反
  bound_to:
    - 现金流来源质量
    - 现金流八象限生命周期
  tags: [counter-example, asset-sale, cash-flow]

- id: ce18
  title: 衰退期继续扩产越投越快
  type: counter-example
  source_chapter: 经营活动现金流为负的企业怎么样？
  source_quote: |
    企业经营走向衰退多半是因为竞争太过激烈、市场供大于求，这时候投得越多，公司死得越快。
  failure_mode: |
    在销售和经营现金流恶化、市场供过于求时仍用投资扩大产能，试图靠更多供给挽救衰退业务。
  mechanism: |
    需求不足时新增产能不能转化为销售，反而增加折旧、库存和融资压力；投资现金流出加速消耗现金，使转型和偿债空间进一步收缩。
  warning_signs:
    - 经营现金流为负且存货、闲置产能上升
    - 行业价格下跌仍追加资本开支
    - 新项目没有订单或明确退出方案
  bound_to:
    - 现金流八象限生命周期
    - 投资规模与节奏压力测试
  tags: [counter-example, decline, overinvestment]

- id: ce19
  title: 借钱存银行反而拉低股东回报
  type: counter-example
  source_chapter: 股东提高收益得靠什么？
  source_quote: |
    琳琳的公司向银行借钱并将这笔钱存在银行；因为存款利率低于贷款利率，净利润和净资产报酬率都会下降。
  failure_mode: |
    误以为提高负债和权益乘数就必然提高 ROE，把借来的钱闲置或投入低回报项目。
  mechanism: |
    杠杆只有在新增资产回报高于债务成本时才增厚股东收益；低息存款与高息贷款之间的利差会直接减少利润并放大偿债风险。
  warning_signs:
    - 债务增长快于可投项目和收入
    - 现金及短期投资增加但 ROIC 下降
    - 新增项目回报率低于贷款利率
  bound_to:
    - ROIC-WACC经济利润门槛
    - 权益乘数与杠杆分析
  tags: [counter-example, leverage, ROE]

- id: ce20
  title: 净利润为正却没有创造经济利润
  type: counter-example
  source_chapter: 什么是赚钱？
  source_quote: |
    如果一家公司的净利润大于0，经济利润小于0，那么这并不是一家赚钱的公司。
  failure_mode: |
    只因净利润、收入或增长率为正就认定企业创造价值，忽略股东资本的机会成本和资本成本。
  mechanism: |
    会计净利润通常只扣除债务成本，没有扣除股东要求的同风险回报；当 ROIC 低于 WACC 时，企业虽有账面利润却在损耗投资者价值。
  warning_signs:
    - ROIC 长期低于估计资本成本
    - 净利润增长但经济利润持续为负
    - 扩张依赖更多资本却没有回报改善
  bound_to:
    - ROIC-WACC经济利润门槛
    - 机会成本与资本成本
  tags: [counter-example, valuation, economic-profit]

- id: ce21
  title: 战略两头落空却把问题归咎行业
  type: counter-example
  source_chapter: 战略定位和执行能力如何影响企业的财务数据？
  source_quote: |
    成本领先公司的毛利率很低、周转率也不高；差异化公司的周转率低，毛利率也不怎么样，说明战略执行出了问题。
  failure_mode: |
    宣称采取成本领先或差异化战略，却同时丢掉效益和效率，仍把低回报归因于行业或战略取舍。
  mechanism: |
    战略本应主动牺牲一个维度换取另一个维度；若低毛利没有换来高周转，或低周转没有换来高毛利，投入和舍弃都没有形成竞争优势。
  warning_signs:
    - 毛利率和总资产周转率同时低于同行
    - 管理层战略叙事与财务画像不一致
    - 改革投入增加但 ROIC 没有改善
  bound_to:
    - 效益-效率战略取舍
    - 环境-战略-执行三层归因
  tags: [counter-example, strategy, execution]

- id: ce22
  title: 资产已经贬值仍按利润表做判断
  type: counter-example
  source_chapter: 什么情况下现金流量表比利润表重要？
  source_quote: |
    应收账款收不回来、存货卖不掉、固定资产过时，都会导致资产减值；此时现金流量表的信息无疑非常重要。
  failure_mode: |
    在资产质量恶化时继续相信账面资产和利润，把尚未确认的减值当作真实盈利和偿债能力。
  mechanism: |
    利润表依赖资产未来有用的判断；一旦应收、存货或固定资产不可收回，资产和利润同时被高估，经营现金流反而更早暴露风险。
  warning_signs:
    - 利润为正但经营现金流持续为负
    - 应收账款、存货或闲置设备大幅增加
    - 减值计提滞后于行业需求或价格变化
  bound_to:
    - 利润与现金流冲突诊断
    - 资产质量与减值扫描
  tags: [counter-example, impairment, cash-flow]

- id: ce23
  title: 替代品出现仍按旧需求生产
  type: counter-example
  source_chapter: 什么样的公司更应该关注现金流？
  source_quote: |
    智能手机和平板电脑流行后，电子书阅读器销售遭遇寒冬；公司仍生产，存货和应收账款大幅增加。
  failure_mode: |
    面对替代品和需求骤降仍维持原有产量与投资，把短期账面利润误作需求复苏信号。
  mechanism: |
    产品卖不动会同时堆积存货、拉长回款并压低经营现金流；继续扩产会放大减值和资金缺口，最终利润集中暴跌。
  warning_signs:
    - 替代技术渗透率上升而销量下降
    - 存货、应收账款与经营现金流背离
    - 经营现金流为负却继续扩产
  bound_to:
    - 行业五力盈利诊断
    - 利润与现金流冲突诊断
  tags: [counter-example, substitution, demand-risk]
