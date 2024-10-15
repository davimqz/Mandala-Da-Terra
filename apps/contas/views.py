from django.shortcuts import render

def RegistroView(request):
    return render (request, 'registro.html')

def LoginView(request):
    return render (request, 'login.html')

def CadastroView(request):
    return render (request, 'cadastro.html')