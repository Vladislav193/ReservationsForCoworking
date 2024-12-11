from rest_framework import serializers
from .models import CustomUser


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ("username",)


class UserSeralizers(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ("username", "last_name", "role")


