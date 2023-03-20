from django.shortcuts import render
from signup_app.forms import NewUser
from django.http import HttpResponse
from first_app.views import index

# Create your views here.

def signup_view(request):
    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            # form.cleaned_data['email'] == form.cleaned_data['verify_email']
            form.save()
            return index(request)
            # print("Validation Success")
            # print("First Name", form.cleaned_data['first_name'])
            # print("Last Name", form.cleaned_data['last_name'])
            # print("Email", form.cleaned_data["email"])
            # return HttpResponse("Here's the text of the web page.")
        else:
            print("Form is invalid --- ")
    else:
        form = NewUser()
    return render(request, 'signup_app/signup.html', {"form": form})
