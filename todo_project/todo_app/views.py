from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer, TodoRegisterSerializer, UserSerializer, UserRegisterSerializer
from .models import Task, User
import jwt, datetime
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Task
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
    todos = Task.objects.all()
    serializer = TodoSerializer(todos, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
    todos = Task.objects.get(id=pk)
    serializer = TodoSerializer(todos, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def todoUpdate(request, pk):
    todos = Task.objects.get(id = pk)
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


class UserLoginView(APIView):

    @method_decorator(csrf_exempt)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = get_user_model().objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret-app-key', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response


class UserRegisterView(APIView):

    def post(self, request):
        js_data = request.data
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        payload = {
            'email': js_data['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret-app-key', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response

class UserLogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response
    
class GetUserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('You are not logged in! Or Token Expired Log in again.')

        try:
            payload = jwt.decode(token, 'secret-app-key', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('En error!')

        user = get_user_model().objects.filter(email=payload['email']).first()
        serializer = UserSerializer(user)

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


