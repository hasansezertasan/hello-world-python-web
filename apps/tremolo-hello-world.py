# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "tremolo",
# ]
# ///

from tremolo import Application

app = Application()


@app.route("/")
async def hello_world(**server) -> str:
    return "Hello, World!"


if __name__ == "__main__":
    app.run("0.0.0.0", 8000, debug=True)
