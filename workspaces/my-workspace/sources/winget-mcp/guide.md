# Windows Package Manager MCP (winget)

This source exposes a local Model Context Protocol (MCP) server that wraps the Windows Package Manager (winget) tooling. It connects over stdio to the provided WindowsPackageManagerMCPServer.exe.

## Scope

- Search and list packages available via winget
- Query installed packages on the local machine
- (If the MCP server supports it) Request install/uninstall operations — these are destructive and are disabled in Explore mode by default

## How it connects

- Transport: stdio
- Command (as configured): `C:\Users\Jwebe\AppData\Local\Microsoft\WindowsApps\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\WindowsPackageManagerMCPServer.exe`
- Auth: none (local stdio)

## Guidelines

- In Explore (read-only) mode, only list/search/get operations are allowed by default. Installation/uninstallation requires explicit confirmation and elevated privileges — do not run those without your consent.
- If `source_test` fails, confirm that the executable path above exists and is runnable from your user account. If the executable requires elevated privileges, run the installer or point to a user-accessible wrapper.

## Examples

- List available packages (tool names depend on the MCP server implementation):
  - `mcp__winget-mcp__list_packages`
  - `mcp__winget-mcp__search_packages` (body: `{ "query": "git" }`)
  - `mcp__winget-mcp__list_installed`

If you want me to also configure the source to permit install/uninstall in non-Explore modes, tell me and I will add the appropriate permissions and note the safety prompts.