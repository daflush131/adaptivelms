# accounts/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import LoginForm, UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.conf import settings
from learncontent.kmeans import perform_clustering, plot_clusters
from .models import PreTest, Difficulty, ClusterResults
from django.contrib.auth.hashers import check_password

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'accounts:login'  # Specify the login URL after logout

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have been successfully logged out.')  # Add a success message
        return super().dispatch(request, *args, **kwargs)

def checkpass(request):
    if check_password('P@ssw0rd12', request.user.password):
        return redirect('accounts:changepassword')
    else:
        return render(request,'accounts/dashboard.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to prevent logout
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/changepass.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid() and password_form.is_valid():
            form.save()
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form, 'password_form': password_form})

""" #K-Means Clustering for Each Student
lesson1 = [list(item) for item in PreTest.objects.values_list('score1', 'items1')]
lesson2 = [list(item) for item in PreTest.objects.values_list('score2', 'items2')]
lesson3 = [list(item) for item in PreTest.objects.values_list('score3', 'items3')]
lesson4 = [list(item) for item in PreTest.objects.values_list('score4', 'items4')]
l1 = "Lesson 1"
l2 = "Lesson 2"
l3 = "Lesson 3"
l4 = "Lesson 4"
lesson1_data = []
lesson2_data = []
lesson3_data = []
lesson4_data = []

user_id = 1
num_clusters = 3

# Lesson 1
clusters, centroids, student_cluster_mapping = perform_clustering(num_clusters, lesson1)
lesson1_data = [(student, cluster) for student, cluster in student_cluster_mapping.items()]
lesson1_results, _ = ClusterResults.objects.get_or_create(user_id=user_id, defaults={'clesson1': lesson1_data})
lesson1_results.clesson1 = lesson1_data
lesson1_results.save()
plot_clusters(clusters, centroids, l1)

# Lesson 2
clusters, centroids, student_cluster_mapping = perform_clustering(num_clusters, lesson2)
lesson2_data = [(student, cluster) for student, cluster in student_cluster_mapping.items()]
lesson2_results, _ = ClusterResults.objects.get_or_create(user_id=user_id, defaults={'clesson2': lesson2_data})
lesson2_results.clesson2 = lesson2_data
lesson2_results.save()
plot_clusters(clusters, centroids, l2)

# Lesson 3
clusters, centroids, student_cluster_mapping = perform_clustering(num_clusters, lesson3)
lesson3_data = [(student, cluster) for student, cluster in student_cluster_mapping.items()]
lesson3_results, _ = ClusterResults.objects.get_or_create(user_id=user_id, defaults={'clesson3': lesson3_data})
lesson3_results.clesson3 = lesson3_data
lesson3_results.save()
plot_clusters(clusters, centroids, l3)

# Lesson 4
clusters, centroids, student_cluster_mapping = perform_clustering(num_clusters, lesson4)
lesson4_data = [(student, cluster) for student, cluster in student_cluster_mapping.items()]
lesson4_results, _ = ClusterResults.objects.get_or_create(user_id=user_id, defaults={'clesson4': lesson4_data})
lesson4_results.clesson4 = lesson4_data
lesson4_results.save()
plot_clusters(clusters, centroids, l4)
"""

# Fetch ClusterResults for user 1
try:
    cluster_results_user1 = ClusterResults.objects.get(user_id=1)
except ClusterResults.DoesNotExist:
    cluster_results_user1 = None

# Fetch pretest results for all users except user id 1
pretests = PreTest.objects.exclude(user_id=1)

# Iterate through each pretest
for pretest in pretests:
    user = pretest.user
    
    # Iterate through each lesson in the pretest
    for lesson_num in range(1, 5):
        pretest_score_field = f"score{lesson_num}"
        pretest_items_field = f"items{lesson_num}"
        pretest_score = getattr(pretest, pretest_score_field)
        pretest_items = getattr(pretest, pretest_items_field)

        if cluster_results_user1 is not None:
            # Fetch clustered results for user 1 for the lesson
            cluster_field = f"clesson{lesson_num}"
            cluster_data = getattr(cluster_results_user1, cluster_field, [])
        else:
            cluster_data = []

        # Compare pretest scores with clustered results for the lesson
        for cluster_entry in cluster_data:
            cluster_score, cluster_items = cluster_entry[0]
            cluster_cluster = cluster_entry[1]

            # Check if pretest score matches clustered result
            if pretest_score == cluster_score and pretest_items == cluster_items:
                # Update or create instance of Difficulty model
                difficulty, _ = Difficulty.objects.get_or_create(user=user)
                setattr(difficulty, f"lesson{lesson_num}", cluster_cluster)
                difficulty.save()