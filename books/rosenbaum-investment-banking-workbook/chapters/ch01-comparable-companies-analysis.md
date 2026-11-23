# Chapter 1: Comparable Companies Analysis

## Core Idea
Trading comparables estimate a company's implied market value by benchmarking it against publicly traded peers. The work is not selecting a convenient multiple: it is normalizing the target and peer data, matching periods and claims, and explaining why differences in growth, risk, margins, and capital intensity justify a range.

## Frameworks Introduced
- **Trading-comps workflow**: Define the peer set; collect market and operating data; calculate enterprise/equity values; normalize financials; compute trading multiples; interpret and apply the range.
  - When to use: Market-based valuation of a public company or a private-company reference point.
  - How: Select genuinely comparable businesses, use a common valuation date and fiscal period, calculate fully diluted equity and enterprise value, normalize LTM/forward metrics, then apply relevant peer multiples to target metrics.
- **Treasury-stock method (TSM)**: Include in-the-money options as incremental shares net of the shares repurchased with exercise proceeds.
  - How: For options with strike K below share price P, net new shares = options × (P−K)/P; sum in-the-money tranches, add to basic shares, and add convertible securities only when dilutive and appropriately converted.
- **EV/equity claim matching**: Enterprise-value multiples use pre-financing operating metrics; equity multiples use metrics attributable to common shareholders.
  - Why it works: It prevents mixing enterprise value with equity earnings or vice versa.

## Key Concepts
- **Fully diluted shares**: Basic shares plus net dilutive shares from options, warrants, and convertible securities.
- **Enterprise value**: Equity value plus debt and other debt-like claims less cash and cash equivalents, subject to the definition used.
- **LTM**: Last twelve months of historical operating results, often assembled from latest fiscal year and interim periods.
- **Forward multiple**: Current valuation divided by a forecast-period metric (for example, NTM EBITDA).
- **Trading comps**: Public-company valuation benchmarks based on observed market prices.
- **Normalization**: Adjustment of reported results for nonrecurring or non-operating items on a defensible, consistent basis.
- **FCF yield**: Free cash flow divided by equity value or enterprise value; state the chosen denominator.

## Mental Models
- Treat the peer set as a hypothesis about substitutability, not a list of industry labels.
- Keep the numerator and denominator on the same claim basis and the same time horizon.
- Move from observed peers to target value only after explaining differences; the median is a reference, not an answer.

## Anti-patterns
- **Mixing claims**: Applying EV/EBITDA to equity value or P/E to enterprise value produces a category error.
- **Unexamined outliers**: A low or high multiple may reflect different growth, risk, leverage, accounting, or a bad denominator—not a data point to blindly average.
- **Convenient normalization**: Adjusting only the target or accepting every peer's “one-time” add-back biases the comparison.
- **Blind peer selection**: Shared sector codes do not establish similar economics.

## Reference Tables
| Metric | Numerator | Denominator | Typical use |
|---|---|---|---|
| EV/Sales | Enterprise value | Revenue | Early-stage/low-margin firms; ignores profitability differences |
| EV/EBITDA | Enterprise value | EBITDA | Capital structure-neutral operating comparison; ignores capex and taxes |
| EV/EBIT | Enterprise value | EBIT | Includes depreciation burden |
| P/E | Equity value per share / share price basis | Net income / EPS | Equity-level earnings comparison |
| FCF yield | Free cash flow (define FCFF or FCFE) | EV or equity value | Cash return benchmark; denominator must match cash-flow claim |
| Debt/EBITDA | Debt (define gross or net) | EBITDA | Credit leverage, not an equity valuation multiple |

## Worked Example
A company has 100.0 million basic shares, $50 share price, and 2.75 million in-the-money options with $62.5 million aggregate exercise proceeds. TSM repurchases 1.25 million shares at $50; net option dilution is 1.50 million shares. Fully diluted shares are 101.50 million and equity value is $5,075 million. With $1,850 million debt and $100 million cash, EV is $6,825 million. Before applying peer multiples, check whether the share count, debt, cash, and financial metric refer to the same measurement date; then choose EV multiples for operating metrics or P/E for common earnings.

## Key Takeaways
1. Establish an economically defensible peer group before calculating summary statistics.
2. Calculate diluted equity value before bridging to enterprise value.
3. Use EV multiples with operating metrics and equity multiples with equity metrics.
4. Align LTM and forecast periods; identify fiscal-year conventions explicitly.
5. Normalize consistently and explain why target multiples should differ from peer observations.

## Connects To
- **Ch 2**: Precedent transactions add control and deal-context effects to market benchmarks.
- **Ch 3**: DCF offers an intrinsic cross-check with explicit cash-flow assumptions.
- **Glossary**: Fully diluted shares, EV, TSM, LTM, normalization.
