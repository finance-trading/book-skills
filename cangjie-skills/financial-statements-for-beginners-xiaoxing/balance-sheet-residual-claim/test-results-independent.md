# Independent Blind Trigger Test

**Skill:** `balance-sheet-residual-claim`  
**Verdict:** FAIL (4/6, 66.7%)

| Test | Would trigger | Skill that should trigger | Verdict | Reason |
|---|---:|---|---|---|
| should-trigger-01 | Yes | `balance-sheet-residual-claim` | PASS | Directly requests accounting-identity and residual-claim analysis. |
| should-trigger-02 | Yes | `balance-sheet-residual-claim` | PASS | Balance-sheet closure, debt priority, and shareholder residual are defining signals. |
| should-trigger-03 | No | None | FAIL | Generic diagnostic-process advice does not select a balance-sheet identity or creditor-priority analysis. |
| should-not-trigger-01 | No | None | PASS | A standalone dictionary definition does not need this skill. |
| should-not-trigger-02 | No | `industry-strategy-execution` | PASS | The stated subject is industry competitive strategy. |
| edge-01 | No | None | FAIL | One quarter versus long-term value is a general scope question, not a residual-claim question. |

The two failing cases could be answered conservatively using this skill's boundary, but neither contains a signal that would make it the appropriate routing target.
