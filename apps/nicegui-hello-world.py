# /// script
# requires-python = ">=3.10"
# dependencies = ["nicegui"]
# ///
from nicegui import ui


def main():
    ui.label("Hello, World!")
    ui.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
