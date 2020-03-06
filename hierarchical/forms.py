from django import forms
from hierarchical.models import File


class TreeForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['name', 'parent']


# class SignupForm(forms.Form):
#     username = forms.CharField(max_length=30)
#     password = forms.CharField(max_length=30)


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=30)
#     password = forms.CharField(max_length=30)
