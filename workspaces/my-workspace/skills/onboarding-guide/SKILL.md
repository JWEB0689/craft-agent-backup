---
name: "Onboarding Guide"
description: "Create a concise Getting Started guide with commands to run locally, common issues, and how to contribute."
globs:
  - "README.md"
  - "docs/**"
---

# Onboarding Guide

When invoked, produce a short, practical Getting Started guide that includes:

- Prerequisites (OS, tools, versions)
- Environment variables and how to set them (use `.env.example` as reference)
- Step-by-step local setup commands (install, build, run, test)
- How to run the test suite and linters
- Common troubleshooting tips and where to find help (chat, issues, maintainers)
- Contribution steps: branching model, commit message format, PR checklist

Output: `ONBOARDING.md` content (3–6 short sections) and a suggested PR description to add it to the repo.