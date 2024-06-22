from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'email']

        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Username',
        #
        #     }),
        #     'email': forms.EmailField(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Email',
        #
        #     }),
        #     'password1': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Password',
        #
        #     }),
        #     'password2': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Confirm Password',
        #
        #     }),
        #
        # }
