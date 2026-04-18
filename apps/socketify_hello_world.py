# /// script
# requires-python = ">=3.10"
# dependencies = ["socketify>=0.0.31"]
# ///
from socketify import App


def main() -> None:
    app = App()
    app.get("/", lambda res, req: res.end("Hello, World!"))
    app.listen(
        8000,
        lambda config: print("Listening on port http://0.0.0.0:%d" % config.port),
    )
    app.run()


if __name__ == "__main__":
    main()
