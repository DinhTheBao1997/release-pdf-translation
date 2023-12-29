from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
env = environ.Env()
DEBUG = env.bool("DJANGO_DEBUG", False)
# Allowed Hosts Definition
if DEBUG:
    # If Debug is True, allow all.
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['example.com'])
SECRET_KEY = env('DJANGO_SECRET_KEY')
# Databases
# DATABASES = {
#     "default": env.db("DATABASE_URL")
# }
# DATABASES["default"]["ATOMIC_REQUESTS"] = True
# DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {  # 'catch all' loggers by referencing it with the empty string
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
