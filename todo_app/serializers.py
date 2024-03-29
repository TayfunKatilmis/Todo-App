from rest_framework import serializers

from .models import Task, User

class TodoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Task
        fields = '__all__'

class TodoRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'