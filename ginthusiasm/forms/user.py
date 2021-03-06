from django import forms
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password'}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {'profile_image'}
