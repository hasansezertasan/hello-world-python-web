import asyncio
from collections.abc import Callable


class ASGIServer:
    def __init__(
        self,
        app: Callable[[dict, Callable, Callable], object],
        host: str = "0.0.0.0",
        port: int = 8000,
    ) -> None:
        self.app = app
        self.host = host
        self.port = port

    async def handle_client(self, reader, writer) -> None:
        """Handle incoming ASGI HTTP requests."""
        request_data = await reader.read(1024)
        if not request_data:
            writer.close()
            return

        # Parse HTTP request
        request_line = request_data.decode().split("\r\n")[0]
        method, path, _ = request_line.split()

        # Create ASGI scope
        scope = {
            "type": "http",
            "asgi": {"version": "3.0"},
            "http_version": "1.1",
            "method": method,
            "scheme": "http",
            "path": path,
            "query_string": b"",
            "root_path": "",
            "headers": [],
            "server": (self.host, self.port),
            "client": writer.get_extra_info("peername"),
        }

        # Response variables
        response_started = False
        status_code = 200
        response_headers = []

        async def send(message: dict) -> None:
            nonlocal response_started, status_code, response_headers
            if message["type"] == "http.response.start":
                response_started = True
                status_code = message["status"]
                response_headers = message.get("headers", [])
            elif message["type"] == "http.response.body":
                if not response_started:
                    return
                body = message.get("body", b"")
                response = f"HTTP/1.1 {status_code} OK\r\nContent-Type: text/plain\r\nContent-Length: {len(body)}\r\n\r\n".encode()
                writer.write(response + body)
                await writer.drain()

        async def receive():
            return {"type": "http.request", "body": request_data, "more_body": False}

        # Call ASGI application
        await self.app(scope, receive, send)
        writer.close()

    async def run(self) -> None:
        """Start the ASGI server."""
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        print(f"ASGI Server running on {self.host}:{self.port}")
        async with server:
            await server.serve_forever()


# Example ASGI application
async def app(scope, receive, send) -> None:
    if scope["type"] == "http":
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [[b"content-type", b"text/plain"]],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": b"Hello, ASGI World!",
            }
        )


if __name__ == "__main__":
    server = ASGIServer(app)
    asyncio.run(server.run())
