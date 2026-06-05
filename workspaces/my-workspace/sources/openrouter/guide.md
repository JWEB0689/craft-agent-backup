# OpenRouter API Source

This source provides access to various large language models (LLMs) through the OpenRouter unified API. It allows you to utilize models from different providers with a single API key.

## Scope

-   Access to a wide range of LLMs available on the OpenRouter platform.
-   Ability to perform chat completions, typically by specifying the model, messages, and other parameters.
-   Primarily focused on text generation and understanding tasks.

## Guidelines

-   **Authentication**: An OpenRouter API key is required. You will be prompted to enter it upon the first use or after running `source_test`.
-   **Model Selection**: When making requests, specify the desired model using the `model` parameter. You can find a list of available models and their identifiers on the OpenRouter website (e.g., `~openai/gpt-latest`, `anthropic/claude-3-opus`, or potentially `openclaw/your-model-name` if "OpenClaw" is available there).
-   **Rate Limits**: Be aware of OpenRouter's rate limits and fair usage policies.
-   **Cost**: Different models have different pricing. Monitor your usage on the OpenRouter platform.

## Examples

### Making a Chat Completion Request

To make a chat completion request, you would typically use a tool that interacts with this API source. Here's a conceptual example of how you might call the API (actual tool call structure may vary slightly depending on how the Craft Agent's internal API client exposes the OpenRouter API):

```python
# Conceptual example - actual tool call will use specific parameters
mcp__openrouter__api_openrouter(
    _displayName="Chat Completion with OpenRouter",
    _intent="Generate a response from an LLM via OpenRouter.",
    path="/chat/completions",
    method="POST",
    params={
        "model": "openclaw/your-model-name", # Replace with the actual OpenClaw model ID if available
        "messages": [
            {"role": "user", "content": "Explain the concept of quantum entanglement in simple terms."}
        ],
        "temperature": 0.7
    }
)
```

**Note**: To use a specific model like "OpenClaw," you need to know its exact model ID on the OpenRouter platform. You can browse the OpenRouter website for a list of available models.

### Listing Available Models

You can check available models using the `GET /models` endpoint (this is also used for source testing):

```python
mcp__openrouter__api_openrouter(
    _displayName="List Available Models",
    _intent="Retrieve a list of all models accessible via OpenRouter API.",
    path="/models",
    method="GET"
)
```
