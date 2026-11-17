# Chapter 8: Risk Analysis in Investment Decisions

## Core Idea
Risk has two parts — the dispersion of an investment's own returns and their correlation with a diversified portfolio — and the honest way to handle the second, harder dimension is a ladder of techniques: sensitivity, scenario, simulation, decision trees, and real options.

## Frameworks Introduced
- **Two dimensions of risk**: (1) *dispersion* (the spread of an asset's own possible returns) and (2) *correlation* (how those returns move with the rest of your portfolio).
  - When to use: to separate "risky alone" from "risky in a portfolio" — they're different numbers.
  - How: measure dispersion with standard deviation; then ask whether the asset's returns offset or amplify the portfolio's.
- **Diversification as a free lunch**: holding a portfolio reduces risk below the sum of the parts whenever returns are less than perfectly correlated.
  - When to use: to argue that the *relevant* risk is portfolio risk, not standalone ("Robinson Crusoe") risk.
- **Risk-analysis ladder** (from quick to expensive):
  1. **Sensitivity analysis** — change one variable at a time and watch NPV.
  2. **Scenario analysis** — change several variables together to a coherent state (boom/base/bust).
  3. **Simulation (Monte Carlo)** — draw the key variables' distributions and simulate thousands of outcomes.
  4. **Decision trees** — sequence of contingent decisions; value the branches by working backward.
  5. **Real options** — treat the ability to expand, defer, or abandon as an option you can price.
  - When to use: escalate up the ladder as the stakes and uncertainty grow.

## Key Concepts
- **Expected return** — the probability-weighted average of possible returns.
- **Standard deviation** — the probability-weighted spread of returns around the expected value.
- **Total (standalone) risk vs. portfolio risk** — dispersion vs. the increment added to a diversified portfolio.
- **Correlation** — the co-movement of returns; imperfect correlation is what makes diversification work.
- **Beta** — (appendix) the asset's contribution to a diversified portfolio's risk, used with CAPM to set a discount rate.
- **APV (adjusted present value)** — (appendix) valuing a project by adding financing side-effects to the base all-equity NPV.

## Mental Models
- **Risk has two parts; never quote just one.** Standalone risk misleads once the holder can diversify.
- Think of diversification as the **ice-cream-stand + umbrella-shop portfolio**: gains and losses cancel, so combined risk → zero while expected return survives.
- Model an investment as a **contingent claim** — the right to abandon, delay, or expand is itself valuable.

## Anti-patterns
- **Equating standalone dispersion with relevant risk** when the holder can diversify.
- **Relying on a single point estimate** for the key drivers; always stress the most sensitive variable.
- **Ignoring the value of flexibility**: a straight DCF can understate projects where management can adapt.
- **Adding risk adjustment ad hoc** rather than using a consistent, portfolio-derived discount rate.

## Worked Example
The text opens with the **ice-cream stand vs. umbrella shop** pair. Each is risky alone (ice cream: +60% sun / −20% rain; umbrella: −30% sun / +50% rain). But in a 50/50 portfolio they cancel exactly: `0.5×60% + 0.5×−30% = 15%` in sun, and `0.5×−20% + 0.5×50% = 15%` in rain — a riskless 15% either way. Expected return is preserved while dispersion goes to zero. This is the chapter's proof that "there really is a free lunch in finance — it's called diversification," and it grounds the rule that the risk that matters is the asset's contribution to the portfolio, not its risk in isolation.

## Key Takeaways
1. Split risk into **dispersion + correlation**; the second is the one a portfolio owner cares about.
2. Diversify to eliminate risk that co-movement doesn't charge you for; **relevant risk is portfolio risk**.
3. Escalate the analysis ladder — **sensitivity → scenario → simulation → decision trees → real options** — as uncertainty grows.
4. Price flexibility explicitly; an **option to abandon/expand** is real, quantifiable value.
5. Set the discount rate from **beta/CAPM** (or APV for financing side-effects), not gut feeling.

## Connects To
- **Ch 7**: the discount rate this chapter justifies is applied in DCF.
- **Ch 9**: valuation of firms under uncertainty uses these risk tools on free cash flow.
- **Ch 5**: the derivative/option appendix for hedging is the same option pricing now applied to investment.