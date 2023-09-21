from django.shortcuts import render
from .models import Todo

# Create your views here.

# from django.http import HttpResponse


def home(request):
    # all = Todo.objects.first() /last()/filter()
    all = Todo.objects.all()
    return render(request,'home.html', {'todos1':all})


def say_hello(request):
    # pass
    # return HttpResponse('Hello User ...')

    person = {'name': 'Zahra'}
    # return render(request,'hello.html', context= person)
    return render(request,'hello.html', context= {'name': 'Zahra'})
