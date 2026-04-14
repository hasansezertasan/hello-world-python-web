# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = ["lona"]
# ///
from lona import LonaApp, LonaView
from lona.html import H1, HTML

app = LonaApp(__file__)


@app.route("/")
class HelloView(LonaView):
    def handle_request(self, request):
        return HTML(H1("Hello, World!"))


def main() -> None:
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
