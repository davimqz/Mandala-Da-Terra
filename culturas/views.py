from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . models import Plantacao
from django.urls import reverse


# culturas/views.py
from django.shortcuts import render, redirect
from .models import Plantacao

def add_plantacao_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        tipo = request.POST.get('tip')
        ruas = ', '.join(request.POST.getlist('rua'))  # Combina as ruas em uma string
        data_colheita = request.POST.get('data_colheita')
        data_regada = request.POST.get('data_regada')

        # Salva a nova plantação no banco de dados associada ao usuário logado
        Plantacao.objects.create(
            nome=nome,
            tipo=tipo,
            ruas=ruas,
            data_colheita=data_colheita,
            data_regada=data_regada,
            usuario=request.user  # Associar ao usuário logado
        )
        return redirect('plantacoes_info')  # Redireciona para a página de informações

    return render(request, 'add_plantacao.html')

# culturas/views.py
def plantacoes_info(request):
    plantacoes = Plantacao.objects.filter(usuario=request.user)  # Filtra as plantações pelo usuário logado
    return render(request, 'plantacoes_info.html', {'plantacoes': plantacoes})




# Create your views here.
def horta_view(request):
    return render(request, 'horta.html')

def saf_view(request):
    return render(request, 'saf.html')

# def add_plantacao_view(request):
#     return render(request, 'add_plantacao.html')

def painel_view(request):
    return render(request, 'painel.html')

def detalhe_plantacao_view(request):
    return render(request, 'detalhe_plantacao.html')








