# /// script
# requires-python = ">=3.7"
# dependencies = ["klein>=23.12.0"]
# ///
from klein import Klein

app = Klein()


@app.route("/")
def root(request) -> str:
    return "Hello, World!"


def main() -> None:
    app.run("0.0.0.0", 8000)


if __name__ == "__main__":
    main()
