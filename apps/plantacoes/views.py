from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from . models import Plantacao

def HomeView(request):
    return render (request, 'home.html')

def SafView(request):
    return render (request, 'saf.html')

def HortaView(request):
    return render (request, 'horta.html')

def AdicionarPlantacaoView(request):
    return render (request, 'adicionar_plantacao.html')

@login_required(login_url='login')
def AdicionarPlantacao(request):
    if request.method == 'POST':
        nome_plantacao = request.POST.get('nome')
        tipo_plantacao = request.POST.get('tip')
        rua = request.POST.get('rua')
        data_colheita = request.POST.get('data_colheita')
        data_regada = request.POST.get('data_regada')

        plantacao = Plantacao(
            nome_plantacao=nome_plantacao,
            tipo_plantacao=tipo_plantacao,
            rua=rua,
            data_colheita=data_colheita,
            data_regada=data_regada,
            
        )
        plantacao.save()

        return redirect('plantacoes/home')
    
    return render(request, 'plantacoes/adicionar_plantacao.html')
