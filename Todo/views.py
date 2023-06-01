from django.http import JsonResponse
from .models import Todo,Task
from .serializers import TodoSerializer,TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets

#### for class based views
class TodoViewSet(viewsets.ModelViewSet):
    
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TaskViewSet(viewsets.ModelViewSet):
    
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


### for function based views

# @api_view(['GET', 'POST'])
# def todo_list(request):

#     if request.method == 'GET':
#         todo =TodoSerializer(Todo.objects.all(), many=True,)
#         return Response(todo.data)
    
#     elif request.method == 'POST':
#         todo = TodoSerializer(data=request.data)
#         if todo.is_valid():
#             todo.save()
#             return Response(todo.data,status=status.HTTP_201_CREATED)
#         return Response(todo.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def todo_detail(request, id):

#     try:
#         todo= Todo.objects.get(pk=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method== 'GET':
#         todo_item = TodoSerializer(todo)
#         return Response(todo_item.data)
#     elif request.method== 'PUT':
#         todo_item = TodoSerializer(todo, data=request.data)
#         if todo_item.validate_status(todo_item, todo_item.data.task_status):     
#             if todo_item.is_valid():
#                 todo_item.save()
#                 return Response(todo_item.data)
#         return Response(todo_item.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET','POST'])
# def task_list(request):
#     if request.method == 'GET':
#         task= TaskSerializer(Task.objects.all(), many=True)
#         return Response(task.data)
#     elif request.method== 'POST':
#         task=TaskSerializer(data=request.data)
#         if task.is_valid():
#             task.save()
#             return Response(task.data,status=status.HTTP_201_CREATED)
#         return Response(task.errors,status=status.HTTP_400_BAD_REQUEST)
        

# @api_view(['GET','PUT','DELETE','PATCH'])
# def task_detail(request,id):
#     try:
#         task= Task.objects.get(pk=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method=='GET':
#         return Response(TaskSerializer(task).data)
#     elif request.method=='PUT':
#         task_item= TaskSerializer(task, data=request.data)

#         if task_item.is_valid():
#             task_item.save()
#             return Response(task_item.data)
#         return Response(task_item.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='PATCH':
#         task_item= TaskSerializer(task, data=request.data, partial=True)
#         if task_item.is_valid():
#             task_item.save()
#             return Response(task_item.data)
#         return Response(task_item.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
