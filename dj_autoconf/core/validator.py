from abc import ABC, abstractmethod

class BaseValidator(ABC):

    # позволяет привязать имя поля, к которому относится дескриптор
    def __set_name__(self, owner, name):
        self.field_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.field_name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.field_name] = value

    def validate(self, value):
        if len(value) < self.min_length or len(value) > self.max_length:
            raise ValueError('%s must be in (%d, %d) characters' % (self.field_name.upper(), self.min_length, self.max_length))

""" Validator for Not-None fields"""
class NoneValidator(BaseValidator):

    def validate(self, value):
        if value is None:
            raise ValueError('Field %s must be presented' % self.field_name)

class UsernameValidator(BaseValidator):
    
    def __init__(self, min_length, max_length, unacceptable_symbols=None):
        if unacceptable_symbols is None:
            unacceptable_symbols = [' ', '!', '?']

        self.min_length = min_length
        self.max_length = max_length
        self.unacceptable_symbols = unacceptable_symbols

    def validate(self, value: str):
        if len(value.split(' ')) != 1:
            raise ValueError('Spaces not allowed in username')
        super(UsernameValidator, self).validate(value)


class EmailValidator(BaseValidator):

    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value: str):
        if '@' not in value:
            raise ValueError('Email must contains @ symbol')
        super(EmailValidator, self).validate(value)

""" Так как валидация пароля по своей структуре идентична валидации username, наследуемся от UsernameValidator"""
class PasswordValidator(UsernameValidator):

    def validate(self, value: str):
        super(PasswordValidator, self).validate(value)

    # def __init__(self, min_length, max_length, unacceptable_symbols=None):
    #     super(PasswordValidator, self).__init__(min_length, max_length, unacceptable_symbols)
