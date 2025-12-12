# /// script
# requires-python = ">=3.10"
# dependencies = ["molten>=1.0.0"]
# ///
"""Molten Hello World Example.

Molten is a modern web framework that combines the best of different frameworks.
"""

from molten import App, Route


def root() -> str:
    return "Hello, World!"


app = App(routes=[Route("/", root)])


if __name__ == "__main__":
    app.start()
