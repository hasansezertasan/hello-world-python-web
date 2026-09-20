# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "tremolo",
# ]
# ///
"""Tremolo Hello, World! Example.

Tremolo is a lightweight and fast async HTTP server framework.
"""

from tremolo import Application

app = Application()


@app.route("/")
async def root(**server) -> str:
    return "Hello, World!"


def main() -> None:
    app.run("0.0.0.0", 8000, debug=True)


if __name__ == "__main__":
    main()
