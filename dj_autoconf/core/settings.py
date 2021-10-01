import os
import re

from django.conf import settings

BACKEND_URL_PREFIX = 'http://localhost:8000/api/v1/'
CONFIG_FILENAME = 'settings_local.py'
SITE_ROOT = settings.SITE_ROOT
PROJECT_SETTINGS_FILE = os.path.join(SITE_ROOT, 'settings.py')
PATH_TO_SAVE = os.path.join(SITE_ROOT, CONFIG_FILENAME)
IMPORT_COMMAND = 'from .%s import *' % re.sub('\.py$', '', CONFIG_FILENAME)