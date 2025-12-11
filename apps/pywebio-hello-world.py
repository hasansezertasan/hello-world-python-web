# /// script
# requires-python = ">=3.10"
# dependencies = ["pywebio"]
# ///
from pywebio.output import put_text
from pywebio import start_server


def hello_world():
    put_text("Hello, World!")


def main():
    start_server(hello_world, port=8000)


if __name__ == "__main__":
    main()
