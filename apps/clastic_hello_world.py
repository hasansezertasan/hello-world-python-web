# /// script
# requires-python = ">=3.10"
# dependencies = ["clastic"]
# ///
from clastic import Application, Response


def root():
    return Response("Hello, World!")


routes = [
    ("/", root, "root"),
]

app = Application(routes)


def main() -> None:
    app.serve(port=8000)


if __name__ == "__main__":
    main()
