# /// script
# requires-python = ">=3.10"
# dependencies = ["masonite", "setuptools"]
# ///
from masonite.foundation import Application
from masonite.routes import Route


def hello_world() -> str:
    return "Hello, World!"


def main() -> None:
    app = Application()
    Route.get("/", hello_world)
    app.run()


if __name__ == "__main__":
    main()
