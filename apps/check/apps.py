from django.apps import AppConfig


class CheckConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.check'

    def ready(self):
        import apps.check.signal