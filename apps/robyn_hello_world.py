# /// script
# requires-python = ">=3.10"
# dependencies = ["robyn>=0.5.2"]
# ///
from robyn import Robyn

app = Robyn(__file__)


@app.get("/")
def root() -> str:
    return "Hello, World!"


def main() -> None:
    app.start(port=8000)


if __name__ == "__main__":
    main()
