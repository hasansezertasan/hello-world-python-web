# /// script
# requires-python = ">=3.10"
# dependencies = ["dash>=3.3.0"]
# ///
import dash
from dash import html

app = dash.Dash(__name__, url_base_pathname="/dashboard/")
app.layout = html.H1("Hello, World!")


@app.server.route("/")
def index() -> str:
    return "Hello, World!"


def main() -> None:
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
