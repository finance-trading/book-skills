# 关键术语词典 (Glossary)

- id: g01
  term: 阿尔法（Alpha）
  type: term
  source_chapter: 第3章
  author_definition: |
    "阿尔法是希腊字母α的音译，常用于量化表述投资者的盈利能力，或投资者得到的与市场波动无关的回报。在通常的定义中，阿尔法是指扣除市场基准回报之后的投资回报率，或仅仅是由投资策略所带来的价值。"
  key_distinction: |
    ≠ "总收益" — 阿尔法是超过市场基准的部分
    ≠ "贝塔收益" — 阿尔法与市场因素无关
    ≠ "运气" — 阿尔法应该来自策略而非偶然
    = 投资策略带来的、与市场因素无关的超额收益
  why_it_matters: |
    阿尔法是量化交易的核心目标。所有阿尔法模型的目标就是产生正阿尔法。
    如果混淆了阿尔法和贝塔，会错误评估策略的真实价值。
  tags: [term, core-concept, alpha]

- id: g02
  term: 贝塔（Beta）
  type: term
  source_chapter: 第3章
  author_definition: |
    "由于市场因素带来的回报率称为贝塔，例如，某基金的回报率是12%，而同时期的市场基准回报率是10%，则该基金的阿尔法值就是2%（这里假设了基金投资组合的贝塔恰好为1）。"
  key_distinction: |
    ≠ "阿尔法" — 贝塔是市场带来的收益
    ≠ "风险" — 贝塔是市场系统性风险的补偿
    = 由市场整体表现带来的回报率
  why_it_matters: |
    贝塔代表市场系统性风险。量化策略追求的是阿尔法，而不是贝塔。
    投资者可以通过低成本指数基金获得贝塔收益，不需要支付高额管理费。
  tags: [term, core-concept, beta, market-risk]

- id: g03
  term: 敞口（Exposure）
  type: term
  source_chapter: 第4章
  author_definition: |
    "阿尔法是一种敞口，宽客借此获利。但我们也注意到，接受这个敞口也会时不时遇到风险。还有另外一些敞口，通常与追求阿尔法收益有关。不能期望这些敞口带来任何收益，但它们经常和追求收益的敞口同时出现。这些敞口称为风险。"
  key_distinction: |
    ≠ "头寸" — 敞口是风险暴露的程度
    ≠ "投资" — 敞口可以是主动承担的（阿尔法）或被动承受的（风险）
    = 投资组合对某种风险因素的暴露程度
  why_it_matters: |
    敞口是风险管理的基本单位。风险管理的目标是：
    - 主动承担有利的敞口（阿尔法）
    - 消除不利的敞口（风险）
  tags: [term, risk-management, exposure]

- id: g04
  term: 风险模型（Risk Model）
  type: term
  source_chapter: 第4章
  author_definition: |
    "相比之下，风险模型旨在帮助宽客控制不太可能带来收益但会造成损失的敞口规模。风险模型存在的主要目的就是控制敞口规模并处理不希望出现的敞口。风险模型的目的是破坏可能带来损失或不确定的事情。"
  key_distinction: |
    ≠ "阿尔法模型" — 风险模型是悲观派，阿尔法模型是乐观派
    ≠ "规避风险" — 风险模型是控制风险，不是消除风险
    = 度量、限制和控制风险敞口的工具
  why_it_matters: |
    风险模型是量化交易系统的核心组件之一。
    好的风险管理可以提高收益的质量和稳定性，而不仅仅是降低损失。
  tags: [term, core-concept, risk-management, risk-model]

- id: g05
  term: 阿尔法模型（Alpha Model）
  type: term
  source_chapter: 第3章
  author_definition: |
    "阿尔法模型就是，为了增加盈利，在投资过程中所使用的一系列技巧或策略。阿尔法模型旨在预测宽客所考虑交易的金融产品未来趋势。从某种意义上看，在量化策略的各个组成部分中，阿尔法模块就像个乐观主义者，它通过对未来的预测来取得收益。"
  key_distinction: |
    ≠ "交易策略" — 阿尔法模型是策略的预测部分
    ≠ "风险模型" — 阿尔法模型追求收益，风险模型控制风险
    = 预测金融资产未来趋势的模型或策略
  why_it_matters: |
    阿尔法模型是量化交易系统的核心，决定了策略是否能产生超额收益。
    阿尔法模型分为理论驱动型和数据驱动型两大类。
  tags: [term, core-concept, alpha-model, prediction]

- id: g06
  term: 理论驱动型阿尔法模型
  type: term
  source_chapter: 第3章
  author_definition: |
    "理论驱动型的宽客通过观察市场行为，寻找可能用来解释这些行为的普适性理论，再依据市场数据来检验该理论是否可以有效解释市场行为。绝大多数理论驱动型交易策略可以较为容易地划分为六类：趋势型、回复型、技术情绪型、价值型/收益型、成长型和品质型。"
  key_distinction: |
    ≠ "数据驱动型" — 理论驱动型先有理论再验证
    ≠ "主观判断" — 理论驱动型仍然是系统化的
    = 基于经济学理论构建的预测模型
  why_it_matters: |
    理论驱动型是最常见的阿尔法模型类型。
    优势是可解释性强，劣势是可能错过数据中的非线性模式。
  tags: [term, alpha-model, theory-driven]

- id: g07
  term: 数据驱动型阿尔法模型
  type: term
  source_chapter: 第3章
  author_definition: |
    "经验型科学家认为，通过对现实情况的经验观察和分析并进行总结，可以取代理论的地位。简言之，这类科学家认为，通过合理使用正确的技术性手段，人们可以识别出隐藏在数据中的模式或规律。经验型科学家有时被戏称为'数据矿工'（data miners）。"
  key_distinction: |
    ≠ "理论驱动型" — 数据驱动型从数据中发现模式
    ≠ "数据挖掘" — 数据驱动型是科学方法，不是随意挖掘
    = 从数据中发现预测模式的模型
  why_it_matters: |
    数据驱动型在大数据时代越来越重要。
    优势是可以发现人类难以察觉的模式，劣势是可解释性差、容易过拟合。
  tags: [term, alpha-model, data-driven]

- id: g08
  term: 投资组合构建模型（Portfolio Construction Model）
  type: term
  source_chapter: 第6章
  author_definition: |
    "投资组合构建模型利用阿尔法模型、风险模型和交易成本模型的结果作为输入变量，主要在追求利润和控制风险、交易相关成本间进行平衡，从而确定最佳的投资组合。"
  key_distinction: |
    ≠ "阿尔法模型" — 投资组合构建模型综合多个模型的结果
    ≠ "简单加权" — 投资组合构建模型是优化问题
    = 综合多个模型结果，构建最优投资组合的模型
  why_it_matters: |
    投资组合构建模型是量化交易系统的决策核心。
    它需要在收益、风险、成本三个目标之间平衡。
  tags: [term, core-concept, portfolio-construction, optimization]

- id: g09
  term: 交易成本模型（Transaction Cost Model）
  type: term
  source_chapter: 第5章
  author_definition: |
    "交易成本模型用于帮助确定从目前的投资组合到新的投资组合（已达到最优投资组合模型）的交易成本。无论交易者预计能获利丰厚还是收益微薄，进行任何交易都需要成本。"
  key_distinction: |
    ≠ "佣金" — 交易成本包括显性成本和隐性成本
    ≠ "固定成本" — 交易成本与交易规模和市场冲击相关
    = 计算交易成本的模型
  why_it_matters: |
    交易成本直接影响净收益。
    好的交易成本模型可以帮助权衡收益与成本，避免过度交易。
  tags: [term, transaction-cost, cost-model]

- id: g10
  term: 执行模型（Execution Model）
  type: term
  source_chapter: 第7章
  author_definition: |
    "执行算法执行所需执行的交易，并利用其他各种输入（如需要执行交易的紧迫性以及市场动态流动性）以高效和低成本的方式执行交易。"
  key_distinction: |
    ≠ "交易" — 执行模型是交易的实施部分
    ≠ "投资策略" — 执行模型关注如何执行，不是执行什么
    = 负责高效执行交易的算法和系统
  why_it_matters: |
    执行质量直接影响策略的实际表现。
    好的执行算法可以降低市场冲击和交易成本。
  tags: [term, execution, algorithm]

- id: g11
  term: 波动率（Volatility）
  type: term
  source_chapter: 第4章
  author_definition: |
    "市场上，对风险的度量有两种被广为认可的方式。第一种是通过纵向方式来度量不确定性，计算不同时期各个产品收益的标准差来度量风险。在金融业中，这个概念通常称为波动率。波动率越高，说明目前的市场风险越大。"
  key_distinction: |
    ≠ "风险" — 波动率是风险的度量方式之一
    ≠ "离散度" — 波动率是时间序列概念，离散度是横截面概念
    = 收益率的标准差，度量价格波动的不确定性
  why_it_matters: |
    波动率是最常用的风险度量指标。
    但需要注意：波动率假设数据服从正态分布，而实际市场数据经常呈现厚尾特征。
  tags: [term, risk-measurement, volatility]

- id: g12
  term: 离散度（Dispersion）
  type: term
  source_chapter: 第4章
  author_definition: |
    "度量风险的第二种方式是，在给定产品范围内对各种金融产品表现的相似水平进行测量，通常是计算在给定时间所有相关金融产品的横截面标准差（cross-sectional standard deviation）。离散度越高，说明所包含在内的金融产品的表现种类越多样化。"
  key_distinction: |
    ≠ "波动率" — 离散度是横截面概念，波动率是时间序列概念
    ≠ "相关性" — 离散度度量表现的多样性
    = 横截面标准差，度量不同资产表现的多样性
  why_it_matters: |
    离散度高意味着市场风险低，因为可以选择多样化的产品。
    离散度低意味着所有资产表现相似，分散化效果差。
  tags: [term, risk-measurement, dispersion]

- id: g13
  term: 模型风险（Model Risk）
  type: term
  source_chapter: 第10章
  author_definition: |
    "模型风险是任何一个量化交易系统都会带给投资者的最基本的风险类型。模型是对现实生活的一种近似表述。如果研究者对一种特定的现象不能很好地进行建模，那么即使在一个通常对该现象有较好效果的环境中，这个策略也可能不会获利。"
  key_distinction: |
    ≠ "市场风险" — 模型风险是模型本身的缺陷
    ≠ "执行错误" — 模型风险是理论基础问题
    = 策略不能精确表述、匹配或预测现实世界现象的风险
  why_it_matters: |
    模型风险是量化交易最根本的风险。
    来源包括：建模的不适宜性、错误设定、执行错误。
  tags: [term, risk-type, model-risk]

- id: g14
  term: 回测（Backtesting）
  type: term
  source_chapter: 第9章
  author_definition: |
    "量化交易者通过输入数据，对信息进行加工，做出交易决策，进而建立输入/输出模型。通过研究，宽客可以判断量化策略的运行情况。回测是用历史数据检验策略表现的方法。"
  key_distinction: |
    ≠ "实盘交易" — 回测是历史模拟
    ≠ "数据挖掘" — 回测是科学方法的一部分
    = 用历史数据检验策略表现的方法
  why_it_matters: |
    回测是策略验证的关键步骤。
    但需要注意：回测结果可能受前视偏差、过拟合等问题影响。
  tags: [term, research, backtesting]

- id: g15
  term: 过拟合（Overfitting）
  type: term
  source_chapter: 第9章
  author_definition: |
    "过拟合是指模型在训练数据上表现很好，但在新数据上表现很差。这通常是因为模型过于复杂，捕捉到了数据中的噪声而非真实模式。"
  key_distinction: |
    ≠ "欠拟合" — 过拟合是模型太复杂，欠拟合是模型太简单
    ≠ "数据挖掘" — 过拟合是数据挖掘的陷阱
    = 模型在历史数据上表现好但未来表现差
  why_it_matters: |
    过拟合是量化策略研发中最常见的陷阱。
    需要通过样本外测试、交叉验证等方法避免。
  tags: [term, research, overfitting]
