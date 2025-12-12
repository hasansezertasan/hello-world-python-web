# /// script
# requires-python = ">=3.10"
# dependencies = ["fastapi[all]>=0.121.2"]
# ///
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world() -> str:
    return "Hello, World!"


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
