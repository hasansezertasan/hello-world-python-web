# /// script
# requires-python = ">=3.10"
# dependencies = ["robyn>=0.5.2"]
# ///
from robyn import Robyn

app = Robyn()


@app.get("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.start(port=8000)
