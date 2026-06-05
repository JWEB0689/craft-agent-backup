---
name: "Monitoring Alerts"
description: "Create Prometheus alert rules and dashboard snippets plus an escalation and runbook checklist."
requiredSources:
  - "github"
---

# Monitoring Alerts

When invoked, produce concrete monitoring artifacts and runbooks:

- Prometheus alerting rules (YAML) for common failure modes: high error rate, elevated latency, job failures, instance/pod restarts, disk pressure, OOMs
- Example Grafana dashboard panels (JSON snippets) for key service metrics
- A short runbook for each alert: how to triage, immediate remediation steps, escalation contacts, and rollback suggestions
- Severity and notification guidance (pager vs Slack/email), and silence schedules for known maintenance windows

Example alert rule:
```yaml
- alert: HighErrorRate
  expr: rate(http_requests_total{job="api",status=~"5.."}[5m]) > 0.05
  for: 10m
  labels:
    severity: page
  annotations:
    summary: "High 5xx error rate on API"
    runbook: "docs/runbooks/high-error-rate.md"
```

Output:
- `monitoring/alerts.yaml`
- `monitoring/grafana-panels/` snippets
- `monitoring/runbooks/` markdown runbooks

Notes: If `github` is available, include suggested PR title/body to add these files to the repository.