from django.contrib.auth.hashers import make_password
from django_filters import rest_framework as djfilters
from rest_framework import viewsets, filters

from users.models import User
from users.serializers import (UserSerializer, UserSimpleSerializer)
from users.pagination import DefaultPagination


class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()

    pagination_class = DefaultPagination

    filter_backends = (filters.SearchFilter, djfilters.DjangoFilterBackend,)
    search_fields = ['first_name', 'last_name', 'email']
    filter_fields = {
        'email': ['icontains'],
        'first_name': ['icontains'],
        'last_name': ['icontains']
    }

    def get_serializer_class(self):
        if self.request.query_params.get('is_simple'):
            return UserSimpleSerializer
        return UserSerializer

    def perform_create(self, serializer):
        if self.request.data.get('password'):
            serializer.save(
                password=make_password(self.request.data['password'])
            )
        else:
            serializer.save()

    def perform_update(self, serializer):
        if self.request.data.get('password'):
            serializer.save(
                password=make_password(self.request.data['password'])
            )
        else:
            serializer.save()


class UserSettingsAPI(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_update(self, serializer):
        id = self.request.user.id
        if self.request.data.get('password'):
            serializer.save(
                id=id,
                password=make_password(self.request.data['password'])
            )
        else:
            serializer.save(
                id=id
            )
