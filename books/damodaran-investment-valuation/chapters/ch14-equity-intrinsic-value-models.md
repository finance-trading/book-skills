# Chapter 14: Equity Intrinsic Value Models

## Core Idea
Value equity using cash flows available to shareholders, discounted at a cost of equity. Actual dividends, potential dividends, and FCFE can differ sharply when firms retain cash, repurchase shares, or change leverage.

## Frameworks Introduced
- **Dividend discount model (DDM)**: Discount expected dividends, including terminal dividends, at the equity required return.
  - When to use: A stable payout policy transmits most distributable cash to shareholders, such as a regulated utility or mature bank.
- **Augmented dividend model**: Add buybacks to dividends when repurchases are a recurring mechanism for returning cash.
  - How: Use net repurchases rather than gross announcements and check whether debt issuance funds payouts.
- **FCFE model**: Discount cash flow available after reinvestment and debt financing, regardless of whether management distributes it.
  - When to use: Payouts diverge from cash-generating capacity, but equity cash flows can be forecast.
- **Stable/two-stage/three-stage growth**: Match the number of growth phases to the firm's expected transition rather than defaulting to one perpetual rate.

## Key Concepts
- **Dividend payout ratio**: Dividends relative to earnings.
- **Share repurchase**: Cash distribution through buying back shares; may be discretionary or offset by issuance.
- **FCFE**: Cash remaining for common equity after taxes, reinvestment, and net debt financing.
- **Cost of equity**: Return shareholders require for the risk of equity cash flows.
- **Transition period**: Explicit span over which above-normal growth and payout fade toward maturity.

## Mental Models
- A low dividend does not necessarily make equity less valuable if undistributed cash is invested productively or held for owners.
- A high dividend can exceed sustainable FCFE and require borrowing or asset sales.

## Reference Formulas
- Stable dividend model: `P0 = D1 / (Ke − g)`, where `D1` is next-period dividend, `Ke` is cost of equity, and `g < Ke` is sustainable perpetual dividend growth.
- FCFE model: `Equity value = Σ[FCFE_t / (1 + Ke)^t] + TV_equity,n / (1 + Ke)^n`; the terminal value uses next-period FCFE and a stable equity growth/return/reinvestment path. Repurchases belong in an augmented payout model only on a **net** basis, after related issuance.

## Anti-patterns
- **DDM on a firm with arbitrary low payout**: It can understate value when cash is retained or used for buybacks.
- **Counting gross buybacks without issuance**: Employee share compensation and new issuance can offset the claimed distribution.
- **FCFE with WACC**: Equity cash flows require the cost of equity.

## Reference Table
| Model | Cash flow discounted | Best fit | Main check |
|---|---|---|---|
| DDM | Dividends | Stable payout | Dividends versus capacity |
| Augmented DDM | Dividends + net repurchases | Repurchase-heavy payout | Net issuance and debt funding |
| FCFE | Potential equity cash flow | Payout differs from capacity | Reinvestment and net borrowing |

## Worked Example
The Consolidated Edison illustration values a regulated monopoly using dividends because payout and mature growth are relatively interpretable. In contrast, the Nestlé FCFE illustration evaluates distributable cash after reinvestment and financing instead of assuming historical dividends reveal the entire equity cash flow. For either firm, growth-phase assumptions must shift payout and reinvestment together; an unchanged payout ratio paired with arbitrary growth may not be feasible.

## Key Takeaways
1. Choose the equity cash flow that best represents shareholder capacity.
2. Check dividends and buybacks against FCFE and balance-sheet funding.
3. Match growth stages, reinvestment, and equity discount rate.

## Connects To
- **Ch 10**: Constructs FCFE from earnings.
- **Ch 15**: Contrasts direct equity valuation with firm valuation.

