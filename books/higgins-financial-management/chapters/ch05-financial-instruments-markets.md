# Chapter 5: Financial Instruments and Markets

## Core Idea
Every financial instrument is a bargain over three variables — the claim on future cash flow, the right to participate in decisions, and the claim on assets in liquidation — and in an efficient market the price of that bargain already reflects all available information.

## Frameworks Introduced
- **The three-variable model of any security**: (1) investors' claims on future cash flow, (2) their right to participate in company decisions, (3) their claims on company assets in liquidation.
  - When to use: to classify any new instrument — bond, stock, or hybrid — by *contract terms*, not by name.
  - How: for a debt instrument, cash-flow claims are fixed and decision claims minimal; for equity, cash-flow claims are residual and decision claims broad.
- **Fixed vs. residual claims**: debt pays a specified amount on a specified date; equity receives whatever cash remains after all fixed claims are paid.
  - When to use: to explain the fundamental risk-return split between lenders and owners.
- **The Efficient Market Hypothesis** (weak / semi-strong / strong forms): prices already incorporate all the information in past prices / all public information / all information including inside.
  - When to use: to decide how much to pay an analyst to "beat the market," and to price securities.
  - How: identify which information set the market is assumed to reflect; test whether that information predicts abnormal returns.
- **Derivatives & hedging**: forwards, futures, swaps, and options each lock in or cap a future price, transferring risk to a counterparty.

## Key Concepts
- **Bond** — a fixed-income security sold to the public in small ($1,000) increments; three defining terms are par value, coupon rate, maturity.
- **Par value / coupon rate / maturity** — the principal due / the % of par paid as interest / the repayment date.
- **Sinking fund** — periodic principal repayment.
- **Floating-rate debt** — interest reset against a short-term reference rate, so price ≈ par.
- **Derivative** — a security whose payoff depends on the value of another underlying asset.
- **Hedging** — using a derivative to offset an existing exposure (e.g., a forward contract to fix a future currency price).

## Mental Models
- When evaluating an instrument, **name the three contractual variables** before anything else.
- Think of investing abroad as **two investments**: the foreign asset *plus* a currency bet — `(1 + return) = (1 + interest rate)(1 + change in exchange rate)`.
- In an efficient market, **expected abnormal return is a mirage**: you are paid only for bearing systematic risk, not for information everyone has.

## Anti-patterns
- **Assuming a security's features are fixed by law**: instrument characteristics are set by the *contract* between issuer and buyer.
- **Comparing nominal interest rates across currencies** without adjusting for exchange-rate movement (a high foreign yield can be a low dollar return).
- **Chasing "hot tips"** in a semi-strong efficient market; public information is already priced.

## Worked Example
The text works the **sterling-bond currency trap**: invest $1,000 in a one-year U.K. bond yielding 8% when today £1 = $1.25 and one year out £1 = $1.20. Your $1,000 buys £800, which grows to £864 at 8%; converting back at 1.20 gives $1,036.80 — a **3.68% dollar return**, not 8%. The 4% pound depreciation eats the yield. The exact relationship `(1 + Return) = (1 + Interest rate)(1 + Change in exchange rate)` = `(1.08)(0.96) = 1.0368` is the reusable formula for decomposing any foreign investment into its asset return and its currency return.

## Key Takeaways
1. Classify any security by its **three contractual variables** — cash-flow claim, decision rights, liquidation claim.
2. Debt = fixed claim, equity = residual claim; hybrids fall in between.
3. Price securities as if the market is **efficient at the relevant information level** until evidence says otherwise.
4. A derivative is a claim *on another asset's value*; every hedge is a risk transfer, never free.
5. Adjust cross-border yields for **currency** before comparing them.

## Connects To
- **Ch 6**: the financing decision chooses among these instruments along the debt-equity spectrum.
- **Ch 8**: real options apply option pricing to investment decisions.
- **Ch 7**: bond pricing mechanics (rates up, price down) are the concrete case of discounting.