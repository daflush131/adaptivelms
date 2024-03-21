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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['course', 'yearandsection']
        widgets = {
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg. BS Computer Engineering, BS Electrical Engineering, ...', 'id': 'course'}),
            'yearandsection': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg. 1-1,1-2,...1-6', 'id': 'year'}),
        }

class UserMainForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserMainForm, self).__init__(*args, **kwargs)

        # Set attributes for the username field
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '2024-13397-MN-1',
            'id': 'studentNo',
        })

        # Set attributes for the email field
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'youremail@domain.com',
            'id': 'email',
        })

        # Set attributes for the first_name field
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter first name',
            'id': 'firstName',
        })

        # Set attributes for the last_name field
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter last name',
            'id': 'lastName',
        })

        # Set attributes for the password1 field
        self.fields['password1'].widget.attrs.update({
            'type':'password',
            'class': 'form-control',
            'placeholder': 'Enter password',
        })

        # Set attributes for the password2 field
        self.fields['password2'].widget.attrs.update({
            'type':'password',
            'class': 'form-control',
            'placeholder': 'Confirm password',
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

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