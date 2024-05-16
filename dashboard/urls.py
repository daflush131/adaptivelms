# dashboard/urls.py

from django.urls import path
from .views import dashboard, update_practice_question_status

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('update/', update_practice_question_status, name='update'),
    # Add other dashboard-related URLs as needed
]
