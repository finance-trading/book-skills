# PIPELINE_STATE.md — 《一本书读懂财报》蒸馏流水线

## 基本信息

- **书籍**: 《一本书读懂财报（全新修订版）》
- **作者**: 肖星
- **来源**: `.library/Financial_freedom/《一本书读懂财报（全新修订版）》.pdf`
- **输出 slug**: `financial-statements-for-beginners-xiaoxing`
- **开始日期**: 2026-09-06

## 阶段进度

### ✅ Stage 0: Adler 整书理解

- **状态**: 完成，用户已确认骨架
- **产出**: `BOOK_OVERVIEW.md`, `source.txt`
- **覆盖**: 结构、解释、批判、应用潜力
- **下一步**: 用户确认后进入 Stage 1 五路候选提取

### ✅ Stage 1: 并行提取

- **状态**: 完成（五路候选已生成并通过结构、ID、引文长度检查）
- **产出**: `candidates/frameworks.md`（25）、`principles.md`（30）、`cases.md`（24）、`counter-examples.md`（23）、`glossary.md`（15）
- **下一步**: Stage 1.5 三重验证

### ⏳ Stage 1.5: 三重验证筛选

- **状态**: 已完成初筛，15 个单元通过；等待用户轻确认后进入 Stage 2
- **产出**: `verified.md`, `rejected/README.md`

### ✅ Stage 2: RIA++ 构造

- **状态**: 完成 15 个 skill 初稿，含 `SKILL.md` 与 `test-prompts.json`
- **下一步**: Stage 3 Zettelkasten 链接与共享词典

### ✅ Stage 3: Zettelkasten 链接

- **状态**: 完成 15 个 skill 的相关链接、`INDEX.md` 与共享 `GLOSSARY.md`
- **下一步**: Stage 4 压力测试

### ✅ Stage 4: 压力测试

- **状态**: 15/15 skill 通过结构化复核（每个 6 条用例，100%）
- **残余风险**: 初版通用用例经独立盲测判定过宽，已替换为专属触发和边界用例；多 skill 同时命中仍需线上观察
- **产出**: 各 skill 的 `test-prompts.json`, `test-results.md`, `test-results-independent.md`
- **下一步**: Stage 5 交付

### ✅ Stage 5: 交付

- **状态**: `DIGEST.md`、`INDEX.md`、`GLOSSARY.md` 和 15 个可调用 skill 已生成
- **安装**: 尚未复制/ symlink 到用户或项目 skills 目录，等待用户指定安装位置

## 审计约束

- 保留 `source.txt`、`candidates/` 和 `rejected/`，不覆盖后续已完成产物。
- 每个最终 skill 必须包含 R/I/A1/A2/E/B、原文短引、兄弟 skill 诱饵测试和 `test-prompts.json`。
- 下游引用必须指向本 skill 目录内文件。
