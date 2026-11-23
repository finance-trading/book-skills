---
name: curtis-faith-turtle-trading
description: "Knowledge base from 《海龟交易法则》(Way of the Turtle) by Curtis Faith. Use when applying Turtle trading rules — 20-day/55-day breakouts, N/ATR position sizing, 1% risk per unit, 2N stops, 4-unit caps, pyramiding, 10/20-day exits, money management, backtest robustness, or trading psychology."
---

# 海龟交易法则

**Author**: Curtis Faith（柯蒂斯·费思）著，乔江涛 译 | **Pages**: ~250 | **Chapters**: 13 + 尾声 + 附录 | **Generated**: 2026-11-19

> **Text source**: this PDF is a ~96 DPI scan. It was re-OCR'd with RapidOCR at 300 DPI and the core rules were cross-checked against Tesseract 5 (`chi_sim+eng`) and ocrmypdf on the same pages. The trading rules and numbers below are reliable; see [Data Reliability](#data-reliability) for the two known book-internal inconsistencies.

## How to Use This Skill

- **Without arguments** — load the core Turtle frameworks and rule set below.
- **With a topic** — ask about `头寸规模`, `N值`, `止损`, `退出`, `系统1`, `系统2`, `加仓`, `资金管理`, `回测`, `最优化`, `稳健性`, `心理`, or another indexed topic; read the linked chapter.
- **With chapter** — ask for `ch01`–`ch15`; load that file.
- **Need the exact rules** — read [ch15](chapters/ch15-original-turtle-rules.md); it reproduces the complete original Turtle system.

---

## Core Frameworks & Mental Models

### 1. A complete mechanical system answers five questions
Market (what to trade), position size (how much), entry (when to buy/sell), stop (when to abandon a loser), exit (when to close a winner) — plus tactics (how to place orders). A system that omits any one of these is incomplete. Use `ch10`, `ch15`.

### 2. Volatility normalization via N
N is the 20-day ATR (average true range, in price points). Every position is sized so that a 1N move equals **1% of account equity**. This makes one unit in crude oil and one unit in gold carry the same dollar risk. Use `ch15`.

### 3. Risk budget: 2N stop, 4-unit cap
- Stop-loss = **2N** from entry (long: entry − 2N; short: entry + 2N) → ~2% risk per unit.
- Add units every **1/2N** in the trade's favor, up to **4 units** per market.
- Caps per direction: **4** per market, **6** in closely correlated markets, **10** in loosely correlated markets, **12** total.
Use `ch08`, `ch15`.

### 4. Two entry systems
- **System 1**: 20-day breakout; skip a signal if the previous breakout was profitable; use the 55-day breakout as the failsafe.
- **System 2**: 55-day breakout; every breakout is valid.
Use `ch15`.

### 5. Exits are half the system
- System 1 exits on a **10-day** opposite breakout.
- System 2 exits on a **20-day** opposite breakout.
Letting profits run is deliberate: most breakouts fail, so the few large trends must pay for many small losses. Use `ch15`.

### 6. Edge is measurable, not mystical
An edge is a positive statistical expectancy. Measure entries with **E-ratio**: average Maximum Favorable Excursion (MFE) divided by average Maximum Adverse Excursion (MAE), both normalized by ATR. E-ratio > 1 suggests a positive entry edge. Use `ch05`.

### 7. Robustness beats optimization
Historical tests mislead through trader effect, random effect, over-optimization, and sample-size error. Prefer simple rules, more markets, out-of-sample and rolling-window tests, and robust metrics (RAR, R-cubed) over peak-fit CAGR/Sharpe/MAR. Use `ch11`, `ch12`, `ch13`.

### 8. Trade the present, not a prediction
You cannot know whether price will rise or fall; you can know that trends recur because human psychology recurs. Judge decisions by process and expectancy, not by whether one trade won. Use `ch04`.

### 9. Survival precedes returns
Control bankruptcy risk first: size positions so a losing streak cannot remove you from the game. A steady 20–30% annual return compounds enormously if you never blow up. Use `ch08`.

---

## Chapter Index

| # | Chapter | File | Core theme |
|---|---|---|---|
| 01 | 冒险迷 | [ch01](chapters/ch01-risk-junkies.md) | Traders vs investors; risk transfer; liquidity/price risk; floor panic |
| 02 | 揭秘海龟思维 | [ch02](chapters/ch02-turtle-mindset.md) | Cognitive biases; trading styles; four market states |
| 03 | 得之不易的200万美元 | [ch03](chapters/ch03-million-dollar-education.md) | The Turtle training; four core principles; bankruptcy risk |
| 04 | 像海龟一样思考 | [ch04](chapters/ch04-think-like-a-turtle.md) | No right/wrong; forget the past; probability thinking |
| 05 | 掌握优势 | [ch05](chapters/ch05-mastering-the-edge.md) | Edge components; MFE/MAE; E-ratio; filters |
| 06 | 寻找优势 | [ch06](chapters/ch06-finding-an-edge.md) | Support/resistance; where trends start; choppy markets |
| 07 | 如何衡量风险 | [ch07](chapters/ch07-measuring-risk.md) | Drawdown, CAGR, volatility, Sharpe, MAR, system death |
| 08 | 风险与资金管理 | [ch08](chapters/ch08-money-management.md) | Bankruptcy risk; position sizing; survival first |
| 09 | 海龟式积木 | [ch09](chapters/ch09-turtle-building-blocks.md) | Breakouts, moving averages, channels, timed exits |
| 10 | 海龟式交易：按部就班 | [ch10](chapters/ch10-step-by-step.md) | Building and testing six systems; adding stops |
| 11 | 历史测试的谎言 | [ch11](chapters/ch11-backtest-lies.md) | Trader effect, random effect, optimization |
| 12 | 脚踏实地 | [ch12](chapters/ch12-on-solid-ground.md) | Statistical basis; robust metrics; Monte Carlo; sample size |
| 13 | 防卫系统 | [ch13](chapters/ch13-defensive-systems.md) | Robust trading; diversification; market categories; humility |
| 14 | 尾声：万事俱备 | [ch14](chapters/ch14-epilogue.md) | Life as a trader; learning from failure; money and meaning |
| 15 | 附录：原版海龟交易法则 | [ch15](chapters/ch15-original-turtle-rules.md) | Complete original rule set and worked examples |

---

## Topic Index

- **破产风险** → ch03, ch08
- **策略/系统死亡** → ch07
- **支撑与阻力** → ch06
- **E-比率 / MFE / MAE** → ch05
- **过滤器** → ch05, ch13
- **加仓 / 金字塔加仓** → ch15
- **价格动荡** → ch07
- **交易者效应** → ch11
- **均值 / 移动均线** → ch09, ch10
- **蒙特卡洛检验** → ch12
- **N值 / ATR** → ch15
- ** robustness 稳健性** → ch12, ch13
- **市场状态** → ch02, ch09
- **随机效应** → ch11
- **头寸单位 / 头寸规模** → ch08, ch15
- **退出** → ch09, ch15
- **系统1 / 系统2** → ch15
- **心理偏差** → ch02, ch04
- **最优化 / 曲线拟合** → ch11
- **止损** → ch08, ch15
- **资金管理** → ch08

---

## Key Rules & Formulas (verified)

```text
TR  = max(H − L, H − PDC, PDC − L)
N   = (19 × PDN + TR) / 20          # 20-day ATR, exponential smoothing
$vol = N × dollars_per_point
Unit = (0.01 × account_equity) / $vol   # round down to whole contracts

Stop (long)  = entry − 2N
Stop (short) = entry + 2N
Add unit at entry ± 0.5N intervals, max 4 units per market
Exit System 1: 10-day opposite breakout
Exit System 2: 20-day opposite breakout
```

Worked example from the book (heating oil): N = 0.0141, account = $1,000,000, $42,000 per point → unit = 0.01 × 1,000,000 / (0.0141 × 42,000) = 16.88 → **16 contracts** (`ch15`).

---

## Data Reliability

The scan is low-resolution (~96 DPI) and heavily watermarked. Three engines were compared on the critical pages:

| Fact | RapidOCR 300 | Tesseract 300 | ocrmypdf | Verdict |
|---|---|---|---|---|
| 20-day breakout | ✓ | ✓ | ✓ (number; “日” misread as “月”) | reliable |
| 55-day breakout | ✓ (multiple pages) | ✓ | ✓ | reliable |
| 1N = 1% of equity | ✓ | ✓ | ✓ | reliable |
| 2N stop / 2% cap | ✓ | ✓ | ✓ | reliable |
| 1/2N adds, 4 units | ✓ | ✓ | ✓ | reliable |
| 4 / 6 / 10 / 12 caps | ✓ (body text) | ✓ | partial | reliable |
| 10-day / 20-day exits | ✓ | ✓ | partial | reliable |
| N = 20-day ATR formula | ✓ (definition) | partial | ✓ `(19×PDN+TR)/20` | reliable |

Known book-internal inconsistencies (not OCR errors — confirmed by two engines):
1. **System 2 length**: the appendix says **55-day**; the main text (ch03) describes it as **60 trading days / 12 trading weeks**. Both are reported; the appendix rule (55-day) is treated as authoritative for the rule set.
2. **N definition wording**: the appendix once calls N a “20-day simple average”, while the body and the formula define it as a **20-day exponential moving average** (`(19×PDN+TR)/20`). Use the formula.

OCR limitations: body prose still contains character substitutions (e.g. 入市→人市), and charts/tables are unreliable. No key number or rule above depends on an unverified chart reading.

---

## Supporting Files

- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — reusable trading techniques and system patterns
- [cheatsheet.md](cheatsheet.md) — decision tables and quick reference

---

## Scope & Limits

This skill covers the book only. The Turtle rules were designed for liquid US futures in the 1980s; position limits, contract specifications, commissions and slippage differ today. Nothing here is investment advice. Backtest any rule set on your own market, costs and account size before risking capital.
