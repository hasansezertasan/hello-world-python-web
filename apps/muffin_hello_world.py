# /// script
# requires-python = ">=3.10"
# dependencies = ["muffin>=0.102.3", "uvicorn>=0.34.0"]
# ///
import uvicorn
import muffin

app = muffin.Application()


@app.route("/")
async def root(request) -> str:
    return "Hello, World!"


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
