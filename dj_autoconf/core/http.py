import requests

from dj_autoconf.core import settings
from dj_autoconf.core.config_writer import ConfigWriter
from dj_autoconf.core.parser import Parser


class HttpConnection:
    def __init__(self):
        pass


def register_on_server(user):
    request = requests.post(settings.BACKEND_URL_PREFIX + 'auth/account/', data=vars(user))
    if request.status_code == 201:
        print(request.content)
        print('Successful registered')

def login_on_server(user):
    request = requests.post(settings.BACKEND_URL_PREFIX + 'auth/account/login/', auth=(user.username, user.password))
    if request.status_code == 200:
        config_writer = ConfigWriter(data=request.content)
        config_writer.write()
        print('Successful logged')
    if request.status_code == 401:
        print('Unauthorized, please check your credentials and try again')



