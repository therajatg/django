from django.shortcuts import render
from first_app.models import User

# Create your views here.
def user_func(request):
    user_dict = {"users": User.objects.order_by("first_name")}
    return render(request, "first_app/user.html", context=user_dict)

def index(request):
    return render(request, "index.html")