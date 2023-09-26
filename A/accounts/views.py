from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_register(request):
    return HttpResponse('User registration page')
