# /// script
# requires-python = ">=3.10"
# dependencies = ["pycnic>=0.1.0"]
# ///
"""Pycnic Hello World Example.

Pycnic is a minimalist, object-oriented REST API framework.
"""

from pycnic.core import WSGI, Handler


class HelloWorldHandler(Handler):
    def get(self):
        return {"message": "Hello, World!"}


# Create the application
class app(WSGI):
    routes = [
        ("/", HelloWorldHandler()),
    ]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    server = make_server("127.0.0.1", 8000, app)
    print("Server running on http://127.0.0.1:8000")
    server.serve_forever()
