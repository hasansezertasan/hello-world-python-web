# /// script
# requires-python = ">=3.10"
# dependencies = ["hug", "legacy-cgi", "setuptools"]
# ///
import hug
from wsgiref.simple_server import make_server


@hug.get("/")
def hello():
    return "Hello, World!"


def main() -> None:
    server = make_server("0.0.0.0", 8000, __hug_wsgi__)
    server.serve_forever()


if __name__ == "__main__":
    main()
