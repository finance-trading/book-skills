# Chapter 6: Market Efficiency—Definition, Tests, and Evidence

## Core Idea
Market efficiency is about whether information can be converted into repeatable excess returns after risk and costs, not whether every market price is always intrinsically correct.

## Frameworks Introduced
- **Efficient-market test**: Specify the information set, trading rule, horizon, risk adjustment, and transaction costs before claiming a pricing anomaly.
  - When to use: Evaluating an investment strategy or a historical backtest.
  - How: Use information available at the decision date, compare with a relevant benchmark, and account for turnover and implementation.
- **Event study**: Measure abnormal returns around a defined information event against an expected-return model.
  - Failure mode: A poorly specified event window, overlapping events, or selective cases can create spurious results.
- **Portfolio study**: Sort securities on a characteristic, rebalance according to a fixed rule, and test whether subsequent returns survive risk and cost controls.

## Key Concepts
- **Abnormal return**: Return beyond what a chosen benchmark or risk model predicts.
- **Serial correlation**: Relationship between successive price changes, which can be affected by liquidity and bid–ask bounce.
- **Post-announcement drift**: Continued price adjustment after an information announcement.
- **Data mining**: Finding a rule in historical data that fails when tested independently.
- **Survivorship bias**: Omitting firms that disappeared from the historical sample.

## Mental Models
- Treat a backtest as an experimental design: the information set and implementation decide what it proves.
- A statistically detectable price pattern may still be too small to trade profitably.

## Anti-patterns
- **Hindsight trading**: Using information that was not public or operationally available at the assumed trade time.
- **Ignoring bid–ask spread and illiquidity**: Apparent small profits can vanish after real execution costs.
- **Declaring inefficiency from one anomaly**: Check sample selection, risk exposure, and whether the effect persists outside the discovery period.

## Worked Example
Illustration 6.1 frames an event study around option listing. The analyst specifies the listing event, estimates normal returns from a comparison model, and cumulates departures in a chosen window. Illustration 6.2 studies low-P/E portfolios. A low multiple followed by high returns is not yet evidence of mispricing: the investor must ask whether the stocks were riskier, whether the sample excluded failures, and whether rebalancing costs absorbed the advantage.

## Key Takeaways
1. Define the information set and ex-ante rule before evaluating results.
2. Distinguish statistical significance from investable returns.
3. Use market price as information while testing the assumptions behind it.

## Connects To
- **Ch 1**: Explains why price and value can differ without a claim that markets are always wrong.
- **Ch 17**: Uses market prices in relative valuation while controlling for fundamental differences.

