---
name: "Access Control"
description: "Review IAM/policy files and suggest least-privilege changes for AWS, GCP, and Azure."
globs:
  - "iam/**"
  - "policies/**"
  - "terraform/**"
---

# Access Control

When invoked, analyze IAM and policy definitions and recommend least-privilege improvements:

- Detect overly permissive statements (Action: "*", Resource: "*") and wildcard principals
- Map which identities/users/service accounts have broad permissions and suggest scoped roles
- Suggest role-based access patterns, IAM conditions, and resource scoping (ARNs, project IDs)
- Flag long-lived credentials, recommend short-lived credentials or role chaining and rotation
- Provide safe migration steps: create new scoped role, migrate principals, run smoke tests, then remove legacy permissions

Output: prioritized list of findings with example replacement policy snippets and file/line citations.