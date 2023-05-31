from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def todo_list(request):

    if request.method == 'GET':
        todo =TodoSerializer(Todo.objects.all(), many=True,)
        return Response(todo.data)
    
    elif request.method == 'POST':
        todo = TodoSerializer(data=request.data)
        if todo.is_valid():
            todo.save()
            return Response(todo.data,status=status.HTTP_201_CREATED)
        return Response(todo.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):

    try:
        todo= Todo.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method== 'GET':
        todo_item = TodoSerializer(todo)
        return Response(todo_item.data)
    elif request.method== 'PUT':
        todo_item = TodoSerializer(todo, data=request.data)
        if todo_item.is_valid():
            todo_item.save()
            return Response(todo_item.data)
        return Response(todo_item.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
