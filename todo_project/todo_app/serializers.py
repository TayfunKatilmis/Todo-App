from rest_framework import serializers

from .models import todoItem

class TodoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = todoItem
        fields = '__all__'