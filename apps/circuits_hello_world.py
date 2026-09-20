# /// script
# requires-python = ">=3.10"
# dependencies = ["circuits", "legacy-cgi"]
# ///
"""Circuits Hello, World! Example.

Circuits is an event-driven framework with a component architecture.
"""

from circuits.web import Controller, Server


class Root(Controller):
    def index(self) -> str:
        """Provide the controller's default response for the root route."""
        return "Hello, World!"


def main() -> None:
    (Server(("0.0.0.0", 8000)) + Root()).run()


if __name__ == "__main__":
    main()
