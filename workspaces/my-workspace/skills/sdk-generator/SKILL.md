---
name: "SDK Generator"
description: "Generate SDK clients (JS/Python/Go) from OpenAPI or endpoint descriptions; produce example usage."
globs:
  - "openapi.yaml"
  - "openapi.yml"
  - "spec/**"
alwaysAllow:
  - "Bash"
---

# SDK Generator

When invoked, produce language-specific SDK clients from an authoritative OpenAPI spec:

- Ensure `openapi.yaml` exists; if not, attempt to generate or normalize one (see API Docs skill).
- Use a standard generator (OpenAPI Generator / swagger-codegen) to create client libraries for requested languages (Python, JavaScript/TypeScript, Go).
- Produce a small `README.md` per client with quickstart, installation, auth instructions, and one or two common usage examples.
- Suggest packaging and publishing steps (PyPI, npm, GitHub Packages, Go modules) and CI steps to build and publish SDK artifacts.
- Provide example commands to regenerate the SDK when the API changes.

Output:
- `sdk/python/`, `sdk/js/`, `sdk/go/` (generated client code)
- `sdk/README.md` summarizing usage and regen commands

Notes: When running generators, prefer configurable templates and a deterministic output folder so diffs are reviewable.