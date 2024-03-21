# learncontent/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required 
def learncontent(request):
    #lessons logic goes here
    return render(request, 'learncontent/main.html')

@login_required
def ils(request):
    result = []
    return render(request, 'learncontent/ils.html',{'result': result})

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