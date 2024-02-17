from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import todoItem
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/todo-list/',
        'Detail View' : '/todo-detail/<int:pk>',
        'Create' : '/todo-create/',
        'Update' : '/todo-update/<int:pk>',
        'Delete' : '/todo-delete/<int:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def todoList(request):
    todos = todoItem.objects.all()
    serializer = TodoSerializer(todos, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
    todos = todoItem.objects.get(id=pk)
    serializer = TodoSerializer(todos, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def todoUpdate(request, pk):
    todos = todoItem.objects.get(id = pk)
    serializer = TodoSerializer(instance=todos, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#class TodoList(ListView):
#    model = todoItem
#    context_object_name = 'todos'
#    template_name = 'todo_app/todo_list.html'
    
#class TodoDetail(DetailView):
#    model = todoItem
#    context_object_name = 'todo'
#    template_name = 'todo_app/todo.html'


#class TodoCreate(CreateView):
#    model = todoItem
#    fields = '__all__'
#    success_url = reverse_lazy('todoItems')
#    template_name = 'todo_app/todo_form.html'

#class TodoUpdate(UpdateView):
#    model = todoItem
#    fields = '__all__'
#    success_url = reverse_lazy('todoItems')
#    template_name = 'todo_app/todo_form.html'


#class TodoDelete(DeleteView):
#    model = todoItem
#    context_object_name = 'todo'
#    success_url = reverse_lazy('todoItems')
#    template_name = 'todo_app/todo_confirm_delete.html'


