# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Socket Server.

Try out:

```sh
curl -v http://localhost:8000/hello -d 'Hello World!'
```
"""
import socket

RESPONSE = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain; charset=utf-8\r\n"
    "Content-Length: 12\r\n"
    "\r\n"
    "Hello World!"
)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # So you can restart quickly without "Address already in use"
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind(("localhost", 8000))
        s.listen(1)
        print("Server listening on port 8000...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            # Read the incoming request (not strictly needed, but nice to see)
            request = conn.recv(4096)
            print("Received request:")
            print(request.decode(errors="ignore"))

            # Send HTTP response
            conn.sendall(RESPONSE.encode("utf-8"))

if __name__ == "__main__":
    main()
