# Chapter 6: Recapitalizations, Stub Stocks, LEAPS, Warrants, and Options

## Core Idea
Leverage magnifies equity returns and losses. A recapitalized stub or long-dated call can create a leveraged, limited-loss exposure, but neither is inherently attractive: first establish the underlying business value, then compare the instrument's full cost, expiration, capital structure, and downside with owning the stock or staying out.

## Frameworks Introduced
- **Recapitalization / stub valuation**: A company distributes debt, preferred securities, or cash to shareholders, leaving a highly leveraged residual equity (“stub”). Value the package as distributed claims plus remaining equity; account for tax effects, interest coverage, reduced equity cushion, and multiple compression. Modest operating changes can produce large stub moves in either direction.
- **Underlying security before leverage**: Find a compelling stock or special situation first; only then compare calls/LEAPS, warrants, or common shares. Leverage should express a well-researched thesis, not substitute for one.
- **LEAPS payoff comparison**:
  1. Estimate the stock's value under adverse, base, and favorable cases by expiration.
  2. For a call, calculate payoff as max(stock value − strike, 0) less premium; maximum loss is premium, but total loss is plausible.
  3. Compare the call's price with intrinsic value, time value, implied financing cost, volatility/protection cost, and remaining time.
  4. Reject calls whose expiration arrives before the catalyst or thesis can reasonably play out.
- **Event-driven option mispricing**: Option models may not capture imminent corporate actions if the future price move comes from a spinoff, restructuring, or merger rather than historical volatility. Confirm distribution mechanics, adjusted deliverables, dates, strike, and expiration; the market may already price the event.
- **Warrants**: Because the issuer creates them and they often have longer lives than exchange calls, check whether an attractive company's warrant offers a suitable leveraged claim. Account for dilution, exercise terms, and expiration.

## Key Concepts
- **Recapitalization**: Change in a firm's capital structure, often distributing debt or securities while leaving common equity more leveraged.
- **Stub stock**: Residual common equity after a recapitalization or after valuing separated assets.
- **Call option**: Right, not obligation, to buy an asset at a strike price before expiration.
- **LEAPS**: Long-dated listed equity options.
- **Warrant**: Issuer-created right to buy newly issued shares, often with a longer term than standard options.
- **Intrinsic value**: For a call, current stock price above strike, if any.
- **Time value**: Premium above intrinsic value reflecting time, financing, and uncertainty.

## Mental Models
An option is prepaid, time-limited, leveraged exposure with a hard loss cap at premium—not a cheap stock substitute. A stub resembles leveraged equity with no contractual expiration but can still be wiped out by insolvency. In event options, the calendar and exact deliverable are part of valuation.

## Anti-patterns
- **Buying options before liking the underlying**: A right to buy a poor business at a fixed price is not a value investment.
- **Ignoring time decay and expiration**: Being right about value after expiry still loses the premium.
- **Treating capped loss as low risk**: Repeated total-premium losses can be severe, and leverage amplifies volatility.
- **Assuming recap tax benefits guarantee value**: Excessive debt can overwhelm tax savings and operating resilience.

## Worked Example
Greenblatt's Wells Fargo case began with a stock thesis: a severe real-estate recession had driven extraordinary loan-loss provisions, yet existing reserves, capital, and cash earnings suggested the bank could survive. At $77, a long-dated $80 call cost $14; if the stock reached $160 by expiry, the option's intrinsic payoff would be $80, a $66 gain, while failure could cost the full $14. The option improved the modeled upside/downside only if the survival analysis and two-year timing held. The lesson is not to copy the historical trade, but compare stock and option outcomes using current terms and independent probabilities.

## Key Takeaways
1. Analyze the business before selecting the leveraged instrument.
2. Model total loss, expiration, financing/time value, and event timing.
3. Use recaps and stubs only when post-deal debt remains serviceable under stress.
4. Compare options with common stock and cash; leverage is a choice, not a requirement.

## Connects To
- **Ch 3–5**: Spinoffs, merger securities, and restructurings provide catalysts and forced sellers.
- **Ch 7**: Primary-source research and cash-flow analysis underpin the thesis.
- **Ch 8**: Position sizing and portfolio limits control leverage's aggregate risk.