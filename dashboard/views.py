# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Use this decorator to ensure that only authenticated users can access the dashboard
def dashboard(request):
    # Your dashboard logic goes here
    return render(request, 'accounts/dashboard.html')