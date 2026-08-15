# 术语表 (Glossary)

> 从《GPT时代的量化交易：底层逻辑与技术实践》中提取的关键术语及其作者特定的定义
> 生成时间：2026-08-12
> 提取范围：Section01-09（初始版本，待补充Section10-35）

---

## 已提取术语

```yaml
- id: g01
  term: 量化交易
  type: glossary
  source_chapter: 1.1
  definition: |
    通过在不确定的金融市场中寻找确定性，从而在特定范围内利用概率（然率、机会率或可能性）优势取得超额收益的方法。核心假设包括：①上帝视角（基于概率的系统思维）；②没有全局最优解，只有局部最优解；③市场普遍存在超额收益（非理性）。
  common_usage: |
    常识认为量化交易等同于算法交易或高频交易，但作者定义更宽泛，强调概率优势和系统思维。
  example: |
    "量化交易是通过在不确定的金融市场中寻找确定性，从而在特定范围内利用概率优势取得超额收益的方法。"
  tags: [concept, core-definition, philosophy]

- id: g02
  term: 广义量化交易
  type: glossary
  source_chapter: 1.4
  definition: |
    所有能通过构建模型来进行复制和追踪的理性交易方法。包括巴菲特的基本面投资、达利欧的资产配置、西蒙斯的阿尔法策略等大师方法，只要是理性的、可量化的投资方法都属于广义量化交易。
  common_usage: |
    常识认为量化交易就等于对冲策略，但作者提出广义量化涵盖所有可模型化的理性投资方法，打破"量化=对冲"的狭隘认知。
  example: |
    "从广义上来讲，对于这些大师们所使用的交易方法，我们都是可以通过构建模型来进行复制和追踪的。"
  tags: [concept, strategy-classification]

- id: g03
  term: 狭义量化交易
  type: glossary
  source_chapter: 1.4
  definition: |
    人们通常理解的量化交易，特指对冲策略相关的量化方法。作者认为这只是量化交易的"冰山一角"。
  common_usage: |
    与作者的广义量化交易概念相对，狭义量化主要指对冲基金使用的策略。
  example: |
    "人们心目中的量化交易通常是狭义量化交易，因为很多人都以为量化交易就等于对冲。"
  tags: [concept, strategy-classification]

- id: g04
  term: 三重核心假设
  type: glossary
  source_chapter: 1.1
  definition: |
    量化交易的哲学基础，包括三个假设：①上帝视角（基于概率的系统思维）；②没有全局最优解，只有局部最优解；③市场普遍存在超额收益（非理性）。
  common_usage: |
    作者独创的量化交易哲学框架，不同于传统金融理论的假设。
  example: |
    "其核心假设是：①上帝视角（基于概率的系统思维）；②没有全局最优解，只有局部最优解；③市场普遍存在超额收益（非理性）。"
  tags: [concept, philosophy, author-original]

- id: g05
  term: 上帝视角
  type: glossary
  source_chapter: 1.1
  definition: |
    三重核心假设之一，指基于概率的系统思维方式，不追求预测具体结果，而是从概率分布的角度看待市场变化。
  common_usage: |
    作者将概率思维称为"上帝视角"，强调全局和系统性的视角。
  example: |
    "上帝视角（基于概率的系统思维）"
  tags: [concept, philosophy, mindset]

- id: g06
  term: 底层逻辑
  type: glossary
  source_chapter: 前言
  definition: |
    市场变化背后的数学规律和决策框架，独立于具体编程工具。作者强调"在投资中，底层思维逻辑最重要，而具体的工具不重要"。
  common_usage: |
    作者强调"逻辑>工具"的认知转变，特别在ChatGPT降低编程门槛后，掌握底层逻辑成为关键竞争力。
  example: |
    "当工具的使用门槛迅速降低时，掌握量化交易的底层逻辑就成了重中之重。"
  tags: [concept, philosophy, book-theme]

- id: g07
  term: 基本面量化交易策略
  type: glossary
  source_chapter: 1.4.1
  definition: |
    五大量化策略之一，通过量化方法分析企业基本面（财务数据、行业景气度等）进行投资决策。代表人物是巴菲特，核心是捕捉基本面反转信号。
  common_usage: |
    将传统价值投资方法（如巴菲特的投资）纳入量化框架，通过模型化实现。
  example: |
    "真正厉害的价值投资者应当是巴菲特这样基本面反转的观察者和参与者。"
  tags: [strategy, fundamental-analysis]

- id: g08
  term: 资产配置量化交易策略
  type: glossary
  source_chapter: 1.4.2
  definition: |
    五大量化策略之一，通过在不同资产类别（股票、债券、现金等）间进行定期再平衡来分散风险、获取稳定收益。代表人物是达利欧，适用于超大规模资金。
  common_usage: |
    对应达利欧的"全天候策略"和美国401K养老金计划的投资方法。
  example: |
    "美国的401K养老金计划采用的就是资产配置量化交易策略。"
  tags: [strategy, asset-allocation]

- id: g09
  term: 阿尔法量化交易策略
  type: glossary
  source_chapter: 1.4.3
  definition: |
    五大量化策略之一，通过挖掘和利用市场中的有效因子来获取不随市场波动的超额收益（阿尔法收益）。代表人物是西蒙斯，已成为量化交易的代名词。
  common_usage: |
    最为人熟知的量化策略类型，难点在于需要不断挖掘有效因子。
  example: |
    "西蒙斯团队取得的平均60%的年化收益率，让所有其他类型的投资都黯然失色。"
  tags: [strategy, alpha, factor-model]

- id: g10
  term: 贝塔量化交易策略
  type: glossary
  source_chapter: 1.4.4
  definition: |
    五大量化策略之一，源自200年前对趋势的追踪方法，通过跟随市场趋势获取贝塔收益（市场波动收益）。代表人物是斯坦利·克罗。
  common_usage: |
    最古老的量化策略，核心是趋势跟踪和择时。
  example: |
    "贝塔量化交易策略源自200年前世界上最古老的量化交易策略，即对趋势的追踪。"
  tags: [strategy, beta, trend-following]

- id: g11
  term: 另类量化交易策略
  type: glossary
  source_chapter: 1.4.5
  definition: |
    五大量化策略之一，利用人性弱点等待市场崩溃，或利用古怪因子等待消息扩散，包括事件驱动、热点追踪等难以复制的策略。代表人物是索罗斯。
  common_usage: |
    听起来难以复制、实施困难的策略，如利用卫星数据、市场恐慌等。
  example: |
    "创建量子基金的乔治·索罗斯一向以杀伐果断而著称，他是另类量化交易策略的代表人物。"
  tags: [strategy, alternative, event-driven]

- id: g12
  term: 阿尔法收益
  type: glossary
  source_chapter: 1.4.3
  definition: |
    不随市场波动的超额收益部分，通过有效因子和选股能力获得，与贝塔收益（市场波动收益）相对应。
  common_usage: |
    金融学标准概念，作者在量化策略分类中将其作为一种独立策略类型。
  example: |
    "阿尔法量化已经成为量化交易的代名词。"
  tags: [concept, technical, return-decomposition]

- id: g13
  term: 贝塔收益
  type: glossary
  source_chapter: 1.4.4
  definition: |
    随市场波动而获得的收益部分，通过跟随市场趋势获取。与阿尔法收益（超额收益）相对。
  common_usage: |
    金融学标准概念，作者将其扩展为一种独立的量化策略类型（趋势跟踪）。
  example: |
    "所有的阿尔法都是贝塔"
  tags: [concept, technical, return-decomposition]

- id: g14
  term: 万物皆可量化
  type: glossary
  source_chapter: 前言
  definition: |
    作者的核心认知，源自恩格斯的"任何一门科学的真正完善在于数学工具的广泛应用"。认为投资不是艺术而是可被数学描述的科学，一切可投资领域均可进行数据分析。
  common_usage: |
    作者提出的哲学理念，将量化方法的适用范围扩展到所有投资领域，甚至高考志愿填报。
  example: |
    "从广义来看，一切可投资的领域均可进行数据分析（万物皆可量化）。"
  tags: [philosophy, book-theme, author-original]

- id: g15
  term: 因子
  type: glossary
  source_chapter: 1.4.3
  definition: |
    与股票收益和风险密切相关的关键数据特征，用于建立预测模型。不仅是数据指标，更是"底层逻辑的量化表达"。需要满足可持续性、可投资性、可区分性、可解释性四个条件。
  common_usage: |
    作者强调因子是底层逻辑的量化表达，而非简单的技术指标。
  example: |
    "数以万计的因子被挖掘出来用于量化交易。"
  tags: [concept, technical, factor-model]

- id: g16
  term: 日本蜡烛图
  type: glossary
  source_chapter: 1.3.1
  definition: |
    又称K线图，由250年前日本的本间宗久发明，记录每次交易的开盘价、最高价、最低价、收盘价，以蜡烛形象呈现价格变化，是量化交易的萌芽。
  common_usage: |
    通用技术分析工具，作者追溯其历史起源和量化意义。
  example: |
    "本间宗久根据自己收集的历史价格，以取光照明的蜡烛的形象，绘制出世界上第一幅日本蜡烛图，量化交易由此萌芽。"
  tags: [technical, historical, charting]

- id: g17
  term: 有效市场假说
  type: glossary
  source_chapter: 1.3
  definition: |
    简称EMP，由芝加哥大学金融学教授尤金·法玛在20世纪60年代提出，基本假设是市场运动遵循随机漫步原理，当前股价已经包含了所有公开信息，因此持续战胜市场几乎是不可能的。
  common_usage: |
    标准金融学理论，作者引用它作为量化交易需要挑战的假说。
  example: |
    "索普的观点与有效市场假说相同，但结论却并不一致。"
  tags: [theory, academic, market-efficiency]

- id: g18
  term: 概率优势
  type: glossary
  source_chapter: 1.1, 1.3
  definition: |
    量化交易的核心机制，指虽然不能准确预测价格的变化，但价格变化的概率是可以被测量的，通过这种概率优势在长期内取得超额收益。
  common_usage: |
    作者将概率思维作为量化交易区别于主观交易的关键特征。
  example: |
    "虽然不能准确预测价格的变化，但价格变化的概率是可以被测量的。"
  tags: [concept, philosophy, probability]

- id: g19
  term: 可转债套利
  type: glossary
  source_chapter: 1.3
  definition: |
    索普发明的量化交易策略，使用权证定价模型计算权证价格，如果权证价格过高就卖空它并同时买入等量股票作为对冲，或进行相反操作，从而获取无风险收益。
  common_usage: |
    经典套利策略，作者追溯其起源于量化交易之父索普。
  example: |
    "1960年代，他发明了基于21点原理的量化股票市场系统，并将其运用于可转债套利。"
  tags: [strategy, arbitrage, historical]

- id: g20
  term: 统计套利策略
  type: glossary
  source_chapter: 1.3
  definition: |
    1983年由格里·班伯格发明，利用一组相对应股票短暂出现异常情况时的价差，通过卖空高价股票并买入低价股票，在它们的价格恢复到历史平均水平时进行平仓获利。是迄今为止最强大的交易策略之一，不论市场如何波动都能获利。
  common_usage: |
    经典量化策略，作者强调其"不论市场如何波动都能获利"的特性。
  example: |
    "这是迄今为止最强大的交易策略，不论市场如何波动都能获利。"
  tags: [strategy, arbitrage, statistical]

- id: g21
  term: 布莱克-斯科尔斯公式
  type: glossary
  source_chapter: 1.3
  definition: |
    简称B-S公式，1973年由费希尔·布莱克和迈伦·斯科尔斯提出，用于期权定价。假设价格随机游走，价格的运动方向是钟形曲线的正中央，价格不会大幅跳动。标志着量化革命的开始。
  common_usage: |
    金融工程的基础公式，作者强调其对量化交易兴起的重要作用。
  example: |
    "华尔街快速接受了这一理论，标志着量化革命的开始。"
  tags: [formula, technical, option-pricing]

- id: g22
  term: 现代投资组合理论
  type: glossary
  source_chapter: 1.3
  definition: |
    由马科维茨提出，采用风险资产的期望收益率（均值）和方差（或标准差）来代表风险，被称为"华尔街的第一次革命"。核心目标是解决投资风险，认为分散投资对象可以降低个别风险。
  common_usage: |
    金融学基础理论，作者追溯其对量化交易发展的推动作用。
  example: |
    "马科维茨提出了资产组合选择理论，该理论最早采用风险资产的期望收益率（均值）和方差（或标准差）来代表风险。"
  tags: [theory, academic, portfolio-management]

- id: g23
  term: 系统风险
  type: glossary
  source_chapter: 1.3
  definition: |
    市场风险的一类，指整个经济体所面临的风险，无法通过分散投资来减少。与个别风险（独特风险或非系统风险）相对。
  common_usage: |
    金融学标准概念，作者在介绍现代投资组合理论时引用。
  example: |
    "市场风险一般分为两类：个别风险和系统风险。后者指整个经济体所面临的风险，无法通过分散投资来减少。"
  tags: [concept, risk-management]

- id: g24
  term: 个别风险
  type: glossary
  source_chapter: 1.3
  definition: |
    又称独特风险或非系统风险，指单个投资收益的不确定性，与特定公司相关，可以通过分散投资来降低。
  common_usage: |
    金融学标准概念，与系统风险相对。
  example: |
    "分散投资对象可以降低个别风险（独特风险或非系统风险）。"
  tags: [concept, risk-management]

- id: g25
  term: 大奖章基金
  type: glossary
  source_chapter: 1.3
  definition: |
    1988年由詹姆斯·西蒙斯设立的量化基金，雇员大多为物理学家、数学家、生物学家及计算机专家。擅长高频交易，在20年里收益率高达70%，但投资策略始终秘而不宣。
  common_usage: |
    量化交易领域的传奇基金，作者将其作为阿尔法策略的代表案例。
  example: |
    "大奖章基金擅长高频交易，是一个典型的多策略基金，在20年里收益率高达70%。"
  tags: [case-study, fund, alpha-strategy]

- id: g26
  term: 高频交易
  type: glossary
  source_chapter: 1.3, 1.4.3
  definition: |
    通过计算机程序以极高速度进行交易的策略，速度成为交易的关键。大奖章基金擅长此类策略。
  common_usage: |
    狭义量化交易的典型形式，作者将其作为阿尔法策略的一种实现方式。
  example: |
    "大奖章基金擅长高频交易。"
  tags: [strategy, technical, execution]

- id: g27
  term: 非结构化数据
  type: glossary
  source_chapter: 1.5.1
  definition: |
    诸如声音、图像和文本等无法被数据模型直接处理的数据，需要采用人工智能方法进行结构化后再由数据模型处理。ChatGPT的核心能力之一就是将非结构化数据快速转换成结构化数据。
  common_usage: |
    数据科学标准概念，作者强调其在量化交易中的应用和ChatGPT的作用。
  example: |
    "ChatGPT的核心能力之一就是可以将非结构化数据更快地转换成结构化数据，这也为未来的量化交易扫清了障碍。"
  tags: [technical, data-processing, ai]

- id: g28
  term: 结构化数据
  type: glossary
  source_chapter: 1.5.1
  definition: |
    可以被数据模型直接处理的有组织的数据，与非结构化数据（声音、图像、文本等）相对。
  common_usage: |
    数据科学标准概念，作者强调量化交易需要将非结构化数据转换为结构化数据。
  example: |
    "除了结构化数据，量化交易中还需要用到诸如声音、图像和文本等非结构化数据。"
  tags: [technical, data-processing]

- id: g29
  term: 元知识学习
  type: glossary
  source_chapter: 1.5.1
  definition: |
    "关于知识的知识"，描述特定知识或知识集合所包含的内容、基本结构及一般特征。在量化交易中，指用机器进行投资策略选择的知识，即如何管理、掌控和使用策略的知识。
  common_usage: |
    人工智能领域的概念，作者认为这是量化交易未来发展的难点和突破方向。
  example: |
    "元知识学习能使我们掌握如何用机器进行投资策略的选择。"
  tags: [technical, ai, meta-learning]

- id: g30
  term: 夏普比率
  type: glossary
  source_chapter: 1.5.3
  definition: |
    衡量策略风险调整后收益的指标，用于评估单位风险下的超额回报。作者提到中国市场量化交易策略的夏普比率为2.50%～3.00%。
  common_usage: |
    金融学标准风险指标，数值越高表示风险调整后收益越好。
  example: |
    "在中国目前的市场上，量化交易策略的夏普比率为2.50%～3.00%。"
  tags: [technical, risk-metric, performance]

- id: g31
  term: 博弈平衡点
  type: glossary
  source_chapter: 1.4.5
  definition: |
    市场发展的最终方向，当五大量化策略占据市场绝大部分时，市场将趋向博弈平衡状态，各策略相互制约达到动态平衡。
  common_usage: |
    作者借用博弈论概念，描述量化交易市场的最终演化状态。
  example: |
    "当下，这五大类策略已经占据了市场的绝大部分，市场发展的最终方向一定是博弈平衡点。"
  tags: [concept, market-structure, game-theory]

- id: g32
  term: WorldQuant阿尔法101因子
  type: glossary
  source_chapter: 1.3
  definition: |
    2015年12月，WorldQuant（世坤投资）公开的101个阿尔法表达式，声称其中80%的因子仍然在实盘中被使用。2016年随着这些因子的公开，中国的量化元年正式开启。
  common_usage: |
    量化交易历史上的里程碑事件，作者将其视为中国量化元年的标志。
  example: |
    "2016年，随着WorldQuant阿尔法101因子的公开，中国的量化元年正式开启。"
  tags: [historical, factor-model, milestone]

- id: g33
  term: 量化元年
  type: glossary
  source_chapter: 1.3
  definition: |
    量化交易在某个市场大规模发展的起始年份。美国的量化元年是2011年，中国的量化元年是2016年（WorldQuant阿尔法101因子公开之年）。
  common_usage: |
    作者用于标记量化交易发展的重要时间节点。
  example: |
    "2011年，美国的量化元年正式开启。"
  tags: [historical, milestone]

- id: g34
  term: 智能投顾
  type: glossary
  source_chapter: 1.5.3
  definition: |
    通过智能化发展降低投资顾问咨询服务的人工成本，提升量化交易利润的业务模式。未来金融元宇宙中的智能投顾业务有望促进量化交易的机构化。
  common_usage: |
    金融科技领域概念，作者将其与量化交易的未来发展联系。
  example: |
    "投资顾问业务的智能化发展，可以帮助降低相应人工服务的成本，提升量化交易的利润。"
  tags: [technical, fintech, future-trend]

- id: g35
  term: 宽客
  type: glossary
  source_chapter: 1.3
  definition: |
    量化交易从业者的称呼，特指运用数学、统计、计算机等技术进行交易的专业人士。索普被誉为"宽客教父"。
  common_usage: |
    量化交易行业通用称呼，来自英文"Quant"。
  example: |
    "此后他成立了普林斯顿-纽波特合伙公司，成为最早采用纯数学技术赚钱的大师之一，并被世人誉为'宽客教父'。"
  tags: [terminology, profession]
```

---

## 待补充

子代理正在阅读Section10-35章节，将补充以下类型的术语：
- 凯利公式相关术语
- 因子建模详细术语（IC、换手率等）
- 2%法则等风险控制术语
- 具体的技术指标和评估方法
- A股市场特定术语

预计总术语数量：40-50个
