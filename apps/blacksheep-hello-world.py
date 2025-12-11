# /// script
# requires-python = ">=3.10"
# dependencies = ["blacksheep>=2.4.5", "uvicorn>=0.38.0"]
# ///
import uvicorn
from blacksheep import Application, get

app = Application()


@get("/")
async def home():
    return "Hello, World!"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
