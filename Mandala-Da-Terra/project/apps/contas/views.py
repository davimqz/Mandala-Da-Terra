from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import User
from django.urls import reverse
from apps.culturas.views import saf_view, horta_view, add_plantacao_view


User = get_user_model()

def cadastro_view(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')

        # Verifique se o CPF já existe
        if User.objects.filter(cpf=cpf).exists():
            return render(request, 'cadastro.html', {'error': 'CPF já cadastrado!'})

        # Crie um novo usuário
        user = User.objects.create_user(cpf=cpf, password=password)

        return redirect(reverse('login'))  # Redirecionar para a página de login após o cadastro

    return render(request, 'cadastro.html')



# contas/views.py

def login_view(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')

        user = authenticate(request, username=cpf, password=password)  # Autentica usando CPF

        if user is not None:
            login(request, user)
            messages.success(request, 'Você foi logado com sucesso!')
            return redirect('home')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Usuário ou senha inválidos!')

    return render(request, 'login.html')



def home_view(request):
    return render(request, 'home.html')



# views.py
from django.shortcuts import render, redirect



#puxando view de outra pasta
def saf(request):
    return saf_view(request)

def horta(request):
    return horta_view(request)

def add_plantacao(request):
    return add_plantacao_view(request)

def painel_view(request):
    return painel_view(request)

def criar_plantacao(request):
    return add_plantacao(request)

from apps.culturas.views import plantacoes_info as culturas_plantacoes_info

def plantacoes_info(request):
    return culturas_plantacoes_info(request)  # Chama a função da outra view

def info_view(request):
    return plantacoes_info(request)