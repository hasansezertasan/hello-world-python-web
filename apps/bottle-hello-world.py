# /// script
# requires-python = ">=3.10"
# dependencies = ["bottle>=0.13.4"]
# ///
from bottle import route, run


@route("/")
def index():
    return "Hello World!"


def main():
    run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
