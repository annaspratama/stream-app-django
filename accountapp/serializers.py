from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name', 'is_staff', 'username', 'password', 'is_staff', 'email', 'phone', 'image',)
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        """
        A function that creates a new instance based on the validated data.
        
        Parameters:
            validated_data (dict): The validated data to create the instance.
        
        Returns:
            The newly created instance.
        """
        
        validated_data['password'] = make_password(password=validated_data['password'])
        
        return super().create(validated_data)