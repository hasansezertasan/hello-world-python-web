# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = ["lona"]
# ///
"""Lona Hello, World! Example.

Lona is a web application framework for interactive web apps in pure Python.
"""

from lona import LonaApp, LonaView, Route
from lona.responses import Response

app = LonaApp(__file__)


class HelloView(LonaView):
    def handle_request(self, request) -> Response:
        """Use an explicit response for Lona's HTTP pass-through route."""
        return Response(text="Hello, World!", status=200)


app.routes = [
    Route("/", HelloView, http_pass_through=True),
]


def main() -> None:
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
