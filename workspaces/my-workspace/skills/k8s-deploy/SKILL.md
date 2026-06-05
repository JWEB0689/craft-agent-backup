---
name: "Kubernetes Deploy"
description: "Generate Kubernetes manifests and Helm chart suggestions with best-practices for readiness, liveness, and resource sizing."
globs:
  - "k8s/**"
  - "charts/**"
  - "deploy/**"
  - "Dockerfile"
---

# Kubernetes Deploy

When invoked, produce deployment artifacts and guidance:

- Generate `Deployment`, `Service`, `Ingress` (or IngressRoute), and `HorizontalPodAutoscaler` examples tailored to the app
- Recommend resource `requests` and `limits`, readiness/liveness probes, and security context (non-root user)
- Provide a Helm chart skeleton (`charts/<name>/`) with values.yaml and templates for common patterns
- Include deployment strategies: rolling updates, maxUnavailable/maxSurge, canary configuration notes
- Suggest health checks, resource quotas, and PodDisruptionBudget examples

Output:
- `k8s/deployment.yaml`, `k8s/service.yaml`, `k8s/hpa.yaml`, and a `charts/` skeleton
- A short `deploy/README.md` with `kubectl`/`helm` commands and rollback instructions

Notes: Prefer minimal, secure defaults and include comments explaining each field for reviewers.