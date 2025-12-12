# /// script
# requires-python = ">=3.10"
# dependencies = ["nanodjango"]
# ///
from nanodjango import Django

app = Django()


@app.route("/")
def hello_world(request) -> str:
    return "Hello, World!"


if __name__ == "__main__":
    app.run(port=8000)
