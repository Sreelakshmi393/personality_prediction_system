from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import *
from pyresparser import ResumeParser

import json
import en_core_web_sm
from test_code import test

def resume_data(path):
    data = ResumeParser(path).get_extracted_data()
    name=data["name"]
    email=data["email"]
    mob=data["mobile_number"]
    skills=data["skills"]
    experience=data["experience"]
    designation=data["designation"]
    degree=data["degree"]
    total_exp=data["total_experience"]
    companies=data["company_names"]
    name="Not Avilable" if name is None else name
    email="Not Avilable" if email is None else email
    mob="Not Avilable" if mob is None else mob
    skills="Not Avilable" if skills is None else skills
    experience="Not Avilable" if experience is None else experience
    designation="Not Avilable" if designation is None else designation
    degree="Not Avilable" if degree is None else degree
    total_exp="Not Avilable" if total_exp is None else total_exp
    companies="Not Avilable" if companies is None else companies
    data_json=json.dumps(data)
    return name,email,mob,skills,experience,designation,degree,total_exp,companies,data_json

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
    
     
 
    
def regi(request):
    return render(request,'register.html')    
    
    
    
def addreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=reg(name=name,email=email,password=password)
        user.save()
    return render(request,'register.html')
 

def dash(request):
    return render(request,'admin/index.html')
    
     
def login(request):
    return render(request,'login.html')
    
     
def logint(request):
    email = request. POST.get('email')
    password = request.POST.get('password')
   # print(email)
    if email == 'admin@gmail.com' and password == 'admin':
        request.session['logintdetail'] = email
        request.session['logint'] = 'admin'
        print ("ello")
        return render(request, 'admin/index.html')

    elif reg.objects.filter(email=email,password=password).exists():
        userdetails=reg.objects.get(email=email, password=password)
        request.session['uid'] = userdetails.id
        
        return render(request,'index.html')  


        
    else:
        return render(request, 'login.html', {'status': 'INVALID USERID OR PASSWORD'})           


  
         
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)  

def viewjobadmin(request):
    sel=posts.objects.all()
    return render(request,'admin/viewjob.html',{'res':sel})

def deletejobpost(request,id):
    post=posts.objects.get(id=id)
    post.delete()
    return redirect(viewjobadmin)


def post(request):
    return render(request,'admin/joobpool.html')
    
def addpost(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        date=request.POST.get('date')
        user=posts(name=name,description=description,date=date)
        user.save()
    return render(request,'admin/joobpool.html')
       


def viewpost(request):
    sel=posts.objects.all()
    return render(request,'viewjob.html',{'res':sel})     
    
           
       

def apply(request,id):
    sel=posts.objects.get(id=id)
    return render(request,'applyjoob.html',{'res':sel})     
    
    
"""def jobposts(request):
    if request.method == 'POST':
        job_id=request.POST.get('job_id')
        
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
       
        emp=upload(userid=request.session['uid'],job_id=job_id,image=filename)    
        emp.save()
    return render(request,'applyjoob.html')
   """ 
    
def jobposts(request):
    if request.method == 'POST':
        job_id=request.POST.get('job_id')
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        print("flg1")
        name,email,mob,skills,experience,designation,degree,total_exp,companies,data_json=resume_data("media/{}".format(myfile.name))
        print("flg2")
        print("DataType:",type(experience))
        personality=test.predict("media/{}".format(myfile.name))
        #print(name,email,mob,skills,experience,designation,degree,total_exp,companies,data_json,personality)
        user=upload(userid=request.session['uid'],job_id=str(job_id),name=name,email=email,phone=mob,skill=skills,experience=str(experience),jsondata=data_json,image=filename,personality=personality)
        user.save()
        #return render(request,'admin/viewresume.html')
        sel=posts.objects.all()
        return render(request,'viewjob.html',{'res':sel,'status':'registered succesfully'})
    
    
    
def viewjobpost(request):
    sel=upload.objects.all()
    return render(request,'admin/viewresume.html',{'res':sel})