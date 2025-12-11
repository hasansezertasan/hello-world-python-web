# /// script
# requires-python = ">=3.10"
# dependencies = ["hug>=2.6.1"]
# ///
import hug


@hug.get("/")
def hello_world():
    return "Hello, World!"


def main():
    hug.run(port=8000)


if __name__ == "__main__":
    main()
