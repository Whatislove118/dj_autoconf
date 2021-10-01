from django.core.management.base import BaseCommand
from django.utils import timezone
from dj_autoconf.core import action

class Command(BaseCommand):
    help = 'Displays current time'

    allowed_commands = {
        'reg': action.RegisterAction(),
        'login': action.LoginAction(),
        'create': action.CreateConfigurationAction()
    }

    def add_arguments(self, parser):
        parser.add_argument('action', nargs='*', type=str, help=u'If you want to create new account')

    def handle(self, *args, **kwargs):
        action_name = ''.join(kwargs.get('action'))
        action_object = self.allowed_commands.get(action_name)
        if action_object is None:
            self.stderr.write('Action %s doesn\'t support' % action_name)
            exit()
        action_object.action(self)
