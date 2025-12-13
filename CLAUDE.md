# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains "Hello, World!" implementations for 50+ Python web frameworks and tools. The purpose is to provide standardized examples for comparing syntax, structure, and minimal setup across different frameworks.

## Project Structure

The repository is organized around web protocol specifications:

- **WSGI (Web Server Gateway Interface)**: Synchronous specification (PEP 333/3333)
- **ASGI (Asynchronous Server Gateway Interface)**: Async specification
- **RSGI (Rust Server Gateway Interface)**: Granian-specific specification
- **TCP/Socket-based**: Low-level network implementations

### Key Files

- `apps/*_hello_world.py`: Individual framework implementations (20 files)
- `apps/run_all.py`: Test runner that verifies all implementations
- `wsgi.py`: Bare WSGI application callable
- `asgi.py`: Bare ASGI application callable
- `wsgi_server.py`: Custom WSGI server implementation using sockets
- `asgi_server.py`: Custom ASGI server implementation using asyncio

## Running Applications

All applications use PEP 723 inline script metadata for dependency management. Run any framework implementation with:

```sh
uv run apps/<framework-name>_hello_world.py
```

Each app starts on port 8000 and returns "Hello, World!" at the root path.

### Testing All Implementations

```sh
uv run apps/run_all.py
```

This runner:
1. Executes each `*_hello_world.py` file in `apps/`
2. Verifies HTTP 200 response with "Hello, World!" content on port 8000
3. Kills processes occupying port 8000 between tests (uses `lsof` and `kill`)
4. Reports success/failure summary

## Code Conventions

### File Naming

Framework implementations follow the pattern: `apps/<framework>_hello_world.py` (underscores, not hyphens)

### Application Structure

Each `*_hello_world.py` file follows this pattern:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["framework>=version"]
# ///
# Framework-specific imports and setup

def main() -> None:
    # Start server on 0.0.0.0:8000
    pass

if __name__ == "__main__":
    main()
```

Key requirements:
- Function return type annotations must be included
- Host must be `0.0.0.0`
- Port must be `8000`
- Response must contain "Hello, World!"

## Protocol Server Examples

The repository demonstrates running WSGI/ASGI apps with production servers:

### ASGI Servers

```sh
uvx uvicorn --host 0.0.0.0 --port 8000 asgi:app
uvx daphne --bind 0.0.0.0 --port 8000 asgi:app
uvx granian --host 0.0.0.0 --port 8000 asgi:app
uvx hypercorn asgi:app
```

### WSGI Servers

```sh
uvx gunicorn wsgi:app
uvx --from waitress waitress-serve --port 8000 wsgi:app
uvx uwsgi --http 0.0.0.0:8000 --master -p 4 -w wsgi:app
```

## Architecture Notes

### WSGI Implementation Pattern

WSGI apps follow PEP 3333 callable signature:

```python
def app(environ, start_response) -> list[bytes]:
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]
```

### ASGI Implementation Pattern

ASGI apps follow ASGI 3.0 specification:

```python
async def app(scope, receive, send) -> None:
    if scope["type"] == "http":
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"text/plain"]],
        })
        await send({
            "type": "http.response.body",
            "body": b"Hello, World!",
        })
```

### Custom Server Implementations

- `wsgi_server.py`: Demonstrates minimal WSGI server using raw sockets, parsing HTTP manually and building the `environ` dict
- `asgi_server.py`: Demonstrates minimal ASGI server using `asyncio.start_server`, handling scope/receive/send protocol

## Git Workflow

Main branch: `main`
Current working branch: `feat/implementations`

Recent refactoring renamed files from hyphenated to underscored format (e.g., `flask-hello-world.py` → `flask_hello_world.py`).
