from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import User
from django.urls import reverse
# from apps.crops.views import predict_harvest


User = get_user_model()

# contas/views.py

def cadastro_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nome = request.POST.get('nome')  # Recebe o nome do formulário
        password = request.POST.get('password')

        # Verifique se o email já existe
        if User.objects.filter(email=email).exists():
            return render(request, 'cadastro.html', {'error': 'Email já cadastrado!'})

        # Crie um novo usuário com nome
        user = User.objects.create_user(email=email, nome=nome, password=password)

        return redirect(reverse('login'))  # Redirecionar para a página de login após o cadastro

    return render(request, 'cadastro.html')




# contas/views.py

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)  # Autentica usando email

        if user is not None:
            login(request, user)
            return redirect('crops:home')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Usuário ou senha inválidos!')

    return render(request, 'login.html')








