# /// script
# requires-python = ">=3.10"
# dependencies = ["emmett>=2.7.1"]
# ///
from emmett import App

app = App(__name__)


@app.route("/")
async def main():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)