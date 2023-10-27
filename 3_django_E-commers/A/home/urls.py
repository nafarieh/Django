from django.urls import path, include
from . import views


bucket_urls = [
	path('', views.BucketHome.as_view(), name='bucket'),
	path('delete_obj/<str:key>/', views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),
]
#
app_name = 'home'

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('bucket/', include(bucket_urls)),
	path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
