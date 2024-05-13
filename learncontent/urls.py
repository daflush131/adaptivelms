# learncontent/urls.py
from django.urls import path
from .views import (learncontent,lesson1,lesson2,lesson3,lesson4,
    ils,save_learningstyle,pretest,posttest,check_answers,practice_questions)

app_name = 'learncontent'

urlpatterns = [
    path('', learncontent, name='learncontent'),
    path('lesson1/', lesson1, name='lesson1'),
    path('lesson2/', lesson2, name='lesson2'),
    path('lesson3/', lesson3, name='lesson3'),
    path('lesson4/', lesson4, name='lesson4'),
    path('ils/',ils,name='ils'),
    path('save_scores/', save_learningstyle, name='save_scores'),
    path('lesson<int:lesson_number>/pretest/', pretest, name='pretest'),
    path('check_answers/', check_answers, name='check_answers'),
    path('lesson<int:lesson_number>/practice/', practice_questions, name='practice_questions'),
    path('lesson<int:lesson_number>/posttest/', posttest, name='posttest'),
    

]
