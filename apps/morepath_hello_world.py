# /// script
# requires-python = ">=3.10"
# dependencies = ["morepath>=0.19.0"]
# ///
"""Morepath Hello, World! Example.

Morepath is a web microframework with elegant routing.
"""

import morepath


class App(morepath.App):
    pass


@App.path(path="")
class Root:
    pass


@App.view(model=Root)
def root(self, request) -> str:
    return "Hello, World!"


def main() -> None:
    morepath.run(App(), host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
