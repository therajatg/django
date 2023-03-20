from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from signup_app.models import User

class NewUser(forms.ModelForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.first_name = self.cleaned_data['first_name']
        instance.last_name = self.cleaned_data['last_name']
        instance.email = self.cleaned_data['email']
        if commit:
            instance.save()
        return instance