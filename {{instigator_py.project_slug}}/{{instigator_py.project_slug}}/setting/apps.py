from django.apps import AppConfig


class SettingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ instigator_py.project_slug }}.setting'
