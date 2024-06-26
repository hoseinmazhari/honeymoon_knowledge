# https://arash-hatami.ir/commit-sign/


from pathlib import Path
from celery.schedules import crontab
# import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%utfbwoh8f2)#=-70zi$y*0q@9)6cn=u2mk694usvaa6zvdd%h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'birthday',
    'A',
    'honeymoonatr',
    'product',
    'get_the_report',
    'get_coin_report',
    'analyse_excels',
    'club',
    'Lottery',
    # "django.contrib.staticfiles",
    
    # 'django_celery_results',
    'django_celery_beat',
    'celery',
    
]

MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'A.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [f"{BASE_DIR}/tepmlates",'A','product','birthday','get_coin_report','honeymoonatr','analyse_excels',f"{BASE_DIR}/analyse_excels/tepmlates/analyse_excels"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'A.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True
# INTERNAL_IPS = [
#     # ...
#     "127.0.0.1",
#     # ...
# ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# STATIC_URL = '/static/'
# import os
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_TIMEZONE = TIME_ZONE
CELERY_BEAT_SCHEDULE = {
    "update_customers_specifications":{
        "task": "club.tasks.run_update_customers_specifications",
        "schedule":crontab(minute=40,hour='0-23'),
        # "args": ['hello world']
    },
    # "send_daily_birthday":{
    #     "task": "club.tasks.run_send_daily_birthday_message",
    #     "schedule":20,
    #     # "args":['']
    # },
    "send_daily_sms_birthday_customers":{
        "task": "club.tasks.send_daily_sms_birthday_customers",
        "schedule":crontab(minute=00,hour=18), # پیامک تبریک تولد
        # "args":['']
    },
    "fethch_sale_factor_list":{
        "task": "club.tasks.fethch_sale_factor_list",
        "schedule":crontab(minute=15, hour=1)
        # "args":['']
    },
    # "test2":{
    #     "task": "club.tasks.test2",
    #     "schedule":50#crontab(minute=0,hour=10),
    #     # "args":['']
    # },
    # "test3":{
    #     "task": "club.tasks.test3",
    #     "schedule":50#crontab(minute=0,hour=10),
    #     # "args":['']
    # }


}
