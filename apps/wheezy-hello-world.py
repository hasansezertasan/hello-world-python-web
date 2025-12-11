# /// script
# requires-python = ">=3.10"
# dependencies = ["wheezy.web"]
# ///
"""
Wheezy Hello World Example

Wheezy is a lightweight web framework with a focus on performance.
"""

from wheezy.http import HTTPResponse
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.server import WSGIServer


class HelloWorldHandler(BaseHandler):
    def get(self):
        return HTTPResponse(b"Hello, World!")


# URL routing
all_urls = [
    url(r"^$", HelloWorldHandler),
]


# Application factory
def make_app():
    return bootstrap_defaults(all_urls=all_urls)


if __name__ == "__main__":
    app = make_app()
    server = WSGIServer(app, host="127.0.0.1", port=8000)
    print("Server running on http://127.0.0.1:8000")
    server.serve()
