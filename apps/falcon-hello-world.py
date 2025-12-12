# /// script
# requires-python = ">=3.10"
# dependencies = ["falcon>=4.2.0"]
# ///
import falcon


class HelloWorld:
    def on_get(self, req, resp) -> None:
        resp.text = "Hello, World!"


def main() -> None:
    app = falcon.App()
    app.add_route("/", HelloWorld())
    import wsgiref.simple_server

    httpd = wsgiref.simple_server.make_server("", 8000, app)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
