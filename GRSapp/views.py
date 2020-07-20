from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from .models import UsersModal,Mobiles,Laptops,HeadSet,Camera,Powerbank,Refrigerator,Kettle,Television,WashingMachine
from .models import mobilereview,laptopreview,kettlereview,headsetreview,fridgereview,camerareview,powerbankreview,televisionreview,washmanchinereview
from http.cookies import SimpleCookie
from math import floor,ceil
from GRS.randkey import make_ratings,make_rating
from django.core.paginator import Paginator
from django.core.exceptions import MultipleObjectsReturned

def GRSappHome(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
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
    paginator7 = Paginator(kettles,5)
    page7 = request.GET.get('page7')
    kettles = paginator7.get_page(page7)


    tvs = Television.objects.all()
    paginator8 = Paginator(tvs,4)
    page8 = request.GET.get('page8')
    tvs = paginator8.get_page(page8)


    wms = WashingMachine.objects.all()
    paginator9 = Paginator(wms,5)
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
    mobiles = Mobiles.objects.all().order_by('-rating')
    mobiles = make_ratings(mobiles)
    params = {"user":user,"mobiles":mobiles}
    return render(request,'GRSapp/loadMobiles.html',params)

def loadlaptops(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    laptops = Laptops.objects.all().order_by('-rating')
    laptops = make_ratings(laptops)
    params = {"user":user,"laptops":laptops}
    return render(request,'GRSapp/loadLaptops.html',params)

def loadheadsets(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    headsets = HeadSet.objects.all().order_by('-rating')
    headsets = make_ratings(headsets)
    params = {"user":user,"headsets":headsets}
    return render(request,'GRSapp/loadHeadsets.html',params)

def loadcameras(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    cameras = Camera.objects.all().order_by('-rating')
    cameras = make_ratings(cameras)
    params = {"user":user,"cameras":cameras}
    return render(request,'GRSapp/loadCameras.html',params)

def loadpowerbanks(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    pbanks = Powerbank.objects.all().order_by('-rating')
    pbanks = make_ratings(pbanks)
    params = {"user":user,"pbanks":pbanks}
    return render(request,'GRSapp/loadPowerbanks.html',params)

def loadkettles(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    kettles = Kettle.objects.all().order_by('-rating')
    kettles = make_ratings(kettles)
    params = {"user":user,"kettles":kettles}
    return render(request,'GRSapp/loadKettles.html',params)

def loadwashmachines(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    wms = WashingMachine.objects.all().order_by('-rating')
    wms = make_ratings(wms)
    params = {"user":user,"wms":wms}
    return render(request,'GRSapp/loadWashmachines.html',params)

def loadfridges(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    fridges = Refrigerator.objects.all().order_by('-rating')
    fridges = make_ratings(fridges)
    params = {"user":user,"fridges":fridges}
    return render(request,'GRSapp/loadFridges.html',params)

def loadtelevisions(request):
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    televisions = Television.objects.all().order_by('-rating')
    televisions = make_ratings(televisions)
    params = {"user":user,"televisions":televisions}
    return render(request,'GRSapp/loadTelevisions.html',params)




# display specific component
def mobileview(request,id):
    if not Mobiles.objects.filter(id=id):
        return redirect('/')
    ourmobile = Mobiles.objects.get(id=id)
    ourmobile = make_rating(ourmobile)
    reviews = None
    if mobilereview.objects.filter(mobileid=id):
        reviews = mobilereview.objects.all()
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourmobile":ourmobile,"user":user,"reviews":reviews}
    return render(request,'GRSapp/endViews/mobile.html',params)

def laptopview(request,id):
    if not Laptops.objects.filter(id=id):
        return redirect('/')
    ourlaptop = Laptops.objects.get(id=id)
    ourlaptop = make_rating(ourlaptop)
    reviews = None
    if laptopreview.objects.filter(laptopid=id):
        reviews = laptopreview.objects.all()
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourlaptop":ourlaptop,"user":user,"reviews":reviews}
    return render(request,'GRSapp/endViews/laptop.html',params)

def headsetview(request,id):
    if not HeadSet.objects.filter(id=id):
        return redirect('/')
    ourheadset = HeadSet.objects.get(id=id)
    ourheadset = make_rating(ourheadset)
    reviews = None
    if headsetreview.objects.filter(headsetid=id):
        reviews = headsetreview.objects.all()
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourheadset":ourheadset,"user":user,"reviews":reviews}
    return render(request,'GRSapp/endViews/headset.html',params)
    

def powerbankview(request,id):
    if not Powerbank.objects.filter(id=id):
        return redirect('/')
    ourpowerbank = Powerbank.objects.get(id=id)
    ourpowerbank = make_rating(ourpowerbank)
    reviews = None
    if powerbankreview.objects.filter(powerbankid=id):
        reviews = powerbankreview.objects.all()
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourpowerbank":ourpowerbank,"user":user,"reviews":reviews}
    return render(request,'GRSapp/endViews/powerbank.html',params)
    

def cameraview(request,id):
    if not Camera.objects.filter(id=id):
        return redirect('/')
    ourcamera = Camera.objects.get(id=id)
    ourcamera = make_rating(ourcamera)
    reviews = None
    if camerareview.objects.filter(cameraid=id):
        reviews = camerareview.objects.all()
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourcamera":ourcamera,"user":user,"reviews":reviews}
    return render(request,'GRSapp/endViews/camera.html',params)
    

def fridgeview(request,id):
    if not Refrigerator.objects.filter(id=id):
        return redirect('/')
    ourfridge = Refrigerator.objects.get(id=id)
    ourfridge = make_rating(ourfridge)
    reviews = None
    if fridgereview.objects.filter(fridgeid=id):
        reviews = fridgereview.objects.all()
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourfridge":ourfridge,"user":user,"reviews":reviews}
    return render(request,'GRSapp/endViews/fridge.html',params)
    

def kettleview(request,id):
    if not Kettle.objects.filter(id=id):
        return redirect('/')
    ourkettle = Kettle.objects.get(id=id)
    ourkettle = make_rating(ourkettle)
    reviews = None
    if kettlereview.objects.filter(kettleid=id):
        reviews = kettlereview.objects.all()
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourkettle":ourkettle,"user":user,"reviews":reviews}
    return render(request,'GRSapp/endViews/kettle.html',params)
    

def washmachineview(request,id):
    if not WashingMachine.objects.filter(id=id):
        return redirect('/')
    ourwashmachine = WashingMachine.objects.get(id=id)
    ourwashmachine = make_rating(ourwashmachine)
    reviews = None
    if washmanchinereview.objects.filter(washmachineid=id):
        reviews = washmanchinereview.objects.all()
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourwashmachine":ourwashmachine,"user":user,"reviews":reviews}
    return render(request,'GRSapp/endViews/washmachine.html',params)
    

def televisionview(request,id):
    if not Television.objects.filter(id=id):
        return redirect('/')
    ourtelevision = Television.objects.get(id=id)
    ourtelevision = make_rating(ourtelevision)
    reviews = None
    if televisionreview.objects.filter(televisionid=id):
        reviews = televisionreview.objects.all()
    user = request.COOKIES.get('username')
    if UsersModal.objects.filter(username=user):
        user = UsersModal.objects.get(username=user)
    params = {"ourtelevision":ourtelevision,"user":user,"reviews":reviews}
    return render(request,'GRSapp/endViews/television.html',params)



# make comments

def makemobcom(request):
    if request.method == 'POST':
        username = request.POST['username']
        mobileid = request.POST['mobileid']
        commnet = request.POST['comment']
        comobj = mobilereview.objects.create(userid=username,mobileid=mobileid,reviewmsg=commnet)
        comobj.save()
        return HttpResponse('this is post methos')
    else:
        return redirect('/')


def makelapcom(request):
    if request.method == 'POST':
        username = request.POST['username']
        laptopid = request.POST['laptopid']
        commnet = request.POST['comment']
        comobj = laptopreview.objects.create(userid=username,laptopid=laptopid,reviewmsg=commnet)
        comobj.save()
        return HttpResponse('this is post methos')
    else:
        return redirect('/')

def makeketcom(request):
    if request.method == 'POST':
        username = request.POST['username']
        kettleid = request.POST['kettleid']
        commnet = request.POST['comment']
        comobj = kettlereview.objects.create(userid=username,kettleid=kettleid,reviewmsg=commnet)
        comobj.save()
        return HttpResponse('this is post methos')
    else:
        return redirect('/')

def makehstcom(request):
    if request.method == 'POST':
        username = request.POST['username']
        headsetid = request.POST['headsetid']
        commnet = request.POST['comment']
        comobj = headsetreview.objects.create(userid=username,headsetid=headsetid,reviewmsg=commnet)
        comobj.save()
        return HttpResponse('this is post methos')
    else:
        return redirect('/')


def makefdgcom(request):
    if request.method == 'POST':
        username = request.POST['username']
        fridgeid = request.POST['fridgeid']
        commnet = request.POST['comment']
        comobj = fridgereview.objects.create(userid=username,fridgeid=fridgeid,reviewmsg=commnet)
        comobj.save()
        return HttpResponse('this is post methos')
    else:
        return redirect('/')

def makecamcom(request):
    if request.method == 'POST':
        username = request.POST['username']
        cameraid = request.POST['cameraid']
        commnet = request.POST['comment']
        comobj = camerareview.objects.create(userid=username,cameraid=cameraid,reviewmsg=commnet)
        comobj.save()
        return HttpResponse('this is post methos')
    else:
        return redirect('/')


def makepbkcom(request):
    if request.method == 'POST':
        username = request.POST['username']
        powerbankid = request.POST['powerbankid']
        commnet = request.POST['comment']
        comobj = powerbankreview.objects.create(userid=username,powerbankid=powerbankid,reviewmsg=commnet)
        comobj.save()
        return HttpResponse('this is post methos')
    else:
        return redirect('/')


def maketelcom(request):
    if request.method == 'POST':
        username = request.POST['username']
        televisionid = request.POST['televisionid']
        commnet = request.POST['comment']
        comobj = televisionreview.objects.create(userid=username,televisionid=televisionid,reviewmsg=commnet)
        comobj.save()
        return HttpResponse('this is post methos')
    else:
        return redirect('/')


def makewhncom(request):
    if request.method == 'POST':
        username = request.POST['username']
        washmachineid = request.POST['washmachineid']
        commnet = request.POST['comment']
        comobj = washmanchinereview.objects.create(userid=username,washmachineid=washmachineid,reviewmsg=commnet)
        comobj.save()
        return HttpResponse('this is post methos')
    else:
        return redirect('/')






    

