import unittest

from dj_autoconf.core.parser import Parser


class TestParser(unittest.TestCase):

    def test_parser(self):
        file = '/Users/whatislove118/Desktop/Projects_py/django_autoconf/django_autoconf/settings_local.py'
        with open(file, 'r') as file:
            data = bytearray(file.read(), 'utf-8')
        with open('/Users/whatislove118/Desktop/Projects_py/django_autoconf/test_parser.py', 'wb') as file:
            data = Parser(data=data).parse()
            print(data)
            for d in data:
                file.write(d)
            

    def test_code(self):
        with open('/Users/whatislove118/Desktop/Projects_py/django_autoconf/test_parser.py', 'wb') as file:
            file.write(b'int a = 5')

