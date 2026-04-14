# /// script
# requires-python = ">=3.10"
# dependencies = ["ravyn", "uvicorn>=0.38.0"]
# ///
import uvicorn
from ravyn import Gateway, JSONResponse, Ravyn, get


@get("/")
def root() -> JSONResponse:
    return JSONResponse({"message": "Hello, World!"})


def main() -> None:
    app = Ravyn(routes=[Gateway(handler=root)])

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
