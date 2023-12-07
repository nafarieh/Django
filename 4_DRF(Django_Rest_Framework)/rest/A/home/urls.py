from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
	path('', views.Home.as_view(), name='home'), #endpoint
	# path('<str:name>/', views.Home.as_view(), name='home'), #endpoint
	# path('', views.home, name='home'),
	path('questions/', views.QuestionView.as_view()), #endpoint
	path('questions/<int:pk>/', views.QuestionView.as_view()), #endpoint
]