# Patterns

## Leap-of-faith assumption audit
**When to use**: 新业务计划刚形成，尚未投入大量开发。
**How**: 列出计划中的全部假设；标注哪些若为假会导致整体失败；把它们分为 value hypothesis（使用后是否创造价值）与 growth hypothesis（新客如何发现/采用）；按“致命性 × 可验证成本”排序；为每条写出预测、指标与失败阈值。
**Trade-offs**: 假设拆得越细越可测，但可能失去整体战略判断；不要把所有细节都变成实验。

## MVP selection ladder
**When to use**: 需要尽快获得真实客户行为证据。
**How**: 按保真度从低到高选择：smoke test / 视频 → wizard of oz → concierge → 单功能原型 → 完整产品。优先选能回答当前最大风险的那一档，而非最像最终产品的那一档。
**Trade-offs**: 更低保真更便宜更快，但可能产生 false negative（客户因体验太差拒绝）；更高保真更可信，但更慢更贵。

## Smoke test / video MVP
**When to use**: 需求或定位不清，且完整开发成本高。
**How**: 做落地页、广告或演示视频，提供明确的行动（预约、预购、留邮箱）；测量转化率与来源；把“兴趣”与“付费意愿”分开看。
**Trade-offs**: 只能证明初步兴趣，不能证明留存、单位经济或可规模化；定价与承诺需谨慎，避免误导。

## Concierge MVP
**When to use**: 服务交付复杂，需先理解真实工作流程。
**How**: 为 1–10 位 early adopters 人工完整交付；每周收集反馈并收费；在人力成为瓶颈时，只自动化最耗时、最确定的环节。
**Trade-offs**: 极慢、不可规模化；但能暴露真实需求与隐性流程。要区分“在学习”与“在做小生意”。

## Wizard of Oz
**When to use**: 技术难点可能掩盖需求验证。
**How**: 前端呈现完整产品体验，后台由人完成关键步骤；测量使用、留存与推荐；验证后再投资自动化。
**Trade-offs**: 运营成本高、难以规模化；若人工质量不稳定，会污染对产品价值的判断。

## Cohort + split-test setup
**When to use**: 需要判断某项改动是否真的改善客户行为。
**How**: 按时间/来源定义 cohort；同一时间随机分组；只改变一个变量；预先指定主指标与观察窗口；比较组间差异而非总量；记录样本量与混杂因素。
**Trade-offs**: 需要足够流量与统计纪律；小样本易受噪声影响；过度拆分会导致实验碎片化。

## Innovation accounting cycle
**When to use**: 已有 MVP，需要客观判断是否在进步。
**How**: ①用 MVP 建立每条假设的 baseline；②每次只针对一个增长驱动因素做改动，观察指标是否改善；③若多轮调优仍无改善，进入 pivot-or-persevere；pivot 后重建 baseline。
**Trade-offs**: 需要可定义的财务/行为模型；早期数据少，模型本身可能错；不能替代战略判断。

## Five Whys session
**When to use**: 出现技术故障、业务结果失败或客户行为异常。
**How**: 让所有相关方到场；从具体症状开始连续问“为什么”；每层只做与严重度相称的预防投资；指定 Five Whys master 跟进；首次错误宽容，同错不二犯；避免变成 Five Blames。
**Trade-offs**: 耗时、可能暴露敏感管理问题；需要信任与高层支持；不宜一开始就处理所有历史遗留问题。

## Innovation sandbox design
**When to use**: 大组织要给内部团队真实实验权，同时保护核心业务。
**How**: 限定实验影响范围（页面/功能/客户比例/地区）；一个团队端到端负责；设时间上限与客户影响上限；统一 5–10 个 actionable metrics；实验期间监控并可在灾难时中止；成功后逐步扩大沙盒。
**Trade-offs**: 沙盒太小可能学不到关键问题；扩大过快会触发核心业务的政治反弹。

## Pivot-or-persevere meeting
**When to use**: 增长指标长期停滞、调优收益递减，或关键假设被证伪。
**How**: 固定周期召开；产品团队报告完整调优历史与预期对比；业务团队报告客户访谈；对照 learning milestones 判断；明确新战略假设与下一 MVP；记录决策与证据。
**Trade-offs**: 过早 pivot 会浪费已积累的学习；过晚则陷入 living dead；会议不能替代勇气与判断。

## Engine of growth diagnosis
**When to use**: 有早期客户与收入，但增长停滞。
**How**: 判断主引擎：sticky → 看 churn 与 compounding rate；viral → 看 viral coefficient；paid → 看 LTV 与 CPA。只针对主引擎的杠杆投入；当引擎接近耗尽时，规划 engine pivot 或新增长来源。
**Trade-offs**: 同时运营多引擎会造成指标与组织混乱；引擎判断错误会把资源投到无效杠杆。

## Small-batch delivery
**When to use**: 交付周期长、返工多、反馈慢。
**How**: 缩短从假设到证据的批次；跨职能团队端到端负责；每次发布小改动并立即测量；建立自动检测、回滚与根因分析；用 pull（待验证假设）而非部门推动来排优先级。
**Trade-offs**: 需要前期投入工具与自动化；对强依赖外部审批/硬件的业务，需重新设计流程而非照搬软件做法。
