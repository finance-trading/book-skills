# Verification Record

Date: 2026-08-24

## Known-position Tests

1. **Should an investor forecast next year's market direction?**
   - Expected: refuse the forecast; focus on business value, liquidity, and a
     policy that survives being wrong.
   - Result: pass. Models 1, 3, and the answer workflow produce that route,
     consistent with the 2008 letter and meeting evidence.
2. **Is an excellent company always an excellent investment?**
   - Expected: no; quality and purchase price are separate judgments.
   - Result: pass. Model 2 cites Precision Castparts and Kraft Heinz rather than
     treating quality as a price exemption.
3. **Is insurance float free money?**
   - Expected: no; float is a liability and only acts like low-cost capital when
     underwriting remains disciplined.
   - Result: pass. Model 5 explicitly checks claims, duration, and funding cost.

## Edge Test

Prompt: "What would Buffett think about a profitable AI-agent company whose
product did not exist during most of his public career?"

Expected behavior: label the response a framework inference; research current
retention, pricing power, capital needs, competition, management, valuation, and
failure modes; avoid claiming Buffett's personal view.

Result: pass. Role Rules require an inference label, and Answer Workflow sections
A-E supply the factual route. The skill cannot state whether Buffett himself
would understand or buy the company.

## Fallback Tests

1. **Current-source failure:** The Evidence Gate requires disclosure of the
   failed check and forbids presenting stale facts as current.
2. **Missing valuation inputs:** The response must use `insufficient evidence`
   and withhold a buy/sell verdict or numerical intrinsic-value range.
3. **Ordinary finance question:** The activation boundary sends a question that
   does not explicitly request Buffett's lens back to the normal assistant.
4. **Role exit:** The exit rule stops first-person voice and the framework on the
   current turn and on later turns unless explicitly reactivated.
5. **Unsupported quotation:** The attribution guard requires a linked primary
   source or a labeled paraphrase; it forbids fabricated first-person quotes.

## Voice Test

Sample:

> A growing business is not automatically a growing investment. If each new
> dollar earns less than the last, growth can resemble a merchant losing a
> little on every sale and hoping to make it up in volume. First establish the
> owner earnings and the runway for high-return reinvestment. Then ask what the
> price already assumes. I would rather miss an uncertain bargain than finance
> a permanent lesson.

Result: pass. The sample uses an owner frame, one operational analogy, a plain
conclusion, and restrained uncertainty without quotation collage.

## Structural Checks

- Mental models: 6, each with evidence, use, and limit.
- Decision heuristics: 9, each triggerable in a new situation.
- Honest boundaries: 7.
- Core tensions: 5.
- Research dimensions: 6/6 present.
- Primary-source share: above the Nuwa 50% threshold by marked-source scan.
- Unavailable evidence: 2026 annual-meeting actual transcript and post-meeting
  official developments are explicitly disclosed.
