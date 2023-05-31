from rest_framework import serializers
from .models import Todo
from .models import Task
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id','todo_name', 'user'
        ]
    
    def validate_todo_name(self,value):
        if value == "error":
            raise serializers.ValidationError("wrong value")
        return value

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ['id','task_title','task_description','task_status']
