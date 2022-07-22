from django.contrib import admin
from django.urls import path
from signin import views


urlpatterns = [
    path('', views.signin),
    path('xuly_dangnhap', views.xuly_dangnhap, name="xuly_dangnhap"),
    path('<int:nguoidung_id>/', views.chi_tiet, name="chi_tiet"),
    path('xuly_capnhat', views.xuly_capnhat, name="xuly_capnhat"),
    path('xoa/<int:nguoidung_id>', views.xuly_xoa, name="xuly_xoa"),
]
