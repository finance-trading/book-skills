---
name: higgins-financial-management
description: "Knowledge base from \"Analysis for Financial Management\" by Robert C. Higgins & Jennifer L. Koski. Use when applying Higgins' frameworks for financial statement interpretation, ROE/DuPont analysis, sustainable growth, forecasting, capital structure, DCF valuation, and corporate restructuring — or when studying/referencing this foundational corporate-finance text."
---

<!-- argument-hint: [topic, framework name, chapter number, or "sustainable growth" / "ROE" / "valuation"] -->

# Analysis for Financial Management
**Author**: Robert C. Higgins & Jennifer L. Koski | **Pages**: ~465 | **Chapters**: 9 | **Generated**: 2026-09-24

## How to Use This Skill

- **Without arguments** — load the core frameworks below for reference
- **With a topic** — ask about `sustainable growth`, `ROE`, `forecasting`, `WACC`, `free cash flow`, `valuation`, or another topic; I find and read the relevant chapter
- **With a chapter** — ask for `ch04`; I load that specific chapter
- **Browse** — ask "what chapters do you have?"

---

## Core Frameworks & Mental Models

**The Sustainable Growth Equation (the book's signature idea).** Growth consumes cash — new sales require new assets, which must be financed. The fastest a firm can grow sales without new equity or a change in financial policy is:
```
g* = P × R × A × T̂   =   Retention × ROE
```
P = profit margin (NI/sales), R = retention ratio (retained earnings/NI), A = asset turnover (sales/assets), T̂ = leverage (assets/opening equity). To manage growth, first compute g*, then compare it to actual growth: **actual > g* means a financing deficit** (raise equity, add debt, cut payout, prune, outsource, raise price, or merge); **actual < g* means a cash surplus** (pay dividends, buy back stock, or buy growth). Never hand an operator a growth target without stating how it will be financed.

**The DuPont / Three Levers of ROE.** Return on equity decomposes into exactly three management levers:
```
ROE = Profit Margin × Asset Turnover × Financial Leverage
```
Margin summarizes the income statement, turnover the asset side, leverage the financing side. Whatever management does to raise ROE moves one of these three. "Many paths to heaven": a discounter (low margin, high turnover) and a luxury firm (high margin, low turnover) can earn the same ROE. Two known flaws make ROE an unreliable lone yardstick: the *timing problem* (point-in-time snapshot) and the *risk problem* (leverage inflates ROE with added risk).

**Profits ≠ Cash Flow.** The cash cycle — cash → inventory → receivable → cash — and the investment cycle (fixed assets consumed and replenished via depreciation) determine solvency, not profit. A profitable, fast-growing firm can "grow broke" by outrunning its financing. Reconcile profit to cash via *sources and uses*: increases in liabilities/equity and decreases in assets are sources of cash; the reverse are uses.

**Financial Leverage Is a Two-Edged Sword.** Substituting fixed-cost debt for equity raises owners' expected return *and* their risk. `ROE = ROIC × (D+E)/E − after-tax_rate × (D/E)` — leverage helps only while ROIC exceeds the after-tax borrowing rate. Finance by the **pecking order** (internal funds → debt → equity) unless a reason overrides it.

**Value = Discounted Free Cash Flow.** A dollar today beats a dollar tomorrow: `PV = CF/(1+r)^T`; accept projects when **NPV > 0** (believe NPV over IRR when they conflict). Value a whole firm as the **PV of free cash flow** `FCF = EBIT(1−t) + Depreciation − Capex − ΔWorking capital` discounted at WACC. **Fair market value = max(liquidation value, going-concern value)**; a firm destroys value by continuing when break-up value exceeds the value of staying a going concern.

**Risk Has Two Parts — and Only One Matters to Diversified Owners.** Risk = *dispersion* (standalone spread) + *correlation* (co-movement with the portfolio). Diversification cancels the first without cost (ice-cream stand + umbrella shop = riskless return), so the relevant risk is portfolio risk (beta). Escalate uncertainty handling up the ladder: **sensitivity → scenario → simulation → decision tree → real options**.

**Acquisition Discipline.** A buyer pays a *control premium* for what ownership can do that a minority share can't. Cap the bid at **standalone DCF value + PV of realizable synergies**. Paying more for synergies that never materialize is the classic M&A value destroyer.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-interpreting-financial-statements.md) | Interpreting Financial Statements | cash cycle, investment cycle, profits ≠ cash flow, sources & uses |
| [ch02](chapters/ch02-evaluating-financial-performance.md) | Evaluating Financial Performance | ROE, DuPont three levers, control ratios, ROE yardstick flaws |
| [ch03](chapters/ch03-financial-forecasting.md) | Financial Forecasting | percent-of-sales, pro forma, plug/EFR, cash-flow forecast |
| [ch04](chapters/ch04-managing-growth.md) | Managing Growth | sustainable growth equation (PRAT), balanced growth, growth menus |
| [ch05](chapters/ch05-financial-instruments-markets.md) | Financial Instruments and Markets | three-variable security model, efficient markets, hedging/derivatives |
| [ch06](chapters/ch06-the-financing-decision.md) | The Financing Decision | leverage two-edged sword, ROIC spread, WACC, pecking order, EBIT-EPS |
| [ch07](chapters/ch07-discounted-cash-flow.md) | Discounted Cash Flow Techniques | time value, NPV, IRR, payback, conflicting rankings |
| [ch08](chapters/ch08-risk-analysis.md) | Risk Analysis in Investment Decisions | dispersion vs correlation, diversification, risk ladder, real options |
| [ch09](chapters/ch09-business-valuation-restructuring.md) | Business Valuation and Corporate Restructuring | FCF valuation, multiples, control premium, LBO, M&A |

## Topic Index

- **Cash cycle / working capital** → ch01, ch03
- **Control ratios** → ch02
- **Corporate restructuring** → ch09
- **DCF / NPV / IRR** → ch07, ch09
- **DuPont / ROE decomposition** → ch02
- **Efficient markets** → ch05
- **External funding required (EFR)** → ch03
- **Financial leverage** → ch02, ch06
- **Free cash flow (FCF)** → ch09
- **Forecasting / pro forma** → ch03
- **Hedging / derivatives** → ch05, ch08
- **LBO / acquisition price** → ch09
- **Pecking order** → ch06
- **Risk analysis / diversification** → ch08
- **Sources & uses of funds** → ch01
- **Sustainable growth (g\*)** → ch04

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — reusable techniques (DuPont, PRAT, DCF, risk ladder…)
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, and tells on one page

---

## Scope & Limits

This skill covers the book's content only. Formulas and worked examples are faithful reconstructions of Higgins & Koski's framework, not verbatim excerpts. For hands-on implementation (building a live DCF or pro-forma spreadsheet), combine with project-specific tools or the `financial-analysis` skills. For topics beyond this text, ask the agent directly.