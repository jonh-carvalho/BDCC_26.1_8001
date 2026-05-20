import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Como criar a SECRET_KEY no ambiente:

# PowerShell (sessão atual):
# $env:SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# PowerShell (persistente):
# setx SECRET_KEY "$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")"

# CMD (persistente):
# for /f "delims=" %i in ('python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"') do setx SECRET_KEY "%i"

# Linux/macOS (sessão atual):
# export SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"

SECRET_KEY = os.getenv('SECRET_KEY')

if not SECRET_KEY:
    raise RuntimeError(
        'SECRET_KEY não definida. Configure a variável de ambiente SECRET_KEY antes de iniciar o Django.'
    )

# Configuração de DEBUG - True para desenvolvimento
DEBUG = os.getenv('DJANGO_DEBUG', 'False').strip().lower() in ('1', 'true', 'yes', 'on')

# Configuracao do banco de dados
MYSQL_OPTIONS = {
    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
}

def _bool_env(name, default='False'):
    return os.getenv(name, default).strip().lower() in ('1', 'true', 'yes', 'on')


IS_TEST = 'test' in sys.argv

# Verifica se as variáveis de ambiente para RDS estão definidas
USE_RDS = all(
    os.getenv(var)
    for var in ('RDS_DB_NAME', 'RDS_USERNAME', 'RDS_PASSWORD', 'RDS_HOSTNAME')
)

# Verifica se as variáveis de ambiente para MySQL local estão definidas
USE_MYSQL_LOCAL = all(
    os.getenv(var)
    for var in ('MYSQL_DATABASE', 'MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_HOST')
)

if DEBUG or IS_TEST:
    if USE_MYSQL_LOCAL:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.getenv('MYSQL_DATABASE'),
                'USER': os.getenv('MYSQL_USER'),
                'PASSWORD': os.getenv('MYSQL_PASSWORD'),
                'HOST': os.getenv('MYSQL_HOST'),
                'PORT': os.getenv('MYSQL_PORT', '3306'),
                'OPTIONS': MYSQL_OPTIONS,
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
elif USE_RDS:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('RDS_DB_NAME'),
            'USER': os.getenv('RDS_USERNAME'),
            'PASSWORD': os.getenv('RDS_PASSWORD'),
            'HOST': os.getenv('RDS_HOSTNAME'),
            'PORT': os.getenv('RDS_PORT', '3306'),
            'OPTIONS': MYSQL_OPTIONS,
        }
    }
else:
    raise RuntimeError(
        'Banco de dados de producao nao configurado. Defina RDS_DB_NAME, RDS_USERNAME, '
        'RDS_PASSWORD e RDS_HOSTNAME no ambiente.'
    )

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

_default_hosts = 'localhost,127.0.0.1,testserver' if DEBUG or IS_TEST else ''

# Configuração de hosts permitidos
ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv('DJANGO_ALLOWED_HOSTS', _default_hosts).split(',')
    if host.strip()
]

if not ALLOWED_HOSTS:
    raise RuntimeError(
        'DJANGO_ALLOWED_HOSTS nao definido. Informe os hosts permitidos no ambiente.'
    )

# Configurações de segurança para produção
# Em produção, é recomendado usar HTTPS com um certificado SSL válido.
# As configurações abaixo ajudam a garantir que o site seja servido de forma segura.
SECURE_SSL_REDIRECT = (not DEBUG) and _bool_env('DJANGO_SECURE_SSL_REDIRECT', 'True')
SESSION_COOKIE_SECURE = not DEBUG
# Em produção, é recomendado usar HTTPS, então o cookie CSRF deve ser seguro.
# Em desenvolvimento, isso pode ser False para facilitar os testes sem HTTPS.
# Em produção, defina DJANGO_SECURE_SSL_REDIRECT=True e configure um certificado SSL válido.
# Se estiver usando HTTPS em produção, mantenha CSRF_COOKIE_SECURE=True para proteger contra ataques CSRF.
CSRF_COOKIE_SECURE = not DEBUG
# HSTS (HTTP Strict Transport Security) é uma política de segurança que instrui os navegadores a acessarem o site apenas via HTTPS.
SECURE_HSTS_SECONDS = int(os.getenv('DJANGO_SECURE_HSTS_SECONDS', '31536000')) if not DEBUG else 0
# Incluir subdomínios na política HSTS é recomendado em produção para garantir que todo o site seja protegido.
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
# HSTS_PRELOAD é uma opção que permite que o site seja incluído na lista de pré-carregamento de HSTS dos navegadores, garantindo que os usuários acessem o site via HTTPS mesmo na primeira visita.
SECURE_HSTS_PRELOAD = not DEBUG
# Se o Django estiver atrás de um proxy reverso (como Nginx ou AWS ELB) que lida com SSL, essa configuração ajuda o Django a detectar corretamente se a conexão é segura.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Em produção, é recomendado definir CSRF_TRUSTED_ORIGINS para os domínios reais do site para proteger contra ataques CSRF.
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS', '').split(',')
    if origin.strip()
]


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

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []
