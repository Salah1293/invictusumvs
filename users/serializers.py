from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



#SERIALIZER FOR ROLE MODEL
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'



#SERIALIZER FOR PROFILE MODEL
class ProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=True, read_only=True)    
    class Meta:
        model = Profile
        fields = '__all__'



#SERIALIZER FOR REGISTRATION
class RegistrationSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],
        )
        return user
    
    # def get_profile(self, obj):
    #     try:
    #         profile = Profile.objects.get(user=obj)
    #         return ProfileSerializer(profile).data
    #     except Profile.DoesNotExist:
    #         return None
    