from django.contrib import admin
from django.urls import path
from signup import views


urlpatterns = [
    path('', views.signup),
    path('xuly_dangky', views.xuly_dangky, name="xuly_dangky")
]
