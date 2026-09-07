# Independent Blind Trigger Test

**Skill:** `economic-substance-historical-cost`  
**Verdict:** FAIL (4/6, 66.7%)

| Test | Would trigger | Skill that should trigger | Verdict | Reason |
|---|---:|---|---|---|
| should-trigger-01 | Yes | `economic-substance-historical-cost` | PASS | Directly calls for the named economic-substance and historical-cost method. |
| should-trigger-02 | Yes | `economic-substance-historical-cost` | PASS | Asset-versus-expense, historical cost, fair value, and debt-settlement transactions are core signals. |
| should-trigger-03 | No | None | FAIL | A generic request for diagnostic steps lacks a classification, valuation, or economic-substance issue. |
| should-not-trigger-01 | No | None | PASS | A dictionary definition is outside the structured decision use case. |
| should-not-trigger-02 | No | `industry-strategy-execution` | PASS | It expressly excludes report structure in favor of competitive strategy. |
| edge-01 | No | None | FAIL | It supplies no asset classification, historical-cost, fair-value, or transaction-substance context. |

The two failing cases do not uniquely select this accounting-recognition and valuation skill.
