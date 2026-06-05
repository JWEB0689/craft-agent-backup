---
name: "Commit"
description: "Create well-formatted git commit messages following Conventional Commits."
alwaysAllow:
  - "Bash"
---

# Commit Message Skill

When crafting a commit message:

- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`
- Keep subject <= 72 characters, use imperative mood
- Body (when needed) explains *why* the change was made, not just what
- Include references to issues or tickets (e.g., `Refs: #123`)
- Add `Co-Authored-By: Craft Agent <agents-noreply@craft.do>` when appropriate

Example:
```
feat(auth): add OAuth2 token refresh

- Adds refresh flow for long-lived sessions
- Updates tests for token expiry

Refs: #123
```