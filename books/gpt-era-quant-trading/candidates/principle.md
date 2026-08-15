# 量化交易原则候选清单

从《GPT时代的量化交易：底层逻辑与技术实践》一书中提取的原则、检查清单和规则。

---

- id: p01
  title: 量化交易三大核心假设
  type: principle
  source_chapter: Section05.xhtml
  source_quote: |
    其核心假设是：①上帝视角（基于概率的系统思维）；②没有全局最优解，只有局部最优解；③市场普遍存在超额收益（非理性）。
  summary: |
    量化交易建立在三个核心假设之上：采用上帝视角的概率思维、接受只有局部最优解的现实、相信市场存在非理性导致的超额收益机会。这三个假设构成了量化交易的哲学基础。
  tags: [philosophy, core-assumption, quantitative-trading]

- id: p02
  title: 价值投资四条底层逻辑
  type: principle
  source_chapter: Section11.xhtml
  source_quote: |
    （1）持续创造价值很重要，买股票的本质是买企业；（2）要关注安全边际，用低的价格买入；（3）要忽略市场的短期波动；（4）守住自己的能力圈，不懂的行业不要碰。
  summary: |
    格雷厄姆和巴菲特总结的价值投资核心原则：买企业而非股票、寻求安全边际、忽略短期波动、坚守能力圈。前三条来自格雷厄姆，第四条是巴菲特的补充。
  tags: [value-investing, buffett, graham, fundamental]

- id: p03
  title: 巴菲特ROE选股标准
  type: rule
  source_chapter: Section11.xhtml
  source_quote: |
    巴菲特曾提到过，如果非要用一个指标进行选股，那么他会选择净资产收益率。他选择的公司，都是净资产收益率超过20%的公司。
  summary: |
    净资产收益率（ROE）是巴菲特最看重的单一指标。选股标准为ROE>20%，且最好能持续5年以上保持在这个水平，体现企业持续的盈利能力。
  tags: [buffett, stock-selection, roe, fundamental]

- id: p04
  title: 巴菲特毛利率选股标准
  type: rule
  source_chapter: Section11.xhtml
  source_quote: |
    巴菲特曾提醒投资者：如果一个行业的平均毛利率低于20%，那么几乎可以断定这个行业存在着过度竞争。我们可以观察伯克希尔的长期持仓股票，毛利率通常都在40%左右。
  summary: |
    毛利率反映企业的定价能力和核心竞争力。巴菲特的标准是毛利率>40%，低于20%的行业存在过度竞争，应避免投资。可口可乐60%、苹果40%都符合此标准。
  tags: [buffett, stock-selection, profitability, fundamental]

- id: p05
  title: 巴菲特净利率选股标准
  type: rule
  source_chapter: Section11.xhtml
  source_quote: |
    关于净利率，巴菲特没有说具体指标，他只是说要有优秀的管理层，这样就可以做到"以最小的成本获得最大的收益"。业内通常将其总结为，净利率至少要在5%以上。
  summary: |
    净利率体现企业将销售收入转化为利润的能力，反映管理层的运营效率。虽然巴菲特未明确指标，但业界总结其标准为净利率>5%。
  tags: [buffett, stock-selection, profitability, fundamental]

- id: p06
  title: 巴菲特市盈率安全区间
  type: rule
  source_chapter: Section11.xhtml
  source_quote: |
    格雷厄姆所定义的市盈率安全范围是10倍之内，而巴菲特在投资实践中设定的市盈率安全范围则是15倍以内。通过历史数据可以看到，即使A股在底部的时候，市盈率还是高于巴菲特设定的范围，所以我们可以把市盈率设定在20倍到40倍之间。
  summary: |
    市盈率是估值指标。格雷厄姆标准<10倍，巴菲特标准<15倍。针对A股市场特点，建议买入市盈率20倍以下，卖出市盈率40倍以上。低市盈率需结合其他指标综合判断。
  tags: [buffett, valuation, pe-ratio, stop-loss]

- id: p07
  title: 格雷厄姆十条选股标准
  type: checklist
  source_chapter: Section11.xhtml
  source_quote: |
    （1）市盈率的倒数应大于AAA债券收益率的2倍；（2）股票的市盈率应小于最近5年内所有股票平均市盈率的40%；（3）股息率大于AAA债券收益率的2/3；（4）股价低于每股有形账面价值的2/3；（5）股价低于每股净流动资产价值的2/3；（6）债务权益比率必须小于1；（7）流动比率要大于2；（8）负债小于净流动资产价值的2倍；（9）每股收益历史增长大于7%；（10）在过去10年中，盈利的下降不超2年。
  summary: |
    格雷厄姆在《证券分析》中提出的量化选股标准，包含估值（前5条）和质量（后5条）两个维度。前5条衡量股票廉价程度，后5条评估企业质量（杠杆率、偿债能力、盈利增长）。经过80多年仍有效。
  tags: [graham, stock-selection, checklist, fundamental]

- id: p08
  title: 基本面投资分散原则
  type: principle
  source_chapter: Section11.xhtml
  source_quote: |
    投资组合应该采取多元化策略。正如俗话说的"鸡蛋不能都放在一个篮子里"，建议投资者建立一个广泛的投资组合，将其投资分布在各个行业的多家企业中，从而减少风险。
  summary: |
    格雷厄姆提出的风险管理原则。通过分散投资降低个别风险（非系统风险），将资金分布在不同行业和企业。但基本面量化要求单只股票仓位不超过2%。
  tags: [risk-management, diversification, portfolio, graham]

- id: p09
  title: 基本面量化最大持仓限制
  type: rule
  source_chapter: Section11.xhtml
  source_quote: |
    基本面量化交易者的仓位则更加分散（通常最大持仓股不超过2%）。
  summary: |
    基本面量化交易的仓位管理规则：单只股票最大持仓不超过总资金的2%。这样可以有效分散风险，通常会持有100-200只股票构建投资组合。
  tags: [position-sizing, risk-management, quantitative]

- id: p10
  title: 达利欧成功四步法
  type: principle
  source_chapter: Section12.xhtml
  source_quote: |
    第一，寻找最聪明的与自己观点不同的人，以便更好地理解他们的推理；第二，认清自己在哪些情况下没有明确的观点，不急于下结论；第三，逐步总结出永恒和普适的原则，对其进行检验，并加以系统化；第四，通过平衡风险，实现较高的收益和降低下跌波动。
  summary: |
    达利欧在1982年投资失败后总结的成功路径：寻求不同观点、保持开放心态、系统化原则、平衡风险。这四步帮助他建立了全天候策略，成就了桥水基金。
  tags: [dalio, risk-management, principle, bridgewater]

- id: p11
  title: 全天候策略四等分配置
  type: principle
  source_chapter: Section12.xhtml
  source_quote: |
    全天候量化交易策略的投资区分（四等分风险分配）：①高增长，股票、大宗商品、公司信用产品、新兴经济体信用产品；②高通胀，通胀联结债券、大宗商品、新兴经济体信用产品；③低增长，普通债券、通胀联结债券；④低通胀，股票、普通债券。
  summary: |
    桥水基金的全天候策略核心逻辑：将资产按经济环境（高/低增长 × 高/低通胀）四等分配置，每种情况分配25%风险权重，无需预测市场，在任何经济环境下都能获得稳定收益。
  tags: [all-weather, asset-allocation, bridgewater, risk-parity]

- id: p12
  title: 全天候策略三步分析法
  type: checklist
  source_chapter: Section12.xhtml
  source_quote: |
    第一步，选择低相关性的大类资产。第二步，确定相关参数。包括预期收益区间、预期风险区间、无风险收益。第三步，定时定量计算。通过最优化比例计算，使得各个资产的风险贡献度趋于相等。
  summary: |
    实施全天候策略的三个步骤：选择相关性低的资产类别（股票、债券、黄金、商品等）、确定收益和风险参数、定期调整使各资产风险贡献相等。小资金用股票+现金，大资金需加入债券、黄金、大宗商品。
  tags: [all-weather, asset-allocation, process, risk-parity]

- id: p13
  title: 斯坦利·克罗KISS原则
  type: principle
  source_chapter: Section13.xhtml
  source_quote: |
    他的座右铭是：KISS（Keep It Simple，Stupid）——追求简洁。
  summary: |
    斯坦利·克罗的核心投资哲学：保持简单。技术操作手段很多但都十分简单，有时简单到只用一根均线。复杂不等于有效，简单的方法往往更可靠。
  tags: [kroll, simplicity, beta, trend-following]

- id: p14
  title: 克罗盈亏持有原则
  type: principle
  source_chapter: Section13.xhtml
  source_quote: |
    他的投资策略及理论：盈利时是长线，亏损时就是短线。
  summary: |
    斯坦利·克罗的仓位管理原则：当头寸盈利时，持有长线让利润奔跑；当头寸亏损时，快速止损短线处理。这是趋势跟踪策略的核心，体现"截断亏损，让利润奔跑"的理念。
  tags: [kroll, position-management, stop-loss, trend-following]

- id: p15
  title: 克罗七段投资逻辑
  type: checklist
  source_chapter: Section13.xhtml
  source_quote: |
    ①培养、练习耐心和决心，以及客观的思考方式。②识别和分离市场上的主要和次要价格趋势，并只关注主要走势。③当你开始建仓时，假设你已经准备好进行重大变动，不要因为无聊或不耐烦而关闭交易。④一方面，当市场走势有利时，争取大笔交易，不要满足于微薄的利润。另一方面，当头寸与市场走势相反时，将其平仓以将损失降至最低。⑤按照主要趋势方向进行交易，应该在先前趋势或横盘趋势有重大突破时建立头寸。⑥如果只有不到一半的交易是盈利的，那么应该努力提高胜率并减少交易。⑦保持简单。
  summary: |
    斯坦利·克罗总结的七条投资原则：培养耐心和客观性、只关注主要趋势、做好长期准备、让利润奔跑同时快速止损、在趋势突破时建仓、提高胜率、保持简单。这是贝塔量化交易的完整逻辑框架。
  tags: [kroll, checklist, trend-following, beta]

- id: p16
  title: 打板三要素
  type: checklist
  source_chapter: Section13.xhtml
  source_quote: |
    （1）把握时机。建议在开盘3分钟内打板，最迟不超过10分钟。（2）靠前原则。在同一板块中，打最早涨停的个股；在同一梯队中，打最早上板的个股。（3）关注挂撤单量。通过分析每3秒的切片行情下逐笔成交，推算实时盘口。
  summary: |
    打板量化交易的三个核心要素：时机要早（开盘3-10分钟内）、选择要准（同板块或梯队中最早涨停的）、盘口要准（关注大单挂撤单情况）。需要VIP通道保证速度，属于高风险高收益策略。
  tags: [limit-up, timing, high-frequency, beta]

- id: p17
  title: 贝塔值波动判断规则
  type: rule
  source_chapter: Section13.xhtml
  source_quote: |
    当贝塔值＞1时，说明这只股票的波动性比市场的波动性高；当贝塔值=1时，说明这只股票的波动性与市场的波动性一致；当贝塔值＜1时，说明这只股票的波动性比市场的波动性低。
  summary: |
    贝塔值是衡量股票相对市场波动性的指标。β>1表示高波动适合激进策略，β=1表示同步波动，β<1表示低波动适合稳健策略。打板策略需要选择高贝塔值股票。
  tags: [beta, volatility, risk-assessment]

- id: p18
  title: 连板三阶段规律
  type: principle
  source_chapter: Section13.xhtml
  source_quote: |
    阶段一，启动连板：首板最好较前一日有放量，一板量在前一日一倍以内的放量最健康；二板也最好较一板有一倍以内的放量；三板较二板也是一倍以内的放量，最好使一板、二板、三板形成均匀的阶梯状。阶段二，连板加速：连板加速阶段的标志就是开始缩量，强势个股甚至一字量很少。阶段三，连板走坏：连板走坏阶段只需要一天，标志是当天放量收盘跌成阴线。
  summary: |
    连板股票的生命周期三阶段：启动期（一、二、三板逐步放量形成阶梯）、加速期（开始缩量甚至一字板）、走坏期（放量收阴）。理解这三个阶段有助于把握介入和退出时机。
  tags: [limit-up, cycle, volume-analysis, beta]

- id: p19
  title: 索普2%法则
  type: rule
  source_chapter: Section19.xhtml
  source_quote: |
    索普的2%法则：当你过度下注时，你将会失去一切。如果你从不一次下注超过你总筹码的2%，就永远也不可能输光所有的钱。
  summary: |
    爱德华·索普提出的资金管理铁律：单笔交易风险不超过总资金的2%。即使连续失败，也能保留大部分资金继续交易。很多量化基金将单只股票最大持仓设为2%。这是凯利公式的保守应用。
  tags: [thorp, position-sizing, risk-management, kelly-formula]

- id: p20
  title: 因子四要素
  type: checklist
  source_chapter: Section17.xhtml
  source_quote: |
    因子需要满足：（1）可持续性（2）可投资性（3）可区分性（4）可解释性
  summary: |
    量化因子必须满足的四个条件：可持续性（历史有效未来也有效）、可投资性（考虑交易成本后仍能盈利）、可区分性（能区分好股票和坏股票）、可解释性（有合理的经济学或行为金融学解释）。缺一不可。
  tags: [factor, alpha, checklist, quantitative]

- id: p21
  title: IC因子有效性阈值
  type: rule
  source_chapter: Section17.xhtml
  source_quote: |
    IC表现没有达到0.03的最低标准，该因子在沪深300指数成分股中没有突出的预测能力。
  summary: |
    信息系数（IC）是衡量因子预测能力的指标。当IC<0.03时，该因子被认为无效，不具备预测能力。这是因子筛选的最低门槛，低于此值应放弃该因子。
  tags: [factor, ic, threshold, backtesting]

- id: p22
  title: 量化交易不可能三角
  type: principle
  source_chapter: Section18.xhtml
  source_quote: |
    金融交易"不可能三角"：策略长期有效性、高收益风险比、高资金容量，三者不可兼得。
  summary: |
    量化交易的根本约束：长期有效性、高夏普比率、大资金容量三者无法同时满足。高容量策略往往收益率低，高收益策略容量有限，长期有效的策略收益会逐渐降低。投资者需要根据自身情况权衡取舍。
  tags: [constraint, trade-off, strategy-design]

- id: p23
  title: 止盈止损五大类21种
  type: checklist
  source_chapter: Section18.xhtml
  source_quote: |
    止盈止损可以分成五大类21种：固定类止盈止损（3种）、移动类止盈止损（4种）、时间类止盈止损（6种）、比较类止盈止损（4种）、组合类止盈止损（4种）。
  summary: |
    止盈止损的系统分类框架：固定类（固定点位/百分比）、移动类（跟踪止损、动态调整）、时间类（持仓期限限制）、比较类（相对基准）、组合类（多种方法组合）。共21种具体方法可供选择组合。
  tags: [stop-loss, risk-management, classification]

- id: p24
  title: 策略失效三大致命因素
  type: principle
  source_chapter: Section20.xhtml
  source_quote: |
    影响量化交易策略的有效性因素最为致命的有3个：未来函数、过度拟合和夏普比率突变。
  summary: |
    导致量化策略失效的三大杀手：未来函数（使用未来数据导致回测虚高）、过度拟合（过度优化历史数据失去泛化能力）、夏普比率突变（策略有效性发生根本改变）。这三个问题必须在策略开发中严格防范。
  tags: [backtesting, overfitting, strategy-failure]

- id: p25
  title: 夏普比率突变预警规则
  type: rule
  source_chapter: Section20.xhtml
  source_quote: |
    如果滚动夏普比率已经开始超过回测历史中的最大跌幅，则通常预示着这个量化交易策略可能已经失效。
  summary: |
    策略失效的预警信号：当滚动夏普比率超过历史最大回撤时，通常意味着策略已失效。应立即停止使用该策略，重新评估其有效性。这是实盘监控的重要指标。
  tags: [sharpe-ratio, strategy-monitoring, failure-detection]

- id: p26
  title: 米伦坎普三点投资逻辑
  type: checklist
  source_chapter: Section21.xhtml
  source_quote: |
    米伦坎普投资逻辑：（1）价值线投资主线ROE应该达到15%或者更高（2）核对年度财务报表中的数据和注释（3）与管理人员交谈。
  summary: |
    米伦坎普的投资方法论：首先筛选ROE≥15%的公司、仔细核对财务报表（包括注释中的隐藏信息）、与管理层交流验证判断。这三步结合了定量筛选和定性调研。
  tags: [milenkamp, fundamental, roe, checklist]

- id: p27
  title: 米伦坎普四种风险控制
  type: principle
  source_chapter: Section21.xhtml
  source_quote: |
    减少风险的方法：（1）延长投资期限（2）分散投资（3）投资股票最大的风险不是波动性，而是以过高的价格买入（4）根据投资氛围选择投资标的。
  summary: |
    米伦坎普的风险管理原则：拉长投资期限降低短期波动影响、多元化分散风险、重视估值风险而非波动风险、根据市场情绪逆向选择标的。强调价值投资的长期视角。
  tags: [risk-management, milenkamp, valuation]

- id: p28
  title: 低估值绩优股四要素
  type: checklist
  source_chapter: Section23.xhtml
  source_quote: |
    低估值绩优股模型筛选条件：近3年ROE大于20%、动态市盈率小于20倍、市净率小于5倍、毛利率大于30%。
  summary: |
    低估值绩优股的量化筛选标准：盈利能力（ROE>20%）、估值水平（PE<20倍、PB<5倍）、竞争优势（毛利率>30%）。四个条件同时满足，既保证质量又确保价格合理。
  tags: [stock-selection, value, quality, screening]

- id: p29
  title: 高频交易四特点
  type: checklist
  source_chapter: Section24.xhtml
  source_quote: |
    高频交易具备4个特点：（1）处理分笔交易数据（2）高资金周转率（3）日内开平仓（4）算法交易。
  summary: |
    高频交易的四个核心特征：使用Tick级数据、资金快速周转、不持仓过夜、依赖算法自动执行。这四个特点决定了高频交易对技术基础设施的极高要求。
  tags: [high-frequency, hft, characteristics]

- id: p30
  title: CTA策略三大配置价值
  type: principle
  source_chapter: Section24.xhtml
  source_quote: |
    CTA策略有三大配置价值：一是有危机Alpha属性；二是拉长周期以年为单位具有绝对收益；三是与其他资产有低相关性。
  summary: |
    CTA（商品交易顾问）策略的三大优势：危机时期表现优异（危机Alpha）、长期看具有绝对收益能力、与股票债券等传统资产相关性低。因此是资产配置中重要的分散化工具。
  tags: [cta, alternative, diversification, crisis-alpha]

- id: p31
  title: 杯柄形态三阶段规则
  type: rule
  source_chapter: Section24.xhtml
  source_quote: |
    杯柄形态买点规则：阶段一累计升幅至少30%，阶段二调整跌幅为20%-30%（高盈利增长可达50%），阶段三杯柄部分应在c点至d点的上半部分且在200天平均线以上。
  summary: |
    威廉·欧奈尔的杯柄形态识别标准：先涨30%以上形成杯身、回调20-30%形成杯底、杯柄部分在上半部且在200日均线上方。三个阶段完整出现时是买入信号。
  tags: [cup-and-handle, oneil, entry-signal, technical]

- id: p32
  title: 杯柄形态止盈法则
  type: rule
  source_chapter: Section24.xhtml
  source_quote: |
    杯柄形态止盈规则：价格突破f点后，达到d点和c点垂直距离的75%时止盈为最优，下一个最优止盈区间在135%一线，但胜率会下降12%左右。
  summary: |
    杯柄形态的量化止盈标准：突破后上涨至杯深的75%时止盈胜率最高，若追求更高收益可等到135%但胜率降低12%。这是基于大量历史数据统计得出的最优止盈点。
  tags: [cup-and-handle, take-profit, oneil, quantitative]

- id: p33
  title: FoF策略三维度
  type: principle
  source_chapter: Section24.xhtml
  source_quote: |
    FoF策略底层逻辑三个维度：择时能力、选股能力和信息比率。
  summary: |
    基金中的基金（FoF）选择子基金的三个评估维度：择时能力（能否把握市场时机）、选股能力（能否挑选优质标的）、信息比率（单位风险超额收益）。三个维度综合评估基金质量。
  tags: [fof, fund-selection, performance-evaluation]

- id: p34
  title: FoF三个50%法则
  type: checklist
  source_chapter: Section24.xhtml
  source_quote: |
    FoF策略筛选条件：择时能力排名前50%、选股能力排名前50%、信息比率排名前50%。
  summary: |
    FoF筛选子基金的量化标准：三个维度（择时、选股、信息比率）都要排在同类基金前50%。这样可以筛选出综合能力均衡的优质基金，避免单一能力突出但整体表现不佳的基金。
  tags: [fof, screening, ranking, quantitative]

- id: p35
  title: 监督学习五步骤
  type: checklist
  source_chapter: Section25.xhtml
  source_quote: |
    监督学习建模流程：数据获取→数据预处理→特征工程→模型训练→模型选择。
  summary: |
    机器学习在量化交易中的标准流程：获取历史数据、清洗和预处理、构建特征（因子）、训练模型、选择最优模型。每个步骤都需要领域知识和技术能力的结合。
  tags: [machine-learning, process, workflow]

- id: p36
  title: 过拟合控制两类方法
  type: principle
  source_chapter: Section25.xhtml
  source_quote: |
    避免过度拟合方法分两类：第一类对模型复杂度进行惩罚；第二类用验证数据测试模型效果。
  summary: |
    防止机器学习模型过拟合的两大策略：通过正则化惩罚模型复杂度（L1/L2正则、剪枝等）、使用验证集和交叉验证测试泛化能力。两类方法结合使用效果最佳。
  tags: [machine-learning, overfitting, regularization]

- id: p37
  title: 另类策略五大优势
  type: principle
  source_chapter: Section15.xhtml
  source_quote: |
    另类量化交易策略与传统相比具备5个优势：（1）更好利用机器学习（2）发现未被挖掘的观点（3）更长生存时间（4）策略生成更加泛化（5）更加高效。
  summary: |
    另类数据量化策略的五个竞争优势：适合机器学习处理、挖掘传统数据未覆盖的信号、策略衰减慢生命周期长、泛化能力强、处理效率高。这些优势使另类数据成为量化投资的新前沿。
  tags: [alternative-data, advantage, machine-learning]

- id: p38
  title: 另类数据15类来源
  type: checklist
  source_chapter: Section15.xhtml
  source_quote: |
    另类量化交易策略通常考虑15类数据：社交媒体数据、新闻评论、网页搜索数据、天气预报、卫星图像、穿戴设备数据、物联网数据、App数据、高频数据、专家及大V观点、ESG数据、员工数据、商场客流数据、个人消费数据、地理位置。
  summary: |
    另类数据的15个主要类别，涵盖社交、新闻、搜索、气象、遥感、物联网、消费、ESG等各个维度。这些非传统数据源可以提供比财务数据更及时的市场洞察。
  tags: [alternative-data, data-source, checklist]

- id: p39
  title: 事件驱动五步分析法
  type: checklist
  source_chapter: Section15.xhtml
  source_quote: |
    事件驱动量化交易策略五步分析法：定性分析（重要事件或消息有无影响）→定量分析（影响程度有多大）→定时分析（影响时间有多长）→异动分析（龙头股及标的异常表现）→轮动分析（同板块内同概念的股票谁先异动）。
  summary: |
    事件驱动策略的系统化分析框架：先判断事件是否有影响（定性）、量化影响大小（定量）、估计持续时间（定时）、识别龙头标的（异动）、把握板块轮动（轮动）。五步依次递进，构建完整的交易逻辑。
  tags: [event-driven, analysis-framework, alternative]

- id: p40
  title: 可转债套利五步骤
  type: checklist
  source_chapter: Section15.xhtml
  source_quote: |
    可转债事件驱动五步骤：第一步定性分析（评估转股价向下修正的时机）、第二步定量分析（分析可转债的风险和收益）、第三步定时分析（选择合适的时机介入）、第四步异动分析（动态评估风险和收益）、第五步轮动分析（择机离场选择下一标的）。
  summary: |
    可转债下修套利的操作流程：评估下修可能性、计算风险收益比、选择介入时机、动态监控、及时离场轮动。这是另类量化中较为稳健的套利策略。
  tags: [convertible-bond, arbitrage, event-driven]

- id: p41
  title: 可转债下修前提条件
  type: rule
  source_chapter: Section15.xhtml
  source_quote: |
    可转债转股价向下修正有2个前提：一是可转债进入回售期，二是正股股价跌破转股价的70%。
  summary: |
    触发可转债下修的两个必要条件：进入回售期（通常第3年末或第4年初）、正股价格跌破转股价70%。两个条件同时满足时，上市公司有动力下调转股价。
  tags: [convertible-bond, trigger-condition, rule]

- id: p42
  title: 可转债介入时机规则
  type: rule
  source_chapter: Section15.xhtml
  source_quote: |
    投资者需要在正股股价跌破转股价的70%后的第4～10个交易日介入。
  summary: |
    可转债下修套利的最佳介入窗口：跌破转股价70%后的第4-10个交易日。过早介入风险大，过晚介入收益低。这是基于历史统计得出的最优时间窗口。
  tags: [convertible-bond, entry-timing, rule]

---

**说明：**
- 共提取42条原则/检查清单/规则候选
- 覆盖范围：基本面量化、资产配置、贝塔策略、阿尔法策略、另类策略、因子建模、风险管理等
- 所有条目均包含原文引用、来源章节和实用总结
- 标签系统便于后续分类和检索

**提取标准：**
✅ 明确的数值阈值（如ROE>20%、IC<0.03）
✅ 结构化的步骤或要素（如三要素、五步骤）
✅ 条件判断规则（如"当X时做Y"）
✅ 大师级原则（巴菲特、达利欧、克罗等）

❌ 不包括一般性概念框架
❌ 不包括案例和历史叙述
❌ 不包括代码和技术实现细节
