from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        required_fields = ['username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        read_only_fields = ['id']

    def save(self, **kwargs):
        return User.objects.create_user(**self.validated_data)

    # def validate_password(self, value: str) -> str:
    #     """
    #     Hash value passed by user.
    #
    #     :param value: password of a user
    #     :return: a hashed version of the password
    #     """
    #     return make_password(value)

class UserCreateSerializer(UserSerializer):
    re_password = serializers.CharField(required=True, write_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ['re_password']
        required_fields = UserSerializer.Meta.required_fields + ['email']

    def validate(self, attrs):
        re_password = attrs.pop('re_password')
        password = attrs.get('password')
        if re_password != password:
            raise ValidationError('Passwords are not equals')
        return attrs




