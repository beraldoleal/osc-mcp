# OSC MCP Server Demo

## What?

Exposes OSC debugging tools via the MCP protocol.

Intended for use with clients like Cursor, VSCode,
or Vim that mediate between LLMs (e.g., local
Ollama) and tool endpoints.

This is just an experimental demonstration of a MCP
server talking with Openshift clusters to debug the 
Openshift Sandboxed Containers operator using LLM.

## Installing

Create and activate the env:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install with:

```bash
uv pip install -e .
```

## Starting the server

To start the server manually, run the following command:

```bash
python -m oscd.server -t sse
```

Then, point your MCP client to:

```
http://localhost:8000/sse
```
