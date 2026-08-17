# /// script
# requires-python = ">=3.10"
# dependencies = ["sanic>=24.12.0"]
# ///
"""Sanic Hello, World! Example.

Sanic is a Python web framework built for fast HTTP responses.
"""

from sanic import Sanic, response

app = Sanic("hello_world")


@app.route("/")
async def root(request) -> response.HTTPResponse:
    return response.text("Hello, World!")


def main() -> None:
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
