# /// script
# requires-python = ">=3.10"
# dependencies = ["flama>=1.12.1"]
# ///
import uvicorn
from flama import Flama

app = Flama()


@app.route("/")
def hello_world():
    return "Hello, World!"


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
