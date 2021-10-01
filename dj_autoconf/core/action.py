import sys
from abc import ABC, abstractmethod
from getpass import getpass

from dj_autoconf.core import settings
from dj_autoconf.core.http import register_on_server, login_on_server
from dj_autoconf.core.user import User, RegisterUser


class BaseAction(ABC):
    _action_name = None
    data = None

    @abstractmethod
    def action(self, command):
        pass

    @staticmethod
    def input_password(pass_text='Password :\n'):
        if sys.stdin.isatty():
            password = getpass(pass_text)
        else:
            password = sys.stdin.readline().rstrip()
        return password

    def input_info(self, command):
        command.stdout.write('Enter username : ')
        username = input()
        password = self.input_password()
        return {'username': username, 'password': password}

    # def validate_data(self, data):
    #     if self.data.get('username') == '':


class RegisterAction(BaseAction):
    _action_name = 'reg'

    def action(self, command):
        user = RegisterUser(**self.input_info(command))
        register_on_server(user)

    def input_info(self, command):
        command.stdout.write('Enter email : ')
        email = input()
        data = super().input_info(command)
        data.update(
            {
                're_password': super().input_password('Enter a password again : \n'),
                'email': email
            }
        )
        return data


class LoginAction(BaseAction):
    _action_name = 'login'

    def action(self, command):
        user = User(**super().input_info(command))
        login_on_server(user)

class CreateConfigurationAction(BaseAction):
    _action_name = 'create'

    def action(self, command):
        pass





