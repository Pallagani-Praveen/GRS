from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from GRSapp.models import UsersModal,ContactModel,itemslist,Mobiles
from django.contrib import messages
from GRS.randkey import randnum,genOTP
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail

import json



def GRSHome(request):
    user = request.COOKIES.get('username')
    items = itemslist.objects.all()
    if UsersModal.objects.filter(username=user).count()!=0:
        user = UsersModal.objects.get(username=user)
    params = {'user':user,'items':items}
    return render(request,'GRS/GRS.html',params)

def contact(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user).count()!=0:
        user = UsersModal.objects.get(username=user)
    params = {'user':user}
    return render(request,'GRS/contact.html',params)

def about(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user).count()!=0:
        user = UsersModal.objects.get(username=user)
    params = {'user':user}
    return render(request,'GRS/about.html',params)

def viewprofile(request):
    user = request.COOKIES.get('username')
    userobj = UsersModal.objects.get(username=user)
    print(userobj.dob)
    params = {'user':userobj,'userobj':userobj}
    return render(request,'GRS/viewprofile.html',params)

def updateprofile(request):
    if request.method == "POST":
        user = request.COOKIES.get('username')
        userobj = UsersModal.objects.get(username=user)
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['passwd']
        if userobj.firstname==firstname:
            userobj.lastname = lastname
            userobj.email = email
            userobj.password = password
            userobj.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect("/")
        else:
            username = firstname+'_'+str(randnum())
            userobj.firstname = firstname
            userobj.username = username 
            userobj.lastname = lastname
            userobj.email = email
            userobj.password = password
            userobj.save()
            response = HttpResponseRedirect("/")
            response.set_cookie('username',username,max_age=86400)
            messages.success(request,'Profile Updated Successfully and New UserId : '+username)
            return response
    else:
        return redirect("/")


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        dob = request.POST['dob']
        passwd = request.POST['passwd'] 
        genOTP = request.POST['genOTP']
        OTP = request.POST['OTP']
        user_pic = request.FILES.get('user_pic')

        

        clientkey = request.POST['g-recaptcha-response']
        securitykey = '6LeKRd4UAAAAAL0FJ8rlAskzjtiKcOtlcvLlsImk'

        capthchaData = {
            'secret':securitykey,
            'response':clientkey
        }
        
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=capthchaData)
        response = json.loads(r.text)
        verify = response['success']
        print(verify)


        if UsersModal.objects.filter(email=email).count()==0 and verify and genOTP==OTP:
            username=firstname+'_'+str(randnum())
            UsersModal.objects.create(firstname=firstname,lastname=lastname,username=username,email=email,gender=gender,user_pic=user_pic,dob=dob,password=passwd).save()
            response = HttpResponseRedirect('/')
            response.set_cookie('username',username,max_age=86400)
            messages.success(request,'Profile created successfully , UserId : '+username)
            return response
        elif not verify:
            messages.warning(request,'Check the reCAPTCHA')
            return redirect('GRSHome')  
        else:
            messages.warning(request,'Invalid OTP given')
            return redirect('GRSHome') 
    else:
        return redirect('GRSHome')

def otp(request):
    if request.method=="POST":
        user = request.COOKIES.get('username')
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        user_pic = request.FILES.get('user_pic')
        dob = request.POST['dob']
        passwd = request.POST['pass1']
        gen_otp =  genOTP()
        if UsersModal.objects.filter(email=email).count()!=0:
            messages.warning(request,'Email already exists , Profile not created')
            return redirect('GRSHome')
        send_mail('OTP from Review Service Website',
        'Your One Time Password '+str(gen_otp),
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=True)
        params = {'user':user,'fname':firstname,'lname':lastname,'email':email,'gender':gender,'dob':dob,'passwd':passwd,'user_pic':user_pic,'genOTP':gen_otp}
        return render(request,'GRS/verify_opt.html',params)
    else:
        return redirect('GRSHome')

def login(request):
    if request.method=="POST":
        id_email = request.POST['email']
        passwd = request.POST['passwd']
        if UsersModal.objects.filter(email=id_email).count()==1:
            userobj = UsersModal.objects.get(email=id_email)
            if (userobj.password==passwd):
                response = HttpResponseRedirect('/')
                response.set_cookie('username',userobj.username,max_age=86400)
                return response
            else:
                messages.warning(request,'Incorrect Password')
                return redirect('/')
        elif UsersModal.objects.filter(username=id_email).count()==1:
            userobj = UsersModal.objects.get(username=id_email)
            if (userobj.password==passwd):
                response = HttpResponseRedirect('/')
                response.set_cookie('username',userobj.username,max_age=86400)
                return response
            else:
                messages.warning(request,'Incorrect Password')
                return redirect('/')
        else:
            messages.warning(request,'Incorrect Username')
            return redirect('/')
    else:
        return redirect('/')



def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    return response

def issue(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        clientkey = request.POST['g-recaptcha-response']
        securitykey = '6LeKRd4UAAAAAL0FJ8rlAskzjtiKcOtlcvLlsImk'

        capthchaData = {
            'secret':securitykey,
            'response':clientkey
        }
        
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=capthchaData)
        response = json.loads(r.text)
        verify = response['success']

        if verify:
            ContactModel.objects.create(name=name,email=email,subject=subject,message=message).save()
            messages.success(request,'Request submitted successfully')
            send_mail('Contact Form submitted by '+name,
            message,
            settings.EMAIL_HOST_USER,
            ['reviewservice999@gmail.com'],
            fail_silently=True)
            return redirect('contact')
        else:
            messages.warning(request,'reCaptcha Error, Check Your Internet Connection')
            return redirect('contact')

        
    else:
        return redirect("/")


def search(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    if request.method=="POST":
        search_val = request.POST['search']
        mob_srh = Mobiles.objects.none()
        now = datetime.now()
        mob_bn = Mobiles.objects.filter(brandname__icontains=search_val)
        mob_mn = Mobiles.objects.filter(modelname__icontains=search_val)
        later = datetime.now()
        sr_tm = (later-now).total_seconds()
        mob_srh = mob_bn.union(mob_mn)
        params = {'mob_srh':mob_srh,'count':mob_srh.count(),'user':user,"time":sr_tm,'query':search_val}
        if mob_srh.count() == 0:
            messages.warning(request,'No search Results Found')
            return render(request,'GRS/search.html',params)
        return render(request,'GRS/search.html',params)
    else:
        return redirect("/")