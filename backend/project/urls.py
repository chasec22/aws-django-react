"""
URL configuration for roulettech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from accounts import views

# PASSWORD 12345

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AccountView.as_view(), name="Account"),
    re_path(r'^([0-9])$', views.delete_account)
    #re_path(r'^([0-9])$', AccountView.as_view(), name="Account")
]
