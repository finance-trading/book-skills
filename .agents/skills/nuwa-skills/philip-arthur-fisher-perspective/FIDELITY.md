# Philip Fisher Perspective: Fidelity Checks

验证日期：2026-08-24。测试针对 Skill 的框架运行，不声称复现 Fisher 私人想法。

## 已知立场

| Prompt | Expected behavior | Result |
|---|---|---|
| 股票翻倍后是否卖出？ | 先重做 15 点和下一周期盈余测试；涨幅本身不是卖出理由。 | PASS |
| 高 P/E 是否自动否决？ | 不自动否决；核验未来市场、研发、利润率、管理和盈余曲线。 | PASS |
| 如何验证管理层？ | 先做客户、供应商、竞争者等 scuttlebutt，再让管理层解释冲突。 | PASS |

## 边缘问题

| Prompt | Expected behavior | Result |
|---|---|---|
| Fisher 会投资加密资产吗？ | 明确这是框架推断而非本人立场；说明公开材料不足，不给确定答案。 | PASS |

## 风格检查

示例输出应先提出经营核验问题，再列证据、反证和下一步动作；使用“我会问……”等研究动作句，不生成无出处名言或社交媒体式机锋。136 字样例符合该约束。Result: PASS。

## 自动检查

- `scripts/quality_check.py SKILL.md`: 7/7 PASS
- `git diff --check`: PASS
- `references/sources.md`：独立来源清单存在；研究文件使用 `S01`–`S15` 映射
- SKILL.md 相对链接：全部指向本目录内现存文件

## Residual risk

直接访谈与逐笔交易证据稀少，表达 DNA 只覆盖书面结构；新增原始访谈或家族档案后应优先刷新 `references/research/02-conversations.md`、`05-decisions.md` 和本文件。
