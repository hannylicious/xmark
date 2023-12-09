"""Local settings for xmark project."""

from xmark.settings.base import *  # noqa: F403, F401

###
# Overwrite base settings with specific local settings
###

###
# EMAIL
###
# Setup local email backend so emails don't get sent during development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

###
# REMOTE BACKEND
###
ALLOW_REMOTE_USER_BACKEND = env.bool(
    "ALLOW_REMOTE_USER_BACKEND", default=False
)
if ALLOW_REMOTE_USER_BACKEND:
    AUTHENTICATION_BACKENDS += [
        "django.contrib.auth.backends.RemoteUserBackend",
    ]

###
# DJANGO EXTENSIONS
###
DJANGO_EXTENSIONS = env.bool("DJANGO_EXTENSIONS", default=False)
if DJANGO_EXTENSIONS:
    INSTALLED_APPS += ["django_extensions"]

###
# DJANGO DEBUG TOOLBAR
###
DJANGO_DEBUG_TOOLBAR = env.bool("DJANGO_DEBUG_TOOLBAR", default=False)
if DJANGO_DEBUG_TOOLBAR:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    # DEBUG_TOOLBAR_CONFIG = {
    #     "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    # }
    # INTERNAL_IPS = env.list(
    #     "DJANGO_DEBUG_TOOLBAR_INTERNAL_IPS", default=["127.0.0.1"]
    # )

###
# LOGGING
###
