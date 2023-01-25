from rest_framework import serializers
from todo.models import Todo

class TodoSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        exclude = ['created_at', 'updated_at']