from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email',
            'last_login', 'date_joined',
            'is_superuser', 'is_staff', 'is_active',
            'photo_image')