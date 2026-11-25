---
name: lewis-liars-poker
description: "基于迈克尔·刘易斯《Liar's Poker：说谎者的扑克牌》的交易、固定收益与组织知识库。需要运用 Liar's Poker 式市场推理、交易员心理、客户/中介激励、固定收益/按揭证券定价、1980 年代 Salomon Brothers 交易文化、风险转移与组织崩溃等框架时使用；也适合系统研读本书叙事与人物原型。"
---

<!-- argument-hint: [主题、框架名称或章节编号] -->

# Liar's Poker（说谎者的扑克牌）
**作者**：Michael Lewis | **源字数**：约 100,934 | **章节**：12（第 1–11 章 + 后记） | **生成**：2026-11-24

**定位**：这不是情节摘要，而是把 1980 年代 Salomon Brothers 交易桌暴露出的“交易桌认识论”蒸馏成可复用框架：交易如何被定价、如何被赢走、如何被组织与激励放大，以及如何在文化和制度层面崩塌。叙事非虚构，章节按原书顺序组织；引用人名、行话和事件时保留原书用词。

## 使用方法
- **直接提问**：先用下方“核心推理流程”与“关键模型”组织问题；涉及具体市场/组织案例再打开对应章节。
- **指定主题**：查阅“主题索引”，例如 `Liar's Poker`、`固定收益定价`、`客户中介`、`组织崩溃`，再打开相关章节。
- **指定章节**：打开 `chapters/chNN-*.md`。`ch01` 是全书认识论总纲，`ch06/ch07` 是按揭证券与垄断核心。
- **区分来源**：本书是刘易斯以 Salomon 债券销售/交易员身份的第一人称回忆录；其中“我”的观察、受访者转述与作者事后解释需分层使用，不等于市场事实的独立核验。

## 核心推理流程
1. **先定位角色与激励**：把交易、销售、客户、基金经理、高管和监管者放进同一张交易桌。问：谁在承担风险？谁在中间抽佣？谁的奖金由谁决定？“客户”可能是市场里的 fool，高管可能是把部门当交易品的人。
2. **用 Liar's Poker 读局**：先问概率（我的信息优势是什么），再读脸（对方是过度松弛还是过度紧张），再问动机（他是真强手还是在诱我犯错）。保留“接受一切挑战”的枪客代码，但对老板或情绪下的赌局保持“拒绝蠢赌”。
3. **把市场当不对称信息博弈**：任何市场都有 fool；赚钱常来自“收费亭”（toll taking）——把资产在不同买家之间转手、每次抽一小撮价差，而非真正预测。识别谁是 fool，以及 fool 的弱点（无知、绝望、流动性需求）何时暴露。
4. **给风险本身定价**：风险是罐装商品。可以从风险厌恶者那里买风险、卖给风险偏好者，自己不承担风险（warrant/call option、CPO/CMO 分层的逻辑）。固定收益的关键变量是利率、基点（basis point）、利差和再融资/提前还款期权。
5. **诊断组织而非只看利润**：问五项——垄断是否被人才外流侵蚀？公司是否在用自己的创新摧毁自己的护城河？薪酬是否奖励跳槽而不奖励忠诚？高管是否把业务当可丢弃的仓位？文化承诺（covenant）是否被破坏？
6. **复盘周期节点**：交易桌一年中真正“交易”的时刻在年末奖金与人事。观察谁被支付忠诚、谁被漏出、谁把新闻当政策。这些信号比当季利润更早说明组织状态。

## 关键模型
### Liar's Poker 作为交易认识论
Liar's Poker 不是娱乐，是 Salomon 交易桌对“什么是好交易员”的隐喻：概率是容易部分，读人和自我控制是难部分。Meriwether 的强项是同时压制 fear 与 greed、隐藏状态。规则要求接受挑战，但高手会在开局前用加倍注额逼退无利的赌局。用此模型审市场：先找你的对手是谁，再问你是否在用自己的弱点交换他的弱点。参见 [ch01](chapters/ch01-liars-poker.md)、[ch04](chapters/ch04-adult-education.md)。

### 市场 fool 与收费亭
刘易斯引沃纳格：律师（读作债券交易员）在资产转移的“魔法微秒”里抽走一小块。Salomon 的利润常来自让资产再动一次——从 X 卖给 Y，再抽一个 eighth；关键是两边都不完全理解资产价值。“知道市场”等于知道别人的弱点；不知道谁是 fool 的人，往往自己就是 fool。参见 [ch03](chapters/ch03-corporate-culture.md)、[ch06](chapters/ch06-mortgage-money-machine.md)。

### 风险商品化与转移
“风险能被罐装和出售，像番茄。”买风险便宜、卖风险昂贵，中间者不持仓风险。德国利率 warrant 的例子展示了如何把单一客户的大注变成结构化证券，再卖给风险厌恶者。固定收益中的 CMO 把提前还款现金流切成三 tranche，让不同期限偏好的投资者各取所需。参见 [ch07](chapters/ch07-salomon-diet.md)、[ch09](chapters/ch09-art-of-war.md)。

### 固定收益定价与按揭机器
1981 年按揭市场的爆发来自税收补贴和储贷机构（thrifts）的绝望卖盘，而不是宏观趋势。Salomon 垄断买方，利用信息不对称和“买方谨慎”抽佣金。Ranieri 把按揭证券“说成”国债类风险，靠 基点 和 利差 说服投资者；CMO 在 1983 年发明，1986 年成为把按揭债券拉回正常债券利润水平的主因。参见 [ch06](chapters/ch06-mortgage-money-machine.md)、[ch07](chapters/ch07-salomon-diet.md)。

### 交易文化、人物原型与组织崩溃
41 层把“不受约束的自利追求”当健康；Big Swinging Dick、Human Piranha、geek、rabbi、jungle guide 是交易桌的社会角色。Salomon Diet（1986–1988）阶段显示：当利润峰值过去，公司开始用裁员、漏报和高管互斗处理问题。Ranieri 被解雇与市政/货币市场部门被裁，是“文化承诺”破碎的两个节点。参见 [ch04](chapters/ch04-adult-education.md)、[ch07](chapters/ch07-salomon-diet.md)、[ch11](chapters/ch11-bad-things-rich-people.md)。

### 客户与中介关系
销售是交易员对外的嘴，客户是风险的另一端。Dash 的名言“save a client, shoot a geek”提醒销售：客户不是资源而是后果。对大客户的“逻辑谎言”（如“阿拉伯人在卖美元”）是职业技巧，但每一次“把债塞进客户”都会在客户早晨的电话里回来。参见 [ch08](chapters/ch08-from-geek-to-man.md)、[ch10](chapters/ch10-make-you-happier.md)、[ch11](chapters/ch11-bad-things-rich-people.md)。

## 章节索引

| # | 标题 | 重点 |
|---|---|---|
| [ch01](chapters/ch01-liars-poker.md) | Liar's Poker | 游戏规则、Meriwether/Gutfreund、交易员认识论 |
| [ch02](chapters/ch02-never-mention-money.md) | Never Mention Money | 招聘信号、交易桌与 corporate finance、进入路径 |
| [ch03](chapters/ch03-corporate-culture.md) | Learning to Love Our Corporate Culture | Salomonization、toll taking、债券市场 1980s 结构 |
| [ch04](chapters/ch04-adult-education.md) | Adult Education | 培训、岗位 blackboard、交易者/销售者分工 |
| [ch05](chapters/ch05-brotherhood-of-hoods.md) | A Brotherhood of Hoods | 按揭桌文化、Ranieri 的 rise、covenant |
| [ch06](chapters/ch06-mortgage-money-machine.md) | The Fat Men and Their Marvelous Money Machine | 1981–1986 按揭垄断、thrifts 卖盘、定价与收费 |
| [ch07](chapters/ch07-salomon-diet.md) | The Salomon Diet | 1986–1988 人才外流、CMO、创新侵蚀护城河 |
| [ch08](chapters/ch08-from-geek-to-man.md) | From Geek to Man | 销售学徒、客户分层、Olympia & York、中介伦理 |
| [ch09](chapters/ch09-art-of-war.md) | The Art of War | 内部政治、风险商品化、warrant、信用与 blame |
| [ch10](chapters/ch10-make-you-happier.md) | How Can We Make You Happier? | 客户销售、Milken junk bonds、Perelman 逼宫 |
| [ch11](chapters/ch11-bad-things-rich-people.md) | When Bad Things Happen to Rich People | 1987 崩盘、junk、裁员、组织治理崩塌 |
| [ch12](chapters/ch12-epilogue.md) | Epilogue | money belief、风险与退出、教训的有限性 |

## 主题索引
- **Liar's Poker、交易员心理、自我控制、bluff** → ch01, ch04
- **市场 fool、toll taking、收费亭、中介利润** → ch03, ch06, ch08
- **固定收益、按揭证券、CMO、prepayment、基点** → ch06, ch07
- **Ranieri、按揭桌文化、covenant、组织忠诚** → ch05, ch07
- **风险商品化、warrant、期权、结构化** → ch07, ch09
- **客户销售、bluff、客户伤害、中介伦理** → ch08, ch10, ch11
- **内部政治、credit/blame、leak、裁员、治理** → ch09, ch11
- **薪酬与激励、compensation bands、忠诚购买、跳槽** → ch07, ch09, ch11, ch12
- **junk bonds、Milken、Drexel、fallen angels** → ch10, ch11
- **招聘信号、岗位 blackboard、培训、角色分工** → ch02, ch04
- **组织崩溃、创新侵蚀护城河、人才外流** → ch07, ch11, ch12

## 支持文件
- [glossary.md](glossary.md) — 关键术语、人物与机制
- [patterns.md](patterns.md) — 可复用的交易/销售/组织模式
- [cheatsheet.md](cheatsheet.md) — 决策规则、快速检查与反直觉要点

## 范围与限制
本技能蒸馏本书 1980 年代美国金融市场的叙事与框架，不代表对当前证券、公司或监管环境的判断。书中人物与机构为历史描述；交易术语、薪酬数字和事件应按历史背景理解，不直接当作今日标准。若用于现实决策，需结合最新可靠数据、合规要求和自身风险约束。
