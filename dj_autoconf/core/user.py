from dj_autoconf.core.validator import UsernameValidator, EmailValidator, PasswordValidator


class User:
    username = UsernameValidator(min_length=4, max_length=15)
    password = PasswordValidator(min_length=4, max_length=15)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return '%s' % self.username


class RegisterUser(User):
    re_password = PasswordValidator(min_length=4, max_length=15)
    email = EmailValidator(min_length=4, max_length=15)

    def __init__(self, username, email, password, re_password):
        super(RegisterUser, self).__init__(username, password)
        self.email = email
        self.re_password = re_password






