#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys


def main() -> None:
    """Run administrative tasks."""
    import environ

    root_dir = environ.Path(__file__) - 1
    # Take environment variables from .env file
    environ.Env.read_env(root_dir(".env"))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
