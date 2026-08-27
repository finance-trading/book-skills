---
name: graham-dodd-security-analysis
description: "Knowledge base from \"证券分析 Security Analysis\" (1940) by Benjamin Graham & David Dodd (海南出版社1999中译本). Use when applying Graham-Dodd frameworks for 固定价值投资, 债券选择标准, 损益帐户分析, 资产负债表分析, 内在价值, 安全边际, or referencing its concepts."
---

<!-- argument-hint: [主题, 框架名, 或章节号如 ch08] -->

# 证券分析（Security Analysis, 1940）
**作者**: Benjamin Graham & David Dodd | **版本**: 1940年版（海南出版社1999中译本） | **章节**: 导言+52章 | **生成**: 2026-08-27

## How to Use This Skill

- **无参数** — 加载核心框架做参考
- **带主题** — 问 `债券选择标准`、`损益帐户分析`、`清算价值` 等；我会读取相关章节文件后回答
- **带章节号** — 问 `ch08`；我加载该章文件
- **浏览** — 问"有哪些章节？"看完整索引

问到 Core Frameworks 未覆盖的主题时，我会先读相关章节文件再回答。

---

## Core Frameworks & Mental Models

### 1. 投资操作的定义（Ch 4 — 全书基石）
> 投资操作 = **详尽分析** + **本金安全** + **满意回报**，三者缺一即投机。

证券分析三功能：**描述**（呈现事实）→ **选择**（用标准决定买卖）→ **评判**（审查条款、管理层、会计的可疑之处）。内在价值是"近似值范围"而非精确点——价格落在区间之外时才可下结论。

### 2. 固定价值投资四原则（Ch 6）
1. 安全性不来自法定权利，来自**企业履行义务的能力**
2. 用**投资标准逐项检验**——不以名称/收益率取代标准
3. 投资人不当法官——只守安全线，不裁决"值不值得冒险"
4. 拒绝购买必须能陈述具体理由

### 3. 数量化标准（Ch 6–11 — 全书判据宝库）
- 保障倍数门槛：铁路/公用事业 **2×**，工业 **3×**（固定费用）；优先股用**完全扣除法**（利息+股息加总）：2.5× / 4×
- 盈利记录 **7 年**（最低5年）；工业企业规模 ≥ $500万（1940语境）
- 每个数字都是1940年语境的标尺——用时对照当期市场校准，规则的形式比数值更长效

### 4. 优先股的合同弱点（Ch 14）
优先股 = 债券的局限 + 股票的风险。股息是"或有或无"的权利——董事可自主停发。结论：**要么普通股赚钱，要么优先股赔钱**；累积性永远优于非累积性；高股息不能补偿本金风险。

### 5. 损益帐户三查（Ch 31–33 — 会计审查武器库）
逐项检查：**(1) 偶生项目**（资产出售、诉讼、退税）剔除；**(2) 子公司收益**（未合并利润、股票股息入账价值）；**(3) 储备**（折旧/摊销的任意性计提与释放）。
交叉检验：联邦税反推应税所得；盈余变动反推收益。**会计有问题的公司，全部证券退避三舍**。

### 6. 平均收益 vs 趋势（Ch 37–38）
以 **7–10 年平均收益**为估值基础；趋势只能通过乘数（≤16×）有限反映。趋势外推没有数学约束——1929年的教训。摒弃历史记录需要"言之成理"的四类理由（矿藏变化、资产更替、价格异常、竞争格局改变）。

### 7. 估值支柱（Ch 39–43）
- **市盈率**：10× 均值=合理基准，16×=硬上限；资本结构变化必须回溯重述历史 EPS
- **资本结构**：最优杠杆 = 能被安全发行的极限；总额恒定时杠杆只改分配
- **帐面价值**：日常不作选股依据；极端偏离（16× 或 1/10）是警示
- **清算价值**：现金100% / 应收80% / 存货66⅔% / 固定资产≈15%；**股价长期低于清算价值 → 要么买点，要么该清算**

### 8. 结构审查（Ch 46–48）
- 认股权证的价值 = 普通股价值的等额减少（零容忍审查）
- 融资真实成本 ≈ 公众实付的 25–30%
- 金字塔结构：少数股权控制 + 双重杠杆 + 权证循环 = 系统性剥削 → 估值折扣

### 9. 价格与价值的背离（Ch 50–51）
背离根源是群体心理的夸大、过度简化与忽略。成熟证券有价格惯性，不成熟证券极敏感（临界价 <70 才按投机品分析；70–100 是主观离差区）。掉换建议双资格：新标的有吸引力 **或** 存在契约关系，否则沉默。

### 10. 分析师的边界（Ch 52 — 全书收官）
四类有效活动：**(1)** 苛刻标准的高级证券选择；**(2)** 可升级的投资级证券发现；**(3)** 远低于内在价值的普通股/授权性高级证券；**(4)** 相关证券间确定背离的置换·套期·套利。超出即滑入市场分析——预测价格方向没有安全边际。分散化是低估操作的必备边际。

---

## Chapter Index

**第一部分 考察及其方法**
| # | 标题 | 关键框架 |
|---|------|---------|
| [导言](chapters/introduction.md) | 近期金融历史的意义 | 1927-1933教训、新时代陷阱 |
| [ch01](chapters/ch01-scope-intrinsic-value.md) | 证券分析的范围和局限·内在价值 | 分析三功能、近似值范围 |
| [ch02](chapters/ch02-basic-factors.md) | 基本因素·质的与量的因素 | 四因素(S/P/T/I)、内在稳定性 |
| [ch03](chapters/ch03-information-sources.md) | 信息来源 | 信息层次、损益八要素 |
| [ch04](chapters/ch04-investment-vs-speculation.md) | 投资与投机的区别 | 投资定义、五项传统标准批判 |
| [ch05](chapters/ch05-security-classification.md) | 证券的分类 | 三类分类法 |

**第二部分 固定价值类投资**
| [ch06](chapters/ch06-fixed-value-selection.md) | 固定价值类投资的选择 | 四原则 |
| [ch07](chapters/ch07-selection-principles.md) | 选择：第二与第三原则 | 安全边际量化 |
| [ch08](chapters/ch08-bond-standards-i.md) | 债券投资的具体标准 | 记录年限、规模标准 |
| [ch09](chapters/ch09-bond-standards-ii.md) | 具体标准（续） | 保障倍数判据 |
| [ch10](chapters/ch10-bond-standards-iii.md) | 具体标准（续） | 股息记录、趋势 |
| [ch11](chapters/ch11-bond-standards-concl.md) | 具体标准（完） | 双重数量检验 |
| [ch12](chapters/ch12-railroad-utility-bonds.md) | 铁路和公用事业债券特殊问题 | 固定费用构成 |
| [ch13](chapters/ch13-other-bond-factors.md) | 债券分析其他特殊因素 | 价格与安全的补充关系 |
| [ch14](chapters/ch14-preferred-stock-theory.md) | 优先股理论 | 合同弱点、双征收 |
| [ch15](chapters/ch15-selecting-preferred-stocks.md) | 选择优先股的技巧 | 完全扣除法 |
| [ch16](chapters/ch16-income-guaranteed-bonds.md) | 收入债券和担保证券 | 收入债券缺陷、担保实质 |
| [ch17](chapters/ch17-guaranteed-issues-cont.md) | 担保证券（续） | 担保三要素 |
| [ch18](chapters/ch18-protective-covenants.md) | 保护性条款和补救方法 | 条款分类、受托人矛盾 |
| [ch19](chapters/ch19-protective-covenants-cont.md) | 保护性条款（续） | 增发限制、营运资金、偿债基金 |
| [ch20](chapters/ch20-preferred-covenants-adequacy.md) | 优先股保护条款·低级资本充足度 | 双重保护、充足度公式 |
| [ch21](chapters/ch21-managing-investments.md) | 对所持投资的管理 | 三阶段模型、调换规则 |

**第三部分 具有投机特征的高级证券**
| [ch22](chapters/ch22-quality-at-price.md) | 质优价廉的高级证券·附权证券 | 两条路径、平价计算 |
| [ch23](chapters/ch23-technical-features.md) | 附权高级证券的技术特征 | 三种特权、诱饵原理 |
| [ch24](chapters/ch24-convertible-features.md) | 可转换证券的技术特点 | 反稀释、滑动比率 |
| [ch25](chapters/ch25-warrants-participating-compare.md) | 附认股权证的高级证券·参与证券 | 三特权比较 |
| [ch26](chapters/ch26-questionable-senior.md) | 安全性存在问题的高级证券 | 主观离差区、普通股分析法 |

**第四部分 普通股投资理论·股利因素**
| [ch27](chapters/ch27-common-stock-theory.md) | 普通股投资理论 | 新时代谬误批判 |
| [ch28](chapters/ch28-recommendation-principles.md) | 普通股投资的推荐原则 | 组合性操作、两条原则 |
| [ch29](chapters/ch29-dividend-factor.md) | 普通股分析中的股息因素 | 派息率、价值三要素 |
| [ch30](chapters/ch30-stock-dividends.md) | 股票股息 | 特别vs定期、公平安排 |

**第五部分 损益帐户分析·收益因素**
| [ch31](chapters/ch31-income-account-analysis.md) | 损益帐户分析 | 三查清单 |
| [ch32](chapters/ch32-extraordinary-losses.md) | 非常亏损和特别项目 | 存货三方法、递延费用 |
| [ch33](chapters/ch33-misleading-items-subsidiaries.md) | 误导性伎俩·子公司收益 | 联邦税检验、连环虚胀 |
| [ch34](chapters/ch34-depreciation-earning-power.md) | 折旧与盈利能力 | 折旧三问 |
| [ch35](chapters/ch35-amortization-from-investor.md) | 投资者角度的摊销费用 | 已花费折旧底线 |
| [ch36](chapters/ch36-depletion-reserves.md) | 耗损、摊销费用及意外支出储备 | 耗损独立计算 |
| [ch37](chapters/ch37-meaning-of-earnings-record.md) | 收益记录的意义 | 平均vs趋势 |
| [ch38](chapters/ch38-questioning-past-records.md) | 质疑或摒弃过去记录 | 四类合法理由 |
| [ch39](chapters/ch39-pe-ratio-adjustments.md) | 市盈率·资本结构变化的调整 | 10×/16×、回溯重述 |
| [ch40](chapters/ch40-capital-structure.md) | 资本结构 | 最优杠杆 |
| [ch41](chapters/ch41-valuing-common-stock.md) | 如何估价普通股·收益来源 | 来源分离估值 |

**第六部分 资产负债表分析·资产价值**
| [ch42](chapters/ch42-balance-sheet-book-value.md) | 资产负债表分析·帐面价值 | 帐面价值诊断法 |
| [ch43](chapters/ch43-current-asset-value.md) | 流动资产价值的重要性 | NCAV、清算折扣率 |
| [ch44](chapters/ch44-liquidation-shareholder-rights.md) | 清算价值·股东与管理者的关系 | 受托责任 |
| [ch45](chapters/ch45-balance-sheet-concluded.md) | 资产负债表分析（完） | 交叉验证、营运资金标准 |

**第七部分 其他方面·价格与价值的差别**
| [ch46](chapters/ch46-stock-option-warrants.md) | 认股权证 | 稀释量化、零容忍 |
| [ch47](chapters/ch47-financing-management-cost.md) | 融资和管理成本 | 真实成本25-30% |
| [ch48](chapters/ch48-pyramiding.md) | 金字塔式结构 | 双重杠杆 |
| [ch49](chapters/ch49-comparison-analysis.md) | 相同领域公司的比较分析 | 三表法、同质分组 |
| [ch50](chapters/ch50-price-value-divergence.md) | 价格与价值的背离 | 背离机制 |
| [ch51](chapters/ch51-price-value-divergence-cont.md) | 背离（续） | 掉换双资格 |
| [ch52](chapters/ch52-market-vs-security-analysis.md) | 市场分析与证券分析 | 四类有效活动 |

## Topic Index

- **安全边际 margin of safety** → ch01, ch07, ch21, ch28, ch52
- **保障倍数 coverage** → ch07, ch08, ch09, ch11, ch15
- **债券选择标准 bond standards** → ch06–ch11
- **优先股 preferred stock** → ch14, ch15, ch20
- **保护性条款 covenants** → ch18, ch19, ch20
- **可转换证券 convertible** → ch22, ch23, ch24
- **认股权证 warrants** → ch25, ch46, ch48
- **投机性高级证券** → ch22, ch26
- **普通股投资理论** → ch27, ch28
- **股息 dividend** → ch29, ch30
- **损益帐户分析 income account** → ch31, ch32, ch33
- **折旧/摊销/耗损 depreciation** → ch34, ch35, ch36
- **平均收益 vs 趋势 earnings record** → ch37, ch38
- **市盈率 P/E** → ch39
- **资本结构 capital structure** → ch40, ch41
- **帐面价值 book value** → ch42
- **清算价值 liquidation / NCAV** → ch43, ch44
- **营运资金 working capital** → ch19, ch45
- **金字塔结构 pyramiding** → ch48
- **比较分析 comparison** → ch49
- **价格与价值背离 divergence** → ch50, ch51
- **市场分析批判 / 套利** → ch52
- **内在价值 intrinsic value** → ch01, ch27
- **投资与投机 investment vs speculation** → ch04, ch05, ch26
- **会计操纵 earnings manipulation** → ch31, ch32, ch33, ch47

## Supporting Files

- [glossary.md](glossary.md) — 全部关键术语（中英对照）
- [patterns.md](patterns.md) — 全部技术与方法（When/How/Trade-offs）
- [cheatsheet.md](cheatsheet.md) — 决策规则、数字阈值、清算折扣速查

---

## Scope & Limits

本技能覆盖《证券分析》1940年版内容。书中所有数字阈值（2×/3×保障倍数、$500万规模、16×市盈率等）是1940年美国市场语境的标尺——应用于当代市场时，保留规则的**形式与逻辑**，校准**数值**。该书以1930年代美国证券环境为背景，涉及的公司案例（铁路、公用事业、控股公司）多为历史案例。实操请结合当代会计准则（SEC filings、IFRS）与项目工具。相关技能：`benjamin-graham-skill`、`intelligent-investor`（cangjie-skills）、`munger-skill`。
