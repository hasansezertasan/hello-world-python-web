# /// script
# requires-python = ">=3.10"
# dependencies = ["aiohttp>=3.13.2"]
# ///
from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, world")


def main():
    app = web.Application()
    app.router.add_get("/", hello)
    web.run_app(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
