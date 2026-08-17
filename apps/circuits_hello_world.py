# /// script
# requires-python = ">=3.10"
# dependencies = ["circuits"]
# ///
"""Circuits Hello, World! Example.

Circuits is an event-driven framework with a component architecture.
"""

from circuits.web import Controller, Server


class Root(Controller):
    def index(self) -> str:
        return "Hello, World!"


def main() -> None:
    (Server(8000) + Root()).run()


if __name__ == "__main__":
    main()
