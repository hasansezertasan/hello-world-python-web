import socket


def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, WSGI World!"]


def run(app, host="127.0.0.1", port=8000) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    print(f"WSGI Server running on {host}:{port}")

    while True:
        client, _addr = sock.accept()
        data = client.recv(1024).decode()
        environ = {
            "REQUEST_METHOD": data.split()[0],
            "PATH_INFO": data.split()[1],
            "SERVER_NAME": host,
            "SERVER_PORT": str(port),
            "wsgi.version": (1, 0),
            "wsgi.url_scheme": "http",
            "wsgi.input": None,
            "wsgi.errors": None,
            "wsgi.multithread": False,
        }

        response_data = []

        def start_response(status, headers) -> None:
            response = f"HTTP/1.1 {status}\r\n"
            for name, value in headers:
                response += f"{name}: {value}\r\n"
            response += "\r\n"
            response_data.append(response.encode())

        app_iter = app(environ, start_response)
        response_data.extend(app_iter)
        client.send(b"".join(response_data))
        client.close()


if __name__ == "__main__":
    run(app)
