"""diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^agree/$', views.agree, name='agree'),
    url(r'^contact/$', views.ContactView, name='contact'),
    url(r"^accounts/login/$", views.LoginView.as_view(), name="account_login"),
    url(r"^accounts/signup/$", views.SignupView.as_view(), name="account_signup"),
    re_path(r'^accounts/', include('account.urls')),
    re_path(r'^', include('blog.urls')),
    re_path(r'^service/', include('sales.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r"^profile/", include('usext.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

