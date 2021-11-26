"""ppdb_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin, messages
from django.urls import path, include
from django.shortcuts import redirect, render
from ppdb_app.models import Users
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request, 'index.html', {})

def panduan_sd(request):
    return render(request, 'panduan_sd.html', {})

def panduan_smp(request):
    return render(request, 'panduan_smp.html', {})

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "" or password == "":
            messages.add_message(request, messages.WARNING, 'Username and password can not empty!')

        else :
            try:
                

                Admin = Users.objects.filter(username=username).values()            
                if Admin[0]['username'] == username and Admin[0]['password'] == password:
                    print("oke")
                    return redirect('/adminppdb/')

            except:
                print("fail login")
                pass
                messages.add_message(request, messages.WARNING, 'Wrong username or password!')    
        
        return render(request, 'login_admin.html', {messages : messages})
    else:
        return render(request, 'login_admin.html', {})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('panduan/sd', panduan_sd),
    path('panduan/smp', panduan_smp),
    path('login/admin', login_admin),
    path('adminppdb/', include('ppdb_app.urls')),
]
