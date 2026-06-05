---
name: "Release Notes"
description: "Generate release notes from commits and PRs and suggest changelog entries."
requiredSources:
  - "github"
globs:
  - "CHANGELOG.md"
  - ".github/**"
---

# Release Notes

When invoked, compile release notes for a release candidate by:

- Grouping commits/PRs into categories (Features, Fixes, Chores, Breaking Changes)
- Calling out migration steps or breaking changes with clear instructions
- Listing contributors and associated PR numbers
- Producing a markdown-formatted release body suitable for GitHub Releases and CHANGELOG.md
- Suggesting a semantic version and a tag name

Example output:
- ## [v1.2.0] - 2026-06-01
  - Features: Added X, Improved Y
  - Fixes: Resolved crash in Z
  - Contributors: @alice, @bob

Include a short release checklist (upgrade notes, rollout steps).