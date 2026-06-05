---
name: "I18n Review"
description: "Find hard-coded user-facing strings, suggest extraction plans, and generate locale file skeletons."
globs:
  - "**/*.js"
  - "**/*.ts"
  - "**/*.py"
  - "templates/**"
---

# I18n Review

When invoked, assist with internationalization readiness:

- Scan source files and templates for hard-coded user-facing strings and collect candidates for extraction
- Suggest a key-naming scheme and propose locations for locale files (e.g., `locales/en.json`, `locales/en.po`)
- Generate a locale skeleton with keys and default-language strings for easy review and translation
- Flag common i18n pitfalls: string concatenation, interpolated formatting without localization, pluralization issues, and date/number formatting
- Provide an incremental migration plan and sample code snippets for integrating i18n libraries (i18next, gettext, formatjs)

Output:
- `i18n/suggestions.json` listing string candidates with file/line citations
- `locales/en.json` skeleton with suggested keys and values

Notes: Prefer small, incremental PRs that extract a few keys at a time and include tests for formatting.