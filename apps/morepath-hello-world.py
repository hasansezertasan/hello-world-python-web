# /// script
# requires-python = ">=3.10"
# dependencies = ["morepath>=0.19.0"]
# ///
"""
Morepath Hello World Example

Morepath is a web microframework with elegant routing.
"""

from morepath import App


class Root:
    pass


app = App()


@app.view(Root)
def hello_world_view(obj, request):
    """Handler that returns a simple hello world response."""
    return "Hello, World!"


if __name__ == "__main__":
    from morepath.run import run_simple

    app.commit()
    run_simple(app, host="127.0.0.1", port=8000, reloader=True)
