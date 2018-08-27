from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
	path('', views.ProductListView.as_view(), name='all_products'),
	url(r'^(?P<pk>[-\w]+)$', views.ProductDetailView.as_view(), name='product-detail'),
]