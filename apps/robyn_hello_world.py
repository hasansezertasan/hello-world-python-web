# /// script
# requires-python = ">=3.10"
# dependencies = ["robyn>=0.5.2"]
# ///
"""Robyn Hello, World! Example.

Robyn is a fast async Python web framework with a Rust runtime.
"""

from robyn import Robyn

app = Robyn(__file__)


@app.get("/")
def root() -> str:
    return "Hello, World!"


def main() -> None:
    app.start(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
