# /// script
# requires-python = ">=3.10"
# dependencies = ["starlette>=0.41.3", "uvicorn>=0.38.0"]
# ///
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import uvicorn


async def hello_world(request):
    return PlainTextResponse("Hello, World!")


app = Starlette(routes=[Route("/", hello_world)])


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
