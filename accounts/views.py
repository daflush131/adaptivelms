# accounts/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import LoginForm, UserProfileForm, UserMainForm, CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.conf import settings


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:dashboard')
        return super().get(request, *args, **kwargs)

class CustomLogoutView(LogoutView):
    next_page = 'accounts:login'  # Specify the login URL after logout

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have been successfully logged out.')  # Add a success message
        return super().dispatch(request, *args, **kwargs)
    
def register_view(request):
    if request.method == 'POST':
        user_form = UserMainForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Log in the user
            login(request, user)

            return redirect('dashboard:dashboard')

    else:
        user_form = UserMainForm()
        profile_form = UserProfileForm()

    return render(request, 'accounts/registration.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def update_profile_view(request):
    user_form = CustomUserChangeForm(instance=request.user)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard:dashboard')

    return render(request, 'accounts/edit_profile.html', {'user_form': user_form})
class CustomPasswordChangeView(PasswordChangeForm):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:edit_profile')