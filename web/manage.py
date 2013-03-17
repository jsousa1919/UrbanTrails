#!/usr/bin/env python
import os
import sys

SYS_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))

sys.path += [
    os.path.abspath(os.path.join(SYS_ROOT, 'src')),
]

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
