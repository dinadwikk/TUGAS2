from http import cookies
from http.cookiejar import Cookie
from multiprocessing import context
from turtle import title
from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm
from todolist.models import TodolistTemplate
from django.http import JsonResponse
from django.http import HttpResponse


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todos = TodolistTemplate.objects.filter(user=request.user)
    context = {
    'list_todos': data_todos,
    'username': request.user.username,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist_ajax.html", context)

def show_json(request):
    data = TodolistTemplate.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = TodolistTemplate.objects.filter(pk=id)
    #ika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form_listener = form.save(commit=True)
            form_listener.user = request.user
            form_listener.save()
            messages.info(request,'Data berhasil disimpan!')

            return HttpResponseRedirect(reverse('todolist:show_todolist'))
        else:
            messages.info(request,'Terjadi kesalahan saat menyimpan data!')
    context = {'form': form}
    return render(request, 'create.html',context)

def delete(request, id):
    todo_delete = TodolistTemplate.objects.filter(pk=id)
    todo_delete.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))



@login_required(login_url='/todolist/login/')
def create_todo_ajax(request):
    if request.method == "POST":
        user = request.POST.get("user")
        title = request.POST.get("titlr")
        description = request.POST.get("description")

        create_todolist = TodolistTemplate.objects.create(
            user=user, 
            title=title, 
            description=description
        )
        return JsonResponse(
            {
                'error':False,
                'msg':'Success'
            }
        )
    return redirect('todolist:show_todolist')

