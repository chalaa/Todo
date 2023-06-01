from rest_framework import serializers
from .models import Todo,Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ['id','todo','task_title','task_description','task_status']

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ['id','task_title','task_description','task_status']

class TodoSerializer(serializers.ModelSerializer):
    task = TodoTaskSerializer(source='task_set', read_only=True, many=True)
    class Meta:
        model = Todo
        fields = [
            'id','todo_name', 'user', 'task'
        ]

    def validate_todo_name(self,value):
        if value == "error":
            raise serializers.ValidationError("wrong value")
        return value