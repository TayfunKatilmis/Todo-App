from django.urls import path, include
#from .views import TodoList,TodoDetail,TodoCreate, TodoUpdate,TodoDelete
from . import views
urlpatterns = [
    path('user-login/', views.UserLoginView.as_view(), name="user-register"),
	path('user-register/', views.UserRegisterView.as_view(), name="user-login"),
	path('current-user/', views.GetUserView.as_view(), name='current-user'),
	path('user-logout/', views.UserLogoutView.as_view()),

    path('', views.apiOverview, name='api-overview'),
    path('todo-list/', views.todoList, name='todoItems-List'),
    path('todo-detail/<int:pk>/', views.todoDetail, name="todoItems-Detail"),
    path('todo-update/<int:pk>/', views.todoUpdate, name="todoItems-Update"),
    path('todo-create/', views.todoCreate, name="todoItems-Create"),
    path('todo-delete/<int:pk>/', views.todoDelete, name="todoItems-Create"),
]