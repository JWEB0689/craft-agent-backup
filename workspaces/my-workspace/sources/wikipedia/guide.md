# Wikipedia API

This source provides access to the public MediaWiki API for the English Wikipedia. It can be used to search for articles and retrieve their content.

## No Authentication
This is a public API and does not require authentication.

## Common Actions

### Search for an article
To search for an article, use a `GET` request with `action=query`, `list=search`, and your search term in `srsearch`.

**Example Parameters:**
```json
{
  "action": "query",
  "list": "search",
  "srsearch": "Artifical Intelligence",
  "format": "json"
}
```

### Parse an article's content
To get the rendered HTML content of an article, use `action=parse` with the page title.

**Example Parameters:**
```json
{
  "action": "parse",
  "page": "Artificial_intelligence",
  "format": "json"
}
```
