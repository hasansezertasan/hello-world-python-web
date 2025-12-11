# /// script
# requires-python = ">=3.10"
# dependencies = ["tornado>=6.4.1"]
# ///
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")


def main():
    app = tornado.web.Application([(r"/", MainHandler)])
    app.listen(8000)
    print("Server started on port 8000")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
