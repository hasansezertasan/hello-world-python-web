# /// script
# requires-python = ">=3.10"
# dependencies = ["circuits", "legacy-cgi"]
# ///
from circuits.web import Controller, Server


class Root(Controller):
    def index(self):
        return "Hello, World!"


def main() -> None:
    (Server(("0.0.0.0", 8000)) + Root()).run()


if __name__ == "__main__":
    main()
