# /// script
# requires-python = ">=3.10"
# dependencies = ["cherrypy>=18.10.0"]
# ///
import cherrypy


class HelloWorld:
    @cherrypy.expose
    def index(self) -> str:
        return "Hello, World!"


def main() -> None:
    cherrypy.config.update({
        "server.socket_port": 8000,
        "server.socket_host": "0.0.0.0",
    })
    cherrypy.quickstart(HelloWorld())


if __name__ == "__main__":
    main()
