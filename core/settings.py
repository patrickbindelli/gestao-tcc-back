import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = bool(os.environ.get("DEBUG", default=1))
SECRET_KEY = os.environ.get("SECRET_KEY", "change_me")
HASHID_FIELD_SALT = "a long and secure salt value that is not the same as SECRET_KEY"


ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",")
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS]

CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = ("Access-Control-Allow-Origin: http://localhost:3000",)

# Application definition
INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "rest_framework",
    "djoser",
    "accounts",
    "research",
    "api",
    "utilities",
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

# Middleware definition
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


AUTH_USER_MODEL = "accounts.User"

# Urls Definition
ROOT_URLCONF = "core.urls"

# Templates Definition
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = "core.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "pt-br"
USE_I18N = True

TIME_ZONE = "America/Sao_Paulo"
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media Files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# CSRF
CSRF_TRUSTED_ORIGINS = ["http://localhost:1337", "http://localhost:8000"]

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# DRF
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 2,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Sistema de Gestão de TCCs - API",
    "DESCRIPTION": "Sistema aberto para gestão e aprovação de Trabalhos de Conclusão de Curso (TCCs)",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "password-reset/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "activation/{uid}/{token}",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "TOKEN_MODEL": None,
}

AUTH_USER_MODEL = "accounts.UserAccount"


EMAIL_BACKEND = "django_ses.SESBackend"
DEFAULT_FROM_EMAIL = os.environ.get(
    "AWS_SES_FROM_EMAIL", default="patrickvenanbindelli@gmail.com"
)

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", default="AKIAVETPSEYFIMFQGHHB")
AWS_SECRET_ACCESS_KEY = os.environ.get(
    "AWS_SECRET_ACCESS_KEY", default="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"
)
AWS_SES_REGION_NAME = os.environ.get("AWS_SES_REGION_NAME", default="eu-north-1")
AWS_SES_REGION_ENDPOINT = f"email.{AWS_SES_REGION_NAME}.amazonaws.com"
AWS_SES_FROM_EMAIL = os.environ.get(
    "AWS_SES_FROM_EMAIL", default="patrickvenanbindelli@gmail.com"
)
USE_SES_V2 = True
