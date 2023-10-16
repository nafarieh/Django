from django.urls import path
from . import views

app_name= 'home'
urlpatterns= [
    path('' , views.HomeView.as_view(), name='home'),
    # path('',views.home, name='home')
    path('post/<int:post_id>/<slug:post_slug>/',views.PostDetailView.as_view(), name='post_detail'),
    path('post/delete/<int:post_id>/' , views.PostDetailView.as_view(), name='post_delete'),
]

