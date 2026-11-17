# Cheatsheet — Analysis for Financial Management

## Decision Rules (if/then)

| Situation | Do | Because |
|---|---|---|
| Evaluating performance | Compute ROE = margin × turnover × leverage | One number → three levers → one cause |
| ROE just rose | Check the *leverage* lever first | Leverage raises return only with more risk |
| Actual growth > sustainable growth | Sell equity / raise debt / cut payout / prune / merge | Growth beyond g* burns cash faster than it earns it |
| Actual growth < sustainable growth | Dividend / buyback / acquire | The firm is a cash machine with no internal reinvestment |
| New project | Accept iff NPV > 0 | NPV prices timing and full horizon correctly |
| NPV vs IRR conflict | Believe NPV | IRR assumes reinvestment at the IRR, not the cost of capital |
| Adding debt | Require ROIC > after-tax borrowing rate | Only then does leverage add to ROE |
| Valuing a firm | PV of free cash flow at WACC | Everything else is a shortcut to this |
| Deciding to keep operating | Only if going-concern > liquidation value | Otherwise continuing destroys value |
| Acquiring | Cap the bid at DCF + PV(synergies) | Premium beyond realizable synergies is money burned |

## The Sustainable Growth Equation (the book's signature tool)

```
g* = P × R × A × T̂   =   Retention × ROE
     P = profit margin      R = retention (1 − payout)
     A = asset turnover     T̂ = assets/equity (opening)
```
Actual vs. g* → **gap = the management problem**. Deficit → financing menu. Surplus → allocation menu.

## Valuation Bottom Line

```
FMV = max( Liquidation value, Going-concern value )
FCF = EBIT(1 − t) + Depreciation − Capex − Δ Working capital
Equity value = PV(FCF @ WACC) − Debt
Acquisition price ≤ standalone value + PV(synergies)
```

## Risk: Which Number Matters

| If holder can… | Relevant risk | Measure |
|---|---|---|
| Hold only this asset | Standalone ("Robinson Crusoe") | Standard deviation |
| Diversify | Portfolio risk | Beta / correlation |

Ladder by uncertainty: **sensitivity → scenario → simulation → decision tree → real options**.

## Thresholds & Defaults (Higgins' rule of thumb)

- Internal funds (retained profit + depreciation) ≈ **75%** of U.S. business financing — forecast internal capacity first.
- Report ROE decomposition to **two decimals × three factors**; confirm they multiply back to reported ROE before trusting the diagnosis.
- A growth plan is **incomplete without its financing source** — never accept sales targets stated in isolation.

## Tells & Smells

| You see… | You're probably… |
|---|---|
| Cash-days falling (22→7) while payables stretch (39→66) | Funding growth on stretched suppliers — near a liquidity squeeze |
| Rising inventory/receivables with flat turnover | Cash stuck in the working-capital cycle |
| ROE up on climbing debt/equity | Confusing risk for performance |
| Payback looks attractive but NPV < 0 | Being fooled by timing (late losses ignored) |
| An acquirer paying far above standalone DCF | Betting on synergies that must now deliver |