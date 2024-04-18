# learncontent/views.py
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import ILSResult, UserProfile
from django.http import HttpResponseBadRequest

@login_required 
def learncontent(request):
    #lessons logic goes here
    return render(request, 'learncontent/main.html')

@login_required
def ils(request):
    return render(request, 'learncontent/ils.html')

@login_required
def save_learningstyle(request):
    if request.method == 'POST':
        # Extract data from the POST request
        first = request.POST.get('first', None)
        second = request.POST.get('second', None)
        third = request.POST.get('third', None)
        fourth = request.POST.get('fourth', None)
        
        print("First:", first)
        print("Second:", second)
        print("Third:", third)
        print("Fourth:", fourth)
        # Check if all data is provided
        if None in [first, second, third, fourth]:
              return JsonResponse({'error': 'Invalid data'})

        # Create and save the ILSResult object
        ils_result = ILSResult.objects.create(
            user=request.user,  # Assuming user is authenticated
            first=first,
            second=second,
            third=third,
            fourth=fourth
        )
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile.learning_style = first  # Assuming 'first' contains the learning style value
        user_profile.save()

        # Redirect to a success page or perform any other action
        return redirect('success_url')  # Replace 'success_url' with the URL of your success page

    # If request method is not POST, return bad request
    return HttpResponseBadRequest("Invalid request method")
    

@login_required
def lesson1(request):
    return render(request, 'learncontent/lesson1/lesson1.html')

@login_required
def lesson2(request):
    return render(request, 'learncontent/lesson2/lesson2.html')

@login_required
def lesson3(request):
    return render(request, 'learncontent/lesson3/lesson3.html')

@login_required
def lesson4(request):
    return render(request, 'learncontent/lesson4/lesson4.html')