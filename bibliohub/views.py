from django.shortcuts import render

def bienvenida(request):
    return render(request, 'bibliohub/bienvenida.html')
