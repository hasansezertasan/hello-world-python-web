# /// script
# requires-python = ">=3.10"
# dependencies = ["hug>=2.6.1"]
# ///
import hug


@hug.get("/")
def hello_world() -> str:
    return "Hello, World!"


def main() -> None:
    hug.run(port=8000)


if __name__ == "__main__":
    main()
