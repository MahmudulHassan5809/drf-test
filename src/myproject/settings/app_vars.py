import os

from django.conf import settings

# AUTH_USER_MODEL = 'accounts.User' # needed when we want a custom user model
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Dhaka"
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_ROOT = os.path.join(settings.BASE_DIR, "static")
STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DATABASE ENV
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = int(os.environ.get("DB_PORT"))


# REDIS & RABBITMQ ENV
# In this project we dont need RABBITMQ
# REDIS_HOST = os.environ.get('REDIS_HOST')
# RABBITMQ_URL = os.environ.get('RABBITMQ_URL')
# REQUEST_TIMEOUT = int(os.environ.get('REQUEST_TIMEOUT', 8))

# EMAIL ENV
# In this project we dont need EMAIL SERVER
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_PORT = os.environ.get('EMAIL_PORT')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# FROM_EMAIL = os.environ.get('FROM_EMAIL')


# PROJECT
PROJECT_TITLE = os.environ.get("PROJECT_TITLE")
PROJECT_VERSION = os.environ.get("PROJECT_VERSION")
ENVIRONMENT = os.environ.get("ENVIRONMENT")
