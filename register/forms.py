from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length = 200, required= False)
    last_name = forms.CharField(max_length = 200, required= False)
    email = forms.EmailField(required= True)
    date_of_birth = forms.DateField(widget= forms.DateInput(attrs = {'type':'date'}))
    # date_of_birth = forms.DateField(widget= forms.SelectDateWidget)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2","date_of_birth"]
        # for the form without username field
        # fields = ["first_name","last_name","email","password1","password2"]
        # exclude = ['username'] # for excluding or not displaying the username field in the form
