from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.sessions.models import Session
from .camera import VideoCamera  # Ensure you have a camera module
import pandas as pd
import cv2
import os
from .camera import music_rec
import json
import numpy as np
import cv2
import os
from keras.models import model_from_json
from .models import Customer
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import re

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# model_path = os.path.join(BASE_DIR, 'myapp', 'models',
#                           'emotion_model', 'emotion_model.json')
# weight_path = os.path.join(BASE_DIR, 'myapp', 'models',
#                            'emotion_model', 'emotion_model.h5')

# # Load JSON model
# json_file = open(model_path, 'r')
# loaded_model_json = json_file.read()
# json_file.close()

# # Load weights into the model
# emotion_model = model_from_json(loaded_model_json)
# emotion_model.load_weights(weight_path)

# Sample user data
users = {'username': 'password'}
df1 = music_rec().head(15)  # Assuming music_rec() is defined somewhere

def index(request):
    global df1
    return render(request, 'index.html', {'data': df1.to_json(orient='records')})

def face_feed(request):
    return render(request, 'index.html')

def user_feedback(request):
    
    data = Customer.objects.all()
    return render(request, 'userFeedback.html', {'data':data})

def home(request):
    if request.method =='POST':
        data = request.POST
        name = data['name']
        email = data['email']
        message = data['message']
        
        Customer.objects.create(name=name, email=email, message = message)
        messages.success(request , ("Message was sent succesfully !"))
        return render(request, 'landingpage.html')
    return render(request, 'landingpage.html')

def delete_user(request, id):
    data = Customer.objects.get(id=id)
    #data.isDelete = True
    data.delete()
    #data.save()
    return redirect('feedback')
    

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
    while True:
        global df1
        frame, df1 = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_table(request):
    return JsonResponse(df1.to_json(orient='records'), safe=False)

# User Authenticaton

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not email.endswith('@gmail.com'):
            messages.error(request, 'Email must be a @gmail.com address.')
        
        elif not re.match(r'^[a-zA-Z0-9_]+$', username):
            messages.error(request, 'Username can only contain alphanumeric characters and underscores.')
        elif username.isdigit():
            messages.error(request, 'Username cannot be only numbers.')

        elif len(password1) < 8 or not re.search(r'[A-Z]', password1) or not re.search(r'[a-z]', password1) \
                or not re.search(r'[0-9]', password1) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            messages.error(request, 'Password must be at least 8 characters long, include uppercase and lowercase letters, a number, and a special character.')

        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')

        # Check if email is already registered
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')

        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')

    return render(request, 'login.html')



def login_user(request):
    if request.method  == 'POST':
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('home')
        else:
                messages.success(request , ("There was error Logging In, Try Again!"))
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request , ("You were Logged Out!"))
    return redirect('home')

