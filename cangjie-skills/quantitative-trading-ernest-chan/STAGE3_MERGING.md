# Stage 3: 概念合并与蒸馏判断

> 生成时间: 2026-08-14  
> 输入: 32 frameworks + 22 principles + 17 cases + 13 counter-examples  
> 输出: 合并后的蒸馏清单

---

## 一、合并策略说明

### 合并原则

1. **完全重复**: fw 和 pr 讲的是同一个概念 → 合并为一项
2. **包含关系**: pr 是 fw 的核心表述或子集 → 合并为一项
3. **高度相关**: 多个 fw/pr 讲的是同一主题的不同侧面 → 考虑合并
4. **Cases**: 作为 A1 段素材，标注关联的 skill，但**不合并**（案例需要独立保留）
5. **Counter-examples**: 作为 B 段素材，标注关联的 skill，但**不合并**

### 判断"值得蒸馏"的标准

一个概念值得蒸馏成 skill 需要满足：

- ✅ **可执行**: 有明确的输入、处理步骤、输出
- ✅ **可触发**: 用户会在特定情境下需要这个方法论
- ✅ **反直觉**: 包含作者的独特洞察，不是常识
- ✅ **有边界**: 能说明何时不用、何时会失败

一个概念**不值得蒸馏**的情况：

- ❌ **纯描述性**: 只是描述特征，没有决策指导
- ❌ **过于宽泛**: 覆盖范围太大，无法具体执行
- ❌ **常识性**: 虽然是作者观点，但本质是常识

---

## 二、合并后的完整清单

### ✅ 值得蒸馏的 Skills (25 个)

#### 1. **simple-first-principle** (简单至上原则)

**合并关系**:
- fw001 简单至上原则 ↔ pr005 简单至上原则 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 反直觉: 机构用复杂数学亏损，个人用简单策略盈利
- ✅ 可执行: 参数≤5、线性模型优先、奥卡姆剃刀检验
- ✅ 有案例: ca001 作者从机构到独立的亲身经历
- ✅ 有边界: 高频/做市策略可能需要复杂性

**关联素材**:
- Cases: ca001 (从机构亏损到独立盈利)
- Counter-examples: ce01 (高深数学失败), ce06 (过拟合), ce24 (学术策略局限)

---

#### 2. **strategy-selection-four-constraints** (策略选择四要素约束框架)

**合并关系**:
- fw002 策略选择四要素约束框架 (独立项)

**为什么值得蒸馏**:
- ✅ 可执行: 四步评估法（工作时间、编程水平、资本、目标）
- ✅ 反直觉: 先评估自己约束，再看策略好不好
- ✅ 有边界: 约束是硬性的，不能突破

**关联素材**:
- Counter-examples: ce26 (资本不足)

---

#### 3. **capital-scale-strategy-matching** (资本规模决定策略类型)

**合并关系**:
- fw003 资本规模决定策略类型框架 (独立项)

**为什么值得蒸馏**:
- ✅ 可执行: 资本分档 → 对应策略类型
- ✅ 反直觉: 能负担什么 > 喜欢什么
- ✅ 有案例: 自营交易公司 vs 零售账户选择

**关联素材**:
- Cases: ca017 (经纪商选择)

---

#### 4. **strategy-modification-methodology** (策略变形方法论)

**合并关系**:
- fw004 策略变形方法论 ↔ pr008 策略变形的真正窍门 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 反直觉: 基础策略不行，变形才是关键
- ✅ 可执行: 系统性变形流程（持有期、时点、股票池、参数）
- ✅ 有案例: ca006, ca014 都是变形的成功案例

**关联素材**:
- Cases: ca006 (财富实验室策略变形), ca014 (清仓时点调整)
- Counter-examples: ce13 (人为干预)

---

#### 5. **sharing-over-secrecy** (分享优于保密)

**合并关系**:
- fw005 分享优于保密原则 (独立项)

**为什么值得蒸馏**:
- ✅ 反直觉: 分享比保密更有益
- ✅ 可执行: 博客/论坛分享 + 社区反馈
- ✅ 有案例: ca007 读者否定季节性策略

**关联素材**:
- Cases: ca007 (博客读者否定策略)

---

#### 6. **independent-trader-viability** (独立交易员可行性论证)

**合并关系**:
- fw006 独立交易员可行性论证框架 ↔ pr001 独立交易者特点原则 (**包含关系**: pr001 是 fw006 的核心论证)

**为什么值得蒸馏**:
- ✅ 反直觉: 个人可以打败机构
- ✅ 可执行: 评估自身条件（资本、情绪、时间）
- ✅ 有案例: ca019 作者独立交易成功

**关联素材**:
- Cases: ca001 (从机构到独立), ca019 (2006 年独立成功)
- Counter-examples: ce02 (贪婪破产), ce03 (恐惧清仓)

---

#### 7. **ideal-trader-profile** (理想交易员画像)

**合并关系**:
- fw008 理想交易员画像模型 ↔ pr003 情绪平衡原则 (**包含关系**: pr003 是 fw008 的必要条件之一)
- ↔ pr004 充足资本储备原则 (**包含关系**: pr004 是 fw008 的必要条件之一)

**为什么值得蒸馏**:
- ✅ 可执行: 三项必要条件检查（技能、资本、情绪）
- ✅ 反直觉: 不需要高学历，需要情绪稳定
- ✅ 有边界: 缺任一条件则不适合

**关联素材**:
- Counter-examples: ce02 (贪婪), ce03 (恐惧), ce25 (快速致富心态), ce26 (资本不足)

---

#### 8. **sharpe-ratio-supremacy** (夏普比率优于收益率)

**合并关系**:
- fw009 夏普比率优于收益率原则 ↔ pr020 夏普比率与杠杆收益率 (**完全重复**)
- ↔ pr023 策略比较应使用夏普比率和回撤 (**包含关系**)

**为什么值得蒸馏**:
- ✅ 反直觉: 高夏普+高杠杆 > 高收益+低杠杆
- ✅ 可执行: 夏普比率计算、杠杆收益率计算、策略比较
- ✅ 有案例: SAC 资本风控负责人的错误观点

**关联素材**:
- Counter-examples: ce08 (买入持有错误), ce09 (只看收益率)

---

#### 9. **strategy-screening-six-questions** (策略快速筛选六问法)

**合并关系**:
- fw010 策略快速筛选六问法 (独立项)

**为什么值得蒸馏**:
- ✅ 可执行: 六步清单法
- ✅ 反直觉: 先快速淘汰，再详细回测
- ✅ 有边界: 预筛工具，不是深度分析

**关联素材**:
- Cases: ca007 (读者快速否定策略)

---

#### 10. **transaction-cost-impact** (交易成本影响评估)

**合并关系**:
- fw011 交易成本影响评估框架 ↔ pr020 交易成本必须纳入评估原则 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 反直觉: 夏普 3 扣成本后变 -3
- ✅ 可执行: 四类成本分解、估算方法
- ✅ 有案例: ca013 Khandani-Lo 策略

**关联素材**:
- Cases: ca013 (Khandani-Lo), ca014 (清仓时点调整), ca017 (经纪商选择)
- Counter-examples: ce07 (忽略交易成本)

---

#### 11. **data-quality-traps** (数据质量陷阱识别)

**合并关系**:
- fw012 数据质量陷阱识别框架 (独立项)

**为什么值得蒸馏**:
- ✅ 可执行: 四类偏差检查（存活、前视、报价错误、未调整）
- ✅ 反直觉: 数据越多不代表越可靠
- ✅ 有案例: ca011 使用有偏差数据仍盈利

**关联素材**:
- Cases: ca011 (HQuotes 数据)
- Counter-examples: ce04 (存活偏差), ce05 (前视偏差), ce20 (报价错误)

---

#### 12. **parameter-complexity-overfitting** (参数复杂度与过拟合权衡)

**合并关系**:
- fw013 参数复杂度与过拟合权衡原则 (独立项)

**为什么值得蒸馏**:
- ✅ 反直觉: 100 个参数可以完美拟合历史
- ✅ 可执行: 参数数量限制、样本外测试
- ✅ 有边界: 简单模型更可靠

**关联素材**:
- Counter-examples: ce01 (复杂数学失败), ce06 (数据窥探), ce24 (学术策略局限)

---

#### 13. **ai-method-applicability** (AI 方法适用性判断)

**合并关系**:
- fw014 AI 方法在交易中的适用性判断框架 (独立项)

**为什么值得蒸馏**:
- ✅ 可执行: 五项特征检查
- ✅ 反直觉: 金融数据有限，AI 容易过拟合
- ✅ 有边界: 复杂 AI 不适合金融

**关联素材**:
- Cases: ca014 (机器学习预测 GS)
- Counter-examples: ce24 (学术策略局限)

---

#### 14. **small-capacity-advantage** (小容量策略优势)

**合并关系**:
- fw015 小容量策略优势原理 ↔ pr025 机构忽略策略优势原则 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 反直觉: 小容量是优势不是劣势
- ✅ 可执行: 识别小容量策略特征
- ✅ 有案例: ca019 作者独立交易成功

**关联素材**:
- Cases: ca019 (2006 年独立成功)
- Counter-examples: ce15 (竞争导致失效)

---

#### 15. **performance-diagnosis** (业绩偏差诊断)

**合并关系**:
- fw017 业绩偏差诊断框架 ↔ pr017 业绩偏差诊断流程 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 可执行: 六步排查流程
- ✅ 反直觉: 先排除简单原因，再考虑复杂原因
- ✅ 有边界: 系统性诊断工具

**关联素材**:
- Counter-examples: ce21 (模型风险), ce22 (软件风险)

---

#### 16. **transaction-cost-minimization** (交易成本最小化)

**合并关系**:
- fw018 交易成本最小化框架 (独立项)

**为什么值得蒸馏**:
- ✅ 可执行: 四条最小化规则
- ✅ 反直觉: 市值四次方根分配
- ✅ 有边界: 执行层面工具

**关联素材**:
- Cases: ca017 (经纪商选择)

---

#### 17. **paper-trading-validation** (仿真测试验证)

**合并关系**:
- fw019 仿真测试验证流程 ↔ pr018 仿真交易验证原则 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 可执行: 仿真交易流程、比较方法
- ✅ 反直觉: 仿真是发现漏洞的唯一不亏钱方法
- ✅ 有边界: 必须做，不能跳过

**关联素材**:
- Counter-examples: ce22 (软件风险), ce23 (低估准备时间)

---

#### 18. **kelly-criterion-leverage** (凯利公式最优杠杆)

**合并关系**:
- fw020 凯利公式最优杠杆决策 ↔ fw021 半凯利风险控制方法 (**高度相关**: 同一方法论的两个层面)
- ↔ pr009 凯利公式与最优杠杆 (**包含关系**)

**为什么值得蒸馏**:
- ✅ 可执行: f*=m/s² 计算、半凯利应用
- ✅ 反直觉: 超过最优杠杆会降低长期增长
- ✅ 有案例: ca009 作者因贪婪违反凯利

**关联素材**:
- Cases: ca009 (1 亿美元亏损), ca012 (LTCM/Amaranth 破产)
- Counter-examples: ce02 (贪婪破产), ce12 (恐惧贪婪导致过度杠杆)

---

#### 19. **behavioral-bias-management** (行为偏差识别与克服)

**合并关系**:
- fw022 行为偏差识别与克服框架 ↔ pr010 心理准备原则 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 可执行: 三类偏差识别、四种克服方法
- ✅ 反直觉: 具体偏差类型 + 系统化克服
- ✅ 有案例: ca010 作者因恐惧清仓

**关联素材**:
- Cases: ca010 (XLE/CL 恐惧清仓)
- Counter-examples: ce03 (恐惧清仓), ce10 (损失厌恶), ce11 (代表性偏差), ce12 (恐惧贪婪), ce13 (人为干预)

---

#### 20. **stop-loss-appropriateness** (止损策略适用性)

**合并关系**:
- fw023 止损策略适用性判断框架 (独立项)

**为什么值得蒸馏**:
- ✅ 反直觉: 止损在均值回归中有害
- ✅ 可执行: 根据市场状态判断
- ✅ 有边界: 不是万能工具

**关联素材**:
- Counter-examples: ce16 (止损误用)

---

#### 21. **mean-reversion-vs-momentum** (均值回归 vs 动量策略选择)

**合并关系**:
- fw024 均值回归 vs 动量策略选择框架 (独立项)

**为什么值得蒸馏**:
- ✅ 可执行: 三因素判断法（市场状态、持有期、时间）
- ✅ 反直觉: 先判断市场状态再选策略
- ✅ 有边界: 两种策略适用于不同场景

**关联素材**:
- Cases: ca010 (均值回归心理考验)

---

#### 22. **state-transition-prediction** (状态转换预测)

**合并关系**:
- fw025 状态转换预测方法 (独立项)

**为什么值得蒸馏**:
- ✅ 可执行: 两种预测方法（马尔可夫、拐点模型）
- ✅ 反直觉: 可以预测策略失效
- ✅ 有案例: ca014 机器学习预测 GS

**关联素材**:
- Cases: ca014 (GS 状态转换)
- Counter-examples: ce14 (状态转换失效)

---

#### 23. **cointegration-pair-trading** (协整性检验与配对交易)

**合并关系**:
- fw026 协整性检验与配对交易构建 ↔ pr013 配对交易原则 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 可执行: 四步构建流程
- ✅ 反直觉: 相关性≠协整性
- ✅ 有案例: ca015 GLD-GDX

**关联素材**:
- Cases: ca015 (GLD-GDX), ca021 (KO-PEP 反例)

---

#### 24. **seasonal-trading-identification** (季节性交易识别)

**合并关系**:
- fw029 季节性交易识别框架 ↔ pr015 季节性交易原则 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 可执行: 经济意义判断法
- ✅ 反直觉: 只交易有经济意义的季节性
- ✅ 有案例: ca015, ca016 汽油/天然气季节性

**关联素材**:
- Cases: ca015 (汽油季节性), ca016 (天然气季节性)

---

#### 25. **independent-trader-advantage** (独立交易者优势分析)

**合并关系**:
- fw032 独立交易者优势分析框架 ↔ pr016 独立交易者优势论证 (**完全重复**)

**为什么值得蒸馏**:
- ✅ 反直觉: 机构有结构性劣势
- ✅ 可执行: 四项优势识别
- ✅ 有案例: ca017, ca018 机构欺诈案例

**关联素材**:
- Cases: ca017 (法兴银行欺诈), ca018 (投行交易员欺诈), ca019 (独立成功)
- Counter-examples: ce17 (机构约束), ce18 (激励错位), ce19 (管理层干预)

---

### ❌ 不值得蒸馏的概念 (7 个)

#### 1. **quantitative-trading-business-characteristics** (量化交易业务特性)

**合并关系**:
- fw007 量化交易业务特性框架 ↔ pr007 量化交易业务特性 (**完全重复**)

**不值得蒸馏的原因**:
- ❌ **纯描述性**: 只是描述量化交易的三大特性（易扩大、节省时间、营销非必需）
- ❌ **无决策指导**: 不能帮助用户做具体决策
- ❌ **常识性**: 这些特性是量化交易的固有属性，不是方法论

**处理建议**: 作为背景知识，不蒸馏成 skill

---

#### 2. **backtest-tool-selection** (回测工具选择)

**合并关系**:
- fw016 回测工具选择决策树 (独立项)

**不值得蒸馏的原因**:
- ❌ **时代局限**: 2009 年的工具推荐（Excel/MATLAB/TradeStation）已过时
- ❌ **V3 未通过**: 验证时已标记 ❌ 拒绝
- ❌ **无普适性**: 2026 年的工具生态完全不同（Python/pandas/backtrader）

**处理建议**: 不蒸馏，但可在相关 skill 的 B 段提及时代局限

---

#### 3. **factor-model-construction** (因子模型构建)

**合并关系**:
- fw027 因子模型构建与应用 (独立项)

**不值得蒸馏的原因**:
- ❌ **过于宽泛**: 因子模型是一个庞大的主题，无法在一个 skill 中讲清
- ❌ **缺乏深度**: 书中只给出定义，没有详细的构建方法
- ❌ **需要专门知识**: 需要金融计量经济学背景

**处理建议**: 作为高级主题，需要专门书籍蒸馏

---

#### 4. **exit-strategy-framework** (清仓策略选择)

**合并关系**:
- fw028 清仓策略选择框架 (独立项)

**不值得蒸馏的原因**:
- ❌ **与 stop-loss-appropriateness 重复**: 清仓策略是止损策略的子集
- ❌ **缺乏独立价值**: 已在 mean-reversion-vs-momentum 中涵盖

**处理建议**: 合并到 stop-loss-appropriateness 和 mean-reversion-vs-momentum

---

#### 5. **high-frequency-trading-judgment** (高频交易判断)

**合并关系**:
- fw030 高频交易特征与适用性判断 (独立项)

**不值得蒸馏的原因**:
- ❌ **过于专门**: 高频交易需要专门的技术基础设施
- ❌ **不适合独立交易员**: 作者明确说"不适合初学者"
- ❌ **缺乏普适性**: 大多数用户不会做高频

**处理建议**: 作为特殊场景，在相关 skill 的 B 段提及

---

#### 6. **portfolio-leverage-beta-choice** (组合杠杆与贝塔选择)

**合并关系**:
- fw031 高杠杆低贝塔 vs 低杠杆高贝塔选择 (独立项)

**不值得蒸馏的原因**:
- ❌ **与 sharpe-ratio-supremacy 重复**: 这是夏普比率原则的具体应用
- ❌ **缺乏独立性**: 已包含在 sharpe-ratio-supremacy 中

**处理建议**: 合并到 sharpe-ratio-supremacy

---

#### 7. **growth-path-planning** (增长路径规划)

**合并关系**:
- fw033 量化交易事业增长路径 ↔ pr014 增长路径规划 (**完全重复**)

**不值得蒸馏的原因**:
- ❌ **过于宏观**: 四阶段增长路径是长期规划，不是具体方法论
- ❌ **缺乏可执行性**: 无法给出具体的执行步骤
- ❌ **个体差异大**: 每个人的增长路径不同

**处理建议**: 作为职业规划建议，不蒸馏成 skill

---

## 三、最终蒸馏清单

### 25 个 Skills 总览

| 编号 | Skill 名称 | 合并的 fw/pr | 关联 cases | 关联 counter-examples |
|------|-----------|-------------|-----------|---------------------|
| 1 | simple-first-principle | fw001, pr005 | ca001 | ce01, ce06, ce24 |
| 2 | strategy-selection-four-constraints | fw002 | - | ce26 |
| 3 | capital-scale-strategy-matching | fw003 | ca017 | - |
| 4 | strategy-modification-methodology | fw004, pr008 | ca006, ca014 | ce13 |
| 5 | sharing-over-secrecy | fw005 | ca007 | - |
| 6 | independent-trader-viability | fw006, pr001 | ca001, ca019 | ce02, ce03 |
| 7 | ideal-trader-profile | fw008, pr003, pr004 | - | ce02, ce03, ce25, ce26 |
| 8 | sharpe-ratio-supremacy | fw009, pr020, pr023 | - | ce08, ce09 |
| 9 | strategy-screening-six-questions | fw010 | ca007 | - |
| 10 | transaction-cost-impact | fw011, pr020 | ca013, ca014, ca017 | ce07 |
| 11 | data-quality-traps | fw012 | ca011 | ce04, ce05, ce20 |
| 12 | parameter-complexity-overfitting | fw013 | - | ce01, ce06, ce24 |
| 13 | ai-method-applicability | fw014 | ca014 | ce24 |
| 14 | small-capacity-advantage | fw015, pr025 | ca019 | ce15 |
| 15 | performance-diagnosis | fw017, pr017 | - | ce21, ce22 |
| 16 | transaction-cost-minimization | fw018 | ca017 | - |
| 17 | paper-trading-validation | fw019, pr018 | - | ce22, ce23 |
| 18 | kelly-criterion-leverage | fw020, fw021, pr009 | ca009, ca012 | ce02, ce12 |
| 19 | behavioral-bias-management | fw022, pr010 | ca010 | ce03, ce10, ce11, ce12, ce13 |
| 20 | stop-loss-appropriateness | fw023 | - | ce16 |
| 21 | mean-reversion-vs-momentum | fw024 | ca010 | - |
| 22 | state-transition-prediction | fw025 | ca014 | ce14 |
| 23 | cointegration-pair-trading | fw026, pr013 | ca015, ca021 | - |
| 24 | seasonal-trading-identification | fw029, pr015 | ca015, ca016 | - |
| 25 | independent-trader-advantage | fw032, pr016 | ca017, ca018, ca019 | ce17, ce18, ce19 |

---

## 四、Cases 分配说明

### 17 个 Cases 的归属

| Case ID | 标题 | 归属 Skill | 用途 |
|---------|------|-----------|------|
| ca001 | 从机构亏损到独立盈利 | simple-first-principle, independent-trader-viability | A1 段 |
| ca006 | 财富实验室策略变形 | strategy-modification-methodology | A1 段 |
| ca007 | 博客读者否定季节性策略 | sharing-over-secrecy, strategy-screening-six-questions | A1 段 |
| ca011 | 使用有存活偏差数据 | data-quality-traps | A1 段 |
| ca013 | Khandani-Lo 交易成本 | transaction-cost-impact | A1 段 |
| ca014 | 清仓时点调整 | strategy-modification-methodology, transaction-cost-impact | A1 段 |
| ca015 | GLD-GDX 配对交易 | cointegration-pair-trading | A1 段 |
| ca017 | 选择经纪商经验 | transaction-cost-minimization | A1 段 |

**剩余 9 个 cases (ca009, ca010, ca012, ca014, ca016, ca018, ca019, ca021)** 来自 verified_cases_p2.md，已在上表中分配。

---

## 五、Counter-examples 分配说明

### 13 个 Counter-examples 的归属

| CE ID | 标题 | 归属 Skill | 用途 |
|-------|------|-----------|------|
| ce01 | 高深数学失败 | simple-first-principle, parameter-complexity-overfitting | B 段 |
| ce02 | 贪婪破产 | kelly-criterion-leverage, ideal-trader-profile | B 段 |
| ce03 | 恐惧清仓 | behavioral-bias-management, ideal-trader-profile | B 段 |
| ce04 | 存活偏差 | data-quality-traps | B 段 |
| ce05 | 前视偏差 | data-quality-traps | B 段 |
| ce06 | 数据窥探 | parameter-complexity-overfitting, simple-first-principle | B 段 |
| ce07 | 忽略交易成本 | transaction-cost-impact | B 段 |
| ce10 | 损失厌恶 | behavioral-bias-management | B 段 |
| ce11 | 代表性偏差 | behavioral-bias-management | B 段 |
| ce12 | 恐惧贪婪 | kelly-criterion-leverage, behavioral-bias-management | B 段 |
| ce13 | 人为干预 | strategy-modification-methodology, behavioral-bias-management | B 段 |
| ce14 | 状态转换失效 | state-transition-prediction | B 段 |
| ce15 | 竞争导致失效 | small-capacity-advantage | B 段 |
| ce16 | 止损误用 | stop-loss-appropriateness | B 段 |
| ce17 | 机构约束 | independent-trader-advantage | B 段 |
| ce18 | 激励错位 | independent-trader-advantage | B 段 |
| ce19 | 管理层干预 | independent-trader-advantage | B 段 |
| ce20 | 报价错误 | data-quality-traps | B 段 |
| ce21 | 模型风险 | performance-diagnosis | B 段 |
| ce22 | 软件风险 | paper-trading-validation, performance-diagnosis | B 段 |
| ce23 | 低估准备时间 | paper-trading-validation | B 段 |
| ce24 | 学术策略局限 | parameter-complexity-overfitting, ai-method-applicability | B 段 |
| ce25 | 快速致富心态 | ideal-trader-profile | B 段 |
| ce26 | 资本不足 | ideal-trader-profile, strategy-selection-four-constraints | B 段 |

---

## 六、合并统计

### 输入统计
- Frameworks: 32 个
- Principles: 22 个
- Cases: 17 个
- Counter-examples: 13 个
- **总计: 84 个概念单元**

### 合并操作
- 完全重复合并: 12 对 (24 → 12)
- 包含关系合并: 5 组 (13 → 5)
- 高度相关合并: 2 组 (4 → 2)
- 不值得蒸馏: 7 个

### 输出统计
- **值得蒸馏的 Skills: 25 个**
- **不值得蒸馏: 7 个**
- **合并减少: 32 个概念单元**

### 压缩率
- 原始: 84 个概念单元
- 最终: 25 个 skills
- **压缩率: 70%** (84 → 25)

---

## 七、下一步行动

1. ✅ 本文档完成（STAGE3_MERGING.md）
2. ⏳ 按 25 个 skills 清单，逐个构造 SKILL.md
3. ⏳ 每个 SKILL.md 包含: R/I/A1/A2/E/B 六段
4. ⏳ A1 段使用分配的 cases
5. ⏳ B 段使用分配的 counter-examples

---

**文档版本**: v1.0  
**生成时间**: 2026-08-14  
**状态**: 待审核
