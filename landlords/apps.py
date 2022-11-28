from django.apps import AppConfig


class LandlordsConfig(AppConfig):
    name = 'landlords'

    def ready(self):
        import landlords.signals