# remotelab/urls.py

from django.urls import path
from .views import remotelab, receive_time

app_name = 'remotelab'

urlpatterns = [
    path('', remotelab, name='remotelab'),
    path('your-endpoint/', receive_time, name='receive_time'),

]
