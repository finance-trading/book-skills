# Chapter 12: Closure in Valuation: Estimating Terminal Value

## Core Idea
The terminal value is a continuation of operating economics after explicit forecasts, not an independent plug. Stable growth, reinvestment, risk, and survival must fit together.

## Frameworks Introduced
- **Stable-growth closure**: After a finite high-growth period, assume a sustainable growth rate and compute a continuing value from next-period cash flow divided by the gap between discount rate and growth.
  - When to use: A going concern is expected to survive beyond the explicit forecast.
  - How: Choose stable `g` consistent with the currency/economy; normalize margins and returns; set reinvestment to support `g`; check that discount rate exceeds `g`.
- **Competitive advantage period (CAP)**: Estimate how long excess returns can persist before competition drives them toward a mature level.
  - Why it works: The duration of excess returns often matters more than one year's headline growth rate.
- **Survival adjustment**: Model failure explicitly for ventures with meaningful mortality risk, and distinguish failure proceeds from continuing value.

## Key Concepts
- **Terminal value**: Present value at the end of the explicit forecast of subsequent cash flows.
- **Stable growth**: Long-run growth sustainable after exceptional expansion fades.
- **Excess return**: Return on invested capital above the cost of capital.
- **Liquidation value**: Proceeds if a business ceases operations, net of claims and costs.
- **Failure probability**: Chance that a going-concern terminal path never occurs.

## Mental Models
- The terminal period should look economically mature: lower growth normally brings changed reinvestment, margins, and risk.
- A small change in the discount-rate-minus-growth gap can dominate a valuation; test that sensitivity openly.

## Reference Formulas
| Claim being valued | Stable-growth terminal value at year `n` | Cash-flow and rate boundary |
|---|---|---|
| Operating firm | `TV_firm,n = FCFF_(n+1) / (WACC_(n+1) − g)` | FCFF belongs to debt and equity; use cost of capital |
| Equity | `TV_equity,n = FCFE_(n+1) / (Ke_(n+1) − g)` | FCFE belongs to shareholders; use cost of equity |
| Dividend-paying equity | `TV_equity,n = Div_(n+1) / (Ke_(n+1) − g)` | Use only when dividends represent the chosen equity cash flow |

For stable operating growth, `g = reinvestment rate × ROIC`, so `stable reinvestment rate = g / sustainable ROIC` when ROIC is positive. Thus `FCFF_(n+1) = EBIT_(n+1) × (1 − tax rate) × (1 − reinvestment rate)`. These relationships use long-run returns on **new** capital, and `g` must remain below the matching discount rate. An equity model instead links stable growth to equity reinvestment and sustainable ROE; do not transfer a firm ROIC denominator into FCFE.

## Anti-patterns
- **Perpetual super-growth**: A business cannot outgrow its economy indefinitely without becoming implausibly large.
- **Zero reinvestment plus positive stable growth**: The formula hides an unsupported growth engine.
- **Exit multiple as an unexamined plug**: A multiple is a pricing assumption with embedded growth and risk.

## Worked Example
The chapter uses Levi Strauss to ask how long a brand and competitive position could support above-normal growth. A high-growth forecast is first bounded by a plausible competitive advantage period; after that, the business shifts to a mature growth rate and reinvestment requirement. In the Eli Lilly stable-period illustration, `g = 4%` and sustainable `ROIC = 15%` imply a `4% / 15% = 26.67%` reinvestment rate. If an analyst instead raised `g` while leaving reinvestment fixed, terminal cash flow would be overstated. The Alloy Mills illustration similarly shows that the value of growth depends on returns on new capital.

## Key Takeaways
1. Derive terminal cash flow from a coherent mature business state.
2. Test the CAP and `r − g` sensitivity.
3. Include survival or liquidation paths when going-concern assumptions are fragile.

## Connects To
- **Ch 11**: Supplies growth and reinvestment assumptions.
- **Ch 14–15**: Applies terminal value in equity and firm DCFs.

