---
name: "CI Setup"
description: "Generate CI pipeline templates and README instructions for GitHub Actions or GitLab CI."
globs:
  - ".github/**"
  - ".gitlab-ci.yml"
  - "azure-pipelines.yml"
requiredSources:
  - "github"
---

# CI Setup

When invoked, produce one or more CI pipeline templates tailored to the project's language/runtime (Node, Python, Go, Java, Docker):

- Minimal GitHub Actions workflow (checkout, setup, install deps, build, test, lint)
- Matrix testing example (node versions, python versions)
- Docker build and publish job example
- Guidance for secrets configuration (GITHUB_TOKEN, registry creds) and caching
- Suggested `ci/README.md` with commands to run locally and how to troubleshoot failures

Output should include a ready-to-drop `.github/workflows/ci.yml` (or `.gitlab-ci.yml`) and a short PR description to add the workflow.