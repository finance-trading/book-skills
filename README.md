# book-skills

将书籍、长视频、播客等内容蒸馏为可执行的 Claude Skill，让 AI Agent 在真实场景中直接调用。

## 项目结构

```
book-skills/
├── .agents/skills/          # 转换器 & 源 skill（不存放生成产物）
│   ├── book-to-skill/       # 英文书籍 → skill（Python 工具链）
│   ├── cangjie-skill/       # 中文书籍/长内容 → skill（核心蒸馏引擎）
│   ├── huashu-nuwa/         # 华叔女娲 · 多视角拆书框架
│   ├── nuwa-skills/         # 女娲生成的投资大师视角 skill
│   ├── pdf/                 # PDF 处理 skill
│   ├── pdf-ocr-extraction/  # PDF OCR 提取 skill
│   └── book-skills/         # 已生成的书籍 skill（运行时安装）
├── cangjie-skills/          # 仓颉蒸馏输出（按书分目录）
├── output/                  # OCR 等中间产物
├── scripts/                 # 辅助脚本
└── .library/                # 书库原始资料
```

## 已蒸馏书籍

### 量化交易 & 金融科技

| 书籍 | Skill 目录 | 说明 |
|------|-----------|------|
| *AI Quant Trading* | `cangjie-skills/ai-quant-trading/` | A 股 AI 量化交易实战 |
| *GPT Era Quant Trading* | `cangjie-skills/gpt-era-quant-trading/` | GPT 时代的量化交易策略与案例 |
| *Inside the Black Box* | `cangjie-skills/inside-the-black-box/` | 量化对冲基金 Alpha 模型解析 |
| *Quantitative Trading* — Ernest Chan | `cangjie-skills/quantitative-trading-ernest-chan/` | 量化交易入门经典 |

### 价值投资

| 书籍 | Skill 目录 | 说明 |
|------|-----------|------|
| *The Intelligent Investor* — Graham | `cangjie-skills/intelligent-investor/` | 聪明的投资者核心原则 |
| *The Most Important Thing* — Howard Marks | `cangjie-skills/marks-most-important-thing/` | 投资中最重要的事 |

## 投资大师视角 Skill

`nuwa-skills/` 下包含基于女娲框架生成的投资大师决策视角：

| Skill | 说明 |
|-------|------|
| `benjamin-graham-skill` | 本杰明·格雷厄姆价值投资视角 |
| `warren-buffett-perspective` | 沃伦·巴菲特商业所有者视角 |
| `philip-arthur-fisher-perspective` | 菲利普·费雪成长股视角 |
| `munger-skill` | 查理·芒格多元思维模型 |
| `taleb-skill` | 纳西姆·塔勒布反脆弱视角 |
| `stanley-druckenmiller-perspective` | 斯坦利·德鲁肯米勒宏观交易视角 |
| `jesse-livermore-perspective` | 杰西·利弗莫尔趋势投机视角 |
| `duan-yongping-perspective` | 段永平"本分"价值投资视角（7心智模型/12启发式） |

## 工作流

### 蒸馏一本书（中文）

使用 `cangjie-skill`，支持 PDF / 长文 / 播客 / 课程：

```
"把这个视频/播客/课程蒸馏成 skill"
"把 XX 书做成 skill"
"拆书"
```

### 蒸馏一本书（英文）

使用 `book-to-skill`，基于 Python 工具链：

```
"distill this book into a skill"
```

### PDF 处理

- `pdf` — PDF 表单填写与操作
- `pdf-ocr-extraction` — 扫描件 OCR 文字提取

## 约定

- 转换器源码放在 `.agents/skills/`，生成产物按 `cangjie-skills/<slug>/` 组织
- 每个生成 skill 包含 `SKILL.md`、`INDEX.md`、`GLOSSARY.md` 等结构化文件
- `books/<skill-slug>/` 目录存放 `book-to-skill` 的输出

## 许可

各 skill 保留各自的原始许可协议，详见对应目录下的 LICENSE 文件。
