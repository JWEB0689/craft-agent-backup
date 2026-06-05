# Alpaca Markets API

This source provides access to the Alpaca Markets REST API (https://api.alpaca.markets/).

## Scope

- Account endpoints (`/v2/account`)
- Orders (`/v2/orders`) - placement/modification requires explicit user consent (mutations are blocked in Explore mode by default)
- Positions (`/v2/positions`)
- Assets (`/v2/assets`)
- Market data endpoints (`/v2/stocks/...`) depending on your account

## Authentication

Alpaca uses two header keys for authentication:
- `APCA-API-KEY-ID`
- `APCA-API-SECRET-KEY`

I will prompt you to enter both keys securely. After you provide them I will validate by calling `GET /v2/account`.

## Guidelines

- In Explore (read-only) mode, only GET endpoints will be allowed by default. Any trading actions (POST/DELETE/PATCH) are treated as destructive and will be blocked until you explicitly allow them.
- Be careful when placing orders — only do so after reviewing the exact request body and confirming.

## Examples

- Get account info (test endpoint):

  ```json
  { "method": "GET", "path": "account" }
  ```

- List open orders (requires auth):

  ```json
  { "method": "GET", "path": "orders" }
  ```

- Place an order (mutates state — not allowed in Explore mode):

  ```json
  { "method": "POST", "path": "orders", "body": { "symbol": "AAPL", "qty": 1, "side": "buy", "type": "market", "time_in_force": "day" } }
  ```

