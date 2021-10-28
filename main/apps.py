from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    #overwrite the ready
    #when the app is ready all signals are working
    def ready(self):
        import main.signals