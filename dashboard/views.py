# dashboard/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import PreTest, PostTest
from .models import Dashboard
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse

@login_required  # Use this decorator to ensure that only authenticated users can access the dashboard

def dashboard(request):
    user = request.user
    dashboard_instance, created = Dashboard.objects.get_or_create(user=user)

    # Check if instances exist for pre-test and post-test for the logged-in user
    pre_test_instance = PreTest.objects.filter(user=user).exists()
    post1_exists = PostTest.objects.filter(user=user, post1_answers__isnull=False).exists()
    post2_exists = PostTest.objects.filter(user=user, post2_answers__isnull=False).exists()
    post3_exists = PostTest.objects.filter(user=user, post3_answers__isnull=False).exists()
    post4_exists = PostTest.objects.filter(user=user, post4_answers__isnull=False).exists()

    return render(request, 'accounts/dashboard.html', {
        'pre_test_instance': pre_test_instance,
        'post1_exists': post1_exists,
        'post2_exists': post2_exists,
        'post3_exists': post3_exists,
        'post4_exists': post4_exists,
        'p1_checked': dashboard_instance.p1_checked,
        'p2_checked': dashboard_instance.p2_checked,
        'p3_checked': dashboard_instance.p3_checked,
        'p4_checked': dashboard_instance.p4_checked,
    })


@csrf_exempt
def update_practice_question_status(request):
    if request.method == 'POST':
        checked = int(request.POST.get('checked', 0))
        lesson_number = int(request.POST.get('lessonNumber', 0))
        
        # Assuming you have a Dashboard model
        dashboard_instance, created = Dashboard.objects.get_or_create(user=request.user)
    
        # Update the corresponding practice question attribute based on the lesson number
        if lesson_number == 1:
            dashboard_instance.p1_checked = checked
        elif lesson_number == 2:
            dashboard_instance.p2_checked = checked
        elif lesson_number == 3:
            dashboard_instance.p3_checked = checked
        elif lesson_number == 4:
            dashboard_instance.p4_checked = checked
        
        dashboard_instance.save()

        # Return success response
        return JsonResponse({'success': True, 'checked': checked})

    # Return error response if request method is not POST
    return JsonResponse({'success': False, 'error': 'Invalid request method'})