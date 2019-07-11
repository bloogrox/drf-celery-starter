import os
from .base import *  # noqa


DEBUG = False

SECRET_KEY = os.environ['DJ_SECRET_KEY']
