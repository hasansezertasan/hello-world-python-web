# /// script
# requires-python = ">=3.10"
# dependencies = ["quart"]
# ///
"""Quart Hello, World! Example.

Quart is an async Python web framework with Flask-compatible API.
"""

from quart import Quart

app = Quart(__name__)


@app.route("/")
async def root() -> str:
    return "Hello, World!"


def main() -> None:
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
