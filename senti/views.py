
from django.contrib import messages

from django.shortcuts import redirect
from .models import Reg,Review
from .forms import LoginForm,ForgetForm
from .forms import RegForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.base import ContentFile
from subprocess import Popen, PIPE
import commands
import os
from textblob import TextBlob
import smtplib



def forget(request):

    if request.method == "POST":
        form = ForgetForm(request.POST)
        if form.is_valid():
            Email=form.cleaned_data['Email']
            data=Reg.objects.filter(Email=Email)
            for i in data:
                pwd=i.Password
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("yassingh49@gmail.com", "yashpalpy3")
            message = pwd
            s.sendmail("yassingh49@gmail.com",Email, message) 
            s.quit()
            return render(request, 'forget.html', {'form':form,'message':'Check Your email Address, Password and Image have sent.... '})
            

    else:
            form = ForgetForm()
            print("Invalid Details")

    return render(request, 'forget.html', {'form':form})


def registration(request):
     if request.method == "POST":
        form = RegForm(request.POST,request.FILES)
        if form.is_valid():
            if Reg.objects.filter(Username=form.cleaned_data['Username']).exists():
                return render(request, 'registration.html', {
                    'form': form, 
                    'error_message': 'Username already exists.'

                })
            elif Reg.objects.filter(Email=form.cleaned_data['Email']).exists():
                return render(request, 'registration.html', {
                    'form': form, 
                    'error_message': 'Email already exists.'

                })
            else:
                obj=Reg.objects.create(**form.cleaned_data)
                print("valid Details")
                return redirect('login')

     else:
            form = RegForm()
            print("Invalid Details")

     return render(request, 'registration.html', {'form':form})

    


def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST,request.FILES)
        if form.is_valid():
            Username=form.cleaned_data['Username']
            Password=form.cleaned_data['Password']
            
            if Reg.objects.filter(Username=Username,Password=Password).exists():
                request.session['Username']= Username
                return redirect('index')
            else:
                return render(request, 'login.html', {
                    'form': form, 
                    'error_message': 'Username and Password does not matched'})

    else:
            form = LoginForm()
            print("Invalid Details")

    return render(request, 'login.html', {'form':form})

def welcome(request):
    return render(request, 'welcome.html')

def index(request):
     data=Review.objects.all()
     a=Review.objects.filter(reviewtypes='positive')
     pos=0
     for b in a:
         pos=pos+1
     print(pos)
     b=Review.objects.filter(reviewtypes='negative')
     neg=0
     for c in b:
         neg=neg+1
     print(neg)
     su=pos+neg
     print(su)
     x=pos*100/su
     print(x)
     y=neg*100/su
     print(y)
     
     
     
     return render(request, 'parent.html',{'data':data,'x':x,'y':y})

def feature(request):
    return render(request, 'feature.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def process_word(request):
    paraa = request.POST.get('review')
    name = request.session['Username']
    
    para = (TextBlob(str(paraa))).polarity
    if float(para) > 0:
        obj=Review.objects.create(user=name,review=paraa,reviewtypes='positive')
        
        
        return HttpResponse(True)
    else:
        obj=Review.objects.create(user=name,review=paraa,reviewtypes='negative')
    	return HttpResponse(False)

def features(request):
    return render(request, 'feature.html')
