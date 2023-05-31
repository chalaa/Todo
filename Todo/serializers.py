from rest_framework import serializers
from .models import Todo
from .models import Task
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id','todo_name'
        ]
    class Meta:
        model= Task
        fields = ['id','task_title','task_description','task_status']
