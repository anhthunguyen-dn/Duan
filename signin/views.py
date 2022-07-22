from django.shortcuts import render, get_object_or_404
from signup.models import NguoiDung
from signin.models import Nhanvien
# Create your views here.


def signin(request):
    return render(request,'signin.html')

def xuly_dangnhap(request):
    name = request.GET.get('name')
    password = request.GET.get('password')

    thongtin = NguoiDung.objects.filter(name = name, password = password)
    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung': danh_sach
    }
    if(thongtin.exists()):
        return render(request, 'danhsach.html', context)
    else:
        return render(request, 'loi.html')

def xuly_themnhanvien(request):
    ten = request.GET.get('ten')
    chuc_vu = request.GET.get('chuc_vu')
    nam_sinh = request.GET.get('nam_sinh')
    data = Nhanvien(
            ten = ten,
            chuc_vu = chuc_vu,
            nam_sinh = nam_sinh
        )
    data.save()
    return render(request, 'themnhanvien.html')

def chi_tiet(request, nguoidung_id):
    nv = get_object_or_404(NguoiDung, pk = nguoidung_id)
    context = {
        'nguoi_dung':nv
    }
    return render(request, 'chitiet.html', context)

def xuly_capnhat(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    password = request.GET.get('password')
    id_nguoidung = request.GET.get('id_nd')

    NguoiDung.objects.filter(id = id_nguoidung).update(
        name = name,
        password = password,
        email = email
    )

    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung': danh_sach
    }
    return render(request, 'danhsach.html', context)

def xuly_xoa(request, nguoidung_id):
    data = get_object_or_404(NguoiDung, pk = nguoidung_id)
    data.delete()
    danh_sach = NguoiDung.objects.all()
    context ={
        'ds_nguoidung': danh_sach
    }
    return render(request, 'danhsach.html', context)