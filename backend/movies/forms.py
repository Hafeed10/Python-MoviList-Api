from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']




class SignUpForm(forms.ModelForm): 
    class Meta:
        model = User  
        fields = ['username', 'email', 'password']  

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalnum():
            raise forms.ValidationError("Username can only contain letters and numbers.")
        return username