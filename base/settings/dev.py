from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = "django-insecure-4hb2=u$am_x+o^c)l%=6j5v49*+0_y%lj+om3t74-=e8^(o3q5"
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
