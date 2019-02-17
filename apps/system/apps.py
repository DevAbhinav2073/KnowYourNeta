from django.apps import AppConfig


class SystemConfig(AppConfig):
    name = 'apps.system'

    def ready(self):
        import apps.system.signals