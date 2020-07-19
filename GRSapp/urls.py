from django.urls import path
from . import views
urlpatterns = [

    path('',views.GRSappHome,name = 'GRSappHome'),
    path('showitems/<str:slug>',views.loaditem,name = 'loaditem'),
    path('mobiles',views.loadmobiles,name="loadmobiles")

]
