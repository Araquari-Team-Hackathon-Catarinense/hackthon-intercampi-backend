from django.apps import AppConfig


class CreditDjangoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.credit.infra.credit_django_app'

    def ready(self):
        import core.credit.infra.credit_django_app.signal