# Web MCP Server

Small MCP server to search web content and get the content of web pages.

## Features
- Search web content using a search engine. Currently supports Google Custom Search Engine. Documentation: https://developers.google.com/custom-search/docs/overview
- Get the content of a web page using the URL. This is using [MarkItDown](https://github.com/microsoft/markitdown).

## Run the server for local development

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. uv sync
3. uv run mcp dev main.py

## Run the server with SSE

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. uv sync
3. Replace line 15 with line 16 in `main.py`
4. Uncomment the `sse` lines 68 and 69 in `main.py`
5. uv run main.py

### Test SSE MCP Server in VS Code

To test the SSE MCP server, you can test it with GitHub Copilot by adding this configuration to `/.vscode/mcp.json`:

```json
{
  "servers": {
    "<server-name>": {
      "type": "sse",
      "url": "http://localhost:3000/sse"
    }
  }
}
```

Now you need to go in the GitHub Copilot chat, select agent. If there is an error, click on it and select to start the server. You should see the server starting in the terminal and the tools of Web MCP Server should be available in the chat.
