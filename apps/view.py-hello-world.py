# /// script
# requires-python = ">=3.10"
# dependencies = ["view.py"]
# ///
from view import View


class HelloWorld(View):
    def get(self):
        return "Hello, World!"


def main():
    app = View()
    app.add_route("/", HelloWorld)
    app.run(port=8000)


if __name__ == "__main__":
    main()
