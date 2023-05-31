from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer

def todo_list(request):
    todo =TodoSerializer(Todo.objects.all(), many=True,)
    return JsonResponse( {'Todos':todo.data})