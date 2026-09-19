# /// script
# requires-python = ">=3.10"
# dependencies = ["baize>=0.23.1", "uvicorn>=0.34.0"]
# ///
import uvicorn
from baize.asgi import PlainTextResponse, Router

app = Router(
    ("/", PlainTextResponse("Hello, World!")),
)


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
