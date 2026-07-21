"""
Development settings for the Shato Sports Bar project.

Run with:
    DJANGO_SETTINGS_MODULE=shato.settings.dev python manage.py runserver

Or set DJANGO_SETTINGS_MODULE=shato.settings.dev in your .env file so
manage.py picks it up automatically (see .env.example).
"""

from .base import *  # noqa: F401,F403
from .base import BASE_DIR, env_list

# -----------------------------------------------------------------------
# SECURITY (relaxed for local development)
# -----------------------------------------------------------------------
DEBUG = True

ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS", default="127.0.0.1,localhost")


# -----------------------------------------------------------------------
# DATABASE
# -----------------------------------------------------------------------
# SQLite is fine for local development — zero setup required.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# -----------------------------------------------------------------------
# EMAIL
# -----------------------------------------------------------------------
# Print emails to the console instead of sending them for real.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# -----------------------------------------------------------------------
# MISC DEV CONVENIENCES
# -----------------------------------------------------------------------
# Django's default insecure cookie/security settings are fine over plain
# HTTP on localhost, so no HTTPS-related overrides are needed here.
