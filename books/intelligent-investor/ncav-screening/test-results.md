# Test Results — ncav-screening

## Summary
- **Total tests**: 9
- **Expected should_call**: 5
- **Expected should_not_call**: 4
- **Cross-skill confusion tests**: 3 (defensive-stock-checklist, margin-of-safety, diversification)

## Verification
1. ✅ Correct activation for deep value/undervalued stock questions
2. ✅ No activation for standard screening or safety margin
3. ✅ Cross-skill guard: doesn't activate for "帮我筛选一只符合防御型标准的股票"
4. ✅ English trigger detection

**Status**: PASS