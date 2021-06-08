from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class ChangePasswordForm(forms.Form):
    password = forms.CharField(min_length=8)

class MakeAssignmentsForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=250)
