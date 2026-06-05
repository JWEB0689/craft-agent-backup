---
name: "Workflow Automation"
description: "Generate automation workflows (dependabot, auto-merge, labelers) and CI cron jobs."
requiredSources:
  - "github"
globs:
  - ".github/**"
---

# Workflow Automation

When invoked, generate or suggest repository automation to reduce manual work:

- Dependabot configuration for dependency updates with sensible directory and schedule
- Auto-merge action templates (with checks: build, tests, review) and safe gating rules
- PR labeler examples and issue/PR templates to standardize workflows
- Scheduled CI cron jobs for periodic tasks (tests, linting, dependency audits)
- Suggested branch protection rules and CODEOWNERS snippet to route reviews

Output:
- `.github/dependabot.yml`, `.github/workflows/auto-merge.yml`, `.github/labeler.yml`, and `CODEOWNERS` example

Notes: If `github` is available, include sample PR titles/descriptions for adding these automations.