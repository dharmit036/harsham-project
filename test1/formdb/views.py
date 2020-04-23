# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from formdb.forms import userform
from .models import *
# Create your views here.

def index(request):
    return render(request,"index.html")
'''
def register(request):
    if request.method=='POST':
        user= userform(request.POST)
        if user.is_valid():
            print('Data is added')
            print(user.	cleaned_data)
            user.save(commit=False)
            user.save()
            return redirect('admin/')
#            return render(request,"success.html",{'form':user})
        else:
            print("Somthing is happened wrong!!!!")
  #          return render(request,"success.html",{'form':user})
    else:
        user=userform()
   #     return render(request,"success.html",{'form':user})
    #user.save()
    return render(request,"register.html",{'form':user})
'''


def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname'].encode('ascii')
        lastname=request.POST['lastname'].encode('ascii')
        email=request.POST['email'].encode('ascii')
        mobile=request.POST['mobile'].encode('ascii')	
        carnumber=request.POST['carnumber'].encode('ascii')
        carmodel=request.POST['carmodel'].encode('ascii')
        lastservice=request.POST['lastservice'].encode('ascii')
        serviceintime=request.POST['serviceintime'].encode('ascii')
        predictedtime=request.POST['predictedtime'].encode('ascii')
       

        user1=userdata.objects.create(firstname=firstname,lastname=lastname,email=email,mobile=mobile,carnumber=carnumber,carmodel=carmodel,lastservice=lastservice,serviceintime=serviceintime,predictedtime=predictedtime)
        user1.save()
        return redirect('/admin/')
    else:
        print('Error from getting Requests!!!!')
    return render(request,'register.html')