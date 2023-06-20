from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    middle_name = forms.CharField(max_length=101)
    mobile_no = forms.CharField(max_length=101)
    
    class Meta:
        model = User
        fields = ['username','first_name','middle_name','last_name','mobile_no','email','password1','password2']