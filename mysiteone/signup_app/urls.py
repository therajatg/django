from django.urls import path
from signup_app import views

urlpatterns = [
    path('', views.signup_view),
]
