# product-user-test
a user with auto create OneToOne instance(profile) on user creation and a task that create a product with unique name every one minute

create a local-settings.py in main contain:

SECRET_KEY = 'your secret key'

ALLOWED_HOSTS = ['*']

DB = {
    'NAME': 'database name',
    'USER': 'database user name',
    'PASSWORD': 'database pass',
    'HOST': 'database ip',
    'PORT': 'database port',
}
