# /// script
# requires-python = ">=3.10"
# dependencies = ["wheezy.web"]
# ///
from wsgiref.simple_server import make_server

from wheezy.http import HTTPResponse, WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults, path_routing_middleware_factory


class HelloHandler(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write("Hello, World!")
        return response


all_urls = [
    url("", HelloHandler, name="home"),
]

app = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory,
    ],
    options={
        "render_template": lambda *args, **kwargs: "",
        "ticket": None,
    },
)


def main() -> None:
    server = make_server("0.0.0.0", 8000, app)
    server.serve_forever()


if __name__ == "__main__":
    main()
