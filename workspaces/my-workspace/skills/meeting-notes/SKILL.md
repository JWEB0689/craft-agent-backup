---
name: "Meeting Notes"
description: "Turn meeting transcripts into concise notes, decisions, and action items with owners and due dates."
globs:
  - "meetings/**"
  - "**/*-notes.md"
---

# Meeting Notes Skill

Given a transcript or meeting text, produce:

- A concise summary (3–5 bullets)
- Decisions made with short rationale
- Action items extracted with suggested owners and due dates (if implicit)
- Open questions and follow-ups
- Output as a checklist with suggested assignees and short next steps

Example output:
- Summary: "Planning sync for Q3 roadmap — decided to prioritize feature X."
- Decisions: "Adopt library Y for data ingestion (owner: Alice)."
- Action items:
  - [ ] Integrate library Y into pipeline (owner: Alice, due: 2026-06-10)