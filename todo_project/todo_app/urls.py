from django.urls import path
from .views import TodoList,TodoDetail,TodoCreate, TodoUpdate,TodoDelete

urlpatterns = [
    path("", TodoList.as_view(), name="todoItems"),
    path("todo/<int:pk>/", TodoDetail.as_view(), name="todoItems"),
    path("todo-create/", TodoCreate.as_view(), name="todoItems-create"),
    path("todo-update/<int:pk>/", TodoUpdate.as_view(), name="todoItems-update"),
    path("todo-delete/<int:pk>/", TodoDelete.as_view(), name="todoItems-delete"),
]