"""CustomUser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from account.views import CustomPasswordChangeView, custom_password_change_done

urlpatterns = [
    path('admin/password_change/done/', custom_password_change_done, name='password_change_done'),
    path('admin/password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('admin/', admin.site.urls),
    path('user/', include('account.urls'))
]

admin.site.site_header = "Honda Motor World Admin"
admin.site.site_title = "Honda Motor World Admin Portal"
