from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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
        data_plantacao = request.POST.get('data_plantacao')
        data_regada = request.POST.get('data_regada')

        # Salva a nova plantação no banco de dados associada ao usuário logado
        Plantacao.objects.create(
            nome=nome,
            tipo=tipo,
            ruas=ruas,
            data_plantacao=data_plantacao,
            data_regada=data_regada,
            usuario=request.user  # Associar ao usuário logado
        )
        return redirect('home')  # Redireciona para a página de informações

    return render(request, 'add_plantacao.html')

# culturas/views.py

# Create your views here.
def horta_view(request):
    plantacoes = Plantacao.objects.filter(tipo='horta', usuario=request.user)  # Filtra por tipo e usuário logado
    return render(request, 'horta.html', {'plantacoes': plantacoes})

def saf_view(request):
    plantacoes = Plantacao.objects.filter(tipo='saf', usuario=request.user)  # Filtra por tipo e usuário logado
    return render(request, 'saf.html', {'plantacoes': plantacoes})


def painel_view(request):
    return render(request, 'painel.html')

def detalhe_plantacao_view(request):
    return render(request, 'detalhe_plantacao.html')



import requests
from django.shortcuts import render
from django.conf import settings

def plantacoes_info(request, nome):
    # Lógica para buscar a plantação
    plantacao = get_object_or_404(Plantacao, nome=nome, usuario=request.user)

    # Lógica para buscar a previsão do tempo
    city = request.GET.get('city', 'Carpina')  # Cidade padrão ou cidade selecionada pelo usuário
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'

    response = requests.get(url)
    weather_data = response.json()

    if weather_data.get('cod') == 200:
        weather_context = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
    else:
        weather_context = {'error': 'Cidade não encontrada'}

    # Combinar os contextos de plantação e previsão do tempo
    context = {
        'plantacao': plantacao,
        **weather_context  # Mesclar o contexto da previsão do tempo
    }

    return render(request, 'plantacoes_info.html', context)





