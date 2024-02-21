from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from todo_app.models import User


def list(request):
    from notifications.signals import notify
    recipient = User.objects.get(id=1) 
    notify.send(recipient, recipient=recipient, verb='New Contact us request')

    return render(request, 'frontend/list.html', context={'user': recipient})


def user_login(request):
    return render(request, 'frontend/user_login.html')


def user_register(request):
    return render(request, 'frontend/user_register.html')