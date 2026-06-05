# GitHub API

This source provides access to the GitHub REST API (https://api.github.com/) for repositories, issues, pull requests, users, and related resources. It is configured for bearer-token (Personal Access Token / PAT) authentication by default.

## Scope
- Access is limited to the authenticated user and any repositories/organizations the provided token has permissions for.
- Typical read-only tasks: list repositories, read issues and PRs, search issues, fetch commits and user profiles.
- If you grant write scopes to the token (not recommended unless you need it), the source can also create/update issues and PRs.

## Setup hints (what I did for you)
- I added a clear `testEndpoint` (GET `user`) so the system can validate credentials quickly.
- I set default request headers (`Accept: application/vnd.github.v3+json`, `User-Agent: Craft Agent`) so responses are consistent.
- Permissions.json allows read-only GET requests in Explore mode.

## Authentication (how to finish setup)
1. Create a Personal Access Token (PAT) on GitHub:
   - Classic token: Settings → Developer settings → Personal access tokens → Classic → Generate new token
   - Fine-grained token (recommended for limited scope): Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token
2. Recommended scopes for common tasks:
   - Read-only exploration (recommended): repo:status, read:org, user
   - Search/read-only: public_repo (or no repo scopes if you only need public data)
   - Write actions (only if needed): repo
3. To authenticate, allow me to prompt you securely and paste the PAT (do not paste tokens in chat). I will then store it securely and re-run the validation.

## How validation works
- I will run `source_test` which:
  - Validates the config.json schema
  - Attempts an authenticated GET /user (testEndpoint) to verify the token
  - Downloads and caches the icon
  - Auto-enables the source if validation passes
- If the test reports `needs_auth`, I will prompt you for the PAT using a secure UI.

## Example API usage (paths relative to baseUrl)
- Get authenticated user: GET `user`
- List a user's repos: GET `users/{username}/repos`
- List issues in a repo: GET `repos/{owner}/{repo}/issues`
- Search issues: GET `search/issues?q={query}`

When calling endpoints via the agent, pass paths without a leading slash (e.g., `repos/craft-ai-agents/craft-agents/issues`).

## Troubleshooting
- If you see rate limit errors, create a token and authenticate; authenticated tokens have higher limits.
- If authentication fails with 401/403, regenerate a PAT with the required scopes and try again.
- I will not accept tokens pasted directly into chat — use the secure prompt I provide.

## Next steps
- Would you like me to run `source_test` now and, if needed, prompt you to enter the PAT securely to finish setup?