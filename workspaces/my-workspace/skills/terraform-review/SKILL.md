---
name: "Terraform Review"
description: "Lint and audit Terraform for best-practices, drift risks, and sensitive outputs."
globs:
  - "terraform/**"
  - "**/*.tf"
alwaysAllow:
  - "Bash"
---

# Terraform Review

When invoked, perform a safety-first review of Terraform code and configurations:

- Run and summarize results of common tools when available (`tflint`, `tfsec`, `checkov`)
- Detect sensitive outputs, plaintext secrets in variables, and risky resource attributes (public IPs, wide CIDR blocks)
- Identify anti-patterns: hard-coded credentials, missing lifecycle rules for critical resources, and dangerous `create_before_destroy`/`force_destroy` usage
- Check for state management issues and recommend remote state/backends and locking
- Provide remediation steps and, when applicable, safer alternative resource configurations

Output: prioritized findings with file/line refs and recommended commands to validate/fix issues.