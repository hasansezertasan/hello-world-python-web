# /// script
# requires-python = ">=3.10"
# dependencies = ["quart"]
# ///
from quart import Quart

app = Quart(__name__)


@app.route("/")
async def hello_world():
    return "Hello, World!"


def main():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
