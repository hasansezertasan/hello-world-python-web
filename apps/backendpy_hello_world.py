# /// script
# requires-python = ">=3.10"
# dependencies = ["backendpy", "uvicorn"]
# ///
import uvicorn
from backendpy import Backendpy
from backendpy.router import Routes

app = Backendpy()
routes = Routes()


@routes.get("/")
async def hello(request):
    return "Hello, World!"


app.routes = routes


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
