# Snyk API

This source provides access to the Snyk REST API, which allows for managing projects, viewing vulnerabilities, and interacting with other Snyk resources.

## Authentication

Authentication is handled via a Personal Access Token (PAT). You can generate a token in your Snyk account settings under the "Service accounts" section. The agent will prompt you to enter this token.

## API Versioning

The Snyk REST API uses a date-based versioning scheme. A version must be supplied as a query parameter to every API call.

**Example:** `?version=2024-05-23`

## Common Endpoints

### List Organizations
- **Method:** `GET`
- **Path:** `/orgs`

### List Projects
- **Method:** `GET`
- **Path:** `/orgs/{org_id}/projects`
