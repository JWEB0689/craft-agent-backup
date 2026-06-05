import base64
import json

with open(r"C:\Users\Jwebe\.craft-agent\workspaces\my-workspace\sessions\260601-sleek-orchid\long_responses\2026-06-01T16-51-28-219_api_github-api_.txt", "r") as f:
    data = json.load(f)

decoded_content = base64.b64decode(data['content']).decode('utf-8')

with open(r"C:\Users\Jwebe\.craft-agent\workspaces\my-workspace\sessions\260601-sleek-orchid\data\decoded_readme.md", "w", encoding="utf-8") as f:
    f.write(decoded_content)
