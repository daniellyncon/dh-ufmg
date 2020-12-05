"""
Django settings for DH project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k35!kzmjobp(p#9rdpysfy$&kjs9zmic-q598%vg02yp-=6--f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "import_export",
    "debug_toolbar",
    "nested_inline",
    "Atendimento",
    "Administracao",
    "bootstrap_datepicker_plus",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


ROOT_URLCONF = 'DH.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = 'DH.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'America/Sao_Paulo'

LOCALE_PATHS = [
    BASE_DIR / "locale"
]

# English default
gettext = lambda s: s  # NOQA
LANGUAGES = [
    ["pt-BR", gettext("Portuguese")],
]

AUTH_USER_MODEL = 'Administracao.Usuario'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _: True}

FORMAT_MODULE_PATH = [
    'Administracao.formats',
]

########################
# Third party settings #
########################
JAZZMIN_SETTINGS = {
    # title of the window
    "site_title": "Clínica Direitos Humanos",
    # Title on the brand, and the login screen (19 chars max)
    "site_header": "DH",
    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    "site_logo": 'brand.png',
    # Welcome text on the login screen
    "welcome_sign": "Bem-vindo ao DH-UFMG",
    # Copyright on the footer
    "copyright": "PUC Minas",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "Atendimento.Tarefa",
    # Field name on user model that contains avatar image
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "Tarefa"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "Atendimento"},
        {"app": "books"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True, },
        {"model": "Atendimento.Tarefa"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps to base side menu (app or model) ordering off of
    "order_with_respect_to": [
        "Administracao.Usuario",
        "Administracao.Eixo",
        "Administracao.Entidade",
        "Administracao.Documento",
        "Administracao.Tarefa",
        "Administracao.Frase",
        "Atendimento.Caso",
        "Atendimento.Pessoa",
        "Atendimento.Processo",
        "Atendimento.Recurso"
    ],
    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "loans": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["loans.view_loan"],
            }
        ]
    },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "admin.LogEntry": "fas fa-file",
        "Administracao.Usuario": "fas fa-user-friends",
        "Administracao.Eixo": "fas fa-hand-holding-heart",
        "Administracao.Entidade": "fas fa-hands-helping",
        "Administracao.Documento": "fas fa-file-invoice",
        "Administracao.Tarefa": "fas fa-tasks",
        "Administracao.Frase": "fas fa-quote-left",
        "Atendimento.Caso": "fas fa-hands",
        "Atendimento.Pessoa": "fas fa-users",
        "Atendimento.Processo": "fas fa-gavel",
        "Atendimento.Recurso": "fas fa-balance-scale-right",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Activate Bootstrap modal
    "related_modal_active": True,
    #############
    # UI Tweaks #
    #############

    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "carousel",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs", },
    # Add a language dropdown into the admin
    "language_chooser": False,
}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-cyan",
    "accent": "accent-maroon",
    "navbar": "navbar-pink navbar-dark",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-lightblue",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True
}

X_FRAME_OPTIONS = 'ALLOWALL'

XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']
