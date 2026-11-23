# Chapter 5: LBO Analysis

## Core Idea
LBO analysis translates an entry price, operating case, financing package, and exit assumption into sponsor equity returns and an implied maximum purchase price. Work backward from a required return or forward from a proposed price; make timing and cash-flow conventions explicit.

## Frameworks Introduced
- **LBO model sequence**: Set transaction assumptions and sources/uses; build operating projections; calculate cash available for debt service; roll forward each debt tranche; calculate exit enterprise/equity value; measure sponsor returns; sensitize key assumptions.
  - When to use: Assessing sponsor feasibility, bid capacity, or equity return potential.
  - How: Reconcile entry equity value and EV, include fees and refinancing; model interest and amortization by tranche; apply exit multiple to a stated metric; bridge exit EV to equity proceeds after debt and fees.
- **IRR and MOIC**: MOIC = total equity proceeds / invested equity; IRR is the annualized rate equating invested capital with dated proceeds. For a single investment and exit after `n` years, `IRR = MOIC^(1/n) − 1`.
- **Maximum purchase price**: Hold financing, operations, and exit assumptions constant; solve for the entry price at which sponsor IRR equals the hurdle. The answer is assumption-dependent, not a market fact.
- **Debt roll-forward**: Opening debt + borrowings − required amortization − optional repayments = ending debt; calculate interest using a consistent average-balance or contractual convention.

## Key Concepts
- **MOIC**: Multiple of invested equity capital returned at exit, before considering timing.
- **IRR**: Annualized discount rate that equates dated cash outflows and inflows.
- **Exit multiple**: Valuation multiple applied to a chosen terminal operating metric.
- **Cash available for debt repayment**: Cash after operating needs, taxes, interest, and required uses, subject to model conventions.
- **Debt tranche**: Financing instrument with distinct pricing, maturity, amortization, priority, or covenants.
- **Equity bridge**: Exit EV adjusted for debt, cash, and other claims to sponsor proceeds.
- **Hurdle rate**: Sponsor's target return used to evaluate price or deal feasibility.

## Mental Models
- Return is the product of entry discipline, business delivery, deleveraging, and exit—not a single multiple.
- MOIC ignores time; compare deals with IRR when holding periods differ.
- Separate operational performance from valuation-multiple expansion in attribution.

## Anti-patterns
- **Treating MOIC as an annual return**: A 2.0x in three years is not 100% IRR.
- **Ignoring interest circularity or debt terms**: Financing affects cash available for paydown and therefore returns.
- **Changing entry and exit definitions mid-model**: Keep EV, equity value, cash, debt, and fees consistent.
- **Crediting all return to leverage** while ignoring operating assumptions and exit multiple.
- **False precision in the maximum bid**: Report sensitivities and key constraints.

## Reference Tables
| Driver | Higher value generally does what? | Model check |
|---|---|---|
| Entry multiple | Reduces sponsor returns / bid capacity | Same metric and enterprise-value basis |
| EBITDA growth/margin | Raises cash generation and exit value | Support with operating drivers |
| Debt paydown | Raises equity proceeds if other factors fixed | Cash flow and debt waterfall support it |
| Exit multiple | Raises proceeds but increases market dependence | Sensitize compression and expansion |
| Holding period | Changes IRR for same MOIC | Use dated cash flows, not just endpoint ratio |

## Worked Example
A sponsor invests $100 and receives $200 after three years with no interim flows. MOIC is 2.0x; annual IRR is `2^(1/3)−1`, approximately 26.0%, not 100%. In an LBO model, exit proceeds would first be built from exit operating metric × exit multiple, then reduced by remaining debt and other claims. The sponsor's actual return uses the initial equity check and dated distributions, so recapitalizations or interim dividends require an IRR calculation from all dated flows.

## Key Takeaways
1. Build a transparent entry-to-exit bridge before interpreting returns.
2. Model each debt tranche and cash sweep explicitly.
3. Use IRR for time-adjusted return and MOIC for invested-capital multiple.
4. Solve bid capacity only under stated financing, operating, and exit assumptions.
5. Stress weaker operations, lower exit multiples, and slower repayment together.

## Connects To
- **Ch 4**: LBO suitability and financing logic.
- **Ch 1–3**: Entry and exit values can be cross-checked against comps and DCF.
