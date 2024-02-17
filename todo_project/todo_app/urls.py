from django.urls import path
from .views import TodoList,TodoDetail,TodoCreate

urlpatterns = [
    path("", TodoList.as_view(), name="todoItems"),
    path("todo/<int:pk>/", TodoDetail.as_view(), name="todoItems"),
    path("todo-create/", TodoCreate.as_view(), name="todoItems-create"),
]