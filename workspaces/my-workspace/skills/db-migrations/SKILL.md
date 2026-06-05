---
name: "DB Migrations"
description: "Help author or review SQL/ORM migrations and detect breaking changes."
globs:
  - "migrations/**"
  - "**/*migration*.sql"
  - "alembic/**"
  - "prisma/**"
---

# DB Migrations

When invoked, review migration scripts and provide a safety-focused checklist and remediation suggestions:

- Verify idempotency and reversible down migrations where appropriate
- Detect destructive operations (DROP COLUMN, ALTER COLUMN type) and suggest safe rollout strategies (shadow tables, backfills)
- Check for missing indexes that may cause slow queries after schema changes
- Estimate potential downtime and recommend zero-downtime patterns when needed
- Produce a rollout plan with steps: apply in staging, run backfills, monitor slow queries, release in phases

Output: list of concerns with file/line citations and a recommended deployment plan.