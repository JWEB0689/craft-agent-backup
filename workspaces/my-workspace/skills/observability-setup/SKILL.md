---
name: "Observability Setup"
description: "Add logging, tracing, and metrics examples (OpenTelemetry, Prometheus); recommend instrumentation points."
globs:
  - "src/**"
  - "otel/**"
  - "observability/**"
---

# Observability Setup

When invoked, produce practical observability scaffolding tailored to the project's stack:

- Identify critical code paths (HTTP handlers, background workers, DB access) to instrument
- Provide example instrumentation snippets for OpenTelemetry (Python/Node): automatic instrumentation and manual spans with attributes
- Add Prometheus metrics exporter examples and suggested metric names (request_latency_seconds, request_errors_total, db_query_seconds)
- Provide an example OTEL collector config and brief Grafana dashboard queries to visualize latency and error rates
- Recommend sampling strategy, semantic attributes to include, and performance considerations

Output:
- `observability/` examples (instrumentation snippets, collector config, sample dashboard queries)
- A short checklist of where to add spans/metrics in the codebase

Notes: Prefer incremental instrumentation and include examples for context propagation across HTTP calls and background jobs.