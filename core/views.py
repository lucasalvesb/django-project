from django.shortcuts import render
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    name = request.POST.get("name")
    Pessoal.objects.create(name=name)
    pessoas = Pessoal.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})
