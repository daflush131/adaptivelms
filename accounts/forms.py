# accounts/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Student-No'}),
        label='Student No'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password'}),
        label='Password'
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(UserProfileForm(*args, **kwargs).fields)

    def save(self, commit=True):
        user = super().save(commit)
        profile_form = UserProfileForm(self.cleaned_data, instance=user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
        return user