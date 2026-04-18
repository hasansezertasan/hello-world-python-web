# /// script
# requires-python = ">=3.10"
# dependencies = ["emmett>=2.7.1", "granian>=2.5.0"]
# ///
from emmett import App
from granian import Granian

app = App(__name__)


@app.route("/")
async def root() -> str:
    return "Hello, World!"


def main() -> None:
    server = Granian(
        f"{__name__}:app",
        address="0.0.0.0",
        port=8000,
        interface="asgi",
    )
    server.serve()


if __name__ == "__main__":
    main()
