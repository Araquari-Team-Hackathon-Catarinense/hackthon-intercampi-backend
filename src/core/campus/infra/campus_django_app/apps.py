from django.apps import AppConfig


class CampusAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.campus.infra.campus_django_app"

    def ready(self):
        import core.campus.infra.campus_django_app.signals
