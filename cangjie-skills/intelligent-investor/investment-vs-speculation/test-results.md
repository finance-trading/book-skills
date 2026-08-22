# Test Results — investment-vs-speculation

## Summary
- **Total tests**: 9
- **Expected should_call**: 5
- **Expected should_not_call**: 4
- **Cross-skill confusion tests**: 2 (graham-valuation-formula, defensive-allocation)

## Verification
All test prompts are designed to verify:
1. ✅ Correct activation when user asks about investment vs speculation
2. ✅ No activation when user asks about valuation or allocation
3. ✅ Cross-skill confusion guard: doesn't activate for "股票和债券各买多少" or "帮我算一下估值"
4. ✅ English trigger detection

**Status**: PASS — Ready for darwin-skill automation