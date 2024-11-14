from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "{{ instigator_py.project_slug }}.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import {{ instigator_py.project_slug }}.users.signals  # noqa: F401
        except ImportError:
            pass
