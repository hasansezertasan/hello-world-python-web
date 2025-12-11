"""WSGI Hello World Example.

Run with:
    - Gunicorn: `uvx gunicorn wsgi:app`
    - Waitress: `uvx --from waitress waitress-serve --port 8000 wsgi:app`
    - Werkzeug: `uv run --with werkzeug python -c "from werkzeug.serving import run_simple; from wsgi import app; run_simple('localhost', 8000, app)"`
"""


def app(environ, start_response):
    """
    Simple WSGI application that returns "Hello, World!"
    """
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]
