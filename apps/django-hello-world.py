# /// script
# requires-python = ">=3.10"
# dependencies = ["django>=5.2.8"]
# ///
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
import django
from django.conf import settings


if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="secret-key-for-development",
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
        ],
        ROOT_URLCONF=__name__,
    )
    django.setup()


def hello_world(request):
    return HttpResponse("Hello, World!")


urlpatterns = [
    path("", hello_world),
]


def main():
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])


if __name__ == "__main__":
    main()
