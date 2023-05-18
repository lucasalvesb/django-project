from django.shortcuts import render
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    vname = request.POST.get("name")
    vage = request.POST.get("age")
    vcpf = request.POST.get("cpf")
    vemail = request.POST.get("email")
    vphone = request.POST.get("phone")
    vaddress = request.POST.get("address")
    Pessoa.objects.create(name=vname, age=vage, cpf=vcpf, email=vemail, phone=vphone, address=vaddress)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})
