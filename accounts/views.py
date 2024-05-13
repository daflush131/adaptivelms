# accounts/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import LoginForm,  CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.conf import settings
from learncontent.kmeans import perform_clustering, plot_clusters


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

database_data = [
        [222, 85, 20],
        [233, 70, 15],
        [100, 90, 25],
        [344, 60, 10],
        [343, 95, 30],
        [643, 55, 12],
        [222, 85, 20],
        [233, 70, 15],
        [100, 90, 25],
        [344, 60, 10],
        [343, 95, 30],
        [643, 55, 12],
        [222, 85, 20],
        [233, 70, 15],
        [100, 90, 25],
        [344, 60, 10],
        [343, 95, 30],
        [643, 55, 12],
        [222, 85, 20],
        [233, 23, 15],
        [100, 90, 25],
        [344, 60, 10],
        [343, 95, 30],
        [643, 55, 12],
        [222, 85, 40]
    ]

num_clusters = 3
clusters, centroids, student_cluster_mapping = perform_clustering(num_clusters,database_data)

## Initialize an empty list to store the data
data = []
# Loop through the student_cluster_mapping dictionary
for user_id, cluster in student_cluster_mapping.items():
    # Append the user_id and cluster as a list to the data list
    data.append([user_id, cluster]) 
print(data)
plot_clusters(clusters, centroids)