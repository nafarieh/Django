from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

# from django.http import HttpResponse


def home(request):
    # all = Todo.objects.first() /last()/filter()
    all = Todo.objects.all()
    return render(request,'home.html', {'todos1':all})


# def say_hello(request):
#     # pass
#     # return HttpResponse('Hello User ...')
#
#     person = {'name': 'Zahra'}
#     # return render(request,'hello.html', context= person)
#     return render(request,'hello.html', context= {'name': 'Zahra'})


def detail(request, todo_id):
    todo = Todo.objects.get(id= todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id= todo_id).delete()
    return redirect('home')