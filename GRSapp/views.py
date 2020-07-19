from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from .models import UsersModal,Mobiles,Laptops,HeadSet,Camera,Powerbank,Refrigerator,Kettle,Television,WashingMachine
from http.cookies import SimpleCookie
from math import floor,ceil
from GRS.randkey import make_ratings,make_rating
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
    paginator7 = Paginator(kettles,4)
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

# display all gadgets by category
def loadmobiles(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    mobiles = Mobiles.objects.all()
    mobiles = make_ratings(mobiles)
    params = {"user":user,"mobiles":mobiles}
    return render(request,'GRSapp/loadMobiles.html',params)

def loadlaptops(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    laptops = Laptops.objects.all()
    laptops = make_ratings(laptops)
    params = {"user":user,"laptops":laptops}
    return render(request,'GRSapp/loadLaptops.html',params)

def loadheadsets(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    headsets = HeadSet.objects.all()
    headsets = make_ratings(headsets)
    params = {"user":user,"headsets":headsets}
    return render(request,'GRSapp/loadHeadsets.html',params)

def loadcameras(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    cameras = Camera.objects.all()
    cameras = make_ratings(cameras)
    params = {"user":user,"cameras":cameras}
    return render(request,'GRSapp/loadCameras.html',params)

def loadpowerbanks(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    pbanks = Powerbank.objects.all()
    pbanks = make_ratings(pbanks)
    params = {"user":user,"pbanks":pbanks}
    return render(request,'GRSapp/loadPowerbanks.html',params)

def loadkettles(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    kettles = Kettle.objects.all()
    kettles = make_ratings(kettles)
    params = {"user":user,"kettles":kettles}
    return render(request,'GRSapp/loadKettles.html',params)

def loadwashmachines(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    wms = WashingMachine.objects.all()
    wms = make_ratings(wms)
    params = {"user":user,"wms":wms}
    return render(request,'GRSapp/loadWashmachines.html',params)

def loadfridges(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    fridges = Refrigerator.objects.all()
    fridges = make_ratings(fridges)
    params = {"user":user,"fridges":fridges}
    return render(request,'GRSapp/loadFridges.html',params)

def loadtelevisions(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    televisions = Television.objects.all()
    televisions = make_ratings(televisions)
    params = {"user":user,"televisions":televisions}
    return render(request,'GRSapp/loadTelevisions.html',params)




# display specific component
def mobileview(request,id):
    ourmobile = Mobiles.objects.get(id=id)
    ourmobile = make_rating(ourmobile)
    print(ourmobile.rating)
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourmobile":ourmobile,"user":user}
    return render(request,'GRSapp/endViews/mobile.html',params)

def laptopview(request,id):
    ourlaptop = Laptops.objects.get(id=id)
    ourlaptop = make_rating(ourlaptop)
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourlaptop":ourlaptop,"user":user}
    return render(request,'GRSapp/endViews/laptop.html',params)

def headsetview(request,id):
    ourheadset = HeadSet.objects.get(id=id)
    ourheadset = make_rating(ourheadset)
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourheadset":ourheadset,"user":user}
    return render(request,'GRSapp/endViews/headset.html',params)
    

def powerbankview(request,id):
    ourpowerbank = Powerbank.objects.get(id=id)
    ourpowerbank = make_rating(ourpowerbank)
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourpowerbank":ourpowerbank,"user":user}
    return render(request,'GRSapp/endViews/powerbank.html',params)
    

def cameraview(request,id):
    ourcamera = Camera.objects.get(id=id)
    ourcamera = make_rating(ourcamera)
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourcamera":ourcamera,"user":user}
    return render(request,'GRSapp/endViews/camera.html',params)
    

def fridgeview(request,id):
    ourfridge = Refrigerator.objects.get(id=id)
    ourfridge = make_rating(ourfridge)
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourfridge":ourfridge,"user":user}
    return render(request,'GRSapp/endViews/fridge.html',params)
    

def kettleview(request,id):
    ourkettle = Kettle.objects.get(id=id)
    ourkettle = make_rating(ourkettle)
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourkettle":ourkettle,"user":user}
    return render(request,'GRSapp/endViews/kettle.html',params)
    

def washmachineview(request,id):
    ourwashmachine = WashingMachine.objects.get(id=id)
    ourwashmachine = make_rating(ourwashmachine)
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourwashmachine":ourwashmachine,"user":user}
    return render(request,'GRSapp/endViews/washmachine.html',params)
    

def televisionview(request,id):
    ourtelevision = Television.objects.get(id=id)
    ourtelevision = make_rating(ourtelevision)
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourtelevision":ourtelevision,"user":user}
    return render(request,'GRSapp/endViews/television.html',params)



        
    

