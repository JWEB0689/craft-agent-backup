---
name: "API Docs"
description: "Generate or update API reference and OpenAPI from code/comments; produce markdown API guides."
globs:
  - "src/**/*.py"
  - "src/**/*.js"
  - "src/**/*.ts"
  - "openapi.yaml"
  - "openapi.yml"
---

# API Docs

When invoked, produce or update a machine-readable OpenAPI 3.x document and a human-friendly API reference:

- Extract endpoints, path/query parameters, request/response schemas and examples from code annotations, docstrings, or controllers.
- Normalize results into `openapi.yaml` (or `openapi.yml`) at repo root or `docs/openapi.yaml`.
- Generate `docs/api.md`: grouped endpoints by tag, short descriptions, example cURL/HTTP requests and sample JSON responses, and code samples in Python/JavaScript.
- If an OpenAPI already exists, validate it and fill missing schema pieces with best-effort inferred types; mark items that require manual review.
- Include suggestions for tools/commands to regenerate (swagger-jsdoc, apispec, drf-spectacular, openapi-generator) and a brief README snippet explaining how to maintain the spec.

Outputs:
- `openapi.yaml` (OpenAPI 3.x)
- `docs/api.md` with examples and quickstart usage

Citations: For each generated path/schema, include source file and line references so maintainers can review the inferred definitions.