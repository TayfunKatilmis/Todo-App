from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import todoItem
# Create your views here.

class TodoList(ListView):
    model = todoItem
    context_object_name = 'todos'
    template_name = 'todo_app/todo_list.html'
    
class TodoDetail(DetailView):
    model = todoItem
    context_object_name = 'todo'
    template_name = 'todo_app/todo.html'