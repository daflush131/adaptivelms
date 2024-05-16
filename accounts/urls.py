from django.urls import path
from .views import CustomLoginView, edit_profile, CustomLogoutView, checkpass, change_password
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', edit_profile, name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', checkpass, name='checkpassword'),
    path('changepassword/', change_password, name='changepassword' )

    # Add other accounts-related URLs as needed
]
