---
name: "Changelog Manager"
description: "Maintain CHANGELOG.md from conventional commits and release tags."
globs:
  - "CHANGELOG.md"
---

# Changelog Manager

When invoked, generate or update `CHANGELOG.md` using Conventional Commits and repository tags:

- Create an `Unreleased` section from recent commits since the last tag
- Format entries under headings: Added, Changed, Fixed, Deprecated, Removed, Security
- List PRs/commits with short summaries and links (when available)
- When releasing, move `Unreleased` to a versioned heading and add a release date
- Provide a suggested PR body for publishing the release

Output: well-formatted markdown snippet suitable for appending to `CHANGELOG.md`.