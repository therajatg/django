from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


    #No need for this now as this we simply achieved by using djnago's in-built validators in the botcatcher field itself.
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha Bot")
    #     return botcatcher


    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data.get('email', None)
    #     vmail = all_clean_data.get('verify_emil', None)
    #     if email != vmail:
    #         # raise ValidationError("Make sure emails match")
    #         raise forms.ValidationError("Make sure emails match")


# Note that some validation is automatic like when we said EmailField, Django knows that email will come in that field  and for other validators like for example email and verify_email should be same, we write function.