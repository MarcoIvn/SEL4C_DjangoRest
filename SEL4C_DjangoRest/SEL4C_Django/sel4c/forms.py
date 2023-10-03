from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from django import forms    

class RegisterAdministratorForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    
    class Meta:
        model = Administrator
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')


class ChangeAdministratorForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)

    class Meta(UserChangeForm.Meta):
        model = Administrator  
        fields = ('username', 'first_name', 'last_name', 'email')


class ChangePassword(PasswordChangeForm):
    class Meta:
        model = Administrator
        fields = ['old_password', 'new_password1', 'new_password2']