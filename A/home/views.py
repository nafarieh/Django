from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm

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
    messages.success(request, 'todo deleted seuccesfully', 'success' )
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(first_name= cd['title'], last_name= cd['body'])
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('home')
            # print(form.cleaned_data)
    else:
        form= TodoCreateForm()
    return render(request, 'create.html', {'form':form})
