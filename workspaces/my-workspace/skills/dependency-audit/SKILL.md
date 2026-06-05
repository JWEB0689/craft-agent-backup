---
name: "Dependency Audit"
description: "Scan dependency manifests for outdated or vulnerable dependencies and produce an upgrade plan."
globs:
  - "package.json"
  - "requirements.txt"
  - "pyproject.toml"
  - "Pipfile"
  - "yarn.lock"
  - "package-lock.json"
---

# Dependency Audit

When invoked, analyze dependency manifests and lockfiles to:

- List direct and transitive dependencies and their versions
- Identify outdated packages and recommend target versions
- Run vulnerability checks (e.g., pip-audit, `npm audit`, `yarn audit`) and summarize CVEs
- Group recommended upgrades by risk/effort (major/minor/patch)
- Produce a safe upgrade plan: exact commands, required test steps, and a suggested PR title/body
- Call out breaking changes and migration notes for major upgrades

Example output:
- Outdated: `lodash 4.17.15 -> 4.17.21` (patch)
- Vulnerability: `package-x` CVE-YYYY-NNNN — upgrade to `>=1.2.3`
- Suggested PR: `chore(deps): bump lodash to 4.17.21` with commands to run and verification steps

Notes: Prefer regenerating lockfiles and running full test suites after upgrades. When applicable, recommend batch PRs (low-risk) vs single-change PRs (high-risk).