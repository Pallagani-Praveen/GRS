from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UsersModal,Mobiles,Laptops,HeadSet,Camera,Powerbank,Refrigerator,Kettle,Television,WashingMachine
from http.cookies import SimpleCookie
from math import floor,ceil
from GRS.randkey import make_ratings
from django.core.paginator import Paginator

def GRSappHome(request):
    user = request.COOKIES.get('username')
    mobiles = Mobiles.objects.all()
    paginator1 = Paginator(mobiles,6)
    page1 = request.GET.get('page1')
    mobiles = paginator1.get_page(page1)

    laptops = Laptops.objects.all()
    paginator2 = Paginator(laptops,4)
    page2 = request.GET.get('page2')
    laptops = paginator2.get_page(page2)

    headsets = HeadSet.objects.all()
    paginator3 = Paginator(headsets,6)
    page3 = request.GET.get('page3')
    headsets = paginator3.get_page(page3)

    cameras = Camera.objects.all()
    paginator4 = Paginator(cameras,4)
    page4 = request.GET.get('page4')
    cameras = paginator4.get_page(page4)

    powerbanks = Powerbank.objects.all()
    paginator5 = Paginator(powerbanks,6)
    page5 = request.GET.get('page5')
    powerbanks = paginator5.get_page(page5)

    fridges = Refrigerator.objects.all()
    paginator6 = Paginator(fridges,6)
    page6 = request.GET.get('page6')
    fridges = paginator6.get_page(page6)

    kettles = Kettle.objects.all()
    paginator7 = Paginator(kettles,8)
    page7 = request.GET.get('page7')
    kettles = paginator7.get_page(page7)


    tvs = Television.objects.all()
    paginator8 = Paginator(tvs,8)
    page8 = request.GET.get('page8')
    tvs = paginator8.get_page(page8)


    wms = WashingMachine.objects.all()
    paginator9 = Paginator(wms,8)
    page9 = request.GET.get('page9')
    wms = paginator9.get_page(page9)

    

    params = {'user':user,'mobiles':mobiles,'laptops':laptops,'headsets':headsets,'cameras':cameras,'powerbanks':powerbanks,'fridges':fridges,'kettles':kettles,'tvs':tvs,'wms':wms}
        
    return render(request,'GRSapp/GRSHome.html',params)

def loaditem(request,slug): 
    if slug=="Mobiles":
        return redirect('loadmobiles')
    else:
        return HttpResponse("Page Not Found")

def loadmobiles(request):
    user = request.COOKIES.get('username')
    mobiles = Mobiles.objects.all()
    mobiles = make_ratings(mobiles)
    tr_mobile_one = Mobiles.objects.order_by('rating').reverse()[:4]
    tr_mobile_two = Mobiles.objects.order_by('rating').reverse()[4:8]
    tr_mobile_one = make_ratings(tr_mobile_one)
    tr_mobile_two = make_ratings(tr_mobile_two)
    lt_mobile_one = tr_mobile_one
    lt_mobile_two = tr_mobile_two
    params = {'user':user,"mobiles":mobiles,'tr_one':tr_mobile_one,'tr_two':tr_mobile_two,'lt_one':lt_mobile_one,'lt_two':lt_mobile_two}
    return render(request,'GRSapp/showMobiles.html',params)   
        
    

