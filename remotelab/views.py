# remotelab/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def remotelab(request):
    if request.user.id != 1:
        return HttpResponseForbidden("You don't have permission to access this page.")
    # Your dashboard logic goes here
    
    return render(request, 'remotelab/remotelab.html')

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Disable CSRF protection for simplicity. In a production environment, use a proper setup.
def receive_time(request):
    if request.method == 'POST':
        try:
            time_data = json.loads(request.body.decode('utf-8'))
            received_time = time_data.get('time')
            # Do something with the received time, such as saving it to the database
            print("Received time:", received_time)
            return HttpResponse("Data received successfully")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data", status=400)
    else:
        return HttpResponse("Method not allowed", status=405)