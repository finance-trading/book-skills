# Decision Cheatsheet

| If you face… | Do this | Because… |
|---|---|---|
| Public-company peer valuation | Define peers and period first; use diluted equity and EV | The numerator is only meaningful with sound peer and claim definitions |
| Options / warrants | Use TSM for in-the-money tranches | Exercise proceeds offset part of share dilution |
| EV / EBITDA, EV / EBIT, EV / sales | Compare against operating metrics | Enterprise value represents all capital providers |
| P/E | Compare equity value with common net income/EPS | Both are equity-level measures |
| Peer multiple outlier | Investigate growth, margin, risk, capital needs, and denominator quality | Outlier may be economics or noisy data |
| Acquisition benchmark | Normalize EV and target metric; inspect deal date and process | Precedents include context-specific control and competition effects |
| DCF growth forecast | Forecast capex and working capital with growth | Growth consumes reinvestment cash |
| DCF discount rate | Match FCFF with WACC; align currency and nominal/real basis | Mismatch systematically distorts value |
| Perpetuity terminal value | Require WACC > g and test a stable-state business | Formula breaks down and becomes implausible as g approaches WACC |
| LBO candidate | Stress cash conversion, capex, working capital, interest, and covenants | Debt is serviced with cash, not EBITDA |
| Sources/uses do not balance | Fix funding or transaction uses before modeling returns | An unbalanced deal has no valid sponsor check |
| Similar MOICs, different holding periods | Compare dated-flow IRR | MOIC ignores time |
| High sponsor return | Attribute to operations, debt paydown, entry, and exit multiple | Separates controllable execution from market re-rating |
| Seller gets competing bids | Compare financing, conditions, timing, and certainty as well as price | A high conditional offer may not close |
| Buyer claims synergies | Net costs, probability-weight, and time benefits; set walk-away price | Gross synergy claims overstate value available to the buyer |
| Deal is EPS-accretive | Test NPV and return on invested capital separately | Accretion is not proof of value creation |

## Fast model checks

- `Equity value = share price × fully diluted shares` (state any share-class adjustments).
- `EV = equity value + debt-like claims − cash` (apply consistent claim definitions).
- `FCFF = EBIT × (1 − tax rate) + D&A − capex − ΔNWC`.
- `TV = next-period FCFF / (WACC − g)` only for a sustainable stable state with `WACC > g`.
- `MOIC = equity proceeds / invested equity`; for one entry and one exit after `n` years, `IRR = MOIC^(1/n) − 1`.
- LBO sources must equal uses; exit EV must be bridged to equity proceeds after remaining debt and other claims.
- A model output is not diligence: verify inputs, timing, accounting definitions, and financing terms.
