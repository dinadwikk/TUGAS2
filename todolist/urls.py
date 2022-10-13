from ast import Delete
from django.urls import path
from todolist.views import register, create_todo_ajax, show_json, show_json_by_id
from todolist.views import show_todolist
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create
from todolist.views import delete



app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create, name='create'),
    path('delete/<int:id>', delete, name='delete'),
    path('create-ajax/', create_todo_ajax, name= 'create_todo_ajax'),
]