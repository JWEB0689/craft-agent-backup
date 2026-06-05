# Memory MCP

Local stdio-based Memory MCP server for testing and development.

## Scope

- Provides simple memory/store and test tools via an MCP server run over stdio.
- No authentication required by default.

## Guidelines

- This source uses `npx -y @modelcontextprotocol/server-memory` as the stdio command. If `npx` or network access is not available on the host, the source_test step may fail. In that case, you can either:
  - Install the package locally and update `mcp.command`/`args` to point to a local binary, or
  - Replace this with an HTTP/SSE MCP server URL if you have one.

## Examples

- List available tools (after the server is running):
  - `mcp__memory-mcp__list` (agent-internal tool invocation format)

- Use as a sandbox for building MCP-based integrations.
