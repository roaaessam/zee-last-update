"""
WSGI config for zee project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import sys
sys.path.append('/path/to/your/project')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zee.settings')

application = get_wsgi_application()
