# 三重验证通过的候选单元

> 验证状态：进行中
> 最后更新：2026-08-14

---

## 批次1: Frameworks (fw001-fw033)

**验证进度**: 32/33 通过，通过率 97%

### fw001: 简单至上原则
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第1章: 作者从机构亏损到独立盈利的转折，使用简单策略
    - 第2章: 策略变形方法论，简单调整比复杂优化更有效
    - 第3章: 参数复杂度与过拟合权衡，简单模型更可靠
    - 第7章: AI方法适用性判断，强调概念简单
V2_predictive_power:
  passed: true
  novel_question: "如果用AI自动生成的策略参数怎么办？"
  derived_answer: "仍然应该从最简单的模型开始，AI生成的复杂参数同样需要样本外验证"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'要简化'，但作者的反直觉见解是：'在机构用复杂数学亏损后，独立后用简单策略盈利'——这是基于亲身经验的结构化论证"
```

### fw002: 策略选择四要素约束框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章2.1节: 工作时间、编程水平、交易资本、目标四要素
    - 第2章2.1.3节: 资本规模决定策略类型的详细讨论
    - 第4章: 设备配置受资本约束的具体应用
V2_predictive_power:
  passed: true
  novel_question: "如果用AI自动选策略怎么办？"
  derived_answer: "AI也必须遵守四要素约束，不能推荐超出用户资本或编程能力的策略"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'选策略看收益'，作者的反直觉见解是'先评估自己的约束条件，再看策略好不好'"
```

### fw003: 资本规模决定策略类型框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章2.1.3节: 资本规模是策略选择的硬约束
    - 第4章: 自营交易公司vs零售账户选择取决于杠杆需求
V2_predictive_power:
  passed: true
  novel_question: "如果资本增加10倍，策略选择会如何调整？"
  derived_answer: "从单向交易转向配对交易，从高频转向低频，从小容量转向大容量"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'喜欢什么策略选什么'，作者的反直觉见解是'能负担什么策略选什么'"
```

### fw004: 策略变形方法论
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章开头: 财富实验室论坛策略通过缩短持有期、改变建仓清仓时点成为主要盈利来源
    - 第3章: 清仓策略从收盘改为开盘，夏普比率从-3.19升至0.78
V2_predictive_power:
  passed: true
  novel_question: "如果基础策略完全失效怎么办？"
  derived_answer: "系统性尝试变形：持有期、进出场时点、参数、股票池，而不是寻找'完美策略'"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'找最好的策略'，作者的反直觉见解是'现成策略经不起严格回测，真正有价值的是你自己的变形和窍门'"
```

### fw005: 分享优于保密原则
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章开头: 博客分享策略能获得读者反馈，及时筛掉劣等策略
    - 第2章: 读者否定作者推荐的季节性策略的案例
V2_predictive_power:
  passed: true
  novel_question: "如果竞争对手看到我的博客怎么办？"
  derived_answer: "基础策略早已公开，保密没有意义。真正有价值的是你自己的变形和窍门"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'策略要保密'，作者的反直觉见解是'分享策略比保密更有益'——基于网络效应的开放源码思维"
```

### fw006: 独立交易员可行性论证框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第1章1.1节: Thorp、Simons从自有资金起步的历史先例
    - 第8章: 独立交易员的核心优势是'容量'的理论论证
V2_predictive_power:
  passed: true
  novel_question: "2025年独立交易员还能成功吗？"
  derived_answer: "只要金融市场需要瞬时流动性，小容量策略就有生存空间"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'个人打不过机构'，作者的反直觉见解是'独立交易员在小容量策略上有结构性优势'"
```

### fw007: 量化交易业务特性框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第1章1.2节: 易扩大、节省时间、营销非必需三大特性
    - 第1章: 与互联网创业的对比案例（3倍投资、5倍人力、24倍时间失败）
V2_predictive_power:
  passed: true
  novel_question: "量化交易和其他在线生意有什么区别？"
  derived_answer: "量化交易的规模易改变（只需修改杠杆参数）、高度自动化（每天2-3小时）、无需营销"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'生意都要慢慢做大'，作者的反直觉见解是'量化交易扩大规模只需修改一个参数'"
```

### fw008: 理想交易员画像模型
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第1章1.1节: 三个必要条件（技能基础、财务缓冲、情绪稳定）
    - 第6章: 心理准备的具体讨论
V2_predictive_power:
  passed: true
  novel_question: "我没有金融博士学位能做量化交易吗？"
  derived_answer: "不需要高学历，需要：金融或编程经历、足够存款撑过收入空窗期、情绪稳定"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'量化交易需要高学历'，作者的反直觉见解是'关键是情绪平衡和足够存款'"
```

### fw009: 夏普比率优于收益率原则
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章2.1.4节: 高夏普比率可以通过杠杆获得更高收益的数学论证
    - 第2章: SAC资本风控负责人只看收益率的反面案例
    - 第7章: 高频交易具有更高夏普比率的讨论
V2_predictive_power:
  passed: true
  novel_question: "如果两个策略收益率相同，选哪个？"
  derived_answer: "选夏普比率更高的，因为可以用更高杠杆，最终杠杆收益率更高"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'追求高收益'，作者的反直觉见解是'高夏普+高杠杆 > 高收益+低杠杆'——数学证明"
```

### fw010: 策略快速筛选六问法
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章2.2节: 六个筛选问题的详细列表
    - 第2章2.2.1-2.2.7节: 每个问题的具体讨论
V2_predictive_power:
  passed: true
  novel_question: "如何快速判断一个策略值不值得回测？"
  derived_answer: "先用六问法快速筛选：跑赢基准？夏普>1？回撤可承受？无存活偏差？近年有效？有特色避开竞争？"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'详细回测后再判断'，作者的反直觉见解是'在投入大量时间回测前，先用六问快速淘汰'"
```

### fw011: 交易成本影响评估框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章2.2.3节: E-迷你标普500策略扣除1个基点后夏普从3变-3
    - 第3章: Khandani-Lo均值回归策略夏普从4.47降至-3.19的案例
V2_predictive_power:
  passed: true
  novel_question: "为什么回测盈利的策略实盘亏损？"
  derived_answer: "很可能是忽略了交易成本。交易成本包括：佣金、流动性成本、市场冲击、滑价"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'回测盈利就能赚钱'，作者的反直觉见解是'夏普比率3扣除交易成本后变-3'"
```

### fw012: 数据质量陷阱识别框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章2.2.4节: 存活偏差的定义和影响
    - 第2章2.2.5节: 时间衰减和非平稳性问题
    - 第3章: 使用前视偏差检测程序
V2_predictive_power:
  passed: true
  novel_question: "为什么10年前的策略现在失效？"
  derived_answer: "三个原因：存活偏差夸大早年业绩、量化竞争加剧、市场结构变化（状态转换）"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'数据越多越好'，作者的反直觉见解是'金融时间序列是非平稳的，数据越多并不意味着回测越可靠'"
```

### fw013: 参数复杂度与过拟合权衡原则
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章2.2.6节: 100个参数可以完美拟合历史但未来糟糕
    - 第3章: 经验法则参数不超过5个
V2_predictive_power:
  passed: true
  novel_question: "我的策略有20个参数怎么办？"
  derived_answer: "高度怀疑其未来表现。简单模型更可靠，应该减少参数，用移动回顾窗口验证"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'参数越多模型越精确'，作者的反直觉见解是'100个参数可以完美拟合历史，但未来业绩可能截然不同'"
```

### fw014: AI方法在交易中的适用性判断框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章"人工智能与选股"方框: 有效AI方法的五个特征
    - 第2章: 作者自己AI模型回测优秀但实盘失望的案例
V2_predictive_power:
  passed: true
  novel_question: "用深度学习预测股价行不行？"
  derived_answer: "金融数据独立样本量有限，复杂AI容易过拟合。有效的AI必须：基于正确理论、参数少、只用线性回归、概念简单、移动窗口优化"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'AI能预测一切'，作者的反直觉见解是'金融数据量有限，AI容易过拟合，简单线性回归反而更有效'"
```

### fw015: 小容量策略优势原理
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第2章2.2.7节: 机构忽略小容量策略的逻辑
    - 第8章: 容量是独立交易员核心优势的论证
V2_predictive_power:
  passed: true
  novel_question: "为什么独立交易员能打败机构？"
  derived_answer: "小容量策略（交易频繁、持仓少、标的少）被机构忽略，未被套利才有alpha"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'大基金更厉害'，作者的反直觉见解是'大容量策略竞争激烈无利可图，小容量策略才是独立交易员的生存空间'"
```

### fw016: 回测工具选择决策树
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第3章3.1节: Excel/MATLAB/TradeStation的对比讨论
V2_predictive_power:
  passed: true
  novel_question: "用什么工具回测？"
  derived_answer: "简单策略用Excel，复杂策略用MATLAB，想要一站式用TradeStation"
V3_exclusivity:
  passed: false
  why_not_common: "2009年的工具推荐在2025年已过时。Python生态（pandas、backtrader、zipline）已成为主流，书中关于设备、数据、执行系统的建议部分过时"
```
**状态**: ❌ 拒绝（V3未通过）

### fw017: 业绩偏差诊断框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第5章: 系统性诊断流程（软件漏洞→执行成本→数据窥探→状态转换→运气）
    - 第6章: 仿真交易揭示偏差的讨论
V2_predictive_power:
  passed: true
  novel_question: "实盘业绩不如回测怎么办？"
  derived_answer: "按顺序排查：1.软件漏洞 2.执行成本超预期 3.流动性问题 4.数据窥探偏差 5.状态转换 6.运气不好"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'业绩差就放弃'，作者的反直觉见解是'先排除简单原因（软件、成本），再考虑复杂原因（状态转换），最后才承认运气不好'"
```

### fw018: 交易成本最小化框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第5章: 避免低价股、限制指令规模（日均交易量1%）、资本权重与市值四次方根成正比
    - 第4章: 选择经纪商时考虑成交速度和暗池流动性
V2_predictive_power:
  passed: true
  novel_question: "如何降低大额订单的市场冲击？"
  derived_answer: "1.避免低价股 2.单指令不超过日均交易量1% 3.大单拆分分时执行 4.按市值四次方根分配资本"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'按市值线性分配资本'，作者的反直觉见解是'用市值四次方根分配，最大权重比不超过10倍'"
```

### fw019: 仿真测试验证流程
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第5章: 仿真交易的5大好处
    - 第3章: 仿真交易是最可靠的样本外测试
V2_predictive_power:
  passed: true
  novel_question: "回测成功后能直接实盘吗？"
  derived_answer: "不能，必须先仿真交易至少1个月，比较仿真盈亏与回测理论盈亏，差异若非交易成本引起则是软件漏洞"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'回测成功就能赚钱'，作者的反直觉见解是'仿真交易是发现软件漏洞的唯一不亏钱方法'"
```

### fw020: 凯利公式最优杠杆决策
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第6章: 凯利公式推导和应用（f*=m/s²）
    - 第6章附录: 数学推导
    - 第2章: 高夏普比率+高杠杆的铺垫
V2_predictive_power:
  passed: true
  novel_question: "我的策略应该用多少杠杆？"
  derived_answer: "用凯利公式f*=m/s²计算最优杠杆，实际操作用半凯利（f*/2），并与历史最大亏损下的最大杠杆取较小值"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'杠杆越高赚得越多'，作者的反直觉见解是'凯利公式给出数学最优杠杆，超过就会降低长期增长率'"
```

### fw021: 半凯利风险控制方法
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第6章: 半凯利的定义和理由（参数估计误差、收益率非正态）
    - 第6章: 与历史最大亏损约束的结合
V2_predictive_power:
  passed: true
  novel_question: "凯利公式计算出的杠杆太大怎么办？"
  derived_answer: "用半凯利（凯利最优的一半），并与历史最大亏损下的最大杠杆取较小值"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'用最优杠杆'，作者的反直觉见解是'参数估计有误差，实际用半凯利更安全'"
```

### fw022: 行为偏差识别与克服框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第6章: 禀赋效应、代表性偏差、恐惧、贪婪的详细讨论
    - 第6章: 作者自己在XLE/CL策略上因恐惧清仓的案例
V2_predictive_power:
  passed: true
  novel_question: "为什么我知道该怎么做但还是做不到？"
  derived_answer: "因为行为偏差：禀赋效应让你不愿止损，代表性偏差让你过度反应近期亏损，恐惧让你在最差时机清仓。解决方法：从小额开始、用凯利公式系统化、找其他收入来源分散注意力"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'控制情绪'，作者的反直觉见解是'具体识别三类偏差（禀赋、代表性、恐惧贪婪），用凯利公式替代情绪化决策'"
```

### fw023: 止损策略适用性判断框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第6章: 止损在惯性状态有益、在均值回归状态有害
    - 第7章: 清仓策略选择的详细讨论
V2_predictive_power:
  passed: true
  novel_question: "我的策略应该用止损吗？"
  derived_answer: "看策略类型：惯性（趋势）策略用止损（价格会继续偏离），均值回归策略不用止损（价格会回归），用持有期或盈利上限清仓"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'止损是万能的风险管理工具'，作者的反直觉见解是'止损在均值回归策略中是有害的'"
```

### fw024: 均值回归vs动量策略选择框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第7章: 两种策略的定义、适用条件、持有期、竞争影响
    - 第2章: 工作时间与策略类型匹配的讨论
V2_predictive_power:
  passed: true
  novel_question: "我应该做均值回归还是动量策略？"
  derived_answer: "看三个因素：1.市场状态（均值回归还是趋势）2.持有期偏好（短用均值回归，长用动量）3.可用时间（全职可做日内均值回归，兼职用动量）"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'追涨杀跌'，作者的反直觉见解是'价格可能均值回归也可能趋势延续，必须先判断市场状态再选策略'"
```

### fw025: 状态转换预测方法
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第7章: 马尔可夫状态转换模型和拐点模型
    - 第5章: 状态转换的定义和影响
V2_predictive_power:
  passed: true
  novel_question: "如何预测策略失效？"
  derived_answer: "用两种方法：1.马尔可夫状态转换模型（假设转移概率固定）2.拐点模型（数据挖掘方法，用机器学习预测）"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'预测市场不可能'，作者的反直觉见解是'可以用数据挖掘方法预测拐点，虽然不完美但有帮助'"
```

### fw026: 协整性检验与配对交易构建
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第7章: 平稳性、协整性的定义和检验方法
    - 第3章: GLD-GDX配对交易案例
V2_predictive_power:
  passed: true
  novel_question: "如何构建配对交易？"
  derived_answer: "1.用ADF检验确认协整性 2.用回归得到对冲比率 3.在差价偏离均值时建仓，回归时清仓 4.用半衰期确定最优持有期"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'同行业股票可以配对'，作者的反直觉见解是'必须用协整检验，不是相关性。相关性≠协整性'"
```

### fw027: 因子模型构建与应用
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第7章: 因子模型定义（R=Xb+u）、Fama-French三因子、PCA方法
V2_predictive_power:
  passed: true
  novel_question: "如何用基本面因素量化交易？"
  derived_answer: "用因子模型：1.基本面因子（Fama-French三因子）2.数据驱动因子（PCA主成分分析）"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'基本面分析太主观'，作者的反直觉见解是'可以用因子模型量化基本面因素'"
```

### fw028: 清仓策略选择框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第7章: 固定持有期、目标价格、反向信号、止损价格四种清仓方式
V2_predictive_power:
  passed: true
  novel_question: "何时清仓？"
  derived_answer: "看策略类型：1.惯性模型用固定持有期或反向信号 2.均值回归用目标价格或半衰期 3.趋势策略用止损价格"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'设置止损价'，作者的反直觉见解是'按策略类型选择不同的清仓方式'"
```

### fw029: 季节性交易识别框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第7章: 股票季节性策略已失效，商品期货季节性仍有效
V2_predictive_power:
  passed: true
  novel_question: "季节性策略还能做吗？"
  derived_answer: "股票市场季节性（如一月效应）已失效，商品期货季节性（如汽油夏季驾驶高峰）仍有效，但只交易有实际经济意义的策略"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'季节性是数据挖掘'，作者的反直觉见解是'只交易有实际经济意义的季节性策略，商品期货比股票更可靠'"
```

### fw030: 高频交易特征与适用性判断
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第7章: 高频交易定义、高夏普比率原因、优缺点、适用性
V2_predictive_power:
  passed: true
  novel_question: "应该做高频交易吗？"
  derived_answer: "高频交易有高夏普比率优势，但对回测（交易成本敏感）和执行速度要求极高，不适合初涉此领域的独立交易员"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'高频交易最赚钱'，作者的反直觉见解是'高频交易门槛高，对初学者不合适'"
```

### fw031: 高杠杆低贝塔vs低杠杆高贝塔组合选择
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第7章: 两种提高收益率方法的比较
    - 第6章: 夏普比率与复合增长率的关系
V2_predictive_power:
  passed: true
  novel_question: "如何提高收益率？"
  derived_answer: "两种方法：1.提高杠杆（低贝塔+高杠杆）2.提高贝塔（高贝塔+低杠杆）。选择前者，因为低贝塔组合风险更低、夏普比率更高"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'高贝塔=高收益'，作者的反直觉见解是'低贝塔+杠杆更优，因为复合增长率与夏普比率的平方成正比'"
```

### fw032: 独立交易者优势分析框架
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第8章: 容量优势、机构劣势（约束、干预、代理人问题）
    - 第1章: 铺垫（独立交易员可以打败机构）
V2_predictive_power:
  passed: true
  novel_question: "独立交易员vs机构谁更有优势？"
  derived_answer: "独立交易员在小容量策略上有结构性优势：1.可以交易机构忽略的小容量策略 2.没有官僚成本 3.不受管理层约束和干预 4.用自己的钱没有代理人问题"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'机构资源更多更厉害'，作者的反直觉见解是'机构有结构性劣势（约束、干预、代理人问题），独立交易员在小容量策略上更有优势'"
```

### fw033: 量化交易事业增长路径
```yaml
V1_cross_domain:
  passed: true
  evidence:
    - 第8章: 四阶段增长路径（单策略→策略数量→合作外包→外部资本）
    - 第6章: 凯利公式实现净值指数增长
V2_predictive_power:
  passed: true
  novel_question: "如何从小规模做到机构？"
  derived_answer: "四阶段：1.单策略指数增长（凯利公式）2.策略数量扩展（更高频/更长持有期/跨市场）3.合作与外包 4.引入外部资本"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'慢慢积累'，作者的反直觉见解是'有明确的四阶段路径，从小规模到机构有系统化的方法'"
```

---

## 批次2: Principles (pr001-pr079)

**验证进度**: 
- p1 batch: 16/79 通过 (pr001-pr016)
- p2 batch: 8/28 通过 (p01-p28)
- 累计: 24/107 通过，通过率 22.4%

---

## 批次3: Cases (ca001-ca031) + Glossary (gl001-gl046)

**验证进度**: 
- cases_p1 batch: 8/18 通过 (ca001-ca018)
- cases_p2 batch: 待处理
- glossary_p1 batch: 待处理
- glossary_p2 batch: 待处理

**cases_p1 验证详情**:
- 通过案例: ca001, ca006, ca007, ca011, ca013, ca014, ca015, ca017
- 拒绝案例: ca002(V3), ca003(重复), ca004(重复), ca005(重复), ca008(重复), ca009(重复), ca010(V3), ca012(重复), ca016(重复), ca018(V3)
- 通过率: 44% (8/18)
- 验证报告: VERIFICATION_REPORT_cases_p1.md

---

## 统计汇总

**批次1 (Frameworks)**: 32/33 通过，通过率 97%
**批次2-p1 (Principles)**: 16/79 通过，通过率 20.3%
**批次2-p2 (Principles)**: 8/28 通过，通过率 28.6%
**批次3-cases_p1 (Cases)**: 8/18 通过，通过率 44%

**总体进度**: 64/158 通过（fw: 32+33, pr: 16+28, cases: 8），总体通过率 40.5%
