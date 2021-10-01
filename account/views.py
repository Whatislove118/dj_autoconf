from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from account.permissions import IsAccountOwnerPermission
from account.serializers import UserSerializer, UserCreateSerializer
from configurations.models import Configuration
from django_autoconf import settings

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'id'
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = None
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        configuration = Configuration.objects.get_configuration_by_user_id(user_id=user.id)
        return Response(configuration.path_to_file, content_type='file', status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def login(self, request, *args, **kwargs):
        user = request.user
        print(user)
        configuration = Configuration.objects.get_configuration_by_user_id(user_id=user.id)
        return Response(configuration.path_to_file, content_type='text/plain', status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsAccountOwnerPermission, ]
        if self.action == 'login':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = UserCreateSerializer
        return super().get_serializer_class()
    #
    # def perform_create(self, serializer):
    #     instance = serializer.save(is_staff=True)
    #     print(instance)
    #     print('is_staff user created')






