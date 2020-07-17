
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GRSHome,name="GRSHome"),
    path('contact',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('search',views.search,name="search"),
    path('otp',views.otp,name="otp"),
    path('signup',views.signup,name = 'signup'),
    path('login',views.login,name = 'login'),
    path('logout',views.logout,name = 'logout'),
    path('viewprofile',views.viewprofile,name = 'viewprofile'),
    path('updateprofile',views.updateprofile,name = 'updateprofile'),
    path('issue',views.issue,name = 'issue'),
    path('GRSapp/',include('GRSapp.urls'))
] + static(settings.MEDIA_URLS,document_root= settings.MEDIA_ROOT)
