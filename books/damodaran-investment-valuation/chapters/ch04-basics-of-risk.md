# Chapter 4: The Basics of Risk

## Core Idea
The discount rate should compensate investors for risks they bear in the relevant claim. Equity models focus on exposure to market-wide risk; debt models focus on default risk and promised payments.

## Frameworks Introduced
- **Diversifiable versus nondiversifiable risk**: Separate firm-specific uncertainty that a diversified investor can spread away from systematic exposure that remains.
  - When to use: Choosing a required return for a traded equity or project.
  - How: Identify the marginal investor, the market portfolio, and the sensitivity of the investment to market returns; avoid charging twice for diversifiable noise.
- **CAPM**: Required equity return equals risk-free rate plus beta times an equity risk premium.
  - How: Use a risk-free rate and premium in the same currency, estimate beta for the business and leverage, and check whether the investor and market definition fit the case.
- **Default-risk pricing**: Lenders require a spread over a default-free rate, with ratings and coverage informing the spread.

## Key Concepts
- **Beta**: Sensitivity of an asset's return to the market portfolio, not a measure of total business risk.
- **Equity risk premium**: Extra return investors require for the market portfolio over a risk-free investment.
- **Default spread**: Additional promised yield reflecting the chance and severity of nonpayment.
- **Marginal investor**: Investor whose trading sets the market price and whose diversification matters for risk pricing.
- **Cost of capital**: Required return on the combined debt and equity financing of operations.

## Mental Models
- Risk in cash flows and risk in discount rates must describe the same uncertainty; do not haircut both for the same event.
- Distinguish volatility around expected returns from permanent operating damage and default exposure.

## Anti-patterns
- **Using total standard deviation as a CAPM premium**: It charges diversified investors for idiosyncratic risk.
- **Treating a rating as a constant of nature**: Ratings and spreads change with coverage, leverage, and the cycle.
- **Using a local equity premium by default for a globally owned asset**: Investor base and market exposure matter.

## Worked Example
Consider two firms with equally volatile stock returns. One moves with the broad market; the other has volatile company-specific product outcomes. A diversified investor may require a larger systematic premium for the first despite similar standalone volatility. For debt, a firm with weaker interest coverage and heavier borrowing generally faces a larger default spread even if its equity beta is modest. The chapter uses this distinction to explain why cost of equity and cost of debt need separate risk models.

## Key Takeaways
1. State whose risk is being priced and how diversified that investor is.
2. Use beta for systematic equity exposure and credit analysis for debt.
3. Keep risk-free rate, premium, and cash-flow currency consistent.

## Connects To
- **Ch 7**: Estimates risk-free rates and market/default premiums.
- **Ch 8**: Converts firm-specific betas and credit spreads into financing costs.

