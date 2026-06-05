---
name: "Codebase Summary"
description: "Summarize the project structure: modules, entry points, large files, dependencies, and tests."
globs:
  - "**/*.py"
  - "**/*.js"
  - "**/*.ts"
  - "**/*.go"
  - "**/*.java"
  - "**/*.rs"
---

# Codebase Summary

When activated, analyze the source tree to produce:

- High-level module breakdown (folders, packages, main entry points)
- Key files and their sizes
- Dependency list from manifests (package.json, requirements.txt, go.mod, Cargo.toml)
- Test presence and test runner hints (pytest, jest, go test, cargo test)
- TODOs and FIXME comment counts
- Suggested areas for documentation, refactor, or testing

Output: a structured bullet list highlighting entry points, top 5 largest files, dependencies summary, tests found, and recommended next steps.