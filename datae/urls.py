"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('UserTable',views.usertable,name="usertable"),
    path('location',views.location,name="location"),
    path('LocationTable/',views.locationtable,name="locationtable"),
    path('Create',views.stinsert,name="stinsert"),
    path('Edit/<int:id>/',views.stedit,name="stedit"),
    path('Update/<int:id>',views.stupdate,name="stupdate"),
    path('Delete/<int:id>',views.stdel,name="stdel"),
    path('check_rfid/', views.check_rfid, name='check_rfid'),
    path('view_rfid_info/', views.view_rfid_info, name='view_rfid_info'),
    path('getdata/', views.get_data, name='get_data'),
]

