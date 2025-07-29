from django . shortcuts import redirect, render
from django.contrib.auth.models import User
from todo_app import models
from todo_app.models import Todo
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        email_id = request.POST.get('email')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=email_id).exists():
            messages.error(
                request, "Email already exists. Please choose another one.")
            return redirect('/signup')

        my_user = User.objects.create_user(
            username=email_id, email=email_id, password=pwd)
        my_user.first_name = fnm
        my_user.save()
        return redirect('/signin')
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        pwd = request.POST.get('pwd')
        my_user = authenticate(request, username=email_id, password=pwd)
        if my_user is not None:
            login(request, my_user)
            return redirect('/todo')
        else:
            return redirect('/signin')

    return render(request, 'signin.html')

@login_required(login_url='/signin')
def todo(request):
    if request.method == "POST":
        title = request.POST.get('title')

        if not title:
            messages.error(request, "Title is required.")
            return redirect('/todo')

        obj =models.Todo(title=title, user=request.user)
        obj.save()
        messages.success(request, "Todo added successfully.")

        res = models.Todo.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo', {"res": res})

    res = models.Todo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})

@login_required(login_url='/signin')
def edit_todo(request,id):
    if request.method == "POST":
        title = request.POST.get('title')
       

        obj = models.Todo.objects.get(id=id)
        obj.title=title
        obj.save()
        user=request.user
        res = models.Todo.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo', {"res": res})

    obj = models.Todo.objects.get(id=id)
    res = models.Todo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'edit_todo.html', {'obj': obj})

@login_required(login_url='/signin')
def delete_todo(request,id):
     obj = models.Todo.objects.get(id=id)
     obj.delete()
     return redirect('/todo')
@login_required(login_url='/signin')
def signout(request):
    logout(request)
    return redirect("/signin")

     

     

