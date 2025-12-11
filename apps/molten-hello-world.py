# /// script
# requires-python = ">=3.10"
# dependencies = ["molten>=1.0.0", "uvicorn>=0.20.0"]
# ///
"""
Molten Hello World Example

Molten is a modern web framework that combines the best of different frameworks.
"""

from molten import App, Response


def hello_world() -> Response:
    """Handler that returns a simple hello world response."""
    return Response(content="Hello, World!")


# Create the application with routes
app = App(
    handlers=[
        hello_world,
    ]
)


if __name__ == "__main__":
    from molten.servers import gunicorn
    import uvicorn

    # Using uvicorn as ASGI server
    uvicorn.run(app, host="127.0.0.1", port=8000)
