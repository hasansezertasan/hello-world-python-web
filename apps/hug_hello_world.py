# /// script
# requires-python = ">=3.10"
# dependencies = ["hug"]
# ///
"""Hug Hello, World! Example.

Hug is a framework for developing APIs with automatic documentation.
"""

from wsgiref.simple_server import make_server

import hug


@hug.get("/")
def hello() -> str:
    return "Hello, World!"


def main() -> None:
    server = make_server("0.0.0.0", 8000, __hug_wsgi__)
    server.serve_forever()


if __name__ == "__main__":
    main()
