"""Local test settings for xmark project."""

from xmark.settings.base import *  # noqa: F403, F401

# Set up a global variable to indicate we are running in test mode
TESTING = True

###
# EMAIL
###
# Setup local email backend so emails don't get sent during development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

###
# DATABASE
###
# Use in-memory database for testing
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
# Use the model backend for authentication when testing
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)
