# Decision Cheatsheet

| If you face… | Do this | Because… |
|---|---|---|
| FCFF forecast | Discount at WACC, bridge firm value to equity | Cash belongs to all capital providers |
| FCFE/dividend forecast | Discount at Ke | Cash belongs to equity holders |
| Nominal cash in a currency | Use nominal discount rate in that currency | Inflation/currency mismatch changes value mechanically |
| High growth and little reinvestment | Challenge sales-to-capital and marginal ROIC | Growth must be funded |
| Perpetual `g` near `r` | Rebuild stable state, returns and reinvestment | Terminal value becomes unstable |
| Low P/E | Normalize earnings, payout, growth and risk | Multiple can signal weak economics |
| Low P/B | Compare sustainable ROE with Ke | Below-book pricing may be justified |
| Low EV/EBITDA | Inspect taxes, capex and working capital | EBITDA is before owner cash costs |
| Bank | Use equity distributions or excess ROE | Debt is an operating input and capital is regulated |
| Loss-making firm | Diagnose cyclical, temporary, investment or structural loss | Different causes require different forecasts |
| Young firm | Forecast market × share × margin, then capital and survival | History is too short to extrapolate |
| Acquisition | Value target status quo, control, synergy, cost and price separately | Combined value need not accrue to buyer |
| Patent/reserve/project option | Prove the right and exercise choice, then check base DCF | Uncertainty alone is not an option |
| Multiple plausible future states | Choose scenario/tree/simulation by decision structure | A single discount-rate premium can hide branches |

## Compact equations and boundaries

- `FCFF = EBIT(1−t) + D&A − capex − ΔNWC`; discount at WACC.
- `FCFE = NI + D&A − capex − ΔNWC + net debt issued`; discount at Ke.
- Stable firm `TV_n = FCFF_(n+1)/(WACC−g)` and stable equity `TV_n = FCFE_(n+1)/(Ke−g)`; require `g < r` and `stable reinvestment = g/ROIC` for firm growth.
- Stable trailing `P/E = payout(1+g)/(Ke−g)`; stable `P/B = (ROE−g)/(Ke−g)` when book equity is meaningful.
- Bank `excess equity return = (ROE−Ke)×equity capital`; EVA `= NOPAT−WACC×invested capital`.

Treat these as model relationships under their stated assumptions, not market price targets. Check the linked chapters before applying them to a real company.

