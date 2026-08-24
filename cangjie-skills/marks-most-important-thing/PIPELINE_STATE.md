# PIPELINE_STATE.md — 《投資最重要的事》蒸馏流水线

## 基本信息

- **书籍**: 《投資最重要的事：一本股神巴菲特讀了兩遍的書》 / *The Most Important Thing Illuminated*
- **作者**: 霍華·馬克斯 (Howard Marks)
- **开始日期**: 2026-08-23

---

## 阶段进度

### ✅ Stage 0: Adler 整书理解
- **状态**: 完成
- **产出**:
  - `raw_text.txt`
  - `BOOK_OVERVIEW.md`

### ✅ Stage 1: 5 个 extractor 并行提取
- **状态**: 完成
- **产出**:
  - `candidates/frameworks.md`（28 条原始候选）
  - `candidates/principles.md`（63 条原始候选）
  - `candidates/cases.md`（35 条原始候选）
  - `candidates/counter-examples.md`（44 条原始候选）
  - `candidates/glossary.md`（30 条原始候选）
- **总计**: 200 条原始候选

### ✅ Stage 1.5: 三重验证筛选
- **状态**: 完成，用户确认 14 个单元全部进入 Stage 2
- **产出**:
  - `verified.md`（14 个合并后的通过单元）
  - `rejected/README.md`（合并、降级和淘汰原因）

### ⏳ Stage 2: RIA++ 构造 skill
- **状态**: 完成
- **产出**: 14 个独立 `SKILL.md`

### ✅ Stage 3: Zettelkasten 链接
- **状态**: 完成
- **产出**:
  - `INDEX.md`
  - `GLOSSARY.md`
  - 14 个 skill 的相关关系段

### ✅ Stage 4: 压力测试
- **状态**: 完成（fallback 静态触发审计）
- **产出**:
  - 14 个 `test-prompts.json`
  - 14 个 `test-results.md`
  - 共 84 条测试用例
- **结果**: 各 skill 结构化测试均为 6/6；未执行独立盲测

### ✅ Stage 5: 交付
- **状态**: 完成（仓库形式；未安装到宿主 skills 目录）
- **产出**:
  - `DIGEST.md`
  - `INDEX.md`
  - `GLOSSARY.md`

---

## 最终统计

- 独立 skills: 14
- 测试用例: 84
- 原始候选: 200
- 通过单元: 14
- 交付方式: 保留在 `cangjie-skills/marks-most-important-thing/`

---

## 收尾说明

- 14 个单元均已按用户确认生成
- 当前产物保留在仓库中，未复制到用户级或项目级宿主 skills 目录
- Stage 4 为 fallback 静态触发审计；如需更高置信度，可再接入独立 agent 盲测
