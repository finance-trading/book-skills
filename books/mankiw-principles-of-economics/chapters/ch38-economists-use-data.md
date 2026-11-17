# Appendix: How Economists Use Data

## Core Idea
Economic data can describe, estimate relationships, test hypotheses, and predict, but observational patterns require special care because confounding and reverse causation can mimic a causal effect.

## Frameworks Introduced
- **Data-design choice**: Use cross-sectional data for differences across units at a date, time-series data for one unit over time, and panel data for multiple units over time. A randomized trial offers stronger identification when feasible and ethically appropriate.
- **Regression interpretation**: Ordinary least squares fits coefficients to observed data. A standard error measures sampling uncertainty under model assumptions; statistical significance does not establish causation or practical importance.
- **Causal-threat checklist**: Identify omitted confounders, reverse causality, selection into treatment, measurement error, and extrapolation beyond observed data before acting on an estimate.

## Key Concepts
- **Econometrics**: Statistical methods for studying economic data.
- **Randomized controlled trial**: Treatment assigned by random mechanism.
- **Observational data**: Data generated without experimental assignment.
- **Confounder**: Factor related to both explanatory variable and outcome.
- **Standard error**: Estimate of sampling uncertainty in a statistic.

## Mental Models
- A precisely measured association may still be causally wrong.
- Ask how a variable came to vary in the data; that design determines what the estimate can support.

## Anti-patterns
- **Reading a regression coefficient as a causal lever automatically**: Omitted factors or reverse causation may drive it.
- **Equating small p-value with large economic impact**: Magnitude and uncertainty are separate.

## Worked Example
Suppose cities with more police also have more crime. A simple cross-sectional regression could show a positive association. That does not establish that police cause crime: high-crime cities may hire more officers, and other city conditions affect both. An analyst would look for a credible source of variation in police staffing, compare outcomes, and report remaining uncertainty before drawing a causal conclusion.

## Key Takeaways
1. Match data type and design to the question.
2. Report coefficient, uncertainty, and causal assumptions together.
3. Separate prediction accuracy from causal interpretation.

## Connects To
- **Ch 2**: Economic models produce testable claims.
- **Ch 21**: Inequality measurement is sensitive to definitions and populations.
