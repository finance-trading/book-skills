# Independent Blind Trigger Test

**Skill:** `three-statement-reconciliation`  
**Verdict:** FAIL (4/6, 66.7%)

| Test | Would trigger | Skill that should trigger | Verdict | Reason |
|---|---:|---|---|---|
| should-trigger-01 | Yes | `three-statement-reconciliation` | PASS | Directly requests the named three-statement income-profit-cash reconciliation. |
| should-trigger-02 | Yes | `three-statement-reconciliation` | PASS | Profit growth with negative cash flow, accrual accounting, and three-statement reconciliation are definitive signals. |
| should-trigger-03 | No | None | FAIL | A generic request for financial diagnostic steps does not identify an income-versus-cash reconciliation. |
| should-not-trigger-01 | No | None | PASS | A dictionary explanation needs no three-statement analysis. |
| should-not-trigger-02 | No | `industry-strategy-execution` | PASS | It targets industry competitive strategy rather than statements. |
| edge-01 | No | None | FAIL | The prompt is about the sufficiency of one quarterly observation, with no revenue, profit, cash, accrual, or reconciliation signal. |

The two failing cases may deserve a general financial-analysis response, but they do not make this specialized reconciliation skill the correct trigger.
