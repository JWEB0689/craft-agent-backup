# Local Workspace Files

Access to local workspace files located at:

C:\Users\Jwebe\.craft-agent\workspaces\my-workspace

## Scope

- All files under the workspace: `sources/`, `skills/`, `sessions/`, and other project files.
- Intended for read-only exploration and searching via the agent.

## Guidelines

- Use this source for searching and reading files in the workspace.
- Avoid destructive commands; permissions.json restricts write/delete commands in Explore mode.
- If you need write/update capabilities, ask and I can create a scoped source with explicit write permissions.

## Examples

- List workspace root:

  - Windows: `dir C:\\Users\\Jwebe\\.craft-agent\\workspaces\\my-workspace`
  - Unix-style: `ls C:/Users/Jwebe/.craft-agent/workspaces/my-workspace`

- Show a file:
  - `type sessions\\260531-silver-ruby\\conversation.txt` (Windows)
  - `cat sessions/260531-silver-ruby/conversation.txt` (Unix)

## Notes

- This source is intentionally set up for read-only exploration. If you'd like broader access (search & modify), tell me which folders and I will prepare a secure config.