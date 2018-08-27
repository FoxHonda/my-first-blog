# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('',  views.UserExtendsUpdate.as_view(), name='profile'),
]
