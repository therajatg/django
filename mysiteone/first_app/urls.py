from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index),
    path('users', views.user_func)
]
