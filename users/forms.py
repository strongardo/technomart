from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'firstname', 'lastname')