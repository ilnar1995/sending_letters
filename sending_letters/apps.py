from django.apps import AppConfig


class SendingLettersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sending_letters'

    def ready(self):
        from . import signals
