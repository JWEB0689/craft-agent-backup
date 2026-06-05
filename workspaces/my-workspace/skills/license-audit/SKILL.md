---
name: "License Audit"
description: "Detect repository license, scan dependency licenses, and flag incompatible or risky licenses."
globs:
  - "LICENSE"
  - "package.json"
  - "pyproject.toml"
  - "go.mod"
  - "Cargo.toml"
---

# License Audit

When invoked, perform a license and compliance scan:

- Detect the repository's license file and summarize its permissions and restrictions
- Scan dependency manifests and lockfiles to collect declared licenses for direct dependencies
- Flag dependencies with copyleft/viral licenses (GPL family) or other licenses that may be incompatible with the repo license
- Provide remediation recommendations: replace dependency, seek a permissive alternative, or obtain legal approval
- Suggest adding a `LICENSE` badge and updating `CONTRIBUTING`/`README` with license notes

Output: a short report listing repo license, dependency license summary, and high-priority compatibility concerns with file/line citations where relevant.