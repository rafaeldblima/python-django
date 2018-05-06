from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def exibir(request, id):
    return render(request, 'perfil.html')