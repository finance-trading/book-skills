# Chapter 7: Riskless Rates and Risk Premiums

## Core Idea
The risk-free rate is the base for valuation in a given currency and horizon; risk premiums compensate for bearing equity or default risk. Inconsistent currencies, maturities, or stale premiums contaminate every discounted value.

## Frameworks Introduced
- **Risk-free-rate selection**: A riskless investment has no default risk and no reinvestment risk over the cash-flow horizon.
  - When to use: Setting the discount-rate base in a DCF.
  - How: Use a long-term default-free government rate in the same currency as nominal cash flows; remove a sovereign default spread where necessary; use a real rate only with real cash flows.
- **Implied equity risk premium (ERP)**: Solve for the market premium that makes a broad index's observed level consistent with expected aggregate cash flows and a growth path.
  - Why it works: It ties a forward-looking market price to assumptions visible at the valuation date, unlike a historical average alone.
- **Country-risk adjustment**: Estimate incremental country exposure and decide whether the firm is exposed through operations, not just incorporation.
  - How: Consider sovereign default spreads, relative equity/bond volatility, and a firm-specific exposure factor; avoid adding the same risk twice.

## Key Concepts
- **Nominal rate**: Return stated in currency units including expected inflation.
- **Real rate**: Return in purchasing-power units.
- **Historical ERP**: Realized stock-minus-riskless return over a past sample.
- **Implied ERP**: Premium backed out from today's index price and forecast cash flows.
- **Sovereign spread**: Market compensation for a government's default risk.

## Mental Models
- A currency's inflation belongs in both cash flows and discount rate, or in neither.
- Country risk follows where revenues, costs, and assets are exposed, not merely where the firm is registered.

## Anti-patterns
- **Risky government yield as risk-free**: A sovereign default premium should not become the riskless base.
- **Blind historical average**: Sampling period, arithmetic/geometric choice, and structural market change can shift the estimate.
- **Country double count**: Do not add a separate premium when the cash-flow scenarios or base ERP already incorporate the same exposure.

## Worked Example
The chapter builds an implied ERP from the S&P 500 level at the start of 2024. It forecasts index cash flows and solves for the discount rate consistent with the observed level, then subtracts the matching risk-free rate. The result is not a universal constant: a change in expected earnings, payout, or index price changes the implied premium. When valuing a firm with emerging-market operations, the analyst then asks how much of its cash flow is exposed to country conditions before adding a country component.

## Key Takeaways
1. Match currency, inflation basis, and horizon throughout a valuation.
2. Treat the equity premium as a dated estimate with explicit method.
3. Separate sovereign, equity-market, and firm-specific exposure.

## Connects To
- **Ch 4**: Defines which risks are compensated.
- **Ch 8**: Applies risk-free rates and premiums to individual firms.

