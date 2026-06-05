---
name: "Cost Optimizer"
description: "Analyze infra configs and suggest cost-saving changes (instance types, reserved instances, idle resources)."
globs:
  - "terraform/**"
  - "k8s/**"
  - "cloud/**"
---

# Cost Optimizer

When invoked, analyze infrastructure configuration and highlight opportunities to reduce cost:

- Identify expensive resources (large VM types, oversized persistent volumes, over-provisioned replicas)
- Suggest lower-cost alternatives: smaller instance types, spot/preemptible instances, right-sizing, reserved/committed use discounts
- Point out idle or orphaned resources (unused volumes, idle instances) and recommend safe reclamation steps
- Recommend autoscaling, scheduling (stop non-critical resources off-hours), and caching improvements to reduce ongoing costs
- Provide an estimated cost delta (high-level/ballpark) for each recommendation and suggested PR/changes to implement them

Output: prioritized recommendations with affected file/lines and suggested commands or TF changes to apply.