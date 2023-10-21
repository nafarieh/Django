from django.shortcuts import render
from django.shortcuts import render
from django.views import View
# from .models import Product, Category

# Create your views here.


# from . import tasks
# from django.contrib import messages
# from utils import IsAdminUserMixin
# from orders.forms import CartAddForm


class HomeView(View):
	def get(self, request):
		return render(request,'home/home.html')
