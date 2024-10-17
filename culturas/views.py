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
        return redirect('home')  # Redireciona para a página de informações

    return render(request, 'add_plantacao.html')

# culturas/views.py
def plantacoes_info(request):
    #plantacoes = Plantacao.objects.filter(usuario=request.user)  # Filtra as plantações pelo usuário logado
    return render(request, 'plantacoes_info.html')#, {'plantacoes': plantacoes})




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

def weather_view(request):
    city = request.GET.get('city', 'Carpina')  # Cidade padrão ou cidade selecionada pelo usuário
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'

    response = requests.get(url)
    weather_data = response.json()

    if weather_data.get('cod') == 200:
        context = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
    else:
        context = {'error': 'Cidade não encontrada'}

    return render(request, 'weather.html', context)





