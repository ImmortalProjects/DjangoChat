# my_new_app/apps.py
from django.apps import AppConfig


class MyNewAppConfig(AppConfig):
    name = 'mysite'
    verbose_name = "My Brand New Application"


# my_new_app/__init__.py
default_app_config = 'my_new_app.apps.MyNewAppConfig'
