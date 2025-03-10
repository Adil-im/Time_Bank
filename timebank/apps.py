from django.apps import AppConfig


class TimebankConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "timebank"

    def ready(self):
        # Import your models here to ensure they're registered
        from . import models