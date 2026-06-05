---
name: "Code Review"
description: "Review diffs and PRs for quality, security, style, and test coverage; provide actionable suggestions."
globs:
  - "**/*.py"
  - "**/*.js"
  - "**/*.ts"
  - "**/*.java"
  - "**/*.go"
alwaysAllow:
  - "Bash"
---

# Code Review Skill

When reviewing a diff or PR:

- Summarize the intent of the change
- Surface bugs, edge cases, and incorrect assumptions
- Note security issues (input validation, authentication, secrets handling)
- Comment on readability, naming, and abstraction
- Check for tests: suggest missing tests and how to test
- Provide prioritized, actionable suggestions with brief code snippets when helpful

Example output:
- Summary: "Adds feature X; modifies files A, B."
- Blockers: "Null check missing in foo() — see suggested snippet"