from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.contrib import messages

def RegistroView(request):
    return render (request, 'registro.html')

def LoginView(request):
    return render (request, 'login.html')

def CadastroView(request):
    return render (request, 'cadastro.html')

def PainelView(request):
    return render (request, 'painel.html')

def Login(request):
    if request.method == 'GET':
        return render (request, 'login.html')
    else:
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        user = authenticate(request, cpf=cpf, senha=senha)

        if user is not None:
            auth_login(request, user)
        else:
            return HttpResponse('CPF ou senha inválidos')
        
def Cadastro(request):
    if request.method == 'GET':
        return render (request, 'cadastro.html')
    else:
        nome = nome.POST.get('nome')
        data_nascimento = data_nascimento.POST.get('data_nascimento')
        cpf = cpf.POST.get('cpf')
        senha = senha.POST.get('senha')

        user = User.objects.filter(cpf=cpf).first()

        if user:
            return HttpResponse ('Já existe um usuário com esse CPF')
        
        user = User.objects.create_user(
            nome=nome,
            data_nascimento=data_nascimento,
            cpf=cpf,
            senha=senha,
        )
        user.save()

        return render (request, 'login.html', {'sucess_message':'Usuário cadastrado com sucesso!'})
