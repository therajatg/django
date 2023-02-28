from django.shortcuts import render
from formapp.forms import MyForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'formapp/index.html')

def myform_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)

        if form.is_valid():
            # form.cleaned_data['email'] == form.cleaned_data['verify_email']
            print("Validation Success")
            print("Name", form.cleaned_data['name'])
            print("Email", form.cleaned_data["email"])
            print("Text", form.cleaned_data['text'])
            return HttpResponse("Here's the text of the web page.")
        else:
            print("Form is invalid --- ")
    return render(request, 'formapp/form_page.html', {"form": MyForm()})
