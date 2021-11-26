from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from ppdb_app.models import Users
from django.contrib import messages
#from django.contrib.auth import authenticate

# Create your views here.
def dashboard_admin(request):
    #TODO define object to pass onto dashboard field 
    return render(request, '../templates/ppdb_app/dashboard.html', {})