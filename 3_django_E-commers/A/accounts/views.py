from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm #, VerifyCodeForm, UserLoginForm
import random
# from utils import send_otp_code
from .models import OtpCode, User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class UserRegisterView(View):
	form_class = UserRegistrationForm
	template_name = 'accounts/register.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		pass
		# form = self.form_class(request.POST)
		# if form.is_valid():
		# 	random_code = random.randint(1000, 9999)
		# 	send_otp_code(form.cleaned_data['phone'], random_code)
		# 	OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
		# 	request.session['user_registration_info'] = {
		# 		'phone_number': form.cleaned_data['phone'],
		# 		'email': form.cleaned_data['email'],
		# 		'full_name': form.cleaned_data['full_name'],
		# 		'password': form.cleaned_data['password'],
		# 	}
		# 	messages.success(request, 'we sent you a code', 'success')
		# 	return redirect('accounts:verify_code')
		# return render(request, self.template_name, {'form':form})

