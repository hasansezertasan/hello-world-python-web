# /// script
# requires-python = ">=3.10"
# dependencies = ["TurboGears2"]
# ///
from wsgiref.simple_server import make_server

from tg import AppConfig, TGController, expose


class MyController(TGController):
    @expose()
    def index(self):
        return "Hello, World!"


config = AppConfig(minimal=True, root_controller=MyController())
application = config.make_wsgi_app()


def main() -> None:
    server = make_server("0.0.0.0", 8000, application)
    server.serve_forever()


if __name__ == "__main__":
    main()
