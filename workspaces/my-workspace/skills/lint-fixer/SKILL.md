---
name: "Lint & Fix"
description: "Run linters and propose or apply auto-fixable changes (eslint, ruff, clang-format)."
globs:
  - "**/*.py"
  - "**/*.js"
  - "**/*.ts"
  - "**/*.jsx"
  - "**/*.tsx"
alwaysAllow:
  - "Bash"
---

# Lint & Fix

When invoked, detect available linters/formatters in the project (eslint, ruff, black, prettier, clang-format) and:

- Run linters with autofix flags (e.g., `eslint --fix`, `ruff --fix`, `prettier --write`)
- Capture changes and summarize which rules were fixed and which remain
- For non-fixable issues, provide actionable suggestions and minimal code snippets
- Provide a recommended command sequence to include in CI

Example output:
- Ran `ruff --fix` and fixed 42 style issues; remaining 3 errors require manual review.