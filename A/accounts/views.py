from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_register(request):
    # return HttpResponse('User registration page')
    if request.method == "POST" :
        # pass
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # pass
            cd = form.cleaned_data
            user= User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name= cd['first_name']#'amirbig'
            user.last_name= cd['last_name']#'bigderloo'
            user.save()
            messages.success(request, 'user registerd successfully', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html',{'form':form})
