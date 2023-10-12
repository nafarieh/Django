from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# def home(request):
#     # return HttpResponse('Home page...')
#     return render(request, 'home/index.html')

class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')

    def post(self, request):
        return render(request, 'home/home.html')