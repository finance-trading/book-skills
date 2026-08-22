# Test Results — diversification

## Summary
- **Total tests**: 9
- **Expected should_call**: 4
- **Expected should_not_call**: 5
- **Cross-skill confusion tests**: 3 (margin-of-safety, defensive-allocation, defensive-stock-checklist)

## Verification
1. ✅ Correct activation for diversification questions
2. ✅ No activation for safety margin, allocation, or stock screening
3. ✅ Cross-skill guard: doesn't activate for "股票和债券各买多少合适" (defensive-allocation)
4. ✅ English trigger detection

**Status**: PASS