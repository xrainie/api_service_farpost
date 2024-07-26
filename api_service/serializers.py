from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(validators=[validate_password])
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают!'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
