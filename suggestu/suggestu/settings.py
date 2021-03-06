# Django settings for suggestu
import os
import sys
from django import VERSION
import mongoengine

sys.path.insert(0, '../..')

CUSTOM_USER_MODEL = bool(int(os.environ.get('CUSTOM_USER_MODEL', '1')))
MODE = os.environ.get('MODE', 'standalone')
BASE_ROOT = os.path.abspath(
    os.path.join(os.path.split(__file__)[0]))
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

TEST_RUNNER = 'suggestu.users.tests.NoSQLTestRunner'

DEBUG = True #False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Archit Sharma', os.environ.get('EMAIL_FROM')),
)

MANAGERS = ADMINS
'''
DATABASES = {
    'default': {
        'ENGINE': '',
    },
}
'''
SESSION_ENGINE = 'mongoengine.django.sessions' # optional

_MONGODB_USER = os.environ.get('HE_USER')
_MONGODB_PASSWD = os.environ.get('HE_PASS')
_MONGODB_HOST = 'localhost'
_MONGODB_NAME = os.environ.get('HE_DB')
_MONGODB_DATABASE_HOST = \
                         'mongodb://%s:%s@%s/%s' \
                         % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'suggestu.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/' + os.environ.get('USER') + '/collected/media/'
# MEDIA_ROOT = os.path.join(BASE_ROOT, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/' + os.environ.get('USER') + '/collected/static/'
# STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files

#STATICFILES_ROOT =  os.path.join(BASE_ROOT, 'static/')

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join( PROJECT_ROOT, 'static'),
    #os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'suggestu.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'suggestu.wsgi.application'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), \
                 'suggestu/templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'haystack',
    'search',
    'social.apps.django_app.default',
    'suggestu.app',
    'django_facebook',
    'south',
    'open_facebook',
    'users',
    'relater',
    'scrapers',
    #'bootstrap_pagination',
    #'django_extensions',
)

'''

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'arxiv',
    },
}

'''

'''

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
'''

#SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'django.core.context_processors.tz',
    # django-facebook specific
    'django_facebook.context_processors.facebook',
    # and add request if you didn't do so already    
    'django.core.context_processors.request',
)

AUTHENTICATION_BACKENDS = (
    #'social.backends.amazon.AmazonOAuth2',
    #'social.backends.angel.AngelOAuth2',
    #'social.backends.aol.AOLOpenId',
    #'social.backends.appsfuel.AppsfuelOAuth2',
    #'social.backends.behance.BehanceOAuth2',
    #'social.backends.belgiumeid.BelgiumEIDOpenId',
    #'social.backends.bitbucket.BitbucketOAuth',
    #'social.backends.box.BoxOAuth2',
    #'social.backends.clef.ClefOAuth2',
    #'social.backends.coinbase.CoinbaseOAuth2',
    #'social.backends.dailymotion.DailymotionOAuth2',
    #'social.backends.disqus.DisqusOAuth2',
    #'social.backends.douban.DoubanOAuth2',
    #'social.backends.dropbox.DropboxOAuth',
    #'social.backends.evernote.EvernoteSandboxOAuth',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.fedora.FedoraOpenId',
    #'social.backends.fitbit.FitbitOAuth',
    #'social.backends.flickr.FlickrOAuth',
    #'social.backends.foursquare.FoursquareOAuth2',
    'social.backends.github.GithubOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GooglePlusAuth',
    #'social.backends.instagram.InstagramOAuth2',
    #'social.backends.jawbone.JawboneOAuth2',
    'social.backends.linkedin.LinkedinOAuth',
    'social.backends.linkedin.LinkedinOAuth2',
    #'social.backends.live.LiveOAuth2',
    #'social.backends.livejournal.LiveJournalOpenId',
    #'social.backends.mailru.MailruOAuth2',
    #'social.backends.mendeley.MendeleyOAuth',
    #'social.backends.mendeley.MendeleyOAuth2',
    #'social.backends.mixcloud.MixcloudOAuth2',
    #'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
    'social.backends.open_id.OpenIdAuth',
    #'social.backends.openstreetmap.OpenStreetMapOAuth',
    #'social.backends.orkut.OrkutOAuth',
    'social.backends.persona.PersonaAuth',
    #'social.backends.podio.PodioOAuth2',
    #'social.backends.rdio.RdioOAuth1',
    #'social.backends.rdio.RdioOAuth2',
    #'social.backends.readability.ReadabilityOAuth',
    'social.backends.reddit.RedditOAuth2',
    #'social.backends.runkeeper.RunKeeperOAuth2',
    #'social.backends.skyrock.SkyrockOAuth',
    'social.backends.soundcloud.SoundcloudOAuth2',
    'social.backends.stackoverflow.StackoverflowOAuth2',
    #'social.backends.steam.SteamOpenId',
    #'social.backends.stocktwits.StocktwitsOAuth2',
    #'social.backends.stripe.StripeOAuth2',
    #'social.backends.suse.OpenSUSEOpenId',
    #'social.backends.thisismyjam.ThisIsMyJamOAuth1',
    #'social.backends.trello.TrelloOAuth',
    #'social.backends.tripit.TripItOAuth',
    'social.backends.tumblr.TumblrOAuth',
    #'social.backends.twilio.TwilioAuth',
    'social.backends.twitter.TwitterOAuth',
    #'social.backends.vk.VKOAuth2',
    #'social.backends.weibo.WeiboOAuth2',
    #'social.backends.xing.XingOAuth',
    'social.backends.yahoo.YahooOAuth',
    #'social.backends.yahoo.YahooOpenId',
    #'social.backends.yammer.YammerOAuth2',
    #'social.backends.yandex.YandexOAuth2',
    #'social.backends.vimeo.VimeoOAuth1',
    'social.backends.email.EmailAuth',
    'social.backends.username.UsernameAuth',
    'django.contrib.auth.backends.ModelBackend',
    'django_facebook.auth_backends.FacebookBackend',
    
    'mongoengine.django.auth.MongoEngineBackend',
)

'''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
LIVE_CLIENT_ID               = ''
LIVE_CLIENT_SECRET           = ''
SKYROCK_CONSUMER_KEY         = ''
SKYROCK_CONSUMER_SECRET      = ''
YAHOO_CONSUMER_KEY           = ''
YAHOO_CONSUMER_SECRET        = ''
READABILITY_CONSUMER_SECRET  = ''
READABILITY_CONSUMER_SECRET  = ''
'''

if CUSTOM_USER_MODEL:
    AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
else:
    AUTH_USER_MODEL = 'auth.User'
    AUTH_PROFILE_MODULE = 'member.UserProfile'

#AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'

FACEBOOK_APP_ID = os.environ.get('FB_KEY_L')
FACEBOOK_APP_SECRET = os.environ.get('FB_SECRET_L')

SOCIAL_AUTH_FACEBOOK_APP_ID = os.environ.get('FB_KEY_L')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FB_SECRET_L')
#SOCIAL_AUTH_FACEBOOK_APP_NAMESPACE = 'suggestu'
#SOCIAL_AUTH_FACEBOOK_EXTENDED_PERMISSIONS = ['email']

SOCIAL_AUTH_TWITTER_KEY         = os.environ.get('TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET      = os.environ.get('TWITTER_SECRET')
SOCIAL_AUTH_GITHUB_KEY          = os.environ.get('GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET       = os.environ.get('GITHUB_SECRET')
SOCIAL_AUTH_LINKEDIN_KEY        = os.environ.get('LINKEDIN_KEY')
SOCIAL_AUTH_LINKEDIN_SECRET     = os.environ.get('LINKEDIN_SECRET')

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/done/'
URL_PATH = ''
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

EMAIL_FROM = os.environ.get('EMAIL_FROM')
SOCIAL_AUTH_EMAIL_FORM_URL = '/signup-email'
SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'suggestu.app.mail.send_validation'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
# SOCIAL_AUTH_USERNAME_FORM_URL = '/signup-username'                       
SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'

SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'suggestu.app.pipeline.require_email',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

FILTERS = {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse'
    }
}

MAIL_ADMINS = {
    'level': 'ERROR',
    'class': 'django.utils.log.AdminEmailHandler'
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'open_facebook': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django_facebook': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
LOGGING['handlers']['mail_admins'] = MAIL_ADMINS

if VERSION > (1, 4, 0):
    LOGGING['filters'] = FILTERS
    MAIL_ADMINS['filters'] = ['require_debug_false']
    LOGGING['handlers']['mail_admins'] = MAIL_ADMINS



GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        }
}

if MODE == 'django_registration':
    FACEBOOK_REGISTRATION_BACKEND = 'facebook_example.registration_backends.DjangoRegistrationDefaultBackend'
    INSTALLED_APPS += (
        'registration',
    )
    ACCOUNT_ACTIVATION_DAYS = 10
elif MODE == 'userena':
    '''
    Settings based on these docs
    http://docs.django-userena.org/en/latest/installation.html#installing-django-userena
    '''
    FACEBOOK_REGISTRATION_BACKEND = 'django_facebook.registration_backends.UserenaBackend'
    AUTHENTICATION_BACKENDS = (
        'django_facebook.auth_backends.FacebookBackend',
        'userena.backends.UserenaAuthenticationBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
    LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
    LOGIN_URL = '/accounts/signin/'
    LOGOUT_URL = '/accounts/signout/'
    ANONYMOUS_USER_ID = 1
    INSTALLED_APPS += (
        'userena',
        'guardian',
    )

ALLOWED_HOSTS = ['*']
ALLOWED_INCLUDE_ROOTS = (STATICFILES_DIRS, TEMPLATE_DIRS)
