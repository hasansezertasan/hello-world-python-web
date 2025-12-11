# /// script
# requires-python = ">=3.10"
# dependencies = ["masonite"]
# ///
from masonite.foundation import Application
from masonite.routing import Route


def hello_world():
    return "Hello, World!"


def main():
    import sys
    sys.argv = ["serve", "--port", "8000"]
    app = Application()
    Route.get("/", hello_world)
    app.run()


if __name__ == "__main__":
    main()
