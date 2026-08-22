# 三重验证 — 《聪明的投资者》通过单元

## 验证总览

| 类型 | 候选总数 | 通过 | 淘汰 | 通过率 |
|------|---------|------|------|--------|
| Frameworks | 10 | 9 | 1 | 90% |
| Principles | 16 | 12 | 4 | 75% |
| Cases | 7 | 7 | 0 | 100% (不适于独立skill) |
| Counter-examples | 12 | 8 | 4 | 67% |
| Glossary | 20 | 20 | 0 | 100% (共享词典) |

**通过总量**: 29 个方法论单元 → 合并去重后 → **约 9 个独立 skill**

---

## Frameworks

### f01 — Investment vs Speculation Decision Framework ✅
- **V1**: 第1章定义 + 第1章反复强调混淆的危害 + 第8章市场先生框架中隐含的区分 → 通过
- **V2**: 能用它判断"用期权对冲"是投资还是投机 → 取决于是否分析+安全+回报 → 有意义结论
- **V3**: 反常识 —— 大多数人认为买股票=投资, 但格雷厄姆的三条件非常严格 → 通过

### f02 — Defensive 50/50 Allocation Framework ✅
- **V1**: 第4章详细讨论 + 耶鲁大学案例佐证 + 第1章预期收益计算 → 通过
- **V2**: 在一个没有债券的时代(零利率), 此框架如何调整？→ 需用其他资产替代债券 → 有意义
- **V3**: 不是常识 —— 大多数人要么全仓股票要么全仓现金 → 通过

### f03 — Graham Valuation Formula ✅
- **V1**: 第11章公式 + 第14章选股标准中隐含的市盈率限制 + 第20章安全边际计算 → 通过
- **V2**: 对一家增长率为0的科技公司如何估值？→ 8.5倍EPS, 不受市场情绪影响 → 反直觉
- **V3**: 独特的保守估值方法, 不是常识性DCF → 通过

### f04 — Defensive Stock Selection Checklist (7 Criteria) ✅
- **V1**: 第14章完整列出 + 第5章分散化讨论 + 第7章积极型投资者参照 → 通过
- **V2**: 用此标准评估一家增长迅速但不支付股息的科技公司 → 不通过 → 有意义
- **V3**: 独特的定量筛选体系, 不是常识 → 通过

### f05 — Margin of Safety Framework ✅
- **V1**: 全书贯穿(第1章定义、第20章哲学总结、第8章市场先生、第14章选股标准) → 通过
- **V2**: 加密货币是否可有安全边际？→ 需估算内在价值 → 无内在价值则无安全边际 → 有意义
- **V3**: 独特概念, 不是常识 → 通过

### f06 — "Mr. Market" Mental Model ✅
- **V1**: 第8章寓言 + 第20章总结 + 第1章投资与投机区分 → 通过
- **V2**: 投资人如何在恐慌性新闻中保持理性？→ 市场先生今天抑郁了, 忽略他的报价 → 有意义
- **V3**: 独特的寓言式框架, 不是常识 → 通过

### f07 — NCAV Screening Framework ✅
- **V1**: 第15章详细讨论 + 第17章A&P案例 + 后记格雷厄姆-纽曼基金 → 通过
- **V2**: 现代市场中NCAV股票几乎不存在, 此框架如何适应？→ 使用调整后的净流动资产价值 → 有意义
- **V3**: 独特的极端保守估值方法, 不是常识 → 通过

### f08 — Dollar-Cost Averaging Framework ❌ (淘汰)
- **V1**: 书中提到定投法但篇幅有限, 未在多个独立语境下讨论 → 不通过
- **V2**: 定投在下降市场中确实有效, 但这个结论是常识 → 不通过
- **V3**: 任何理财顾问都会推荐定投, 不是格雷厄姆独有 → 不通过
- **→ 降级为 principle 的 example**

### f09 — Active vs Defensive Investor Decision Tree ✅
- **V1**: 第4章定义防御型 + 第6-7章定义积极型 + 全书策略围绕此二元划分 → 通过
- **V2**: 一个年轻人有大量时间但少资金, 应选哪条路？→ 防御型(因为时间≠分析能力) → 有意义
- **V3**: 独特的投资者分类体系, 不是常识 → 通过

### f10 — Speculation Account Separation Rule 🔄 (合并入 f01/f05)
- **V1**: 第1章明确讨论 + 第8章隐含 → 通过
- **V2**: 有意义 → 通过
- **V3**: 独特 → 通过
- **→ 不独立成skill, 合并入 f01 (Investment vs Speculation)**

---

## Principles

### p01 — Investment Definition (Three Conditions) 🔄 (合并入 f01)
- 与 f01 重复, 作为 f01 的 R 段引用

### p02 — Margin of Safety 🔄 (合并入 f05)
- 与 f05 重复, 作为 f05 的 R 段引用

### p03 — Diversification ✅
- **V1**: 第20章 + 第14章选股标准 + 第5章分散化建议 → 通过
- **V2**: 持有5只科技股算分散化吗？→ 行业集中, 不算 → 有意义
- **V3**: 虽然"不要把所有鸡蛋放在一个篮子里"是常识, 但格雷厄姆的10-30只具体建议是独特的 → 通过

### p04 — Don't Try to Time the Market ✅
- **V1**: 第8章市场先生 + 第4章50/50计划(机械式再平衡替代择时) → 通过
- **V2**: 用技术分析指标决定买卖算投机吗？→ 是的, 因为没有安全边际 → 有意义
- **V3**: 反直觉: 大多数人认为可以预测市场, 格雷厄姆说不能 → 通过

### p05 — Separate Investment and Speculation Accounts 🔄 (合并入 f01)
- 作为 f01 的执行规则

### p06 — The 4 Business Principles of Investing ✅
- **V1**: 第20章总结 + 全书各章分别展开 → 通过
- **V2**: 用这四条原则评估一个朋友推荐的股票 → 适用 → 有意义
- **V3**: 独特的四原则体系, 不是常识 → 通过

### p07 — Historical Valuation as Anchor ❌ (淘汰)
- **V1**: 第2-3章讨论 → 仅两章, 独立性不足 → 不通过
- **V3**: "历史会重演"是常识 → 不通过
- **→ 降级为 f07 的 example**

### p08 — Low P/E Stocks Outperform ❌ (淘汰)
- **V1**: 第11章讨论 → 部分实证 → 但在书中未在其他章节独立佐证 → 不通过
- **V3**: 现代因子投资研究使此结论成为常识 → 不通过
- **→ 降级为 f03/f04 的引用**

### p09 — Growth Stock Risk ✅
- **V1**: 第11章讨论 + 第18章公司案例(AAA等) → 通过
- **V2**: 用此原理分析特斯拉(高估值) → 风险在预期已被定价 → 有意义
- **V3**: "双杀"概念是格雷厄姆独特贡献, 不是常识 → 通过

### p10 — Adequate But Not Extraordinary Returns ❌ (淘汰)
- **V1**: 仅第1章提到 → 书内独立证据不足 → 不通过
- **V3**: "降低预期"是常识性智慧 → 不通过
- **→ 降级为其他 skill 的引用**

### p11 — "This Time Is Different" Fallacy 🔄 (合并入 f06)
- 与市场先生框架高度重叠, 作为 f06 的 A1 段

### p12 — Don't Be Misled by Past Performance ❌ (淘汰)
- **V1**: 第9章讨论 → 独立性不足 → 不通过
- **V3**: 标准投资警告, 不是独特见解 → 不通过
- **→ 降级为 f06 的引用**

### p13 — Inflation is an Investor's Enemy ✅
- **V1**: 第2章整章 + 第1章预期收益讨论 + 第4章资产配置涉及 → 通过
- **V2**: 2020年代高通胀下, 纯债券投资者应如何应对？→ 增持股票 → 有意义
- **V3**: 独特的通胀-股票关系分析, 超越常识 → 通过

### p14 — The Investor's Worst Enemy is Himself ✅
- **V1**: 第8章市场先生(心理) + 第20章纪律 + 全书反复强调 → 通过
- **V2**: 当AI给出投资建议, 投资者最大的敌人是什么？→ 还是自己(不执行) → 有意义
- **V3**: 虽然部分常识, 但将其置于安全边际之上的优先级是独特的 → 通过

### p15 — The Proper Form of Speculation 🔄 (合并入 f01)
- 作为 f01 的补充规则

### p16 — Quality of Management Assessment ❌ (淘汰)
- **V1**: 第19章核心讨论 → 但书中其他章节未独立佐证 → 不通过
- **V3**: "看行动不看言语"是常识 → 不通过
- **→ 降级为 f04 的补充**

---

## Cases (不独立成 skill, 作为其他 skill 的 A1 段素材)

- c01 A&P → A1 for f07 (NCAV)
- c02 LTV → A1 for f05 (Margin of Safety)
- c03 NVF-Sharon → A1 for f01 (Investment vs Speculation)
- c04 AAA IPO → A1 for f01/f09
- c05 Four-Company → A1 for f04 (Diversification)
- c06 Graham-Newman → A1 for f07 (NCAV)
- c07 Two Partners → A1 for f06 (Mr. Market)

---

## Counter-examples (不独立成 skill, 作为其他 skill 的 B 段警示素材)

淘汰的 4 个:
- ce08 Ignoring Inflation → 合并入 p13
- ce09 "This Time Is Different" → 合并入 f06
- ce10 Accounting Tricks → 合并入 f01/f04
- ce11 LTV Overleveraging → 重复 ce02
- ce12 NVF Financial Engineering → 重复 ce03

---

## 最终 Skill 入选名单 (9 个)

| # | 名称 | 类型 | 主要章节 | 核心概念 |
|---|------|------|---------|---------|
| 1 | investment-vs-speculation | skill | Ch.1 | 投资三条件 + 账户分离 + 投机正当形式 |
| 2 | defensive-allocation | skill | Ch.4 | 50/50 资产配置 + 再平衡 |
| 3 | graham-valuation-formula | skill | Ch.11 | V = EPS × (8.5 + 2g) |
| 4 | defensive-stock-checklist | skill | Ch.14 | 7 项选股标准 |
| 5 | margin-of-safety | skill | Ch.20 | 安全边际评估 |
| 6 | mr-market | skill | Ch.8 | 市场先生心理框架 |
| 7 | ncav-screening | skill | Ch.15 | 净流动资产价值筛选 |
| 8 | diversification | skill | Ch.5,14,20 | 分散化原则 |
| 9 | behavioral-discipline | skill | Ch.1,8,20 | 情绪纪律 + 通胀认知 |