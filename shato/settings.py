"""
Django settings for the Shato Sports Bar project.

This project is intentionally small: two public pages (Home, About),
a Notice model editable from a branded admin, and HTMX used to
refresh the "notices" section without a full page reload.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------------------------------------------------------
# SECURITY
# -----------------------------------------------------------------------
# NOTE: Replace SECRET_KEY with a unique value (and load it from an
# environment variable) before deploying to production.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-CHANGE-ME-before-deploying",
)

# NOTE: Set this to False in production, and set ALLOWED_HOSTS below.
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


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
# DATABASE
# -----------------------------------------------------------------------
# SQLite is fine for a small single-location site. Swap for Postgres in
# production by changing this dict (e.g. via dj-database-url).
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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
TIME_ZONE = "Africa/Harare"

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
