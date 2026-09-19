# /// script
# requires-python = ">=3.10"
# dependencies = ["responder>=3.6.2"]
# ///
import responder

api = responder.API()


@api.route("/")
def root(req, resp) -> None:
    resp.text = "Hello, World!"


def main() -> None:
    api.run(address="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
