from .base import *

DEBUG = False
ADMINS = (
('gaskoin', 'dchierntsov@mail.ru'),
)
ALLOWED_HOSTS = ['todo.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'list',
        'USER': 'list',
        'PASSWORD': 'list',
}
}