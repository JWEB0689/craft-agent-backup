---
name: "Cron Jobs"
description: "Create templated scheduled job configs (GitHub Actions, Kubernetes CronJob) with healthchecks and retry policies."
---

# Cron Jobs

When invoked, produce scheduled job templates and recommendations:

- GitHub Actions scheduled workflow example (`on: schedule`) with concurrency controls and notification steps
- Kubernetes `CronJob` manifest template with `concurrencyPolicy`, `backoffLimit`, and `successfulJobsHistoryLimit` configured
- Healthcheck and idempotency recommendations for scheduled tasks and guidance for observability (logs, metrics)
- Retry and failure handling strategies: exponential backoff, dead-letter queues, alerts on repeated failures

Output:
- `.github/workflows/scheduled-task.yml` example
- `k8s/cronjob.yaml` template
- Short checklist for ensuring safe scheduled jobs (idempotency, monitoring, secrets handling)