from django.shortcuts import render
from formapp.forms import MyForm

# Create your views here.
def index(request):
    return render(request, 'formapp/index.html')

def myform_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name", form.cleaned_data['name'])
            print("Email", form.cleaned_data["email"])
            print("Text", form.cleaned_data['text'])
    return render(request, 'formapp/form_page.html', {"form": MyForm()})
