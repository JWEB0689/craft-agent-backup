---
name: "Run Tests"
description: "Run the project's test suite, summarize failures, and recommend fixes."
globs:
  - "**/test/**"
  - "**/*.spec.*"
  - "**/*.test.*"
alwaysAllow:
  - "Bash"
---

# Run Tests Skill

When invoked:

- Detect the project's test command (`npm test`, `pytest`, `go test`, `mvn test`, `cargo test`)
- Run the test command (when allowed) and capture output
- Summarize pass/fail counts and list top failing tests with stack traces
- Suggest probable fixes and next debugging steps
- If many failures, suggest isolating tests and running affected suites

Output: concise summary, failing test names, short failure excerpts, and suggested fixes.