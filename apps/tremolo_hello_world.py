# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "tremolo",
# ]
# ///

from tremolo import Application

app = Application()


@app.route("/")
async def root(**server) -> str:
    return "Hello, World!"


def main() -> None:
    app.run("0.0.0.0", 8000, debug=True)


if __name__ == "__main__":
    main()
