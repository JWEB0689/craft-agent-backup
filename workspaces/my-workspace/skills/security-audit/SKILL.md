---
name: "Security Audit"
description: "Perform static checks for secrets, unsafe patterns, and common vulnerabilities; provide remediation steps."
globs:
  - "**/*.py"
  - "**/*.js"
  - "**/*.ts"
  - "Dockerfile"
  - "**/*.yml"
  - "**/*.yaml"
  - "terraform/**"
alwaysAllow:
  - "Bash"
---

# Security Audit

When invoked, run a focused security review that includes:

- Secret detection (API keys, tokens, private keys) with file/line citations
- Dependency vulnerability checks (coupled with Dependency Audit)
- Insecure configuration patterns (e.g., debug flags, permissive CORS, plaintext secrets in env files)
- Common code issues: SQL injection risks, unsafe deserialization, insecure crypto usage, improper auth checks
- Container misconfigurations (running as root, exposed ports, large surface area)

Produce a prioritized list of findings with:
- File path and excerpt
- Severity (low/medium/high/critical)
- Suggested remediation steps and example code snippets

Example output:
- Issue: Hard-coded AWS key in `scripts/deploy.js` (critical) — remove secret, rotate keys, use secret store
- Suggest running: `gitleaks detect`, `trufflehog`, `pip-audit`, `npm audit`