# LM Studio API Source

This source connects to a locally running LM Studio instance, allowing Craft Agent to interact with local Large Language Models (LLMs).

## Scope

-   Access to LLMs served by LM Studio via its OpenAI-compatible API endpoint.
-   Ability to send prompts to the local model and receive responses.
-   Utilizes the `google/gemma-4-e2b` model as specified in the configuration.

## Guidelines

-   **LM Studio must be running**: Ensure LM Studio is open and the local server is started (typically at `http://localhost:1234/v1/` or the URL provided).
-   **Model Selection**: The configured model is `google/gemma-4-e2b`. If you change the model in LM Studio, you may need to update the source configuration.
-   **No Authentication**: This source is configured without authentication (`authType: "none"`) as it's a local server.
-   **API Interaction**: Craft Agent will communicate with the LM Studio API endpoint to send prompts and receive model outputs.

## Examples

### Making a Chat Completion Request (Conceptual)

To interact with your local LM Studio model, you'll use the `mcp__lmstudio-api__api_lmstudio-api` tool. Here's how a conceptual call might look:

```python
mcp__lmstudio-api__api_lmstudio_api(
    _displayName="Chat Completion with LM Studio",
    _intent="Send a prompt to the local google/gemma-4-e2b model via LM Studio.",
    path="/chat/completions",
    method="POST",
    params={
        "messages": [
            {"role": "user", "content": "Explain the concept of quantum entanglement in simple terms."}
        ],
        "max_tokens": 512, # Adjust as needed
        "model": "google/gemma-4-e2b" # Ensure this matches your loaded model
    }
)
```

**Note**: When using local models, ensure the `model` parameter in your calls matches the model loaded and served by LM Studio.