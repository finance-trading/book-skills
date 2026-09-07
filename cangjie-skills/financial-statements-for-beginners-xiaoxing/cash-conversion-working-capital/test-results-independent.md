# Independent Blind Trigger Test

**Skill:** `cash-conversion-working-capital`  
**Verdict:** FAIL (4/6, 66.7%)

| Test | Would trigger | Skill that should trigger | Verdict | Reason |
|---|---:|---|---|---|
| should-trigger-01 | Yes | `cash-conversion-working-capital` | PASS | Directly requests the named asset-to-cash and working-capital analysis. |
| should-trigger-02 | Yes | `cash-conversion-working-capital` | PASS | Receivables, inventory turns, collection, and working capital identify the method. |
| should-trigger-03 | No | None | FAIL | A request for an unspecified finance diagnostic workflow has no working-capital signal. |
| should-not-trigger-01 | No | None | PASS | A single term definition does not require working-capital diagnosis. |
| should-not-trigger-02 | No | `industry-strategy-execution` | PASS | The requested analysis concerns competitive strategy, not cash conversion. |
| edge-01 | No | None | FAIL | Period sufficiency for long-term value is broad; there is no receivable, inventory, collection, or working-capital issue. |

The two failing cases are broad financial-analysis questions, so routing them here would create false positives.
