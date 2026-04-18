"""ASGI Hello, World! Example.

Run with:
    - Uvicorn: `uvx uvicorn --host 0.0.0.0 --port 8000 asgi:app`
    - Daphne: `uvx daphne --bind 0.0.0.0 --port 8000 asgi:app`
    - Granian: `uvx granian --host 0.0.0.0 --port 8000 asgi:app`
    - Hypercorn: `uvx hypercorn asgi:app`
"""


async def app(scope, receive, send) -> None:
    """Simple ASGI application that returns "Hello, World!"."""
    if scope["type"] != "http":
        msg = "Only the HTTP protocol is supported"
        raise Exception(msg)
    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"text/plain"]],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": b"Hello, World!",
        }
    )
