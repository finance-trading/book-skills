# Chapter 7: Discounted Cash Flow Techniques

## Core Idea
Because a dollar today is worth more than a dollar tomorrow, the value of any investment is the sum of its future cash flows each discounted back to the present — and the correct acceptance rule is net present value, not payback or accounting return.

## Frameworks Introduced
- **Time value of money / discounting**: a cash flow T years out is worth `CF / (1 + r)^T` today.
  - When to use: to convert any stream of future cash flows into a single comparable present value.
  - How: discount each period's cash flow at the opportunity cost of capital r, then sum.
- **Net present value (NPV)**: the sum of discounted cash flows minus the initial outlay; a project is worth accepting if NPV > 0.
  - When to use: as the primary accept/reject and ranking criterion.
- **Internal rate of return (IRR)**: the discount rate that makes NPV exactly zero; accept if IRR exceeds the required return.
  - When to use: to express a project's return as a rate comparable to the cost of capital.
- **Payback period**: the time to recover the initial investment from cash inflows; and **accounting rate of return** (average accounting profit ÷ average investment).
  - When to use: only as rough screens — Higgins treats both as inferior to DCF because they ignore the timing and full horizon of cash flows.
- **Conflicting NPV/IRR rankings**: NPV and IRR can disagree on which project to rank higher (scale and timing of cash flows, reinvestment-rate assumptions).

## Key Concepts
- **Present value (PV)** — today's value of a future cash flow, `CF/(1+r)^T`.
- **Discount rate / cost of capital** — the return foregone on the next-best equal-risk use of funds.
- **Cash-flow diagram** — a timeline of costs and benefits; drawing one avoids most elementary errors.
- **Relevant cash flows** — incremental, after-tax cash flows attributable to the project, including opportunity costs.
- **Capital budgeting** — the process of allocating funds to long-lived investment opportunities.

## Mental Models
- **Draw the cash-flow diagram first** — it surfaces timing mistakes before arithmetic does.
- Use NPV as the **default truth**, IRR as the **communicable rate**, payback as a **screening shortcut**.
- When NPV and IRR conflict, **believe NPV** — it assumes reinvestment at the cost of capital, not at the IRR.

## Anti-patterns
- **Using payback or accounting return to rank projects**: both ignore cash-flow timing and what happens after recovery.
- **Ignoring timing**: a cash flow far in the future is worth less than the same nominal amount now.
- **Ranking by IRR alone** when projects differ in size or timing; IRR can pick the smaller, faster-returning project while NPV identifies the larger value.
- **Discounting at a rate unequal to the actual opportunity cost** of the project's specific risk.

## Worked Example
**Pacific Rim Resources** contemplates a Seattle container pier: $40M to build, $7.5M/year for 10 years, plus $9.5M salvage, so year 10 brings $17M. The text first computes the crude screens — payback (`$40M / $7.5M ≈ 5.3` years) and accounting return — then shows why they mislead. Switching to discounting: money promised in one year at a 10% opportunity cost is worth only `$1/1.10 = $0.909` today, and `$1` two years out is `$1/(1.10)² = $0.826`. Extending the pattern, each pier cash flow is discounted by `(1+r)^T` and summed; accepting only if that present value exceeds the $40M outlay. The before/after contrast — a plausible-looking payback vs. a correct NPV — is the chapter's central lesson in *why* DCF is the right yardstick.

## Key Takeaways
1. Discount every future cash flow: `PV = CF/(1+r)^T`, sum them, subtract the outlay — that's NPV.
2. Accept when **NPV > 0**; express the result as IRR only for communication.
3. Draw the **cash-flow diagram** before computing anything.
4. When NPV and IRR disagree, **trust NPV**.
5. Use payback only as a crude liquidity screen, never as a ranking rule.

## Connects To
- **Ch 8**: risk, once measured, is used to *raise* the discount rate applied here.
- **Ch 9**: business valuation is just this DCF machinery applied to the whole firm's free cash flow.
- **Ch 3**: the capital budget's fixed-asset outlays become the investment's cash flows.