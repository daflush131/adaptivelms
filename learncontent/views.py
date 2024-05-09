# learncontent/views.py
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from accounts.models import ILSResult, UserProfile, PreTest, Difficulty
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
import os, json, random
from django.conf import settings
from django.urls import reverse
from django.views.decorators.http import require_GET
from .kmeans import perform_clustering


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
        redirect_view_name = 'learncontent:learncontent'
        redirect_url = reverse(redirect_view_name)
        alert_script = f'<script> window.location.href = "{redirect_url}";</script>'
        return HttpResponse(alert_script)

    # If request method is not POST, return bad request
    return HttpResponseBadRequest("Invalid request method")
    


@login_required
def check_answers(request):
    if request.method == 'POST':
        # Get the selected values from the request
        user_answers = list(map(int, request.POST.getlist('answers[]')[1:]))  # Start from index 1
        lesson_number = request.POST.get('lesson_number')
        problem_solving = list(map(int, request.POST.getlist('problem_solving[]')))  # Convert to integers

        # Fetch the PreTest instance for the current user if it exists
        pretest_instance, created = PreTest.objects.get_or_create(user=request.user)

        # Get the answer key based on the lesson number
        answer_keys = {
            '1': [1, 0, 2, 3, 1, 3, 1, 1, 2, 1, 0, 0, 2, 3, 0, 3, 0, 2, 3, 3],  
            '2': [0, 1, 2, 3, 1, 3, 1, 2, 0, 3, 2, 1, 2, 3, 1, 3, 1, 2, 0, 3],  
            '3': [0, 1, 2, 0, 1, 1, 1, 0, 2, 2, 1, 2, 1, 3, 3, 2, 0, 3, 0, 0],  
            '4': [2, 1, 1, 3, 0, 2, 0, 1, 1, 0, 3, 3, 0, 2, 0, 1, 2, 1, 1, 3], 
            # Add answer keys for other lessons as needed
        }

        # Check if the lesson number is valid
        if lesson_number in answer_keys:
            answer_key = answer_keys[lesson_number]

            # Ensure that both user_answers, answer_key, and problem_solving have the same length
            if len(user_answers) == len(answer_key) == len(problem_solving):
                identification_score = 0
                problem_solving_score = 0
                correct_item = 0

                for user_answer, key_answer, solving in zip(user_answers, answer_key, problem_solving):
                    if user_answer == key_answer:  # Check if the user's answer matches the key answer
                        if solving == 0:  # Identification question
                            identification_score += 1  # Add 1 point for each correct identification answer
                            correct_item += 1
                            
                        else:  # Problem-solving question
                            problem_solving_score += 3  # Add 3 points for each correct problem-solving answer
                            correct_item += 1

                # Update the relevant scores and answers in the PreTest instance
                setattr(pretest_instance, f'score{lesson_number}', identification_score + problem_solving_score)
                setattr(pretest_instance, f'items{lesson_number}', correct_item)
                setattr(pretest_instance, f'l{lesson_number}_answers', user_answers)
                pretest_instance.save()

                # Return the total score as a JSON response
                return JsonResponse({'total_score': identification_score + problem_solving_score, 'correct_items': correct_item})
            else:
                # If lengths don't match, return error
                return HttpResponseBadRequest('Number of answers does not match answer key or solving values')
        else:
            # If lesson number is invalid, return error
            return HttpResponseBadRequest('Invalid lesson number')

    # If the request method is not POST, return error
    return HttpResponseBadRequest('Invalid request')


def check_pretest_completed(lesson_number):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            pretest_instance = PreTest.objects.filter(user=request.user).first()
            if pretest_instance and getattr(pretest_instance, f'l{lesson_number}_answers', None):
                return view_func(request, *args, **kwargs)
            else:
                redirect_view_name = 'learncontent:learncontent'
                redirect_url = reverse(redirect_view_name, kwargs={'lesson_number': lesson_number})
                alert_message = f'Complete the Pre-Test for Lesson {lesson_number} first.'
                alert_script = f'<script>alert("{alert_message}"); window.location.href = "{redirect_url}";</script>'
                return HttpResponse(alert_script)
        return _wrapped_view
    return decorator

@login_required
@check_pretest_completed(1)
def lesson1(request):
    return render(request, 'learncontent/lesson1/lesson1.html')

@login_required
@check_pretest_completed(2)
def lesson2(request):
    return render(request, 'learncontent/lesson2/lesson2.html')

@login_required
@check_pretest_completed(3)
def lesson3(request):
    return render(request, 'learncontent/lesson3/lesson3.html')

@login_required
@check_pretest_completed(4)
def lesson4(request):
    return render(request, 'learncontent/lesson4/lesson4.html')

def pretest(request, lesson_number):
    # Fetch the PreTest instance for the current user and lesson number
    pretest_instance = PreTest.objects.filter(user=request.user).first()

    # Check if the PreTest instance exists and if the user has already completed the pre-test for the specified lesson
    if pretest_instance and getattr(pretest_instance, f'l{lesson_number}_answers', None):
        # If the user has already completed the pre-test for this lesson, construct a redirect URL
        redirect_view_name = 'learncontent:learncontent'
        redirect_url = reverse(redirect_view_name)  # Adjust the URL to your desired learncontent view
        alert_message = f'You have already completed the pre-test for Lesson {lesson_number}.'
        alert_script = f'<script>alert("{alert_message}"); window.location.href = "{redirect_url}";</script>'
        return HttpResponse(alert_script)
    
    else:
        # If the user hasn't completed the pre-test for this lesson or the PreTest instance doesn't exist, redirect to the original destination
        return render(request, 'learncontent/tests.html')

@login_required
def practice_questions(request, lesson_number):
    user_profile = UserProfile.objects.get(user=request.user)
    
    # Determine the lesson field name
    lesson_field_name = f"lesson{lesson_number}"
    
    # Get the Difficulty instance for the user
    difficulty_instance = Difficulty.objects.get(user=user_profile.user)
    
    # Retrieve the difficulty for the specific lesson number
    difficulty = getattr(difficulty_instance, lesson_field_name, None)
    
    if difficulty is not None:  # Check if difficulty is not None
        # Map cluster numbers to difficulty levels
        if 0 < difficulty <= 3:
            difficulty = ["easy", "medium", "hard"][difficulty - 1]
    else:
        # Redirect to pretest if difficulty for the specific lesson is not set
        redirect_view_name = 'learncontent:pretest'
        redirect_url = reverse(redirect_view_name, kwargs={'lesson_number': lesson_number})
        alert_message = f'All students must answer the pre test first '
        alert_script = f'<script>alert("{alert_message}"); window.location.href = "{redirect_url}";</script>'
        return HttpResponse(alert_script)
    
    context = {
        'user_profile': user_profile,
        'lesson_number': lesson_number,
        'difficulty': difficulty,
    }
    return render(request, 'learncontent/practice.html', context)


