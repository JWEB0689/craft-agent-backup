# YH Finance API (yfapi.net)

This source exposes the YH Finance API (hosted at https://yfapi.net) and is based on the OpenAPI specification you provided. It offers real-time quote data for stocks, ETFs, crypto, and currency pairs.

## Scope

- Real-time quote lookup: `/v6/finance/quote`
- Additional endpoints under `/v6/finance/*` for other market data depending on the provider

## Authentication

- This API uses an API key sent in a request header named `x-api-key`.
- I will prompt you to enter your API key securely the first time the source is tested.

## Guidelines

- By default this source is configured for read-only use (GET requests). Any write or trade-related endpoints (if present) will require explicit confirmation and an appropriate permission change.
- Rate limits may apply. Keep queries small (up to 10 symbols per request) to avoid throttling.

## Examples

- Get quotes for AAPL and BTC:

  ```json
  { "method": "GET", "path": "v6/finance/quote?symbols=AAPL,BTC-USD" }
  ```

- In code the request looks like:

  GET https://yfapi.net/v6/finance/quote?symbols=AAPL,BTC-USD
  Headers:
    x-api-key: <YOUR_API_KEY>

## Notes

- I saved the OpenAPI spec you provided into the source folder as `openapi.json`. If you want me to generate more tailored examples or import additional endpoints from the spec, tell me and I’ll update the guide and permissions accordingly.

- To test the source now, confirm you want me to prompt for the API key and I will run the verification step.