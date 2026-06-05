---
name: "Test Generator"
description: "Produce unit test skeletons for selected functions or files, following project test framework conventions."
globs:
  - "**/*.py"
  - "**/*.js"
  - "**/*.ts"
---

# Test Generator

When invoked for a given file or function, generate test skeletons that:

- Follow the project's test framework (pytest, unittest, jest, mocha)
- Include imports, fixtures/mocks, and at least one positive and one negative test case
- Use clear, descriptive test names and place tests in the recommended location (`tests/` or alongside source)
- Provide guidance on edge cases and how to run the tests locally

Example output:
- `tests/test_utils.py` with `test_parse_valid_input()` and `test_parse_invalid_input()` scaffolding and example assertions.