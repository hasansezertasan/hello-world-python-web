# /// script
# requires-python = ">=3.10"
# dependencies = ["piccolo>=1.0.0", "uvicorn>=0.20.0"]
# ///
"""Piccolo Hello World Example.

Piccolo is a modern async ORM with web capabilities.
"""

from piccolo.web.app import App


# Simple handler
async def hello_world(request) -> str:
    """Handler that returns a simple hello world response."""
    return "Hello, World!"


# Create the web app
app = App(
    routes=[
        {"path": "/", "handler": hello_world},
    ],
)


if __name__ == "__main__":
    import uvicorn

    # Using uvicorn to run the app
    uvicorn.run(app, host="127.0.0.1", port=8000)
