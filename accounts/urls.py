from django.urls import path
from .views import CustomLoginView, update_profile_view, CustomLogoutView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('updateprofile', update_profile_view, name='updateprofile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Add other accounts-related URLs as needed
]
