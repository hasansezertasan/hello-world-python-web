# /// script
# requires-python = ">=3.10"
# dependencies = ["twisted>=25.5.0"]
# ///
from twisted.internet import endpoints, reactor
from twisted.web import resource, server


class HelloResource(resource.Resource):
    isLeaf = True

    def render_GET(self, request) -> bytes:
        request.setHeader(b"content-type", b"text/plain")
        return b"Hello, World!"


def main() -> None:
    site = server.Site(HelloResource())
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8000, interface="0.0.0.0")
    endpoint.listen(site)
    reactor.run()


if __name__ == "__main__":
    main()
