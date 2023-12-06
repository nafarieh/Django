from django.urls import path, include
from . import views
from rest_framework.authtoken import views as auth_token

app_name = 'accounts'
urlpatterns = [
	path('register/', views.UserRegister.as_view()), #endpoint
	path('api-token-auth_token/', auth_token.obtain_auth_token),

]