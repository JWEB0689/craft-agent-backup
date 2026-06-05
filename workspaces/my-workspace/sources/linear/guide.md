# Linear

This source connects to Linear's official MCP server (https://mcp.linear.app/mcp) and exposes tools for searching, listing, and manipulating Linear objects (issues, projects, comments).

Scope
- Access to issues, projects, team assignments, comments for your Linear account once authenticated.

Guidelines
- This source is configured for OAuth authentication (interactive flow). After I run validation, I will trigger the OAuth flow so you can sign in.
- For read-only Explore mode, the agent will be allowed to list/search/read resources by default.
- Use the `Authorization: Bearer <token>` header if you prefer to supply a token instead of the interactive flow.

Examples
- Find recent open issues in your iOS project:
  - mcp tool: `mcp__linear__search` (query: `project:"Craft iOS" state:open sort:createdAt desc`)

- List projects:
  - `mcp__linear__list` (resource: `projects`)

Notes
- See https://linear.app/docs/mcp for official MCP docs and transport details.
- Linear supports Streamable HTTP and SSE transports; this config uses the HTTP/SSE endpoint.