from django.urls import path
from todolist.views import register, show_todolist
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create/', register, name='create'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create, name='create')
]