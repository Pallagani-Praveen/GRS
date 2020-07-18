from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from GRSapp.models import UsersModal,ContactModel,itemslist,Mobiles,Laptops,HeadSet,Camera,Powerbank,Kettle,WashingMachine,Refrigerator,Television
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
        item = request.POST['item']

        if item == 'mobile':
            mob_bn = Mobiles.objects.none()
            mob_mn = Mobiles.objects.none()
            
            now = datetime.now()
            mob_bn = Mobiles.objects.filter(brandname__icontains=search_val)
            mob_mn = Mobiles.objects.filter(modelname__icontains=search_val)
            later = datetime.now()

            sr_tm = (later-now).total_seconds()
            count = mob_bn.count()+mob_mn.count()
            params = {"user":user,'mob_bn':mob_bn,'mob_mn':mob_mn,'count':count,"time":sr_tm,'query':search_val,"item":item}
            if count == 0:
                messages.warning(request,'No Mobile Results Found')
                return render(request,'GRS/search.html',params)
            else:
                return render(request,'GRS/search.html',params)

        elif item == 'laptop':
            lap_bn = Laptops.objects.none()
            lap_mn = Laptops.objects.none()
            
            now = datetime.now()
            lap_bn = Laptops.objects.filter(brandname__icontains=search_val)
            lap_mn = Laptops.objects.filter(modelname__icontains=search_val)
            later = datetime.now()

            sr_tm = (later-now).total_seconds()
            count = lap_bn.count()+lap_mn.count()
            params = {"user":user,'lap_bn':lap_bn,'lap_mn':lap_mn,'count':count,"time":sr_tm,'query':search_val,"item":item}
            if count == 0:
                messages.warning(request,'No Laptop Results Found')
                return render(request,'GRS/search.html',params)
            else:
                return render(request,'GRS/search.html',params)
        
        elif item == 'headset':
            hs_bn = HeadSet.objects.none()
            hs_mn = HeadSet.objects.none()
            
            now = datetime.now()
            hs_bn = HeadSet.objects.filter(brandname__icontains=search_val)
            hs_mn = HeadSet.objects.filter(modelname__icontains=search_val)
            later = datetime.now()

            sr_tm = (later-now).total_seconds()
            count = hs_bn.count()+hs_mn.count()
            params = {"user":user,'hs_bn':hs_bn,'hs_mn':hs_mn,'count':count,"time":sr_tm,'query':search_val,"item":item}
            if count == 0:
                messages.warning(request,'No HeadSet Results Found')
                return render(request,'GRS/search.html',params)
            else:
                return render(request,'GRS/search.html',params)

        elif item == 'camera':
            cam_bn = Camera.objects.none()
            cam_mn = Camera.objects.none()
            
            now = datetime.now()
            cam_bn = Camera.objects.filter(brandname__icontains=search_val)
            cam_mn = Camera.objects.filter(modelname__icontains=search_val)
            later = datetime.now()

            sr_tm = (later-now).total_seconds()
            count = cam_bn.count()+cam_mn.count()
            params = {"user":user,'cam_bn':cam_bn,'cam_mn':cam_mn,'count':count,"time":sr_tm,'query':search_val,"item":item}
            if count == 0:
                messages.warning(request,'No Camera Results Found')
                return render(request,'GRS/search.html',params)
            else:
                return render(request,'GRS/search.html',params)
        
        elif item == 'powerbank':
            pb_bn = Powerbank.objects.none()
            pb_mn = Powerbank.objects.none()
            
            now = datetime.now()
            pb_bn = Powerbank.objects.filter(brandname__icontains=search_val)
            pb_mn = Powerbank.objects.filter(modelname__icontains=search_val)
            later = datetime.now()

            sr_tm = (later-now).total_seconds()
            count = pb_bn.count()+pb_mn.count()
            params = {"user":user,'pb_bn':pb_bn,'pb_mn':pb_mn,'count':count,"time":sr_tm,'query':search_val,"item":item}
            if count == 0:
                messages.warning(request,'No PowerBank Results Found')
                return render(request,'GRS/search.html',params)
            else:
                return render(request,'GRS/search.html',params)
        
        elif item == 'kettle':
            kt_bn = Kettle.objects.none()
            kt_mn = Kettle.objects.none()
            
            now = datetime.now()
            kt_bn = Kettle.objects.filter(brandname__icontains=search_val)
            kt_mn = Kettle.objects.filter(modelname__icontains=search_val)
            later = datetime.now()

            sr_tm = (later-now).total_seconds()
            count = kt_bn.count()+kt_mn.count()
            params = {"user":user,'kt_bn':kt_bn,'kt_mn':kt_mn,'count':count,"time":sr_tm,'query':search_val,"item":item}
            if count == 0:
                messages.warning(request,'No Kettle Results Found')
                return render(request,'GRS/search.html',params)
            else:
                return render(request,'GRS/search.html',params)
        
        elif item == 'washmachine':
            wm_bn = WashingMachine.objects.none()
            wm_mn = WashingMachine.objects.none()
            
            now = datetime.now()
            wm_bn = WashingMachine.objects.filter(brandname__icontains=search_val)
            wm_mn = WashingMachine.objects.filter(modelname__icontains=search_val)
            later = datetime.now()

            sr_tm = (later-now).total_seconds()
            count = wm_bn.count()+wm_mn.count()
            params = {"user":user,'wm_bn':wm_bn,'wm_mn':wm_mn,'count':count,"time":sr_tm,'query':search_val,"item":item}
            if count == 0:
                messages.warning(request,'No WashingMachine Results Found')
                return render(request,'GRS/search.html',params)
            else:
                return render(request,'GRS/search.html',params)
        
        elif item == 'fridge':
            fg_bn = Refrigerator.objects.none()
            fg_mn = Refrigerator.objects.none()
            
            now = datetime.now()
            fg_bn = Refrigerator.objects.filter(brandname__icontains=search_val)
            fg_mn = Refrigerator.objects.filter(modelname__icontains=search_val)
            later = datetime.now()

            sr_tm = (later-now).total_seconds()
            count = fg_bn.count()+fg_mn.count()
            params = {"user":user,'fg_bn':fg_bn,'fg_mn':fg_mn,'count':count,"time":sr_tm,'query':search_val,"item":item}
            if count == 0:
                messages.warning(request,'No Refridgrator Results Found')
                return render(request,'GRS/search.html',params)
            else:
                return render(request,'GRS/search.html',params)
        
        elif item == 'television':
            tv_bn = Television.objects.none()
            tv_mn = Television.objects.none()
            
            now = datetime.now()
            tv_bn = Television.objects.filter(brandname__icontains=search_val)
            tv_mn = Television.objects.filter(modelname__icontains=search_val)
            later = datetime.now()

            sr_tm = (later-now).total_seconds()
            count = tv_bn.count()+tv_mn.count()
            params = {"user":user,'tv_bn':tv_bn,'tv_mn':tv_mn,'count':count,"time":sr_tm,'query':search_val,"item":item}
            if count == 0:
                messages.warning(request,'No Television Results Found')
                return render(request,'GRS/search.html',params)
            else:
                return render(request,'GRS/search.html',params)

        else:
            params = {"user":user,"query":search_val}
            messages.warning(request,'No search Results Found')
            return render(request,'GRS/search.html',params)
    else:
        return redirect("/")