import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dz1&98_p4p#6(s99i9pd_s179)b7fk41x(-*zf2oj&_74_4ky&'

# Configuração de DEBUG - True para desenvolvimento
DEBUG = True if os.getenv('DJANGO_DEBUG', 'True') == 'True' else False

# Configuração do banco de dados

# SQLite para desenvolvimento, preparado para RDS depois
if DEBUG:
        # MySQL para desenvolvimento local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('MYSQL_DATABASE', 'catalogo'),
            'USER': os.getenv('MYSQL_USER', 'root'),
            'PASSWORD': os.getenv('MYSQL_PASSWORD', '123456'),
            'HOST': os.getenv('MYSQL_HOST', '127.0.0.1'),
            'PORT': os.getenv('MYSQL_PORT', '3306'),
        }
    }
else:
    # Configuração preparada para RDS (será ativada depois)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('RDS_DB_NAME', 'ebdb'),
            'USER': os.getenv('RDS_USERNAME', 'ebroot'),
            'PASSWORD': os.getenv('RDS_PASSWORD', 'EM_j2606f'),
            'HOST': os.getenv('RDS_HOSTNAME', 'awseb-e-mbxs5wb9z8-stack-awsebrdsdatabase-uodz22wcnmll.cuj2q0ya6uad.us-east-1.rds.amazonaws.com'),
            'PORT': os.getenv('RDS_PORT', '3306'),
        }
    }

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

# Configuração de arquivos de mídia
# SQLite não suporta S3, mas já preparamos o caminho
if DEBUG:
    # Armazenamento local para desenvolvimento
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    # Configuração preparada para S3 (será ativada depois)
    USE_S3 = os.getenv('USE_S3', 'False') == 'True'
    if USE_S3:
        # Configurações S3 serão ativadas posteriormente
        pass
    else:
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS',
    'localhost,127.0.0.1,.elasticbeanstalk.com,testserver',
).split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'produtos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'catalogo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'catalogo.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []
