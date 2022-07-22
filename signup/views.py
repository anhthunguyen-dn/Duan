from django.shortcuts import render
from signup.models import NguoiDung

# Create your views here.


def signup(request):
    return render(request,'signup.html')

def trangchu(request):
    return render(request,'trangchu.html')

def xuly_dangky(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    password = request.GET.get('password')
    if(len(name) < 10):
        return render(request, 'loi.html')
    else:
        data = NguoiDung(
            name = name,
            email = email,
            password = password
        )
        data.save()

        return render(request, 'signin.html')

    
    

