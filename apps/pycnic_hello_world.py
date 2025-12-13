# /// script
# requires-python = ">=3.10"
# dependencies = ["pycnic>=0.1.0"]
# ///
"""Pycnic Hello, World! Example.

Pycnic is a minimalist, object-oriented REST API framework.
"""

from wsgiref.simple_server import make_server

from pycnic.core import WSGI, Handler


class HelloWorldHandler(Handler):
    def get(self):
        return {"message": "Hello, World!"}


# Create the application
class app(WSGI):
    routes = [
        ("/", HelloWorldHandler()),
    ]


def main() -> None:
    server = make_server("0.0.0.0", 8000, app)
    print("Server running on http://0.0.0.0:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
