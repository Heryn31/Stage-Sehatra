"""
WSGI config for stage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from static_ranges import Ranges
from dj_static import Cling, MediaCling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stage.settings')

# application = get_wsgi_application()
application = Ranges(Cling(MediaCling(get_wsgi_application())))