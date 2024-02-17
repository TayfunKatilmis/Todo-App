from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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


class TodoCreate(CreateView):
    model = todoItem
    fields = '__all__'
    success_url = reverse_lazy('todoItems')
    template_name = 'todo_app/todo_form.html'

class TodoUpdate(UpdateView):
    model = todoItem
    fields = '__all__'
    success_url = reverse_lazy('todoItems')
    template_name = 'todo_app/todo_form.html'


class TodoDelete(DeleteView):
    model = todoItem
    context_object_name = 'todo'
    success_url = reverse_lazy('todoItems')
    template_name = 'todo_app/todo_confirm_delete.html'