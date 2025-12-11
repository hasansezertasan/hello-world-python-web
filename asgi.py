"""ASGI Hello World Example.

Run with:
    - Daphne: `uvx daphne --bind 127.0.0.1 --port 8000 asgi:app`
    - Uvicorn: `uvx uvicorn --host 127.0.0.1 --port 8000 asgi:app`
    - Granian: `uvx granian --host 127.0.0.1 --port 8000 asgi:app`
    - Hypercorn: `uvx hypercorn asgi:app`
"""


async def app(scope, receive, send) -> None:
    """
    Simple ASGI application that returns "Hello, World!"
    """
    if scope["type"] != "http":
        raise Exception("Only the HTTP protocol is supported")
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
