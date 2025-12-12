# /// script
# requires-python = ">=3.10"
# dependencies = ["robyn>=0.5.2"]
# ///
from robyn import Robyn

app = Robyn(__file__)


@app.get("/")
def hello_world() -> str:
    return "Hello, World!"


if __name__ == "__main__":
    app.start(port=8000)
