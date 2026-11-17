# Chapter 33: Probabilistic Approaches in Valuation—Scenario Analysis, Decision Trees, and Simulations

## Core Idea
Uncertainty should be modeled in ways that preserve the economic links among inputs. Scenarios, decision trees, and simulations answer different questions about outcomes, probabilities, and choices.

## Frameworks Introduced
- **Scenario analysis**: Define coherent alternative states and value each state with its own cash-flow and risk assumptions.
  - When to use: Discrete macro, regulatory, competitive, or policy regimes.
- **Decision tree**: Put sequential decisions and conditional probabilities on branches; value cash flows and choices at each node.
  - When to use: A firm can change course after observing a clinical trial, regulatory event, or market response.
- **Monte Carlo simulation**: Draw distributions for uncertain inputs and compute a distribution of values while preserving correlations and constraints.
  - When to use: Many continuous uncertainties interact and a full distribution is more informative than three point cases.

## Key Concepts
- **Conditional probability**: Chance of an outcome given prior branch results.
- **Correlation**: Link between uncertain inputs; ignoring it can create impossible combinations.
- **Value distribution**: Range and frequency of model values under specified input distributions.
- **Margin of safety**: Price discount that protects against estimation error; it is not automatically equal to a simulation percentile.
- **Expected value**: Probability-weighted mean of possible values, which may not be the most likely outcome.

## Mental Models
- A scenario is a coherent world, not independent optimistic tweaks to each input.
- Simulation reveals sensitivity to assumptions; it does not make the assumed distributions objectively true.

## Reference Formula
For mutually exclusive scenarios defined at a common valuation date, `expected value = Σ[p_i × V_i]` with `Σp_i = 1`. Each `V_i` must be a value of the **same claim** under that state's cash flows and risk treatment. In a decision tree, weight branch payoffs by conditional probabilities and value the choices available at each node; do not average terminal outcomes as though management had no option to act.

## Anti-patterns
- **Independent draws for linked drivers**: High revenue, high margins, and low reinvestment may be jointly implausible.
- **Averaging different risks twice**: Adjust probability and discount rate consistently for each scenario.
- **Treating a simulated 5th percentile as a guaranteed floor**: Model error and unmodeled events remain.

## Worked Example
The chapter values a company exposed to possible nationalization with distinct continued-operation and expropriation paths, rather than burying the event in one discount-rate premium. A pharmaceutical decision tree places trial, approval, and commercialization outcomes in sequence, with management investing only after favorable information. The Exxon Mobil simulation varies oil-related inputs to display a distribution, but its usefulness depends on the chosen price process and correlations.

## Key Takeaways
1. Use scenarios for discrete worlds, trees for sequential choices, and simulation for many interacting variables.
2. Set probabilities and correlations from evidence and make them visible.
3. Do not confuse model output with elimination of uncertainty.

## Connects To
- **Ch 13**: Grounds scenarios in business narratives.
- **Ch 28–29**: Values flexibility and conditional decisions.

