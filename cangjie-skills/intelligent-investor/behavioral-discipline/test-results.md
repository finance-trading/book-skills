# Test Results — behavioral-discipline

## Summary
- **Total tests**: 9
- **Expected should_call**: 5
- **Expected should_not_call**: 4
- **Cross-skill confusion tests**: 3 (mr-market, margin-of-safety, defensive-allocation)

## Verification
1. ✅ Correct activation for emotional/panic questions
2. ✅ No activation for pure valuation or safety margin
3. ✅ Cross-skill guard: doesn't activate for "什么是安全边际" (margin-of-safety)
4. ✅ English trigger detection

**Status**: PASS