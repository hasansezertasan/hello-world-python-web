# /// script
# requires-python = ">=3.10"
# dependencies = ["webapp2"]
# ///
import webapp2


class HelloWorld(webapp2.RequestHandler):
    def get(self) -> None:
        self.response.write("Hello, World!")


app = webapp2.WSGIApplication([("/?", HelloWorld)])


def main() -> None:
    from wsgiref import simple_server

    httpd = simple_server.make_server("", 8000, app)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
