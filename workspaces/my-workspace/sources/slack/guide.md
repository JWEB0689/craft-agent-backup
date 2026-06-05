# Slack MCP Source

This source connects to Slack, a popular messaging and collaboration platform. It allows Craft Agent to interact with Slack workspaces, send messages, read channel history, and manage user information (based on granted permissions).

## Scope

-   Sending messages to channels or direct messages.
-   Reading messages and channel history.
-   Accessing information about users and channels.
-   Managing Slack resources (e.g., creating channels, inviting users) if configured with appropriate scopes during OAuth.

## Guidelines

-   **Authentication**: Slack uses OAuth 2.0. You will be redirected to Slack to authorize the Craft Agent app. Ensure you grant the necessary permissions for the tasks you intend to perform.
-   **Permissions**: The capabilities of this source are determined by the OAuth scopes granted during authentication. If certain actions fail, you may need to re-authenticate with broader scopes.
-   **Rate Limits**: Be mindful of Slack API rate limits to avoid disruptions.
-   **Channel/User IDs**: Many Slack API operations require channel or user IDs. You might need to retrieve these using other Slack tools or by inspecting Slack URLs.

## Examples

### Sending a Message to a Channel (Conceptual)

To send a message, you would typically use a tool exposed by the Slack MCP. Here's a conceptual example:

```python
# This is a conceptual example. The actual tool call will depend on the Slack MCP's exposed functions.
# mcp__slack__send_message(
#     _displayName="Send Slack Message",
#     _intent="Send a greeting message to a specific Slack channel.",
#     channel="C1234567890", # Replace with your channel ID
#     text="Hello from Craft Agent!"
# )
```

### Listing Channels (Conceptual)

```python
# This is a conceptual example. The actual tool call will depend on the Slack MCP's exposed functions.
# mcp__slack__list_channels(
#     _displayName="List Slack Channels",
#     _intent="Retrieve a list of public Slack channels."
# )
```

**Note**: The actual tool names and parameters for Slack will become available once the source is fully configured and enabled. You can then use `list_tools("slack")` to discover them.