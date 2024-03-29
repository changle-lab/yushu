"""
Django settings for meiduo_mall project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tpxbec@d4s3ol**4hgb4@&&$x=(j=g_8y0zt!@73wfz41m+k9o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# localhost 是 0.0.0.0
ALLOWED_HOSTS = ['www.meiduo.site', '127.0.0.1', 'localhost', 'api.meiduo.site']
print("```~~~~~~~```")
# print(BASE_DIR)
# django项目默认导包路径
import sys

# print(sys.path)
# 告诉django项目路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# print(sys.path)
# print("``~~~~~~~~``")
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
    'haystack', #搜索模块
    'django_crontab',  # 定时任务

    'corsheaders',
    'users.apps.UsersConfig',
    'oauth.apps.OauthConfig',
    'areas.apps.AreasConfig',
    'goods.apps.GoodsConfig',
    'contents.apps.ContentsConfig',
    'carts.apps.CartsConfig',
    'orders.apps.OrdersConfig',
    #end
    'payments.apps.PaymentsConfig'


]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meiduo_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'meiduo_mall.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shoppingmall',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'meiyu',
        'PASSWORD': 'meiyu',

    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shoppingmall',
        'HOST': '127.0.0.1',
        'PORT': 8306,
        'USER': 'root',
        'PASSWORD': 'mysql',

    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 缓存配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "sms_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

    "history": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/meiduo.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'meiduo_mall.utils.exceptions.exception_handler',
    # 认证配置
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

AUTH_USER_MODEL = 'users.User'

# CORS 增加白名单
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8080',
    'localhost:8080',
    'www.meiduo.site:8080',
    'api.meiduo.site:8000'
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

# jwt配置
JWT_AUTH = {
    # 指定返回结果的方法位置
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'users.utils.jwt_response_payload_handler',
    # 设置token的过期时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}

AUTHENTICATION_BACKENDS = [
    'users.utils.UsernameMobileAuthBackend',
]

# QQ登录参数
QQ_CLIENT_ID = '101474184'

QQ_CLIENT_SECRET = 'c6ce949e04e12ecc909ae6a8b09b637c'

QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html'

# 制定链接哪个服务器
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# 163
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 'changyu_9@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = '881116YUyu'
# 收件人看到的发件人
EMAIL_FROM = '美多<changyu_9@163.com>'

REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
    # 缓存储存的位置，指定redis中的库
    'DEFAULT_USE_CACHE': 'default'
}

CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')
BASE_URL = 'http://image.meiduo.site:8888/'
# django文件存储
DEFAULT_FILE_STORAGE = 'meiduo_mall.utils.fastdfs.fdfs_storage.FastDFSStorage'
# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        # 'width': 300,  # 编辑器宽
    },
}
CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，使用了FastDFS，所以此处设为''

INDEX_FIEL = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc/index.html')
LIST_FILE = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc/list.html')
GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)),
                                               'front_end_pc')


CRONJOBS = [
    # 每50分钟执行一次生成主页静态文件
    ('*/50 * * * *', 'contents.utils.generate_static_index_html',
     '>> /home/changle-lab/Desktop/shopping_mall/shoppingMall/meiduo_mall/logs/crontab.log')
]
# CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'meiduo',  # 指定elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 支付宝
ALIPAY_APPID = "2016101300679226"
ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do?"
ALIPAY_DEBUG = True


# 配置读写分离
DATABASE_ROUTERS = ['meiduo_mall.utils.db_router.MasterSlaveDBRouter']