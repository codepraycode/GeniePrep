from rest_framework import serializers
from datetime import datetime as dt

# Models
from .models import Users

# Authentication
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    
    class Meta:
        model = Users
        fields = ('email', 'matric_number', 'first_name',
                  'surname', 'password', 'created_at')
        read_only = ['created_at',]
    
    def create(self, validated_data):
        return Users.objects.create(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    matric_number = serializers.CharField(max_length=50)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    
    email = serializers.EmailField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    surname = serializers.CharField(read_only=True)
    tokens = serializers.CharField(read_only=True)
    # last_login = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Users
        fields = ('matric_number', 'email', 'first_name','surname','password',
                  'tokens', 'created_at')
    
    def validate(self, attrs):
        matric_number = attrs.get('matric_number', '')
        password = attrs.get('password', '')
        
        try:
            user = Users.objects.get(matric_number=matric_number)
        except:
            raise AuthenticationFailed('Invalid credentials, Matric Number Not Registered')
        
        
        # user = auth.authenticate(email=user.email, password=password)
        
        if user.password != password:
            # status code 401 on exception
            raise AuthenticationFailed('Invalid credentials, try again')
        
        user.last_login = dt.now()
        user.save()
        
        return {
            'matric_number':user.matric_number,
            'email': user.email,
            'first_name': user.first_name,
            'surname': user.surname,
            'tokens': user.tokens()
        }
