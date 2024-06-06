from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientservice'
    verbose_name = 'Сервис управления клиентами'

