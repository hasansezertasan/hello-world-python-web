# /// script
# requires-python = ">=3.10"
# dependencies = ["quixote"]
# ///
"""Quixote Hello, World! Example.

Quixote is a framework for developing web applications in Python.
"""

from quixote.directory import Directory
from quixote.publish import Publisher
from quixote.server.simple_server import run


class RootDirectory(Directory):
    _q_exports = [""]

    def _q_index(self) -> str:
        return "Hello, World!"


def create_publisher() -> Publisher:
    return Publisher(RootDirectory(), display_exceptions="plain")


def main() -> None:
    run(create_publisher, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
