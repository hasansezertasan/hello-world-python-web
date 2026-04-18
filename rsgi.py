"""RSGI Hello, World! Example.

Run with:
    - Granian: `uvx granian --interface rsgi --host 0.0.0.0 --port 8000 rsgi:app`
"""


async def app(scope, protocol) -> None:
    """Simple RSGI application that returns "Hello, World!"."""
    if scope.proto != "http":
        msg = "Only the HTTP protocol is supported"
        raise Exception(msg)
    protocol.response_str(
        status=200,
        headers=[("content-type", "text/plain")],
        body="Hello, World!",
    )
