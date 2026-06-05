---
name: "Documentation Summarizer"
description: "Extract concise summaries, decisions, and action items from documentation and design notes."
globs:
  - "docs/**"
  - "README.md"
  - "CONTRIBUTING.md"
---

# Documentation Summarizer

Given one or more documentation files or folders, produce:

- One-paragraph summary of purpose and scope
- Key architecture decisions and rationale
- Explicit action items and owners if present
- Glossary of important terms (if any)
- Quick links (file path + heading) to where to find further details

Provide citations (file paths + heading names) for any extracted decisions or actions.