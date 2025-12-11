# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
import socket


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8000))
    server_socket.listen(1)
    print("Server listening on port 8000...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
            client_socket.send(response)
            client_socket.close()
    except KeyboardInterrupt:
        print("Server stopped")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
