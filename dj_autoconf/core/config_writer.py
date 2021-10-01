import os
from threading import Thread

from dj_autoconf.core import settings
from dj_autoconf.core.parser import Parser
from dj_autoconf.core.validator import NoneValidator

class ConfigWriter:

    data = NoneValidator()
    filename = NoneValidator()

    def __init__(self, data, filename='settings_local', path_to_save=settings.PATH_TO_SAVE, path_to_import=settings.PROJECT_SETTINGS_FILE):
        self.path_to_save = path_to_save
        self.path_to_import = path_to_import
        self.data = data
        self.filename = filename

    """ Так как мы планируем работать с файлом после проверки его доступности, проще всего реализовать это его открытием"""
    def write(self):
        self._write_import()
        self._write_config()

    def _write_import(self):
        import_string_command = 'from .%s import *\n' % self.filename
        with open(self.path_to_import, 'a') as file:
            file.write(import_string_command) if self._check_if_import_exist(import_string_command) else None

    def _write_config(self):
        with open(self.path_to_save, 'wb') as file:
            data = Parser(data=self.data).parse()
            for line in data:
                file.write(line)


    """ Реализуем простой алгоритм поиска по началу строки"""
    # TODO написать алгоритм
    def _check_if_import_exist(self, import_string_command) -> bool:
        with open(self.path_to_import, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line == import_string_command:
                    return False
            return True

