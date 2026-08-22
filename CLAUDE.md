# Claude Instructions

This repository stores generated knowledge skills from books and long-form sources.

## Directory Rules

- `.agents/skills/` contains converter/source skills only: `book-to-skill`, `cangjie-skill`, `pdf`, and `pdf-ocr-extraction`.
- `book-to-skill` output goes in `books/<skill-slug>/`.
- `cangjie-skill` output goes in `cangjie-skills/<skill-slug>/`.
- Generated book skills should not be written directly into `.agents/skills/` unless the user explicitly asks for a runtime-installed skill.

## Workflow

- On `continue` / `继续`, inspect existing output and resume from the actual breakpoint.
- Preserve completed extraction, distillation, and verification artifacts.
- After generation or movement, check that `SKILL.md`, chapter links, and supporting files are internally consistent.
