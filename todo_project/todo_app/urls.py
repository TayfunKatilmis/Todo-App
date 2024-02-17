from django.urls import path

#from .views import TodoList,TodoDetail,TodoCreate, TodoUpdate,TodoDelete
from . import views
urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('todo-list/', views.todoList, name='todoItems-List'),
    path('todo-detail/<int:pk>/', views.todoDetail, name="todoItems-Detail"),
    path('todo-update/<int:pk>/', views.todoUpdate, name="todoItems-Update"),
    path('todo-create/', views.todoCreate, name="todoItems-Create"),


    #path("", TodoList.as_view(), name="todoItems"),
    #path("todo/<int:pk>/", TodoDetail.as_view(), name="todoItems"),
    #path("todo-create/", TodoCreate.as_view(), name="todoItems-create"),
    #path("todo-update/<int:pk>/", TodoUpdate.as_view(), name="todoItems-update"),
    #path("todo-delete/<int:pk>/", TodoDelete.as_view(), name="todoItems-delete"),
]