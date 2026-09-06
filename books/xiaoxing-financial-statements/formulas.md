# 公式 Formula Reference

> 公式按本书口径整理。涉及资产或权益的期间指标，实际分析优先使用期初、期末平均余额；书中示例为简化有时使用期末数。书中对 NPV 明确给出“NPV > 0”的投资原则，下面的折现展开式是通用财务分析表达。

## 三表与利润形成

| 中文 | English | 公式 |
|---|---|---|
| 会计恒等式 | Accounting Equation | `Assets = Liabilities + Shareholders' Equity` |
| 毛利 | Gross Profit | `Gross Profit = Operating Revenue - Cost of Revenue` |
| 营业利润 | Operating Profit | `Operating Profit = Revenue - COGS - Taxes & Surcharges - Selling Expenses - Administrative Expenses - Finance Costs - Impairment Loss + Fair-value Gains + Investment Income` |
| 利润总额 | Profit Before Tax | `PBT = Operating Profit + Non-operating Revenue - Non-operating Expense + Subsidy Income + FX Gain/Loss` |
| 净利润 | Net Profit | `Net Profit = Profit Before Tax - Income Tax` |
| 生产成本 | Production Cost | `Production Cost = Direct Materials + Direct Labor + Manufacturing Overhead` |

## 盈利能力

| 中文 | English | 公式 |
|---|---|---|
| 毛利率 | Gross Margin | `Gross Margin = Gross Profit / Revenue` |
| 净利润率 | Net Profit Margin | `Net Profit Margin = Net Profit / Revenue` |
| 总资产周转率 | Total Assets Turnover | `Revenue / Average Total Assets` |
| 总资产报酬率 | Return on Assets (ROA) | `ROA = Net Profit / Average Total Assets` |
| 投资回报率 | Return on Investment (ROI) | `ROI = Economic Return from Investment / Investment` |
| 净资产收益率 | Return on Equity (ROE) | `ROE = Net Profit / Average Shareholders' Equity` |
| 权益乘数 | Equity Multiplier | `Equity Multiplier = Total Assets / Shareholders' Equity = 1 / (1 - Liability/Asset Ratio)` |
| 杜邦关系 | DuPont-style relation | `ROE = ROA × Equity Multiplier` |

## 营运能力

| 中文 | English | 公式 |
|---|---|---|
| 应收账款周转率 | Accounts Receivable Turnover | `Revenue / Average Accounts Receivable` |
| 平均收现期 | Average Collection Period | `365 / Accounts Receivable Turnover` |
| 流动资产周转率 | Current Assets Turnover | `Revenue / Average Current Assets` |
| 固定资产周转率 | Fixed Assets Turnover | `Revenue / Average Net Fixed Assets` |
| 存货周转率 | Inventory Turnover | `COGS (or Revenue) / Average Inventory` |
| 存货周转天数 | Inventory Days | `365 / Inventory Turnover` |
| 平均余额 | Average Balance | `(Beginning Balance + Ending Balance) / 2` |

## 偿债能力

| 中文 | English | 公式 |
|---|---|---|
| 流动比率 | Current Ratio | `Current Assets / Current Liabilities` |
| 速动比率 | Quick Ratio / Acid-test Ratio | `(Current Assets - Inventory) / Current Liabilities` |
| 息税前收益 | EBIT | `EBIT = Net Profit + Income Tax + Interest Expense` |
| 利息保障倍数 | Times Interest Earned (TIE) | `TIE = EBIT / Interest Expense` |
| 资产负债率 | Liability/Asset Ratio | `Total Liabilities / Total Assets` |

## 价值创造与资本成本

| 中文 | English | 公式 |
|---|---|---|
| 投资资本 | Invested Capital | `Invested Capital = Interest-bearing Debt + Shareholders' Equity` |
| 税后营业净利润 | NOPAT | `NOPAT = Operating Profit × (1 - Corporate Tax Rate)` |
| 投资资本回报率 | ROIC | `ROIC = NOPAT / Invested Capital` |
| 加权平均资本成本 | WACC | `WACC = (Debt/IC) × Kd × (1 - Tax Rate) + (Equity/IC) × Ke` |
| 超额收益率 | Excess Return | `Excess Return = ROIC - WACC` |
| 经济利润 | Economic Profit / EVA | `Economic Profit = (ROIC - WACC) × Invested Capital` |
| 净现值 | NPV | `NPV = Σ[CF_t / (1 + r)^t] - Initial Investment` |

## 口径提醒

- `ROA` 的分子是股东净利润，而总资产包含债权人资金；`ROIC` 用 NOPAT 与有息负债加权益配对，经济含义更严谨。
- `Current Ratio` 不应脱离存货质量、应收账款回收和短期借款结构解读。
- `TIE` 通常以财务费用近似利息费用；若财务费用含大量非利息项目，应回到附注拆分。
- `NOPAT = Operating Profit × (1 - tax rate)` 是分析近似；实际税率和非经营项目需按公司披露调整。
