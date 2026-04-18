# /// script
# requires-python = ">=3.10"
# dependencies = ["emmett>=2.7.1", "uvicorn>=0.34.0"]
# ///
import uvicorn
from emmett import App

app = App(__name__)


@app.route("/")
async def root() -> str:
    return "Hello, World!"


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
