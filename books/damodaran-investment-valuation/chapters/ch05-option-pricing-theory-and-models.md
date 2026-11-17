# Chapter 5: Option Pricing Theory and Models

## Core Idea
An option is a right rather than an obligation. Its asymmetric payoff makes flexibility valuable even when immediate exercise is unattractive, so a simple discounted average of expected cash flows can miss value.

## Frameworks Introduced
- **Call and put payoff**: At exercise, a call pays `max(S − K, 0)` and a put pays `max(K − S, 0)`, before the premium paid for the option.
  - When to use: To test whether a contingent claim truly behaves like an option.
  - How: Identify underlying value `S`, exercise price `K`, expiration, exercise style, and the holder's right to walk away.
- **Binomial option pricing**: Build an up/down tree for the underlying, derive a hedge or risk-neutral probability, and work backward from terminal payoffs.
  - Why it works: The tree preserves the option's ability to choose whether and when to exercise at each node.
- **Black–Scholes and adjustments**: Price a European option from the underlying value, strike, time, volatility, risk-free rate, and expected payouts; adjust for dividends or early-exercise features when applicable.

## Key Concepts
- **Strike price**: Price at which the holder may buy or sell the underlying.
- **Expiration**: End of the option's exercise right.
- **Volatility**: Dispersion of possible underlying values; greater volatility generally benefits an option holder.
- **European option**: Exercisable at expiration.
- **American option**: Exercisable on or before expiration.
- **Risk-neutral probability**: Pricing weight implied by replication, not an investor's subjective forecast probability.

## Mental Models
- A project with an option to defer can gain value from uncertainty if the investor can avoid bad states while retaining upside.
- The option's value is not the same as the expected value of the underlying asset.

## Reference Formula
In a one-step binomial replication, `option delta = (C_up − C_down) / (S_up − S_down)`. Buy that fraction of the underlying and borrow/lend the amount that reproduces the call's payoff in both states; the option must cost the same as this replicating portfolio if arbitrage is absent. In a multi-step tree, value terminal payoffs first and work backward. The formula assumes the two states and funding terms allow replication; it is not a subjective probability forecast.

## Anti-patterns
- **Using the stock's expected return as the option discount rate**: Replication-based models price contingent payoffs differently.
- **Calling every uncertain project an option**: A real right to defer, expand, abandon, or exercise must exist.
- **Ignoring payouts and exercise rules**: Dividends, patent life, and early exercise can materially alter option value.

## Reference Table
| Claim | Holder may | Terminal payoff |
|---|---|---|
| Call | Buy at `K` | `max(S − K, 0)` |
| Put | Sell at `K` | `max(K − S, 0)` |

## Worked Example
Illustration 5.1 values a call in a two-state binomial setting. At the last node, compute the call's payoff separately when the underlying rises and when it falls. Construct the portfolio of underlying and borrowing that replicates those payoffs, then discount one step back. A call with no value on immediate exercise can still have positive value because the upward branch remains open; subtracting a single expected cash flow from the exercise cost would miss that asymmetry.

## Key Takeaways
1. First prove there is a decision right and asymmetric payoff.
2. Match the model to exercise style, payouts, and underlying uncertainty.
3. Use option value as an addition only when the base valuation has not already included the same flexibility.

## Connects To
- **Ch 28–29**: Applies option logic to delay, expansion, and abandonment.
- **Ch 30**: Treats distressed equity as an option on firm assets.

