"""
Production settings for the Shato Sports Bar project.

Written for cPanel shared hosting via Phusion Passenger, where the
app server just imports `application` from wsgi.py / passenger_wsgi.py
— there's no separate `gunicorn` process to point at a settings
module, so this file is selected directly by import (see wsgi.py).

SECRET_KEY and ALLOWED_HOSTS are still required from the environment —
if they're missing, decouple raises an error at startup rather than
silently falling back to something insecure. Everything else has a
sane shared-hosting default.
"""

from decouple import config

from .base import *  # noqa: F401,F403
from .base import BASE_DIR, env_list

# -----------------------------------------------------------------------
# SECURITY
# -----------------------------------------------------------------------
DEBUG = False

# No default here on purpose: production must explicitly list its hosts,
# e.g. shatosportsbar.com,www.shatosportsbar.com
ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS")

CSRF_TRUSTED_ORIGINS = env_list("DJANGO_CSRF_TRUSTED_ORIGINS")

# cPanel/Apache terminates SSL and proxies to Passenger. Whether it sets
# X-Forwarded-Proto depends on the host's config, so this defaults to
# OFF to avoid a redirect loop — turn it on in .env once you've
# confirmed (via a test request) that the header is being forwarded.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = config("DJANGO_SECURE_SSL_REDIRECT", default=False, cast=bool)
SESSION_COOKIE_SECURE = config("DJANGO_SECURE_SSL_REDIRECT", default=False, cast=bool)
CSRF_COOKIE_SECURE = config("DJANGO_SECURE_SSL_REDIRECT", default=False, cast=bool)

SECURE_HSTS_SECONDS = config("DJANGO_SECURE_HSTS_SECONDS", default=0, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = SECURE_HSTS_SECONDS > 0
SECURE_HSTS_PRELOAD = SECURE_HSTS_SECONDS > 0

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"


# -----------------------------------------------------------------------
# DATABASE
# -----------------------------------------------------------------------
# SQLite is fine here too — a small single-location site on shared
# hosting doesn't need Postgres. Just make sure the db file lives
# outside your public_html docroot and is writable by the hosting
# account's user (see the deployment note in .env.example).
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# -----------------------------------------------------------------------
# EMAIL
# -----------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST", default="")
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="no-reply@shatosportsbar.com")


# -----------------------------------------------------------------------
# LOGGING
# -----------------------------------------------------------------------
# Send warnings and errors to stdout/stderr so a process manager
# (systemd, Docker, a PaaS) can capture and aggregate them.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
