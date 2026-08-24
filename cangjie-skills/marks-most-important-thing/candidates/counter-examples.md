# Counter-Examples — 失败模式、反例与投资陷阱

> Stage 1 / Counter-Example Extractor。以下是从原文中完整提取的候选池，暂不进行三重验证、合并或淘汰。`bound_to` 指出该反例限制哪些正向方法论单元。

- id: ce01
  title: 把投资简化成固定公式
  type: counter-example
  source_chapter: 第1章 学习第二层思考
  source_quote: |
    投资不可能简化成一种逻辑运算，然后交给电脑去做。没有一条规则永远行得通；环境不受控制，情况也很少完全相同地重复。
  failure_mode: |
    把复杂、反身且受心理影响的投资决策压缩成一套机械规则，遇到环境变化仍照表执行。
  mechanism: |
    投资方法会改变参与者行为，心理因素又会使因果关系不稳定；原封不动复制过去的方法会削弱其效果。
  warning_signs:
    - 把模型输出当成必然答案
    - 只寻找固定比率或单一公式
    - 忽略环境与参与者行为已经改变
  bound_to:
    - "第二层思考"
    - "预测局限"
    - "适应性决策"
  tags: [counter-example, mechanical-rule, complexity]

- id: ce02
  title: 把好公司直接等同于好投资
  type: counter-example
  source_chapter: 第1章 学习第二层思考
  source_quote: |
    第一层思考会说：「这是一家好公司，就买这支股票吧！」第二层思考则会问：每个人都认为这家公司很好吗？股价是否已经被高估？
  failure_mode: |
    只凭企业质量、产品体验或增长故事买入，而不检查市场共识和当前价格。
  mechanism: |
    好公司的优点会被广泛发现并反映进价格；当大家都喜欢它时，未来上行空间可能已经被预支。
  warning_signs:
    - 研究结论只有“公司很好”
    - 没有估值或价格假设
    - 买入理由来自使用产品的个人体验
  bound_to:
    - "第二层思考"
    - "价值与价格分离"
    - "找出便宜标的"
  tags: [counter-example, valuation, first-level-thinking]

- id: ce03
  title: 相对报酬胜利掩盖绝对亏损
  type: counter-example
  source_chapter: 第1章 学习第二层思考
  source_quote: |
    在大盘下跌五〇％时，负四五％的投资报酬率代表打败大盘，但对我们大多数的人来说，这样的胜利是多么惨烈。
  failure_mode: |
    只追求跑赢基准，不管组合本身是否发生严重的绝对亏损。
  mechanism: |
    基准比较把注意力从资本是否保全转移到排名；市场下跌时，微小的相对优势仍可能摧毁复利和资金目标。
  warning_signs:
    - 汇报只谈相对排名
    - 用“跑赢大盘”为大额亏损辩护
    - 没有绝对回撤或永久损失上限
  bound_to:
    - "风险优先"
    - "防御型投资"
    - "合理预期"
  tags: [counter-example, relative-return, loss]

- id: ce04
  title: 过度相信投资很简单
  type: counter-example
  source_chapter: 第1章 学习第二层思考
  source_quote: |
    证券公司想让你认为每个人都有能力投资；基金公司想让你认为他们会投资。还有人高估自己的控制能力，忽视亏损年份或把亏损归咎于运气。
  failure_mode: |
    相信销售话术、基金包装或个人直觉，把投资当成人人都能稳定成功的简单活动。
  mechanism: |
    简化叙事隐藏了竞争、费用、失败年份和能力差异，使人高估可控性并低估自己没有记录的偏差。
  warning_signs:
    - 只展示成功案例
    - 没有完整、跨周期的业绩记录
    - 把失败都归因于运气
  bound_to:
    - "第二层思考"
    - "绩效归因"
    - "风险优先"
  tags: [counter-example, sales-pitch, overconfidence]

- id: ce05
  title: 盲目接受市场共识
  type: counter-example
  source_chapter: 第1章 学习第二层思考
  source_quote: |
    尽管同意广泛接受的市场共识很轻松，但是这样通常不会获得高于平均水准的报酬。
  failure_mode: |
    仅重复新闻、共识预测和大众已经知道的理由，却期待得到超额报酬。
  mechanism: |
    共识已经进入价格；在零和竞争中，和所有人做相同的事只能获得平均结果。
  warning_signs:
    - 论据都能在主流媒体找到
    - 没有说明自己与共识的差异
    - 交易理由只是“大家都这么看”
  bound_to:
    - "第二层思考"
    - "价值与价格分离"
  tags: [counter-example, consensus, herd]

- id: ce06
  title: 把高风险误认为高报酬保证
  type: counter-example
  source_chapter: 第2章 了解效率市场与局限
  source_quote: |
    他们忽略多头行情时很容易忘记的事：因为如果要指望用高风险投资来创造高收益，那这些投资也算不上是高风险了。
  failure_mode: |
    在顺风市场中看到高风险资产上涨，就认定承担更多风险必然带来更多报酬。
  mechanism: |
    高风险只扩大结果分布并提高亏损概率，不承诺正向补偿；多头期会暂时遮蔽尾部风险。
  warning_signs:
    - 只看上涨期数据
    - 用历史高收益证明风险“值得”
    - 没有分析亏损情景和风险补偿来源
  bound_to:
    - "理解风险"
    - "合理预期"
    - "防御型投资"
  tags: [counter-example, risk, bull-market]

- id: ce07
  title: 把市场有效当成价格永远正确
  type: counter-example
  source_chapter: 第2章 了解效率市场与局限
  source_quote: |
    我谈到效率，意思是「快速、尽快整合资讯」，而不是「正确」。雅虎股价从二〇〇〇年一月的两百三十七美元到二〇〇一年四月的十一美元。
  failure_mode: |
    因为价格迅速反映信息，就放弃独立估值，认为市场价格必然等于价值。
  mechanism: |
    市场能快速聚合带有情绪和偏误的共识；快速定价不等于正确估价。
  warning_signs:
    - “市场已经定价，所以不必分析”
    - 把流动性或关注度当成正确性的证明
    - 不检查价格与内在价值的差距
  bound_to:
    - "第二层思考"
    - "准确估计实质价值"
    - "找出便宜标的"
  tags: [counter-example, efficient-market, mispricing]

- id: ce08
  title: 把无效率当成免费午餐
  type: counter-example
  source_chapter: 第2章 了解效率市场与局限
  source_quote: |
    无效率市场并不一定会给参与的投资人丰厚的报酬……它们提供错误定价这个原料，允许一些人成为市场赢家，一些人成为输家。
  failure_mode: |
    发现市场可能无效后，就以为任何参与者都能获得超额收益。
  mechanism: |
    错误定价只是机会的必要条件；还需要更好的信息、分析和执行，且交易对手可能正是更有洞察力的一方。
  warning_signs:
    - 只证明市场有偏差，不证明自己有优势
    - 把“便宜”当成“容易赚钱”
    - 不问卖方为何愿意交易
  bound_to:
    - "第二层思考"
    - "增加价值"
    - "找出便宜标的"
  tags: [counter-example, inefficiency, free-lunch]

- id: ce09
  title: 把五十项相关资产误认为分散投资
  type: counter-example
  source_chapter: 第2章 了解效率市场与局限
  source_quote: |
    我们可能买进五十档相关的证券，却误认为我们已经分散投资。
  failure_mode: |
    只增加持仓数量，不检查持仓在压力情景下是否会一起下跌。
  mechanism: |
    分散效果取决于相关性和共同风险来源，而不是证券数量；相关资产会在危机中同时放大损失。
  warning_signs:
    - 组合看起来很分散但行业/因子高度重合
    - 只统计持仓数量
    - 没有共同压力测试
  bound_to:
    - "控制风险"
    - "防御型投资"
  tags: [counter-example, diversification, correlation]

- id: ce10
  title: 把波动性等同于全部风险
  type: counter-example
  source_chapter: 第5章 理解风险
  source_quote: |
    风险等于波动性……我对这个风险的定义不以为然。然而我并不认为大多数投资人关心波动性这种风险。
  failure_mode: |
    只用历史波动率、标准差或 beta 衡量风险，忽略永久亏损、杠杆和流动性风险。
  mechanism: |
    波动既可能是暂时价格变化，也可能掩盖真正的资本损失；低波动资产也可能在尾部事件中永久损失。
  warning_signs:
    - 风险报告只有波动率
    - 没有估计本金永久损失
    - 低波动被当成安全
  bound_to:
    - "理解风险"
    - "确认风险"
    - "控制风险"
  tags: [counter-example, volatility, permanent-loss]

- id: ce11
  title: 把风险当成可见、可量化的常数
  type: counter-example
  source_chapter: 第6章 确认风险
  source_quote: |
    风险主要是未来可能发生的事情，而且风险只有在发生之后才会被观察到。风险意味着未来的不确定性。
  failure_mode: |
    因为过去没有发生损失，或模型给出低风险，就假定未来风险很小。
  mechanism: |
    风险属于未来分布而非已实现结果；平静时期会压低风险感知并鼓励更多承担风险。
  warning_signs:
    - 用“从未亏损”替代风险分析
    - 依赖短样本和后视统计
    - 只分析最可能情景
  bound_to:
    - "确认风险"
    - "预测局限"
    - "合理预期"
  tags: [counter-example, uncertainty, hindsight]

- id: ce12
  title: 在高杠杆下把小错误变成出局
  type: counter-example
  source_chapter: 第7章 控制风险
  source_quote: |
    错误边际包括……戒除杠杆投资；而且分散投资。强调这些要素会在多头行情时限制获利，但会让你有最大的机会在事情发展不好时毫发无伤。
  failure_mode: |
    为了放大回报使用杠杆，导致本来可等待修正的判断错误变成追加保证金或被迫卖出。
  mechanism: |
    杠杆对多空两端都放大；它压缩时间和流动性缓冲，使投资者无法等到价值回归。
  warning_signs:
    - 需要持续融资才能持有
    - 估值下跌会触发强平
    - 回报目标必须靠杠杆才能实现
  bound_to:
    - "控制风险"
    - "防御型投资"
    - "错误边际"
  tags: [counter-example, leverage, forced-sale]

- id: ce13
  title: 把周期当成永远延续的趋势
  type: counter-example
  source_chapter: 第8章 注意景气循环
  source_quote: |
    经济和市场周期会上下起伏，不管这时往哪个方向前进，大部分的人都相信他们会永远朝相同的方向前进。
  failure_mode: |
    根据近期繁荣或衰退外推未来，把周期性改善当成永久趋势。
  mechanism: |
    周期的参与者会因当前结果改变行为，供给、资本和风险偏好最终反转并推动均值回归。
  warning_signs:
    - 连续好几年上涨就认为“这次不同”
    - 只用近期增长率做预测
    - 忽略资本供给和竞争反应
  bound_to:
    - "注意景气循环"
    - "察觉所在的景气位置"
    - "预测局限"
  tags: [counter-example, cycle, extrapolation]

- id: ce14
  title: 在钟摆极端位置加入群体
  type: counter-example
  source_chapter: 第9章 意识到钟摆效应
  source_quote: |
    钟摆的摆荡会使群众在高价买进、低价卖出。因此，身为群众之一后患无穷。
  failure_mode: |
    在乐观和悲观达到极端时，跟随多数人的买入或卖出行动。
  mechanism: |
    群体行为把价格推离价值；极端位置意味着边际买家或卖家已经耗尽，趋势的风险收益比恶化。
  warning_signs:
    - 买入理由是“不能错过”
    - 大家都认为价格还会永远上涨/下跌
    - 估值与情绪同时达到极端
  bound_to:
    - "察觉钟摆效应"
    - "反向投资"
    - "防御型投资"
  tags: [counter-example, pendulum, herd]

- id: ce15
  title: 把反向投资变成机械反着做
  type: counter-example
  source_chapter: 第11章 反向投资
  source_quote: |
    只与群众做出相反的事是不够的……你必须根据理性和分析，确认是否有潜在获利的可能，知道群众为什么是错的。
  failure_mode: |
    因为多数人买入就卖出、因为多数人卖出就买入，不做价值和风险分析。
  mechanism: |
    群众也可能暂时正确，或“反向”本身已经成为流行；没有对错误机制的解释，就无法承受继续逆势的压力。
  warning_signs:
    - 唯一论据是“大家都错”
    - 无法说明共识错在哪里
    - 没有价值、价格和下行风险估计
  bound_to:
    - "反向投资"
    - "第二层思考"
    - "找出便宜标的"
  tags: [counter-example, contrarianism, analysis]

- id: ce16
  title: 把价格过高等同于马上下跌
  type: counter-example
  source_chapter: 第11章 反向投资
  source_quote: |
    「价格过高」与「明天就开始下跌」完全不同。市场价格会过于高估或低估，而且会停在那里很久，甚至好几年。
  failure_mode: |
    发现估值极端后立即押注拐点，无法承受趋势继续运行的时间。
  mechanism: |
    价格偏离价值可以持续；市场情绪、资金流和叙事会让错误定价进一步扩大。
  warning_signs:
    - 交易计划依赖具体反转日期
    - 只要价格继续上涨就否定估值
    - 仓位无法承受多年逆风
  bound_to:
    - "反向投资"
    - "耐心等待时机"
    - "周期与钟摆"
  tags: [counter-example, timing, mispricing]

- id: ce17
  title: 把“反向”本身追成新共识
  type: counter-example
  source_chapter: 第11章 反向投资
  source_quote: |
    当「人人」得出「群众都是错误」的结论时，我认为这时反向投资显然变得过于热门，因此反向投资才会被错认成群体行为。
  failure_mode: |
    因为“反主流”很受欢迎，就买入任何被包装成冷门、逆向或悲观的标的。
  mechanism: |
    反向标签会被市场商品化；当所有人都声称自己逆向时，标签不再代表独立判断。
  warning_signs:
    - 逆向叙事在媒体和社群中泛滥
    - “别人不懂”成为主要论据
    - 冷门身份替代了价值分析
  bound_to:
    - "反向投资"
    - "第二层思考"
  tags: [counter-example, contrarianism, popularity]

- id: ce18
  title: 因为恐惧而等待所有不确定性消失
  type: counter-example
  source_chapter: 第11章 反向投资
  source_quote: |
    当刀子停止落下，尘埃便已经落定，不确定性都解决了，那时已没有获利最丰富的便宜标的留下来。
  failure_mode: |
    只有等坏消息结束、价格稳定、所有风险明朗后才买入。
  mechanism: |
    最高预期回报通常出现在信息最差、最不舒服的阶段；等待确认会让价格先回到安全但昂贵的位置。
  warning_signs:
    - 交易条件要求“确定性”
    - 只在市场情绪恢复后行动
    - 将不确定性本身视为不能投资
  bound_to:
    - "反向投资"
    - "耐心等待时机"
    - "合理预期"
  tags: [counter-example, uncertainty, missed-opportunity]

- id: ce19
  title: 把低价误认为不会再跌
  type: counter-example
  source_chapter: 第12章 找出便宜标的
  source_quote: |
    便宜远远不等于不再进一步下跌。价格过低远远不等于即将上涨。
  failure_mode: |
    仅因价格已经下跌或低于估值，就假定下行空间已经耗尽。
  mechanism: |
    价值估计可能错误，市场也会过度反应；便宜资产仍可能因基本面恶化、流动性或情绪继续下跌。
  warning_signs:
    - 只看跌幅，不重估价值
    - 没有继续下跌的情景
    - 加仓规则只依据价格更低
  bound_to:
    - "找出便宜标的"
    - "确认风险"
    - "耐心等待时机"
  tags: [counter-example, value-trap, falling-knife]

- id: ce20
  title: 追求完美低点而错过机会
  type: counter-example
  source_chapter: 第13章 耐心等待时机
  source_quote: |
    坚持唯有符合完美条件（例如只买在低点）才进场的投资人，可能会因此错过很多机会。希望能在低点买进是个不切实际的作法。
  failure_mode: |
    把买在最低点当成入场前提，因无法确认拐点而长期空仓或错过便宜价格。
  mechanism: |
    低点只能事后确认；市场反弹会收紧供给和流动性，使等待确认的投资者失去赔率。
  warning_signs:
    - 反复等待更低价格
    - 交易计划没有分批或容错
    - 把不是最低价视为失败
  bound_to:
    - "耐心等待时机"
    - "找出便宜标的"
    - "反向投资"
  tags: [counter-example, market-timing, perfectionism]

- id: ce21
  title: 相信自己能稳定预测宏观未来
  type: counter-example
  source_chapter: 第14章 认清预测的局限
  source_quote: |
    很多投资人以为自己知道经济和市场的未来走向，并据此采取行动……根据强烈坚持但不正确的预期来投资，就是造成重大潜在亏损的根源。
  failure_mode: |
    把宏观预测、利率判断或市场方向判断当成高确信度行动依据。
  mechanism: |
    宏观变量相互作用且结果分布宽；即使预测方向偶尔正确，也不代表时点、幅度和资产反应正确。
  warning_signs:
    - 组合高度依赖单一宏观情景
    - 使用“肯定会”描述未来
    - 没有预案和概率范围
  bound_to:
    - "预测局限"
    - "合理预期"
    - "防御型投资"
  tags: [counter-example, forecasting, macro]

- id: ce22
  title: 把一次预测成功当成可复制能力
  type: counter-example
  source_chapter: 第14章 认清预测的局限
  source_quote: |
    在经济预测和投资管理上通常都有人可以准确预测，但是很少有相同的人能成功预测两次。
  failure_mode: |
    根据短期准确预测、热门专家或单次成功交易，扩大仓位并把运气当成技能。
  mechanism: |
    随机结果会制造看似有能力的样本；缺乏长期、跨环境记录时，无法区分洞察和偶然。
  warning_signs:
    - 只展示最近一次成功
    - 忽略失败预测
    - 成功后迅速提高风险暴露
  bound_to:
    - "认识运气扮演的角色"
    - "绩效归因"
    - "合理预期"
  tags: [counter-example, luck, track-record]

- id: ce23
  title: 用故事代替概率分布
  type: counter-example
  source_chapter: 第15章 察觉所在的景气位置
  source_quote: |
    很多人以为世界是按照秩序在运转，能被掌握和预期。他们忽略事物的随机性，以及未来事件发展的机率分布。
  failure_mode: |
    只构建一个最喜欢的未来故事，并按该故事集中下注。
  mechanism: |
    叙事压缩了多种可能结果，令投资者忽略低概率高损失事件和相反情景。
  warning_signs:
    - 研究报告只有单一路径
    - 没有列出不利情景
    - 用故事流畅度代替概率和赔率
  bound_to:
    - "预测局限"
    - "确认风险"
    - "错误边际"
  tags: [counter-example, narrative, probability]

- id: ce24
  title: 在高点乐观、低点悲观
  type: counter-example
  source_chapter: 第15章 察觉所在的景气位置
  source_quote: |
    群众在高点的时候很乐观，在低点的时候很悲观。因此，为了获利，我们必须在高点乐观蔓延时，以及在低点悲观主导时，抱持怀疑的心态。
  failure_mode: |
    把群体情绪当作现实价值的确认，在上涨时追涨、在崩跌时割肉。
  mechanism: |
    情绪在价格极端时被价格本身强化，形成反馈回路，迫使投资者在赔率最差的位置行动。
  warning_signs:
    - “价格上涨证明乐观正确”
    - “价格下跌证明资产没有价值”
    - 新闻情绪与仓位方向高度一致
  bound_to:
    - "察觉所在的景气位置"
    - "反向投资"
    - "对抗情绪"
  tags: [counter-example, sentiment, cycle]

- id: ce25
  title: 把运气造成的结果归功于自己
  type: counter-example
  source_chapter: 第16章 认识运气扮演的角色
  source_quote: |
    运气与技巧之间的区别，在短期内很难分辨。只有经过很长时间，才能看出一个人的结果主要是来自运气还是技巧。
  failure_mode: |
    因为一次或数次盈利就确认自己的分析能力，随后复制相同风险。
  mechanism: |
    结果由技能和外部事件共同生成；小样本、顺风环境和幸存者偏差会放大能力错觉。
  warning_signs:
    - 只复盘“我做对了什么”
    - 没有记录原始概率和当时信息
    - 盈利后变得更自信、更集中
  bound_to:
    - "认识运气扮演的角色"
    - "增加价值"
    - "合理预期"
  tags: [counter-example, luck, attribution]

- id: ce26
  title: 让贪婪替代风险判断
  type: counter-example
  source_chapter: 第10章 对抗情绪带来的负面影响
  source_quote: |
    这些因素使人们拋弃独立判断与怀疑精神，压抑与生俱来的风险趋避心态去相信不合理的事。
  failure_mode: |
    因为想赚更多，接受自己平时会认为不合理的估值、杠杆和承诺。
  mechanism: |
    盈利欲望提高风险容忍度，随后上涨又反过来证明贪婪合理，形成自我强化的泡沫回路。
  warning_signs:
    - “这次机会不能错过”
    - 为达到目标收益不断增加风险
    - 对明显矛盾不再追问
  bound_to:
    - "对抗情绪"
    - "合理预期"
    - "风险优先"
  tags: [counter-example, greed, cognitive-bias]

- id: ce27
  title: 用嫉妒和相对排名破坏投资流程
  type: counter-example
  source_chapter: 第10章 对抗情绪带来的负面影响
  source_quote: |
    答案就在于我们有跟别人比较的倾向，这会对原本有建设性、分析性的投资流程产生有害的影响。
  failure_mode: |
    因为别人赚得更多就追逐其资产，因为暂时落后基准就放弃原本稳健的策略。
  mechanism: |
    相对表现取代绝对目标，迫使投资者拥抱拥挤风险；短期比较还会惩罚耐心和防御。
  warning_signs:
    - 交易理由是“别人都赚到了”
    - 频繁与同业或基准比较
    - 因短期落后而改变策略
  bound_to:
    - "合理预期"
    - "防御型投资"
    - "对抗情绪"
  tags: [counter-example, envy, relative-performance]

- id: ce28
  title: 让自负把风险承担变成名声竞赛
  type: counter-example
  source_chapter: 第10章 对抗情绪带来的负面影响
  source_quote: |
    由于在上涨的市场承担风险可以得到奖励，为了透过获取高额报酬来引人注意，自负能让投资人积极行动。
  failure_mode: |
    为了证明聪明、勇敢或领先市场，主动承担不必要的高风险。
  mechanism: |
    多头期会奖励轻率行为并提供社会认同；成功强化自我叙事，直到环境反转。
  warning_signs:
    - 关心“看起来聪明”胜过风险调整后回报
    - 把谨慎视为软弱
    - 用高收益展示个人能力
  bound_to:
    - "防御型投资"
    - "增加价值"
    - "对抗情绪"
  tags: [counter-example, ego, risk-taking]

- id: ce29
  title: 在压力下投降并追随流行
  type: counter-example
  source_chapter: 第10章 对抗情绪带来的负面影响
  source_quote: |
    投资人会尽可能地坚持自己的信念，但是当无法抗拒经济或心理压力时，他们就会举手投降，跟上流行。
  failure_mode: |
    因为逆势持仓长期不赚钱、别人获利或客户施压，放弃已验证的判断并在趋势末端追入。
  mechanism: |
    自我怀疑、从众压力和错失恐惧随时间累积；趋势持续越久，错误行为越显得合理。
  warning_signs:
    - 反复查看别人收益
    - 说“我不想再显得像个傻瓜”
    - 在趋势后期突然改变策略
  bound_to:
    - "反向投资"
    - "耐心等待时机"
    - "对抗情绪"
  tags: [counter-example, capitulation, herd]

- id: ce30
  title: 忽略价值而追逐科技泡沫
  type: counter-example
  source_chapter: 第10章 对抗情绪带来的负面影响
  source_quote: |
    投资人在泡沫期间拋弃常识，忽略了并不是所有企业都能成为赢家、提供免费服务并不容易获利，以及在没有任何盈余下利用高倍数营收评估亏钱公司的危害。
  failure_mode: |
    因科技潜力、IPO 首日上涨和媒体赞誉，给没有盈利的公司支付极高估值。
  mechanism: |
    真实创新被外推成所有公司都会成功；上涨吸引更多买盘，估值和信念互相强化，最终回撤超过基本面能承受的范围。
  warning_signs:
    - 只用收入倍数给亏损公司估值
    - 以首日涨幅证明投资合理
    - 不知道公司业务仍愿意买入
  bound_to:
    - "价值与价格分离"
    - "对抗情绪"
    - "合理预期"
  tags: [counter-example, bubble, technology]

- id: ce31
  title: 相信“灵丹妙药”或免费午餐
  type: counter-example
  source_chapter: 第18章 避开投资陷阱
  source_quote: |
    灵丹妙药并不存在。没有哪一个投资策略可以在没有风险下创造高报酬。
  failure_mode: |
    相信一种简单、稳定、可复制且几乎没有风险的致富策略。
  mechanism: |
    短期成功会吸引崇拜和资金，隐藏风险在平静时期不显现；策略拥挤后机会消失或损失集中爆发。
  warning_signs:
    - “稳赚不赔”或“适用于所有市场”
    - 只展示顺风期回报
    - 不说明收益来自什么风险或交易对手
  bound_to:
    - "避开投资陷阱"
    - "合理预期"
    - "认识运气扮演的角色"
  tags: [counter-example, silver-bullet, fraud]

- id: ce32
  title: 因短期高收益崇拜策略或经理人
  type: counter-example
  source_chapter: 第18章 避开投资陷阱
  source_quote: |
    当某个市场、某个人或某个投资技术短期创造可观的报酬时，通常会吸引大家过多且毫不怀疑的崇拜。
  failure_mode: |
    把短期漂亮业绩当成稳定技能，忽略样本长度、环境和风险暴露。
  mechanism: |
    结果先于过程被观察，幸存者偏差和媒体叙事把运气包装成能力，资金随后在高位追入。
  warning_signs:
    - 只看最近一两年
    - 不分析策略在不利环境的表现
    - 资产规模增长后仍假定机会不变
  bound_to:
    - "认识运气扮演的角色"
    - "增加价值"
    - "绩效评估"
  tags: [counter-example, performance-chasing, survivorship-bias]

- id: ce33
  title: 忽略历史教训与金融记忆过短
  type: counter-example
  source_chapter: 第18章 避开投资陷阱
  source_quote: |
    极为短暂的金融记忆……过去的经验受到排斥，被认为只是没有洞察力去体会当前惊人奇迹的古老避难所。
  failure_mode: |
    以“当前环境不同”为由，认为过去的泡沫、崩盘和风险规律已经失效。
  mechanism: |
    新叙事让人忘记旧约束；当参与者不再记得惩罚，风险承受会再次扩张并重演周期。
  warning_signs:
    - “这次真的不同”
    - 不复盘历史相似案例
    - 把风险警告称为过时经验
  bound_to:
    - "注意景气循环"
    - "避开投资陷阱"
    - "察觉所在的景气位置"
  tags: [counter-example, memory, historical-analogy]

- id: ce34
  title: 对“好到不像是真的”停止怀疑
  type: counter-example
  source_chapter: 第18章 避开投资陷阱
  source_quote: |
    投资的过程需要强烈的怀疑……怀疑不足会造成投资亏损。事后检视金融崩盘时，经典的话一次又一次出现：「这好得不像是真的」。
  failure_mode: |
    因为想要相信高回报承诺，就主动忽略收益、风险和解释之间的不一致。
  mechanism: |
    愿望使人相信自己希望为真的东西；价格上涨又提供社会证明，进一步压低质疑阈值。
  warning_signs:
    - 回报异常稳定且高
    - 无法解释收益来源
    - 质疑被视为错失机会或不够聪明
  bound_to:
    - "避开投资陷阱"
    - "合理预期"
    - "对抗情绪"
  tags: [counter-example, skepticism, fraud]

- id: ce35
  title: 从众而放弃独立判断
  type: counter-example
  source_chapter: 第10章 对抗情绪带来的负面影响
  source_quote: |
    真正的受试者有很高的机率会忽略眼前所见，说出与其他群体成员一样的答案，即使他们很显然知道答案是错的。
  failure_mode: |
    明知证据与群体意见冲突，仍为了不被排斥而采取共识行动。
  mechanism: |
    同侪一致意见制造社会压力，使个体把归属感置于事实判断之上；市场价格又会把这种一致意见反馈给参与者。
  warning_signs:
    - 担心“只有我看错”
    - 决策前先问别人怎么做
    - 把共识人数当成证据强度
  bound_to:
    - "第二层思考"
    - "反向投资"
    - "对抗情绪"
  tags: [counter-example, conformity, social-proof]

- id: ce36
  title: 因看似便宜而接住没有价值的刀
  type: counter-example
  source_chapter: 第11章 反向投资
  source_quote: |
    我会这样说，没有人跳到高速公路上一台货车的前面，并不表示你就应该与其他人相反，跳进去。
  failure_mode: |
    仅因别人不敢买、价格大跌或市场恐慌，就把任何下跌资产都视为反向机会。
  mechanism: |
    低价可能反映永久性价值损失、流动性断裂或商业失败；反向行动若没有价值判断，会把风险误称为勇气。
  warning_signs:
    - 只依据跌幅或市场悲观
    - 无法说明资产仍有什么持久价值
    - 加码建立在“越跌越便宜”单一逻辑上
  bound_to:
    - "反向投资"
    - "找出便宜标的"
    - "确认风险"
  tags: [counter-example, falling-knife, value-trap]

- id: ce37
  title: 为满足高回报目标而不断加风险
  type: counter-example
  source_chapter: 第20章 合理预期
  source_quote: |
    追求较高的报酬通常都需要增加承受的风险，像是投资较高风险的股票或债券、更集中投资，或是增加杠杆操作。
  failure_mode: |
    先设定过高回报目标，再倒推承担自己原本不愿承担的风险。
  mechanism: |
    目标没有与市场环境、资本约束和可承受损失匹配；为填补目标缺口，投资者逐步集中、杠杆化和降低安全边际。
  warning_signs:
    - “我需要 X%，所以必须加杠杆”
    - 目标不随无风险利率或估值改变
    - 只讨论收益，不讨论失败后果
  bound_to:
    - "合理预期"
    - "风险优先"
    - "防御型投资"
  tags: [counter-example, return-target, leverage]

- id: ce38
  title: 相信马多夫式的稳定高收益
  type: counter-example
  source_chapter: 第20章 合理预期
  source_quote: |
    那马多夫怎么能创造出跟股票一样高的报酬，而且又像国库券一样可靠？他的报酬简单到找不到合理的解释。
  failure_mode: |
    因收益不高但异常稳定，就认为产品兼具股票回报和国库券可靠性。
  mechanism: |
    高回报与低波动的组合需要强有力、可核验的机制；无法解释的平滑收益可能意味着造假、隐藏杠杆或未披露尾部风险。
  warning_signs:
    - 多年几乎没有亏损月份
    - 收益与市场环境脱钩
    - “检查过”却不能说出“检查过且合理”
  bound_to:
    - "合理预期"
    - "避开投资陷阱"
    - "认识运气扮演的角色"
  tags: [counter-example, Madoff, smooth-returns]

- id: ce39
  title: 把市场时机预测当成入场条件
  type: counter-example
  source_chapter: 第20章 合理预期
  source_quote: |
    「低点」只有事后回顾才能确定。没有方法可以知道何时价格会达到无法持续再跌的低点。
  failure_mode: |
    试图精确预测底部和顶部，以时间判断替代价格、价值和风险判断。
  mechanism: |
    拐点不可事前确认；等待确认会错过便宜筹码，过早押注又可能承受继续下跌。
  warning_signs:
    - 仓位完全依赖一个日期或点位
    - 反复修改“底部预测”
    - 因无法预测而放弃分批和容错
  bound_to:
    - "预测局限"
    - "耐心等待时机"
    - "找出便宜标的"
  tags: [counter-example, market-timing, uncertainty]

- id: ce40
  title: 用“足够高”替代“足够好”
  type: counter-example
  source_chapter: 第20章 合理预期
  source_quote: |
    太高的报酬不值得追求，而且不值得为此承担风险。投资人应该考虑什么是「足够的报酬」。
  failure_mode: |
    把超过目标的额外收益视为必需，持续追逐更高收益而牺牲安全边际。
  mechanism: |
    边际收益通常需要非线性增加风险；额外回报对资金目标的帮助有限，却可能造成不可逆损失。
  warning_signs:
    - “还能赚更多”成为加仓理由
    - 不愿在合理回报处止盈或降风险
    - 把保守结果视为失败
  bound_to:
    - "合理预期"
    - "防御型投资"
    - "风险优先"
  tags: [counter-example, enough-return, greed]

- id: ce41
  title: 把分散数量当成错误边际
  type: counter-example
  source_chapter: 第17章 采取防御型投资策略
  source_quote: |
    大部分投资人认为分散投资就是持有很多不同的投资标的，但是很少人了解到，有效分散风险取决于组合在各种环境中做出不同的反应。
  failure_mode: |
    用更多标的掩盖共同暴露，误以为组合已经有足够安全边际。
  mechanism: |
    同一宏观因子、行业、融资来源或流动性会让名义上不同的资产同步损失。
  warning_signs:
    - 只报告持仓数量
    - 相关性在压力期显著上升
    - 所有资产依赖同一流动性环境
  bound_to:
    - "控制风险"
    - "防御型投资"
    - "错误边际"
  tags: [counter-example, diversification, margin-of-safety]

- id: ce42
  title: 用进攻型收益掩盖防守失效
  type: counter-example
  source_chapter: 第19章 增加价值
  source_quote: |
    不管是在下跌行情限制亏损的防御型投资人，或是在上涨市场赚得收益的进攻型投资人，都不能证明他们拥有投资技巧。
  failure_mode: |
    只看适合自己风格的市场阶段，就把风格暴露或 beta 误认成增加价值。
  mechanism: |
    进攻型策略在牛市天然占优，防御型策略在熊市天然占优；只有跨环境的不对称表现才显示技能。
  warning_signs:
    - 只展示牛市或熊市成绩
    - 没有风格调整后的比较
    - 盈利与市场方向高度同步
  bound_to:
    - "增加价值"
    - "认识运气扮演的角色"
    - "绩效评估"
  tags: [counter-example, beta, style-drift]

- id: ce43
  title: 用规模增长继续投资已不存在的机会
  type: counter-example
  source_chapter: 第19章 增加价值
  source_quote: |
    有了更多资金之后，经理人常会投资在没列入长期良好纪录名单的资产。当投资机会减少时，橡树资本确实可以获得资本回报。
  failure_mode: |
    因过去成功而持续吸收资金，把规模扩张和部署资本当成必须完成的目标。
  mechanism: |
    可投资机会有限，规模会降低灵活性和赔率；为投资而投资会迫使管理人降低标准。
  warning_signs:
    - 资金流入后筛选标准放宽
    - 现金被视为拖累而非期权
    - 交易数量成为绩效考核目标
  bound_to:
    - "增加价值"
    - "找出便宜标的"
    - "耐心等待时机"
  tags: [counter-example, asset-growth, opportunity-set]

- id: ce44
  title: 以为自己能免疫人性偏误
  type: counter-example
  source_chapter: 第10章 对抗情绪带来的负面影响
  source_quote: |
    相信自己不会受到本章描述的力量影响的投资人很有可能会咎由自取。如果它们对别人的影响可以大到撼动整个市场，为什么不会影响你？
  failure_mode: |
    把贪婪、恐惧、从众和自负视为别人的问题，不为自己设置外部约束。
  mechanism: |
    个体与群体共享同一心理机制；极端环境会削弱自我判断，越自信越容易撤掉防护。
  warning_signs:
    - 认为自己“不会追高或恐慌”
    - 没有预先写下退出和加仓条件
    - 在极端行情中减少复核
  bound_to:
    - "对抗情绪"
    - "防御型投资"
    - "检查清单决策"
  tags: [counter-example, bias, self-exemption]
