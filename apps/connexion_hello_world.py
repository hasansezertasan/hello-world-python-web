# /// script
# requires-python = ">=3.10"
# dependencies = ["connexion[uvicorn]>=3.3.0", "pyyaml>=6.0"]
# ///
import connexion

OPENAPI_SPEC = {
    "openapi": "3.0.0",
    "info": {"title": "Hello", "version": "0.0.1"},
    "paths": {
        "/": {
            "get": {
                "operationId": "apps.connexion_hello_world.root",
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


app = connexion.AsyncApp(__name__)
app.add_api(OPENAPI_SPEC)


def main() -> None:
    app.run("apps.connexion_hello_world:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
