# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args) -> None:
        pass


def main() -> None:
    server = HTTPServer(("0.0.0.0", 8000), HelloHandler)
    print("Server running on http://0.0.0.0:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
