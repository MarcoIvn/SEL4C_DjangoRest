from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from django import forms    

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')


class ChangeUserForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ChangePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']