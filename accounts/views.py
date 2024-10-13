from django.shortcuts import render

def HomeView(request):
    return render (request, 'home.html')

def LoginView(request):
    return render (request, 'login.html')

def RegistroView(request):
    return render (request, 'registro.html')