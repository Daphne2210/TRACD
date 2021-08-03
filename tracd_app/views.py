from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
from .decorators import check_recaptcha
import time
import pyttsx3
from playsound import playsound
from .forms import Booking_Form


from .models import *

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

 
path = 'images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
    
def detector(request):
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
 
    cap = cv2.VideoCapture(0)
 
    while True:
        success, img = cap.read()
        
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
     
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
 
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
       
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                
                substring="CRIMINAL"
                if name.find(substring) != -1:    
                    playsound('alarm.mp3')
                    return render(request,'tracd_app/alert.html')
                if matches[0]:
                    print(matches[0])
                    return render(request,'tracd_app/entry2.html')
                
                

            #if matches[0]:
            #  substring='CRIMINAL'
#  fullstring=str(name)
#fullstring.find(substring) != -1
            #   if name=="CRIMINAL":
            #        playsound('alarm.mp3')
            #        return render(request,'tracd_app/alert.html')
            #    else:
    
            #        return render(request,'tracd_app/entry2.html')
            #else:
             #   return render(request,'tracd_app/exit.html')
       
    cv2.imshow('Webcam',img)
    cv2.waitKey(0)


def home(request):
    return render(request,'tracd_app/dashboard.html')
   

def schedule_view(request,*args,**kwargs):
	schedule=Schedule.objects.all()
	return render(request,"tracd_app/schedule.html",{'schedule':schedule})


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "tracd_app/login.html", context)

@check_recaptcha
def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid() and  request.recaptcha_is_valid:
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    
    context = {
        'form': form,
    }
    return render(request, "tracd_app/signup.html", context)


def logout_view(request):
    logout(request)#inbuilt function
    return redirect('/')

def Book_view(request,*args,**kwargs):
    form=Booking_Form()
    if request.method=='POST':
        form=Booking_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'tracd_app/dashboard.html')
    context={'form':form}
    return render(request, "tracd_app/book.html", context)

def instruction(request):
    engine = pyttsx3.init()
    engine.say('Initially you need to login in to Metrorails to make your booking. If you dont have an account , click on signup.    After registration , login to the website and click "book here" to make your bookings.      Give in your inputs  along with your   image and your  done to go ')
    engine.runAndWait()
    return render(request,'tracd_app/instruction.html')

