"""WSGI Hello, World! Example.

Run with:
    - Gunicorn: `uvx gunicorn wsgi:app`
    - Waitress: `uvx --from waitress waitress-serve --port 8000 wsgi:app`
    - uwsgi: `uvx uwsgi --http 0.0.0.0:8000 --master -p 4 -w wsgi:app`
    - Werkzeug: `uv run --with werkzeug python -c "from werkzeug.serving import run_simple; from wsgi import app; run_simple('0.0.0.0', 8000, app)"`
"""


def app(environ, start_response) -> list[bytes]:
    """Simple WSGI application that returns "Hello, World!"."""
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]
