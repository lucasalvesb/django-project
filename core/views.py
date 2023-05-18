from django.shortcuts import render, redirect
from .models import Person

def home(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

def save(request):
    vname = request.POST.get("name")
    vage = request.POST.get("age")
    vcpf = request.POST.get("cpf")
    vemail = request.POST.get("email")
    vphone = request.POST.get("phone")
    vaddress = request.POST.get("address")
    Person.objects.create(name=vname, age=vage, cpf=vcpf, email=vemail, phone=vphone, address=vaddress)
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, "update.html", {"person": person})

def update(request, id):
    vname = request.POST.get("name")
    person = Person.objects.get(id=id)
    person.name = vname
    person.save() 
    return redirect(home)