# /// script
# requires-python = ">=3.10"
# dependencies = ["clastic"]
# ///
"""Clastic Hello, World! Example.

Clastic is a functional Python web framework built on Werkzeug.
"""

from clastic import Application, Response


def root() -> Response:
    """Provide the response used by Clastic's registered root route."""
    return Response("Hello, World!")


routes = [
    ("/", root, "root"),
]

app = Application(routes)


def main() -> None:
    app.serve(port=8000)


if __name__ == "__main__":
    main()
