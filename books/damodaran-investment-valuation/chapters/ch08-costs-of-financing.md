# Chapter 8: Estimating Risk Parameters and Costs of Financing

## Core Idea
Translate market-wide rates and premiums into firm-specific costs of equity and debt, then weight them by market values to discount cash flows to the firm.

## Frameworks Introduced
- **Regression beta**: Estimate a traded stock's sensitivity to a relevant market index, but inspect its standard error, trading frequency, business mix, and leverage.
  - When to use: A liquid firm has meaningful return history and a representative business mix.
- **Bottom-up beta**: Estimate unlevered business betas from comparable firms, weight by the subject firm's business mix, and relever for target debt/equity.
  - When to use: A firm has changed businesses or financing, thin trading, or an unstable regression beta.
  - Why it works: Industry economics are more stable than a single noisy stock regression.
- **Cost of debt and WACC**: Infer borrowing cost from traded debt, rating, or interest coverage and a default spread; tax-adjust debt cost when interest is deductible; weight debt and equity by market value.

## Key Concepts
- **Unlevered beta**: Business-risk component after removing the effect of financial leverage.
- **Relevered beta**: Business beta adjusted for the debt/equity mix used in the valuation.
- **Interest coverage**: Earnings capacity relative to interest obligations, sometimes used for a synthetic rating.
- **WACC**: Market-value-weighted required return on debt and equity financing.
- **Lambda**: Firm-specific sensitivity to country risk beyond broad market beta.

## Mental Models
- A company's historical beta describes an old business and capital structure; the valuation should price the expected one.
- An apparently precise WACC is only as good as its business mix, debt definition, and risk premiums.

## Reference Formula
The chapter's standard tax-adjusted leverage relation is `β_levered = β_unlevered × [1 + (1−tax rate) × D/E]`. To build a bottom-up beta, unlever each comparable, weight unlevered betas by the subject's business values, then relever using its target **market-value** debt/equity mix. This formula assumes debt beta is negligible and the interest tax shield is usable; distress and unusual debt risk require more care.

## Anti-patterns
- **Using book weights in a market-value discount rate**: Financing costs apply to current claim values, not historical accounting amounts.
- **Applying an unchanged beta after acquisition or divestiture**: The asset mix and leverage have shifted.
- **Double-counting cash or country risk**: A cash-heavy or multinational firm can have risk exposures different from its operating assets.

## Reference Table
| Situation | Preferred beta starting point | Required checks |
|---|---|---|
| Stable liquid stock | Regression | Index, period, noise, leverage |
| Changed or thinly traded firm | Bottom-up peer assets | Business weights, peer comparability |
| Private business | Bottom-up | Owner diversification and financing |

## Worked Example
The chapter estimates Microsoft's regression beta from stock and index returns, then builds a bottom-up beta from business comparables. An analyst should not choose whichever estimate gives the desired valuation: compare each estimate with the firm's changing product mix and leverage, remove the effect of cash where material, and use a consistent target capital structure. In the Enka example, a domestic-index beta and global-index beta answer different investor-exposure questions.

## Key Takeaways
1. Choose beta methodology from data quality and expected business mix.
2. Estimate the borrowing spread from current credit risk, not an old coupon alone.
3. Weight required returns by market values for firm cash flows.

## Connects To
- **Ch 7**: Supplies riskless rates and market premiums.
- **Ch 15**: Applies WACC in firm valuation.

