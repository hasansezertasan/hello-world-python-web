# /// script
# requires-python = ">=3.10"
# dependencies = ["litestar>=2.9.12", "uvicorn>=0.38.0", "sniffio"]
# ///
import uvicorn
from litestar import Litestar, get


@get("/")
def root() -> str:
    return "Hello, World!"


def main() -> None:
    app = Litestar(route_handlers=[root])

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
