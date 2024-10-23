from django.contrib import admin
from django.urls import path
from ATS.views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('download', download, name = 'download'),
]
