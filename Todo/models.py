from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=255)


class Task(models.Model):
    todo= models.ForeignKey("Todo.Todo", on_delete=models.CASCADE)
    task_title = models.CharField(max_length=255)
    task_status = models.CharField(max_length=255)
    task_description = models.TextField(max_length=500)


