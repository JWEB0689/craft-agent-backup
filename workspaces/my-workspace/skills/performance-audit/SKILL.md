---
name: "Performance Audit"
description: "Run lightweight profiling to identify hotspots and provide optimization suggestions."
globs:
  - "**/*.py"
  - "**/*.js"
  - "**/*.ts"
alwaysAllow:
  - "Bash"
---

# Performance Audit

When invoked, perform an initial performance review that includes:

- Guidance to run lightweight profilers (cProfile/pyinstrument for Python, Node profiler for JS)
- Steps to collect representative traces and example commands
- Summarize CPU and memory hotspots and the call stacks leading to them
- Provide prioritized optimization suggestions (algorithmic changes, caching, batching, I/O improvements)
- Recommend benchmarking commands and regression guardrails for CI

Output: short hotspot list with affected files/lines, estimated impact, and suggested next steps.