# /// script
# requires-python = ">=3.10"
# dependencies = ["connexion[uvicorn]>=3.3.0", "pyyaml>=6.0"]
# ///
import json
import tempfile
from pathlib import Path

import connexion

OPENAPI_SPEC = {
    "openapi": "3.0.0",
    "info": {"title": "Hello", "version": "0.0.1"},
    "paths": {
        "/": {
            "get": {
                "operationId": "connexion_hello_world.root",
                "responses": {
                    "200": {
                        "description": "Hello",
                        "content": {"text/plain": {"schema": {"type": "string"}}},
                    }
                },
            }
        }
    },
}


def root() -> str:
    return "Hello, World!"


spec_dir = Path(tempfile.mkdtemp())
spec_file = spec_dir / "openapi.json"
spec_file.write_text(json.dumps(OPENAPI_SPEC))

app = connexion.AsyncApp(__name__, specification_dir=str(spec_dir))
app.add_api("openapi.json")


def main() -> None:
    app.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
