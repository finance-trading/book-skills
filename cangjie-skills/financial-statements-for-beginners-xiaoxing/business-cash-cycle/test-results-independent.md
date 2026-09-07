# Independent Blind Trigger Test

**Skill:** `business-cash-cycle`  
**Verdict:** FAIL (4/6, 66.7%)

| Test | Would trigger | Skill that should trigger | Verdict | Reason |
|---|---:|---|---|---|
| should-trigger-01 | Yes | `business-cash-cycle` | PASS | Directly requests the named operating-investing-financing cash-cycle method. |
| should-trigger-02 | Yes | `business-cash-cycle` | PASS | Names the three activity classes, cash-flow classification, and a cash break. |
| should-trigger-03 | No | None | FAIL | A request for diagnostic steps has no cash-cycle or three-activity signal. |
| should-not-trigger-01 | No | None | PASS | A dictionary definition needs no structured financial-analysis skill. |
| should-not-trigger-02 | No | `industry-strategy-execution` | PASS | It explicitly asks for industry competitive strategy rather than report structure. |
| edge-01 | No | None | FAIL | It asks a general evidence-sufficiency question; no operating, investing, financing, or cash-cycle fact identifies this skill. |

The two failing cases are underspecified for this specialized skill. A safe response would decline a long-term conclusion from one quarter, but that boundary response alone is not a unique trigger.
