"""
Django base settings for the Shato Sports Bar project.

This file holds everything that is identical across environments.
`dev.py` and `prod.py` both start with `from .base import *` and then
override only what needs to differ (DEBUG, ALLOWED_HOSTS, database,
security headers, etc.).

This project is intentionally small: two public pages (Home, About),
a Notice model editable from a branded admin, and HTMX used to
refresh the "notices" section without a full page reload.
"""

from pathlib import Path

from decouple import Csv, config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# base.py lives in shato/settings/, so BASE_DIR is two levels up.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# -----------------------------------------------------------------------
# SECURITY
# -----------------------------------------------------------------------
# SECRET_KEY has no default: if it's missing from the environment,
# decouple raises an error immediately instead of falling back to an
# insecure placeholder. Set it in your .env file (see .env.example).
SECRET_KEY = config("DJANGO_SECRET_KEY")

# DEBUG and ALLOWED_HOSTS are deliberately NOT set here — they differ
# per environment and are defined in dev.py / prod.py instead.


# -----------------------------------------------------------------------
# APPLICATIONS
# -----------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",  # required for {% static %} + STATICFILES_DIRS
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "shato.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # project-level templates (incl. admin overrides)
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "shato.wsgi.application"


# -----------------------------------------------------------------------
# PASSWORD VALIDATION
# -----------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# -----------------------------------------------------------------------
# INTERNATIONALIZATION
# -----------------------------------------------------------------------
LANGUAGE_CODE = "en-us"

# Shato Sports Bar is in Mvurwi, Zimbabwe (Africa/Harare timezone).
# Overridable via env in case a staging server runs in another region.
TIME_ZONE = config("DJANGO_TIME_ZONE", default="Africa/Harare")

USE_I18N = True
USE_TZ = True


# -----------------------------------------------------------------------
# STATIC FILES (CSS, JavaScript, images)
# -----------------------------------------------------------------------
STATIC_URL = "/static/"

# Where Django looks for static files in development.
STATICFILES_DIRS = [BASE_DIR / "static"]

# Where `collectstatic` gathers everything for production (DEBUG=False).
STATIC_ROOT = BASE_DIR / "staticfiles"

# -----------------------------------------------------------------------
# MEDIA FILES (user uploads, e.g. notice/tournament flyers)
# -----------------------------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# -----------------------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -----------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# -----------------------------------------------------------------------
# Shared helper used by dev.py / prod.py
# -----------------------------------------------------------------------
# Exposed here so both subclasses can build ALLOWED_HOSTS / CSRF_TRUSTED_ORIGINS
# from the same env-parsing utility without re-importing decouple everywhere.
def env_list(key, default=""):
    return config(key, default=default, cast=Csv())
