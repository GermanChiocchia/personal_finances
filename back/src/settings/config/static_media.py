import os
from .dir import *


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'uploads')
