
from django.contrib import admin
from django.urls import include, path
from app1 import views

urlpatterns = [
    path('',views.test , name='test'),
]
