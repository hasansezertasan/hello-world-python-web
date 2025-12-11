# /// script
# requires-python = ">=3.10"
# dependencies = ["flask>=3.1.2"]
# ///
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


def main():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
