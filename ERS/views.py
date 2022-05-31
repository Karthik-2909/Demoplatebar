from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Q
from datetime import datetime
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from CoolerProps.settings import EMAIL_HOST_USER
from django.shortcuts import render
from ERS.demo1 import *
import math, random
from .models import *

def home(request):
    return render(request,"login.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        psw=request.POST['psw']
        user=users.objects.filter(userID=username,password=psw)
        print(len(user))
        if len(user)!=0:
            return render(request,"demo1.html")
        else:
            return render(request,"login.html",{'error':"Incorrect userId or password"})
    else:
        return render(request,"/")

def register(request):
    if request.method == 'POST':
        username = request.POST['userid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        psw1 = request.POST['psw1']
        psw2 = request.POST['psw2']

        user1=users.objects.filter(userID=username)
        user2=users.objects.filter(Email=email)
        print(user1.count())
        print(user2.count())
        if user1.count()>0:
            return render(request,"register.html",{"error":"Username is already taken"})
        elif user2.count()>0:
            return render(request,"register.html",{"error":"Mail-id is already taken"})
        elif psw1!=psw2:
            return render(request,"register.html",{"error":"Password mismatch"})
        else:
            print("Account registered successfully..")
            #request.session['username']=username
            user= users(name=name,userID=username,Email=email,Phone=phone,DOB=dob,password=psw1)
            user.save()
            ######################### mail system ####################################
            sub='welcome to SNS'
            message= f"Your registration is successful.."
            email_from= settings.EMAIL_HOST_USER
            to= [email]
            #send_mail( sub,message,email_from,to)
            return render(request,"login.html")
    else:
        return render(request,"register.html")

def forgot_password(request):
    if request.method=="POST":
        sub="Reset OTP."
        message=f'Your OTP to reset password is 123456.'
        to=["pavan0312c@gmail.com"]
        email_from=settings.EMAIL_HOST_USER
        print(email_from)
        send_mail(sub,message,email_from,to)
        return render(request,"login.html")
    else:
        return render(request,"forgot_password.html")

def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    email=request.GET.get("T_amb")
    print(email)
    o=generateOTP()
    htmlgen = '<p>Your OTP is <strong>o</strong></p>'
    print(o)
    #send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)

def sampleotp(request):
    return render(request,"smapleotp.html")

def password_trial(request):
    return render(request,"password_trial.html")

def demo1(request):
    if request.method=="POST":
        T_amb=request.POST['T_amb']
        RH_amb=request.POST['RH_amb']
        Altitude=request.POST['Altitude']
        FTPQ=request.POST['HCA']
        print(FTPQ)
        HCA=HCA_details.objects.filter(name=FTPQ)
        print(HCA)
        for i in HCA:
            data=i
        print(data.FAD)
        print(data.T_H_In)
        print(data.P_input)
        print(data.Q_input)
        (Q,Weight)=demo123(T_amb,RH_amb,Altitude,data)
        return render(request,"demo1.html",{'T_amb':T_amb,"RH_amb":RH_amb,"Altitude":Altitude,"HCA":FTPQ,"Q":Q,"Weight":Weight})
    else:
        return render(request,"demo1.html",{"Q":Q,"Weight":Weight})
        

    
def reset_password(request):
    un = request.GET["username"]
    try:
        #user = get_object_or_404(User,username=un)
        user = "Pavan"
        otp = random.randint(1000,9999)
        msz="hi...."
        #msz = "Dear {} \n{} is your One Time Password (OTP) \nDo not share it with others \nThanks&Regards \nMyWebsite".format(user.username, otp)
        try:
            #email = EmailMessage("Account Verification",msz,to=[user.email])
            #email.send()
            print("Email Sent...")
            #return JsonResponse({"status":"sent","email":user.email,"rotp":otp})
            return JsonResponse({"status":"sent","email":"abc@gmail.com","rotp":otp})
        except:
            print("Email Sent1...")
            return JsonResponse({"status":"error","email":user.email})
    except:
        print("Email Sent2...")
        return JsonResponse({"status":"failed"})

