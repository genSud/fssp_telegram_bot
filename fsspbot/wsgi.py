"""
WSGI config for fsspbot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""


import os
import sys
import site
#from . import secret
path2 = '/home/fssp_telegram_bot'
path3 = '/home/fssp_telegram_bot/fsspbot'
sys.path.append(path2)
sys.path.append(path3)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fsspbot.settings")

application = get_wsgi_application()
