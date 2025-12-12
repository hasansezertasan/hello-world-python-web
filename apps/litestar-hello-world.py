# /// script
# requires-python = ">=3.10"
# dependencies = ["litestar>=2.9.12", "uvicorn>=0.38.0", "sniffio"]
# ///
from litestar import Litestar, get


@get("/")
def hello_world() -> str:
    return "Hello, World!"


def main() -> None:
    app = Litestar(route_handlers=[hello_world])
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
