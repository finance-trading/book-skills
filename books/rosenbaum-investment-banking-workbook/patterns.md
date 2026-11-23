# Patterns and Techniques

## Build a Trading-Comps Table
**When to use**: Market valuation benchmark for a company.
**How**: Set valuation date and peer criteria; gather share price, diluted share data, debt, cash, and financials; calculate diluted equity value and EV; align LTM and forecast periods; normalize metrics; calculate matching multiples; explain range and target positioning.
**Trade-offs**: Observable prices are current but affected by market sentiment and peer mismatch.

## Calculate Option Dilution with TSM
**When to use**: Options or warrants may materially dilute shares.
**How**: For each in-the-money tranche, calculate net shares as `options × (share price − strike price) / share price`; sum net shares and add to basic shares. Include other securities only under the relevant dilution convention.
**Trade-offs**: Simplifies potential exercise; actual dilution depends on instrument terms and applicable accounting/valuation convention.

## Build a Precedent Transaction Set
**When to use**: Estimating control transaction value or evaluating a bid.
**How**: Select comparable announced/completed deals; record date, buyer, consideration, target metric, and deal circumstances; bridge to EV consistently; normalize denominators; inspect outliers and apply a context-weighted range.
**Trade-offs**: Deal prices embed control, competition, financing markets, and buyer-specific value; stale precedents may mislead.

## Forecast FCFF and Terminal Value
**When to use**: Standalone operating valuation with explicit forecasts.
**How**: Forecast operating drivers; derive EBIT and operating taxes; calculate FCFF after D&A, capex, and NWC investment; discount at WACC; calculate stable-state terminal value; add PVs; bridge EV to equity; sensitize key assumptions.
**Trade-offs**: Transparent and flexible but highly sensitive to long-run assumptions; terminal state must be economically plausible.

## Reconcile LBO Sources and Uses
**When to use**: Screening acquisition financing or building a buyout model.
**How**: List purchase consideration, refinanced debt, fees, and other uses; list debt, rollover, and sponsor equity sources; solve for sponsor check; verify sources equal uses before calculating returns.
**Trade-offs**: A clean reconciliation does not prove debt is financeable or the business can service it.

## Roll Debt Through the Forecast
**When to use**: Estimating cash paydown and sponsor proceeds.
**How**: Forecast cash available after operating requirements and interest; apply mandatory amortization and cash sweep; update ending balances by tranche; calculate interest using documented conventions; test covenant headroom and downside cases.
**Trade-offs**: Detailed financing terms improve fidelity but can create circularity; state how interest and optional repayments are modeled.

## Convert LBO Exit to Equity Returns
**When to use**: Comparing sponsor cases or solving a bid price.
**How**: Apply exit multiple to a stated metric; bridge EV to equity proceeds after debt/claims; include interim flows and initial equity; calculate both MOIC and dated-cash-flow IRR; sensitize entry, operations, debt paydown, exit multiple, and time.
**Trade-offs**: Return estimates depend on financing and exit conditions; do not present a single case as certainty.

## Compare M&A Bids on Certainty-Adjusted Terms
**When to use**: Seller choosing between offers.
**How**: Compare price, consideration, financing, conditions, diligence, regulatory path, timing, and closing probability; assess seller obligations and risk; update as diligence resolves uncertainty.
**Trade-offs**: Certainty is difficult to quantify and seller priorities may include non-price terms.

## Underwrite Synergies and a Walk-Away Price
**When to use**: Buyer evaluating acquisition value beyond standalone economics.
**How**: Identify synergy mechanism and owner; estimate timing, probability, cost, taxes, and dis-synergies; discount expected net benefits; set maximum price and conditions before competitive pressure; revise only for verified evidence.
**Trade-offs**: Estimates are uncertain and benefits can be competed away; strategic rationale is not itself measurable value.
