# /// script
# requires-python = ">=3.10"
# dependencies = ["pyramid>=2.0.2", "waitress>=3.0.1"]
# ///
from pyramid.config import Configurator
from pyramid.response import Response
from waitress import serve


def hello_world(request):
    return Response("Hello, World!")


def main():
    with Configurator() as config:
        config.add_route("hello", "/")
        config.add_view(hello_world, route_name="hello")
        app = config.make_wsgi_app()
    serve(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
