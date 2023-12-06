from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer

User = get_user_model()


class CurrentUserSerializer(UserSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'email',
            'first_name',
            'last_name'
        ]
        read_only_fields = [
            'id',
            'email',
            'first_name',
            'last_name'
        ]


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password',)


class UserSimpleSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'display_name')
