from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
	path('', views.Home.as_view(), name='home'), #endpoint
	# path('<str:name>/', views.Home.as_view(), name='home'), #endpoint
	# path('', views.home, name='home'),
	path('questions/', views.QuestionListView.as_view()), #endpoint
	# path('questions/<int:pk>/', views.QuestionListView.as_view()), #endpoint
	path('questions/create/', views.QuestionCreateView.as_view()), #endpoint
	path('questions/update/<int:pk>/', views.QuestionUpdateView.as_view()), #endpoint
	path('questions/delete/<int:pk>/', views.QuestionDeleteView.as_view()), #endpoint
]