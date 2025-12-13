# Hello World Python Web

Implementing Hello World in different Python Web Application Frameworks / Tools.

The purpose of this project is to provide "Hello World" examples in various Python Web Frameworks / Tools.

## Table of Contents

- [Why](#why)
- [Specification](#specification)
  - [CGI](#cgi)
  - [WSGI](#wsgi)
  - [ASGI](#asgi)
  - [RSGI](#rsgi)
  - [Other](#other)
- [Frameworks](#frameworks)
- [Protocol Servers](#protocol-servers)
- [How to run](#how-to-run)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Why

Learning and comparing different Python web frameworks can be challenging. This project provides a standardized "Hello World" implementation across 50+ different frameworks, making it easy to:

- Compare syntax and structure across frameworks
- Get started quickly with any framework
- Understand the minimal setup required for each framework
- Discover new frameworks and their capabilities

## Specification

### CGI

- Read:
  - [Common Gateway Interface - Wikipedia](https://en.wikipedia.org/wiki/Common_Gateway_Interface)
  - [cgi — Common Gateway Interface support — Python 3.10.19 documentation](https://docs.python.org/3.10/library/cgi.html)
  - [PEP 222 – Web Library Enhancements | peps.python.org](https://peps.python.org/pep-0222/)
  - [wsgiref — WSGI Utilities and Reference Implementation — Python 3.14.2 documentation](https://docs.python.org/3/library/wsgiref.html)

### WSGI

- Read:
  - [Web Server Gateway Interface - Wikipedia](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
  - [What is WSGI? — WSGI.org](https://wsgi.readthedocs.io/en/latest/what.html)
  - [PEP 333 – Python Web Server Gateway Interface v1.0 | peps.python.org](https://peps.python.org/pep-0333/)
  - [PEP 3333 – Python Web Server Gateway Interface v1.0.1 | peps.python.org](https://peps.python.org/pep-3333/)
- Watch:
  - [WSGI for Web Developers (Ryan Wilson-Perkin) - YouTube](https://www.youtube.com/watch?v=WqrCnVAkLIo)

### ASGI

- Read:
  - [Asynchronous Server Gateway Interface - Wikipedia](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
  - [ASGI Documentation — ASGI 3.0 documentation](https://asgi.readthedocs.io/en/latest/)

### RSGI

- Read:
  - [granian/docs/spec/RSGI.md at master · emmett-framework/granian](https://github.com/emmett-framework/granian/blob/master/docs/spec/RSGI.md)

### Other

- Checkout:
  - [abersheeran/a2wsgi: Convert WSGI app to ASGI app or ASGI app to WSGI app.](https://github.com/abersheeran/a2wsgi)
  - [hasansezertasan/a2wsgi-examples: The goal of this project is to provide examples about integrating different Python Web Frameworks and how they can be used together with a2wsgi.](https://github.com/hasansezertasan/a2wsgi-examples)
  - `asgiref.wsgi.WsgiToAsgi` and `asgiref.asgi.AsgiToWsgi`
- Read:
  - [PEP 249 – Python Database API Specification v2.0 | peps.python.org](https://peps.python.org/pep-0249/)

## Frameworks

| Framework                                      | External                                                          | Specification / Format  |
| ---------------------------------------------- | ----------------------------------------------------------------- | ----------------------- |
| [http](./apps/http_hello_world.py)             | [Standard Library](https://docs.python.org/3/library/http.html)   | TCP                     |
| [socket](./apps/socket_hello_world.py)         | [Standard Library](https://docs.python.org/3/library/socket.html) | TCP                     |
| [blacksheep](./apps/blacksheep_hello_world.py) | [Async Web Framework](https://www.blacksheep.dev/)                | ASGI                    |
| [bottle](./apps/bottle_hello_world.py)         | [Micro Framework](https://bottlepy.org/)                          | WSGI                    |
| [cherrypy](./apps/cherrypy_hello_world.py)     | [Object-Oriented Framework](https://docs.cherrypy.dev/)           | WSGI                    |
| [django](./apps/django_hello_world.py)         | [Full-Stack Framework](https://www.djangoproject.com/)            | WSGI (has a history)    |
| [fastapi](./apps/fastapi_hello_world.py)       | [Async API Framework](https://fastapi.tiangolo.com/)              | Based on Starlette      |
| [flask](./apps/flask_hello_world.py)           | [Micro Framework](https://flask.palletsprojects.com/)             | Based on Werkzeug       |
| [falcon](./apps/falcon_hello_world.py)         | [REST API Framework](https://falcon.readthedocs.io/)              | ASGI/WSGI               |
| [litestar](./apps/litestar_hello_world.py)     | [Async Web Framework](https://docs.litestar.dev/)                 | ASGI                    |
| [morepath](./apps/morepath_hello_world.py)     | [Microframework](https://morepath.readthedocs.io/)                | WSGI                    |
| [pycnic](./apps/pycnic_hello_world.py)         | [Minimalist API Framework](https://pycnic.nullism.com/)           | WSGI                    |
| [pyramid](./apps/pyramid_hello_world.py)       | [Full-Stack Framework](https://trypyramid.com/)                   | WSGI                    |
| [quart](./apps/quart_hello_world.py)           | [Async Web Framework](https://quart.palletsprojects.com/)         | Based on Flask but ASGI |
| [sanic](./apps/sanic_hello_world.py)           | [Async Web Framework](https://sanic.dev/)                         | ASGI/WSGI               |
| [starlette](./apps/starlette_hello_world.py)   | [Async Web Framework](https://starlette.dev/)                     | ASGI                    |
| [robyn](./apps/robyn_hello_world.py)           | [Rust-powered Framework](https://robyn.tech/)                     | Standalone              |
| [aiohttp](./apps/aiohttp_hello_world.py)       | [Async Web Framework](https://docs.aiohttp.org/)                  | Standalone              |
| [tornado](./apps/tornado_hello_world.py)       | [Async Web Framework](https://www.tornadoweb.org/)                | Standalone              |

## Protocol Servers

These are battle-tested production servers used to deploy your Web Application.

| Project                                                                 | Specification / Format |
| ----------------------------------------------------------------------- | ---------------------- |
| [uvicorn](https://uvicorn.dev/)                                         | ASGI                   |
| [daphne](https://github.com/django/daphne)                              | ASGI                   |
| [hypercorn](https://hypercorn.readthedocs.io)                           | ASGI                   |
| [granian](https://github.com/emmett-framework/granian)                  | ASGI/WSGI/RSGI         |
| [gunicorn](https://gunicorn.org/)                                       | WSGI                   |
| [waitress](https://docs.pylonsproject.org/projects/waitress/en/latest/) | WSGI                   |
| [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/)                   | WSGI                   |
| [werkzeug](https://werkzeug.palletsprojects.com/)                       | WSGI                   |

Why do we need those?

Because the servers provided by the Web Frameworks are generally development servers and usage of these servers in production is discouraged.

- [django-admin and manage.py | Django documentation | Django](https://docs.djangoproject.com/en/dev/ref/django-admin/#runserver)
- [Deploy to Production — Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/tutorial/deploy/#run-with-a-production-server)

<!--
| [hug](./apps/hug_hello_world.py)               | [API Framework](https://www.hug.rest/)                                 | Based on Falcon           |
| [emmett](./apps/emmett_hello_world.py)         | [Full-Stack Framework](https://emmett.sh/)                             | ASGI/WSGI (has a history) |
| [flama](./apps/flama_hello_world.py)           | [REST API Framework](https://flama.dev/)                               | Based on Starlette        |
| [masonite](./apps/masonite_hello_world.py)     | [Full-Stack Framework](https://docs.masoniteproject.com/)              | Based on Werkzeug         |
| [molten](./apps/molten_hello_world.py)         | [Modern Web Framework](https://molten.readthedocs.io/)                 | WSGI                      |
| [piccolo](./apps/piccolo_hello_world.py)       | [Async ORM with Web](https://piccolo.readthedocs.io/)                  | ASGI                      |
| [responder](./apps/responder_hello_world.py)   | [API Framework](https://responder.kennethreitz.org/)                   | Based on Starlette        |
| [view.py](./apps/view_py_hello_world.py)       | [Web Framework](https://view.zintensity.dev/)                          | ASGI                      |
| [webapp2](./apps/webapp2_hello_world.py)       | [Google App Engine](https://webapp2.readthedocs.io/)                   | WSGI                      |
| [webpy](./apps/webpy_hello_world.py)           | [Micro Framework](https://github.com/webpy/webpy)                      | WSGI                      |
| [wheezy](./apps/wheezy_hello_world.py)         | [Lightweight Web Framework](https://github.com/akornatskyy/wheezy.web) | WSGI                      |
| [nanodjango](./apps/nanodjango_hello_world.py) | [Minimal Django](https://nanodjango.readthedocs.io/)                   | Based on Django           |
| [pywebio](./apps/pywebio_hello_world.py)         | [Web I/O Framework](https://pywebio.readthedocs.io/)                 | ASGI                      |
| [plotly-dash](./apps/plotly-dash_hello_world.py) | [Dashboard Framework](https://dash.plotly.com/)                      | WSGI                      |
| [eve](./apps/eve_hello_world.py)               | [REST API Framework](https://python-eve.org/)                          | Based on Flask            |
| [nicegui](./apps/nicegui_hello_world.py)         | [UI Framework](https://nicegui.io/)                                  | ASGI                      |
| [streamlit](./apps/streamlit_hello_world.py)     | [Data App Framework](https://streamlit.io/)                          | Full-Stack                |
| [apistar](./apps/apistar_hello_world.py)         | [Lightweight API Framework](https://github.com/encode/apistar)       | N/A                       |
| [flet](./apps/flet_hello_world.py)               | [UI Framework](https://flet.dev/)                                    | Desktop/Web               |
| [connexion](./apps/connexion_hello_world.py)     | [OpenAPI/Swagger Framework](https://connexion.readthedocs.io/)       | ASGI                      |
| [bleach](./apps/bleach_hello_world.py)           | [Security-focused HTTP Library](https://bleach.readthedocs.io/)      | WSGI                      |
| [reflex](./apps/reflex_hello_world.py)           | [Reactive Framework](https://reflex.dev/)                            | Full-Stack                |
| [gradio](./apps/gradio_hello_world.py)           | [ML Interface Framework](https://www.gradio.app/)                    | ASGI                      |
-->

## How to run

Each framework has its own implementation file in the `apps/` folder. To run any example:

Simply run:

```sh
uv run apps/<framework-name>_hello_world.py
```

Or use the runner script to test all implementations:

```sh
uv run apps/run_all.py
```

The runner script will:

- Execute each hello_world application with `uv run`
- Verify that each app responds with a "Hello, World!" message on port 8000
- Display a summary of successful and failed implementations

If this does not work, please refer to the specific implementation file for more details.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## Author

- [hasansezertasan](https://www.github.com/hasansezertasan), It's me :wave:

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
