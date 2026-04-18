# /// script
# requires-python = ">=3.10"
# dependencies = ["granian>=1.7.3"]
# ///
from granian import Granian


async def app(scope, protocol):
    if scope.proto != "http":
        msg = "Only the HTTP protocol is supported"
        raise Exception(msg)
    protocol.response_str(
        status=200,
        headers=[("content-type", "text/plain")],
        body="Hello, World!",
    )


def main() -> None:
    server = Granian(
        f"{__name__}:app",
        address="0.0.0.0",
        port=8000,
        interface="rsgi",
    )
    server.serve()


if __name__ == "__main__":
    main()
