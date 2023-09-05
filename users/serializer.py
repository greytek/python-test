from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'user_type',
            'name'
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }
