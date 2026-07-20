from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Configuration for the 'core' app.

    'core' holds the site's two public pages (Home, About) and the
    Notice model used to post announcements (e.g. the weekly pool
    tournament) from the admin.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = "Shato Admin"
