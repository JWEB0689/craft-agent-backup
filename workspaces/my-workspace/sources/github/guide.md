# GitHub MCP (Copilot)

This source connects to GitHub's remote MCP server (https://api.githubcopilot.com/mcp/) and exposes tools for repository-level context: commits, PRs, issues, code search, and Copilot features where available.

Scope
- Repository metadata, pull requests, issues, and code context that your GitHub account has access to.

Guidelines
- This remote MCP source is configured for bearer-token authentication using a GitHub PAT (Authorization: Bearer <PAT>).
- In Explore mode we'll allow read-only operations so the agent can search and summarize repos and PRs.

Examples
- Search for recent PRs touching the mobile app:
  - `mcp__github__search` (query: `repo:your-org/mobile is:pr updated:>2026-01-01`)
- Get PR details:
  - `mcp__github__get` (resource: `pulls`, id: 123)

Notes
- Some Copilot/MCP tools require a Copilot subscription for full functionality.
- Create a GitHub PAT with the minimum required scopes for your intended work and store it through the secure credential prompt, not in chat.