from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=255)

def validate_status(value):
    if value not in ['NOT_STARTED', 'STARTED', 'COMPLETED']:
        raise ValidationError("Invalid status. Only 'NOT_STARTED', 'STARTED', 'COMPLETED' are valid status")

class Task(models.Model):
    todo= models.ForeignKey('Todo.Todo', on_delete=models.CASCADE)
    task_title = models.CharField(max_length=255)
    task_status = models.CharField(max_length=255, default="NOT_STARTED",validators =[validate_status])
    task_description = models.TextField(max_length=5000)


