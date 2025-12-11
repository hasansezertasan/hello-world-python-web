# /// script
# requires-python = ">=3.10"
# dependencies = ["web.py"]
# ///
import web

urls = ("/", "hello")


class hello:
    def GET(self):
        return "Hello, World!"


def main():
    app = web.application(urls, globals())
    app.run(web.config.listen_host, 8000)


if __name__ == "__main__":
    main()
