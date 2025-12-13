# /// script
# requires-python = ">=3.10"
# dependencies = ["starlette>=0.41.3", "uvicorn>=0.38.0"]
# ///
import uvicorn
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def root(request):
    return PlainTextResponse("Hello, World!")


app = Starlette(routes=[Route("/", root)])


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
