from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=66, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

        def validate(self, attrs):
            username = attrs.get('username', '')
            email = attrs.get('email', '')
            password = attrs.get('password', '')

            # if not username.isalnum():
            #     raise serializers.ValidationError('Username should not contain any alphanumeric character')

            if first_name is None:
                raise serializers.ValidationError('First Name should not be empty!')

            if len(username) > 25:
                raise serializers.ValidationError('Username should not contain letters more than 25')

            return attrs

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
