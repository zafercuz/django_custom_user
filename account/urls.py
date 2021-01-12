from django.urls import path

from account import views

urlpatterns = [
    path('get-users', views.connect_user, name="get-users")
]
