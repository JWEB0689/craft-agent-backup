---
name: "Workspace Inspector"
description: "Scan the workspace and produce a concise summary of projects, top-level languages, key files, and suggested next steps."
globs:
  - "README.md"
  - "package.json"
  - "pyproject.toml"
  - "requirements.txt"
---

# Workspace Inspector

When invoked, scan the workspace root and immediate subfolders to identify:

- Top-level projects (by package files: package.json, pyproject.toml, setup.py, go.mod, Cargo.toml)
- Primary languages and runtimes
- Presence of READMEs, CONTRIBUTING, LICENSE
- CI/config files (e.g., .github, .gitlab-ci.yml, azure-pipelines.yml)
- Large files (>1MB) and binary assets
- Test directories and common scripts (start, build, test)
- Dependency manifests and lockfiles (package-lock.json, yarn.lock, poetry.lock, Pipfile.lock)

Output (concise):
- One-line project summary per top-level project
- Detected entry points, package manager, test runner
- Notable risks or missing items (no README, no CI)
- Suggested next steps (run tests, open README, add CI, create issues)

Example output:
- Repo root: Node project (package.json) → entry: index.js; test: jest; next: run `npm test`