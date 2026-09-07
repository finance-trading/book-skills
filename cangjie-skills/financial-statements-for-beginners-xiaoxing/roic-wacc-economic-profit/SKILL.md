---
name: roic-wacc-economic-profit
description: |
  当用户分析财报并出现“ROIC、WACC、经济利润、机会成本”等信号，需要ROIC—WACC 经济利润门槛时调用。适用于结构化诊断与决策，不适用于只要定义术语或复述单一数字的查询。
source_book: 《一本书读懂财报（全新修订版）》 肖星
source_chapter: 怎样的公司才算是好公司
tags: [financial-analysis, decision, accounting]
related_skills: [industry-strategy-execution, leverage-risk-return]
---

# ROIC—WACC 经济利润门槛

## R — 原文 (Reading)

> 投资资本回报率的及格线应该是投资资本成本；用投资资本回报率减去投资资本成本，得到超额收益率。
>
> — 肖星，怎样的公司才算是好公司

## I — 方法论骨架 (Interpretation)

比较投入资本回报率与资本成本，判断增长是在创造还是毁灭价值。先把问题转换成可核验的报表关系，再用业务背景解释数字。输出应区分事实、推断和待核查证据，并避免把单一指标当作结论。

## A1 — 书中的应用 (Past Application)

- **案例**：c20,c23。作者把业务问题映射到本方法，比较报表项目与现金结果，得出风险或价值判断。

## A2 — 触发场景 (Future Trigger) ★

1. 用户要求解释财报中相互矛盾的指标。
2. 用户说“现金流/利润/库存/杠杆看起来不对”。
3. 用户需要在投资、借贷或扩张前做结构化判断。

语言信号：ROIC、WACC、经济利润、机会成本；“为什么净利润和现金流不一致”；“这家公司是在创造价值吗”。

与相邻 skill 的区分：本 skill 聚焦 **ROIC—WACC 经济利润门槛**；若问题核心转为兄弟单元的专门主题，应切换到对应 skill。

## E — 可执行步骤 (Execution)

1. **界定对象与期间**：列出涉及的报表、科目、期间和业务动作。完成标准：所有数字都有来源和时间维度。
2. **建立关系并核验**：按本方法计算/勾稽关键关系，检查异常项与反例信号。完成标准：形成一张关系表；若证据不足，标记 `Unavailable`，不补猜。
3. **给出判断与动作**：区分基准、风险、待核查事项，提出可执行的下一步。完成标准：结论能回答用户问题，并说明适用边界。

## B — 边界 (Boundary) ★

- 不要在只有单一指标、没有期间或业务背景时下结论。
- 警惕对应反例：ce19-ce20。若出现这些信号，应先做穿透核查或压力测试。
- 本方法不能替代审计、法律判断或实时经营数据；历史会计口径可能无法代表未来。

## 相关 skills

- depends-on: `industry-strategy-execution`
- contrasts-with: `leverage-risk-return`
- composes-with: `industry-strategy-execution`

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 待 Stage 4
- **蒸馏时间**: 2026-09-06
