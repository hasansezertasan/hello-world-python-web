# /// script
# requires-python = ">=3.10"
# dependencies = ["bottle>=0.13.4"]
# ///
"""Bottle Hello, World! Example.

Bottle is a fast, simple, and lightweight WSGI micro web framework.
"""

from bottle import route, run


@route("/")
def index() -> str:
    return "Hello, World!"


def main() -> None:
    run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
