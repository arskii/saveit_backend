from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=50, min_length=5)
    email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def validate(self, attrs):
        email = attrs.get('email', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)