"""
Django settings for meu_projeto project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-gx6l$p*d973fp)zlhxui$*h0c+3na!-8w1-i5&*x5p1_k6(%rn"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "reservatorio",  # Aplicativo de monitorar reservatórios d'agua
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "meu_projeto.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "meu_projeto.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CSRF_TRUSTED_ORIGINS = [
    'https://localhost:8000',  # Adicione o domínio que você está usando
    'http://127.0.0.1:8000',   # Inclua também o localhost padrão
]

# Project structure
PROJECT_STRUCTURE = {
    "workspace": "/workspaces/codespaces-blank/",
    "manage.py": "/workspaces/codespaces-blank/manage.py",
    "meu_projeto": {
        "__init__.py": "/workspaces/codespaces-blank/meu_projeto/__init__.py",
        "settings.py": "/workspaces/codespaces-blank/meu_projeto/settings.py",
        "urls.py": "/workspaces/codespaces-blank/meu_projeto/urls.py",
        "wsgi.py": "/workspaces/codespaces-blank/meu_projeto/wsgi.py",
    },
    "reservatorio": {
        "__init__.py": "/workspaces/codespaces-blank/reservatorio/__init__.py",
        "models.py": "/workspaces/codespaces-blank/reservatorio/models.py",
        "views.py": "/workspaces/codespaces-blank/reservatorio/views.py",
        "templates": {
            "reservatorio": {
                "lista_reservatorios.html": """
{% extends 'base.html' %}

{% block title %}Lista de Reservatórios{% endblock %}

{% block content %}
<h1 class="mb-4">Lista de Reservatórios</h1>
<a href="{% url 'adicionar_reservatorio' %}" class="btn btn-primary mb-3">Adicionar Reservatório</a>
<table class="table table-striped">
    <thead>
        <tr>
            <th>Nome</th>
            <th>Capacidade</th>
            <th>Nível Atual</th>
            <th>Estágio</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
        {% for reservatorio in reservatorios %}
        <tr>
            <td>{{ reservatorio.nome }}</td>
            <td>{{ reservatorio.capacidade }}L</td>
            <td>{{ reservatorio.nivel_atual }}L</td>
            <td>
                {% if reservatorio.nivel_atual >= reservatorio.capacidade * 0.75 %}
                    <img src="{% static 'reservatorio/cheio.png' %}" alt="Cheio" width="50">
                {% elif reservatorio.nivel_atual >= reservatorio.capacidade * 0.25 %}
                    <img src="{% static 'reservatorio/metade.png' %}" alt="Na metade" width="50">
                {% else %}
                    <img src="{% static 'reservatorio/vazio.png' %}" alt="Vazio" width="50">
                {% endif %}
            </td>
            <td>
                <a href="{% url 'editar_reservatorio' reservatorio.id %}" class="btn btn-warning btn-sm">Editar</a>
                <a href="{% url 'deletar_reservatorio' reservatorio.id %}" class="btn btn-danger btn-sm">Excluir</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
"""
            }
        }
    },
}
