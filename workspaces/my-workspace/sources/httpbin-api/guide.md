# httpbin.org

Public HTTP testing API. Use this source to verify HTTP requests and the API wiring of the agent.

## Scope

- Endpoints: `/get`, `/post`, `/status/{code}`, `/delay/{seconds}`, `/headers`, `/ip`, `/uuid`, etc.
- No authentication required.

## Guidelines

- This is a public test API; use it to validate request formatting and agent integration.
- Prefer lightweight endpoints such as `/get` or `/status/200` for quick tests.

## Examples

- GET simple endpoint:

  ```json
  { "method": "GET", "path": "get" }
  ```

- POST JSON body:

  ```json
  { "method": "POST", "path": "post", "body": { "hello": "world" } }
  ```
