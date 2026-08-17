# /// script
# requires-python = ">=3.10"
# dependencies = ["dash"]
# ///
"""Dash Hello, World! Example.

Dash is a framework for building analytical web applications.
"""

import dash
from dash import html

app = dash.Dash(__name__)
app.layout = html.H1("Hello, World!")


def main() -> None:
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
