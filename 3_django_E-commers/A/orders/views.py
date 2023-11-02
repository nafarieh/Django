from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# from .cart import Cart
# from home.models import Product
# from .forms import CartAddForm, CouponApplyForm
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from .models import Order, OrderItem, Coupon
# import requests
# import json
# from django.http import HttpResponse
# import datetime
# from django.contrib import messages
from django.core.exceptions import PermissionDenied


# Create your views here.
class CartView(View):
    def get(self, request):
        # cart = Cart(request)
        return render(request, 'orders/cart.html')



class CartAddView(View):
	permission_required = 'orders.add_order'

	def post(self, request, product_id):
		pass

