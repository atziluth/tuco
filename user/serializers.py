from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend

from .models import User, Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ('id', 'lifetime_award_total')

    def create(self, validated_data):
        validated_data.pop('groups', [])
        validated_data.pop('user_permissions', [])

        validated_data['is_staff'] = True
        validated_data['is_active'] = True

        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.email = validated_data.get('email', instance.email)
        instance.identity = validated_data.get('identity', instance.identity)

        instance.save()

        return instance

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # token['id'] = user.id

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        data["lifetime"] = 3600
        data["user_id"] = user.id

        return data


class UserTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        decoded_payload = token_backend.decode(data['access'], verify=True)
        user_id=decoded_payload['user_id']
        
        data["lifetime"] = 3600
        data["user_id"] = user_id

        return data
    
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ('id', )