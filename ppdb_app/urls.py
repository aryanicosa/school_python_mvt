from django.contrib import admin
from django.urls import path, include

from ppdb_app.models import Users
from . import views

urlpatterns = [
    path('', views.dashboard_admin),

]