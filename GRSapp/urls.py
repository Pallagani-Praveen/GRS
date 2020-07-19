from django.urls import path
from . import views
from GRS import views as  grsview
urlpatterns = [
    
    path('',views.GRSappHome,name = 'GRSappHome'),
    
    path('mobiles',views.loadmobiles,name="loadmobiles"),
    path('laptops',views.loadlaptops,name="loadlaptops"),
    path('headset',views.loadheadsets,name="loadheadsets"),
    path('camera',views.loadcameras,name="loadcameras"),
    path('powerbank',views.loadpowerbanks,name="loadpowerbanks"),
    path('kettle',views.loadkettles,name="loadkettles"),
    path('washingmachine',views.loadwashmachines,name="loadwashmachines"),
    path('refrigerator',views.loadfridges,name="loadfridges"),
    path('television',views.loadtelevisions,name="loadtelevisions"),

    path('mobiles/<int:id>',views.mobileview,name="mobileview"),
    path('laptops/<int:id>',views.laptopview,name="laptopview"),
    path('headsets/<int:id>',views.headsetview,name="headsetview"),
    path('cameras/<int:id>',views.cameraview,name="cameraview"),
    path('powerbanks/<int:id>',views.powerbankview,name="powerbankview"),
    path('fridges/<int:id>',views.fridgeview,name="fridgeview"),
    path('kettles/<int:id>',views.kettleview,name="kettleview"),
    path('televisions/<int:id>',views.televisionview,name="televisionview"),
    path('washmachines/<int:id>',views.washmachineview,name="washmanchineview"),

    path('makemobcom',views.makemobcom,name="makemobcom"),
    path('makelapcom',views.makelapcom,name="makelapcom"),
    path('makeketcom',views.makeketcom,name="makeketcom"),
    path('makehstcom',views.makehstcom,name="makehstcom"),
    path('makefdgcom',views.makefdgcom,name="makefdgcom"),
    path('makecamcom',views.makecamcom,name="makecamcom"),
    path('makepbkcom',views.makepbkcom,name="makepbkcom"),
    path('maketelcom',views.maketelcom,name="maketelcom"),
    path('makewhncom',views.makewhncom,name="makewhncom"),
    
]