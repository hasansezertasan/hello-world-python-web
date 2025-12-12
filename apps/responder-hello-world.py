# /// script
# requires-python = ">=3.10"
# dependencies = ["responder>=0.10.1"]
# ///
import responder

api = responder.API()


@api.route("/")
async def hello_world(req, resp) -> None:
    resp.text = "Hello, World!"


def main() -> None:
    api.run(port=8000)


if __name__ == "__main__":
    main()
